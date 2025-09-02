import cherrypy

from server import data_model
from server.rest_resources.RestResource import RESTResource


class ChallengeResource(RESTResource):
    def handle_GET(self, *vpath, **params):
        if len(vpath) > 1:
            raise cherrypy.HTTPError(404, "Resource not found.")
        if len(vpath) == 0:
            return data_model.challenges_list(**params)
        else:
            data_model.check_challenge_existence(vpath[0])
            return data_model.get_challenge(vpath[0])

    def handle_PUT(self, *vpath, **params):
        data = cherrypy.request.json
        if len(vpath) != 0:
            raise cherrypy.HTTPError(404, message="Resource not found.")
        data_model.check_players_opened_challenges(data["champion"]["id"])
        try:
            champion_id = data["champion"]["id"]
            number_of_rounds = data["numberOfRounds"]
        except KeyError:
            raise cherrypy.HTTPError(422, message="Invalid payload")

        cherrypy.response.status = 201
        return data_model.challenge_start(champion_id, number_of_rounds)

    def handle_POST(self, *vpath, **params):
        data = cherrypy.request.json
        if len(vpath) < 2:
            raise cherrypy.HTTPError(405, "Method not implemented.")
        data_model.check_challenge_existence(vpath[0])

        if vpath[1] == "join":
            try:
                challenger_id = data["challenger"]["id"]
            except KeyError:
                raise cherrypy.HTTPError(422, message="Invalid payload")
            data_model.check_challenge_is_pending(vpath[0])
            return data_model.challenge_join(challenger_id, vpath[0])
        elif vpath[1] == "playround":
            data_model.check_challenge_is_ongoing(vpath[0])
            return data_model.challenge_playround(vpath[0])
        else:
            raise cherrypy.HTTPError(404, message="Resource not found.")

    def handle_DELETE(self, *vpath, **params):
        if len(vpath) == 0:
            raise cherrypy.HTTPError(405, "Method not implemented.")
        data_model.check_challenge_existence(vpath[0])
        data_model.check_challenge_is_deletable(vpath[0])
        cherrypy.response.status = 204
        return data_model.delete_challenge(vpath[0])
