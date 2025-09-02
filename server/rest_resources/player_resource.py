import cherrypy

from server import data_model
from server.rest_resources.RestResource import RESTResource


class PlayerResource(RESTResource):
    def handle_GET(self, *vpath, **params):
        if len(vpath) > 1:
            raise cherrypy.HTTPError(404, "Resource not found.")
        if len(vpath) == 0:
            return data_model.players_list(**params)
        else:
            data_model.check_player_existence(vpath[0])
            return data_model.get_player(vpath[0])

    def handle_PUT(self, *vpath, **params):
        data = cherrypy.request.json
        try:
            data_model.check_player_email_unicity(data["email"])
            cherrypy.response.status = 201
            return data_model.put_player(data)
        except KeyError:
            raise cherrypy.HTTPError(422, message="Invalid payload")

    def handle_POST(self, *vpath, **params):
        data = cherrypy.request.json
        if len(vpath) != 1:
            raise cherrypy.HTTPError(405, "Method not implemented.")
        try:
            data_model.check_player_existence(vpath[0])
            data_model.check_hand_signal_existence(data["handSignal"])
            cherrypy.response.status = 204
            return data_model.player_play(vpath[0], data["handSignal"])
        except KeyError:
            raise cherrypy.HTTPError(422, message="Invalid payload")
