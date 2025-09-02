import cherrypy

from chi_fou_mi.game import Challenge, Player, HandSignal

# All the players that abide the game
# keys : playerId
# values : Player objects
players_dict = {}


# All active challenges
# keys :challengeId
# values : Challenge objects
challenges_dict = {}


# Not testable
# For the webservices
def makeGetFilter(**kwargs):
    def myfilter(x):
        good = True
        if "status" in kwargs.keys() and kwargs["status"] == "ongoing":
            good &= x.ongoing()
        elif "status" in kwargs.keys() and kwargs["status"] == "over":
            good &= x.game_over()
        elif "status" in kwargs.keys() and kwargs["status"] == "pending":
            good &= x.pending()
        if "numberOfRounds" in kwargs.keys():
            good &= (x.numberOfRounds == kwargs["numberOfRounds"])
        if "currentRound" in kwargs.keys():
            good &= (x.currentRound == kwargs["currentRound"])
        if "championId" in kwargs.keys():
            good &= (x.champion.id == kwargs["championId"])
        if "challengerId" in kwargs.keys():
            if x.challenger is None:
                good = False
            else:
                good &= (x.challenger.id == kwargs["challengerId"])
        if "name" in kwargs.keys():
            good &= (x.name == kwargs["name"])
        if "email" in kwargs.keys():
            good &= (x.email == kwargs["email"])

        return good

    return myfilter


# Not testable
# For the webservices
def players_list(**kwargs):
    ret = []
    filtered = filter(makeGetFilter(**kwargs), players_dict.values())
    for p in filtered:
        ret.append(p.to_dict_simple())
    return ret


# Not testable
# For the webservices
def challenges_list(**kwargs):
    ret = []
    filtered = filter(makeGetFilter(**kwargs), challenges_dict.values())
    for c in filtered:
        ret.append(c.to_dict(True))
    return ret


# May be used for test purpose
# @parameter playerId : generated playerId Id
def check_player_existence(playerId):
    if playerId not in players_dict.keys():
        raise cherrypy.HTTPError(404, message="Player not found.")


# May be used for test purpose
# @parameter challengeId : generated challenge Id
def check_challenge_existence(challengeId):
    if challengeId not in challenges_dict.keys():
        raise cherrypy.HTTPError(404, message="Challenge not found.")


# May be used for test purpose
# @parameter handsignal :  string, "HandSignal.Scissors",  "HandSignal.Paper", "HandSignal.Stone"
# are the only valid values
def check_hand_signal_existence(handsignal):
    if handsignal not in ("HandSignal.Scissors", "HandSignal.Paper", "HandSignal.Stone"):
        raise cherrypy.HTTPError(422, message="Hand signal does not exist.")


# May be used for test purpose
# @parameter playerId : generated player Id
def check_players_opened_challenges(playerId):
    player: Player = players_dict[playerId]
    if len(list(filter(makeGetFilter(status="pending"), player.history))) > 2:
        raise cherrypy.HTTPError(409, message="Player has too many challenges opened")


# May be used for test purpose
# @parameter email : unchecked email
def check_player_email_unicity(email):
    for p in filter(makeGetFilter(email=email), players_dict.values()):
        if p.email == email:
            raise cherrypy.HTTPError(409, message="A user with this email already exists")


# May be used for test purpose
# @parameter challengeId : generated challenge Id
def check_challenge_is_pending(challengeId):
    if not challenges_dict[challengeId].pending():
        raise cherrypy.HTTPError(409, message="Can't join a non-pending challenge")


# May be used for test purpose
# @parameter challengeId : generated challenge Id
def check_challenge_is_ongoing(challengeId):
    if not challenges_dict[challengeId].ongoing():
        raise cherrypy.HTTPError(409, message="Can't play a round on a challenge that's not ongoing")


# May be used for test purpose
# @parameter challengeId : generated challenge Id
def check_challenge_is_deletable(challengeId):
    if not challenges_dict[challengeId].pending():
        raise cherrypy.HTTPError(409, message="Can't delete a non-pending challenge")


# May be used for test purpose
# @parameter challengeId : generated challenge Id
def get_player(playerId):
    return players_dict[playerId].to_dict()


# May be used for test purpose
# @parameter data : dictionary containing "name" and "email" entries
# @return dictionnary mapping of the player's data
def put_player(data):
    player = Player(data["name"], data["email"])
    players_dict[player.id] = player
    return player.to_dict_simple()


