import cherrypy
from cherrypy import HTTPError
from robot.api.deco import library, keyword

from server import data_model


@library(scope='SUITE', auto_keywords=True)
class ChiFouMiKeyWords:
    def __init__(self):
        self.datamodel = data_model

    @keyword
    def create_player(self, name, email):
        try:
            self.datamodel.check_player_email_unicity(email)
            tmp = self.datamodel.put_player({"name": name, "email": email})
            return tmp["id"]
        except cherrypy.HTTPError as e:
            return str(e)

    @keyword
    def player_initiates_challenge_in_rounds(self, player_ID, NB_rounds: int):
        # data_model.check_players_opened_challenges(player_ID)
        tmp = self.datamodel.challenge_start(player_ID, NB_rounds)
        return tmp["id"]

    @keyword
    def player_joins_challenge(self, player_ID, challenge_ID):
        self.datamodel.check_challenge_is_pending(challenge_ID)
        self.datamodel.challenge_join(player_ID, challenge_ID)

    @keyword
    def player_cancels_challenge(self, player_ID, challenge_ID):
        try:
            self.datamodel.check_challenge_is_deletable(challenge_ID)
            self.datamodel.delete_challenge(challenge_ID)
            return True
        except cherrypy.HTTPError:
            return False

    @keyword
    def play_a_round_of(self, challenge_ID):
        self.datamodel.check_challenge_is_ongoing(challenge_ID)
        self.datamodel.challenge_playround(challenge_ID)

    @keyword
    def player_plays(self, player_ID, gesture):
        g = "HandSignal." + gesture
        self.datamodel.check_hand_signal_existence(g)
        self.datamodel.player_play(player_ID, g)

    @keyword
    def get_challenge_characteristic(self, challenge_ID, characteristic):
        if characteristic in ("challenger", "champion"):
            to_dict = self.datamodel.challenges_dict[challenge_ID].to_dict(False)[characteristic]
            return to_dict["id"]
        else:
            to_dict = self.datamodel.challenges_dict[challenge_ID].to_dict(False)
            return to_dict[characteristic]

    @keyword
    def get_player_characteristic(self, player_ID, characteristic):
        if characteristic == "handSignal":
            to_dict = self.datamodel.players_dict[player_ID].to_dict()
            return to_dict[characteristic][11:]
        else:
            to_dict = self.datamodel.players_dict[player_ID].to_dict()
            if characteristic == "ranking":
                return int(to_dict[characteristic])
            else:
                return to_dict[characteristic]


    @keyword
    def clear_game(self):
        self.datamodel.challenges_dict = {}
        self.datamodel.players_dict = {}


    @keyword
    def check_player_exists_in_system(self, player_ID):
        try:
            self.datamodel.check_player_existence(player_ID)
            return True
        except cherrypy.HTTPError:
            return False


    @keyword
    def check_challenge_exists_in_system(self, challenge_ID):
        try:
            self.datamodel.check_challenge_existence(challenge_ID)
            return True
        except cherrypy.HTTPError:
            return False
