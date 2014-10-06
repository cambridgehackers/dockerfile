
import buildbot
import jinja2
import json
import subprocess
import sys
import twisted
from twisted.python import log
from twisted.internet import defer
from buildbot.status.web.base import ActionResource
from buildbot.status.web.base import HtmlResource
from buildbot.status.web.base import path_to_root


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
	res = yield authz.actionAllowed('forceAllBuilds', req)
	projects = json.load(open('projects.json'))
        log.msg('loaded projects.json')

        projectname = req.args.get('projectname', [])[0]
	projectrepo = req.args.get('projectrepo', [])[0]
	if projectname not in projects:
	    projects[projectname] = {"repo": projectrepo}
	    json.dump(projects, open('projects.json', 'w'))
	    subprocess.call(["/usr/bin/buildbot", "reconfig", "/scratch/buildbot/master"])
	    msg = 'added project: ' + ' '.join(req.args.get('projectname', '')) + ' url: ' + ' '.join(req.args.get('projectrepo', ''))
	else:
	    msg = 'project ' + projectname + ' already exists'
        defer.returnValue((path_to_root(req), msg))

