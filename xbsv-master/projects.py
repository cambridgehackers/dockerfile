
import buildbot
import jinja2
import json
import re
import subprocess
import sys
import twisted
from twisted.python import log
from twisted.internet import defer
from twisted.web.util import Redirect
from buildbot.status.web.base import ActionResource
from buildbot.status.web.base import HtmlResource
from buildbot.status.web.base import path_to_root
from buildbot.status.web.base import path_to_authzfail


class ProjectsResource(HtmlResource):
    pageTitle = "Project Repos"

    def content(self, request, cxt):
        cxt.update(dict(buildbot=buildbot.version,
                        twisted=twisted.__version__,
                        jinja=jinja2.__version__,
                        python=sys.version,
                        platform=sys.platform))

        template = request.site.buildbot_service.templates.get_template("projects.html")
        template.autoescape = True
        return template.render(**cxt)

class AddProjectResource(ActionResource):
    @defer.inlineCallbacks
    def performAction(self, req):
	authz = self.getAuthz(req)
	print authz.getUsername(req), authz.authenticated(req)
	res = yield authz.actionAllowed('forceBuild', req)
	if not res:
    	    defer.returnValue(Redirect(path_to_authzfail(req)))
    	    return
	projects = json.load(open('projects.json'))
        log.msg('loaded projects.json')

	log.msg(str(req.args.items()))
        projectname = req.args.get('projectname', [])[0]
	projectrepo = req.args.get('projectrepo', [])[0]
	paths = req.args.get('path', [])
	boardaddr = req.args.get('boardaddr', [])[0]
        log.msg(str(req.args.get('arches', [])))
        arches = req.args.get('arches', ['bluesim'])
        revisions = req.args.get('revision', [])
        branches = req.args.get('branch', [])

        m = re.match('git://github.com/(.*)/(.*).git', projectrepo)
	if projectname in projects:
	    msg = 'project ' + projectname + ' already exists'
        elif not m:
            msg = 'repo "' + projectrepo + ' must be of the form git://github.com/username/project.git'
	else:
            p = {"repo": projectrepo}
            if arches:
                p['arches'] = arches
            if paths and paths[0] != '':
                p['path'] = paths[0]
            if revisions and revisions[0] != '':
                p['revision'] = revisions[0]
            if branches and branches[0] != '':
                p['branch'] = branches[0]
	    p['owner'] = authz.getUsername(req)
	    projects[projectname] = p
	    json.dump(projects, open('projects.json', 'w'), indent=4)
	    subprocess.call(["/usr/bin/buildbot", "reconfig", "/scratch/buildbot/master"])
	    msg = 'added project: ' + ' '.join(req.args.get('projectname', '')) + ' url: ' + ' '.join(req.args.get('projectrepo', ''))
        defer.returnValue((path_to_root(req), msg))

