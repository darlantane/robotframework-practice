import atexit
import os

import cherrypy

from server.rest_resources.RestResource import jsonify_error
from server.rest_resources.challenge_resource import ChallengeResource
from server.rest_resources.player_resource import PlayerResource
from server.xml_resources.xml_demo import PlayersList, ChallengesList

cherrypy.config.update({'environment': 'embedded'})

if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

class Root(object):
    players = PlayerResource()
    challenges = ChallengeResource()
    playerslist = PlayersList()
    challengeslist = ChallengesList()
    @cherrypy.expose
    def index(self):
        return """<html>
          <body>
            <h1> ChiFouMi service</h1>
            <p> See <a href ="static/swagger.yaml" download="swagger.yaml">swagger</a> for documentation ! </p> 
            Author: Raout Formation vincentraout27@gmail.com 
          </body>
        </html>"""

config = {'/':
    {
        'error_page.default': jsonify_error,
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.abspath(os.getcwd()),
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './server/files'
    }
}
application = cherrypy.Application(Root(), "/chifoumi/", config)