# May be used for test purpose
# @parameter playerId : generated challenge Id
# @return dictionnary mapping of the challenges's data
def get_challenge(challengeId):
    return challenges_dict[challengeId].to_dict(False)


# May be used for test purpose
# @parameter playerId : generated player Id
# @parameter handsignal :  string, may be "HandSignal.Scissors",  "HandSignal.Paper", "HandSignal.Stone"
# @return dictionnary mapping of the player's data
def player_play(playerId, handsignal):
    player = players_dict[playerId]
    if handsignal == "HandSignal.Scissors":
        player.hand_signal = HandSignal.Scissors
    elif handsignal == "HandSignal.Paper":
        player.hand_signal = HandSignal.Paper
    elif handsignal == "HandSignal.Stone":
        player.hand_signal = HandSignal.Stone
    return player.to_dict()


# May be used for test purpose
# @parameter playerId : generated player Id
# @parameter rounds :  optional integer,
# @return dictionnary mapping of the challenges's data
def challenge_start(playerId, rounds=3):
    player: Player = players_dict[playerId]
    ch = Challenge(champion=player, numberOfRounds=rounds)
    challenges_dict[ch.id] = ch
    return ch.to_dict(True)


# May be used for test purpose
# @parameter playerId : generated player Id
# @parameter rounds :  optional integer,
# @return dictionnary mapping of the challenges's data
def challenge_join(playerId, challengeId):
    player = players_dict[playerId]
    ch = challenges_dict[challengeId]
    ch.challenger = player
    return ch.to_dict(True)


# May be used for test purpose
# @parameter challengeId : generated challenge Id
# @return dictionnary mapping of the challenges's data
def challenge_playround(challengeId):
    ch = challenges_dict[challengeId]
    ch.play_round()
    return ch.to_dict(False)


# May be used for test purpose
# @parameter challengeId : generated challenge Id
# @return dictionnary mapping of the challenges's data
def delete_challenge(challengeId):
    deleted = challenges_dict[challengeId].to_dict(False)
    challenges_dict.pop(challengeId)
    return deleted


Alice = Player("Alice", "alice@testdata.com")
Bob = Player("Bob", "bob@testdata.com")
Charly = Player("Charly", "charly@testdata.com")
players_dict[str(Alice.id)] = Alice
players_dict[str(Bob.id)] = Bob
players_dict[str(Charly.id)] = Charly
game1 = Challenge(Alice, Bob, 1)
Alice.hand_signal = HandSignal.Paper
Bob.hand_signal = HandSignal.Scissors
game1.play_round()
game2 = Challenge(Charly, Alice, 1)
Charly.hand_signal = HandSignal.Paper
Alice.hand_signal = HandSignal.Scissors
game2.play_round()
game3 = Challenge(Bob, Charly, 1)
game4 = Challenge(Alice, Bob, 3)
Alice.hand_signal = HandSignal.Paper
Bob.hand_signal = HandSignal.Scissors
game4.play_round()
Alice.hand_signal = HandSignal.Stone
Bob.hand_signal = HandSignal.Scissors
game4.play_round()
Alice.hand_signal = HandSignal.Scissors
Bob.hand_signal = HandSignal.Paper
game4.play_round()
game5 = Challenge(Charly, Alice, 3)
Alice.hand_signal = HandSignal.Paper
Charly.hand_signal = HandSignal.Scissors
game5.play_round()
Alice.hand_signal = HandSignal.Stone
Charly.hand_signal = HandSignal.Scissors
game5.play_round()
Alice.hand_signal = HandSignal.Scissors
Charly.hand_signal = HandSignal.Paper
game5.play_round()
game6 = Challenge(Bob, Charly, 3)
Bob.hand_signal = HandSignal.Scissors
Charly.hand_signal = HandSignal.Paper
game6.play_round()
game7 = Challenge(Alice, numberOfRounds=3)
game8 = Challenge(Alice, numberOfRounds=5)
challenges_dict[game1.id] = game1
challenges_dict[game2.id] = game2
challenges_dict[game3.id] = game3
challenges_dict[game4.id] = game4
challenges_dict[game5.id] = game5
challenges_dict[game6.id] = game6
challenges_dict[game7.id] = game7
challenges_dict[game8.id] = game8

