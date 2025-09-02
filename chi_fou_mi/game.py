import copy
import uuid
from datetime import datetime
from enum import Enum


class Player:
    def __init__(self, name, email):
        self.id = str(uuid.uuid1())
        self.name = name
        self.email = email
        self.hand_signal = None
        self.history = []
        self.ranking = 0

    def historicize(self, challlenge, result):
        self.history.append((challlenge, result))
        self.ranking += result.value

    def to_dict(self):
        dict = self.to_dict_simple()
        dict["email"] = self.email
        dict["handSignal"] = str(self.hand_signal)
        if len(self.history) > 0:
            h = []
            for (c, r) in self.history:
                h.append(c.to_dict(True))
            dict["history"] = h
        return dict

    def to_dict_simple(self):
        dict = {}
        dict["type"] = "chiFouMiPlayer"
        dict["id"] = str(self.id)
        dict["name"] = self.name
        dict["ranking"] = self.ranking
        dict["link"] = "/chifoumi/players/" + self.id
        return dict


class HandSignal(Enum):
    Paper = 0
    Scissors = 1
    Stone = 2


class Result(Enum):
    Draw = 0
    Win = 1
    Loose = -1


class Round:
    def __init__(self, champion: Player, challenger: Player):
        self.champion = champion
        self.challenger = challenger

    def match(self):
        self.champion_hand_signal = copy.copy(self.champion.hand_signal)
        self.challenger_hand_signal = copy.copy(self.challenger.hand_signal)
        if self.champion.hand_signal is None and self.challenger.hand_signal is not None:
            return Result.Loose
        elif self.champion.hand_signal is not None and self.challenger.hand_signal is None:
            return Result.Win
        elif self.champion.hand_signal is not None and self.challenger.hand_signal is not None:
            if self.champion.hand_signal.value - self.challenger.hand_signal.value == 1 \
                    or self.champion.hand_signal.value - self.challenger.hand_signal.value == -2:
                return Result.Win
            elif self.champion.hand_signal.value - self.challenger.hand_signal.value == -1 \
                    or self.champion.hand_signal.value - self.challenger.hand_signal.value == 2:
                return Result.Loose
        return Result.Draw


class Challenge:
    def __init__(self, champion: Player, challenger: Player = None, numberOfRounds=3):
        self.id = str(uuid.uuid1())
        self.timestamp = datetime.now()
        self.champion = champion
        self.challenger = challenger
        self.numberOfRounds = numberOfRounds
        self.score = 0
        self.currentRound = 0
        self.rounds = []

    def play_round(self):
        if not self.game_over():
            e = Round(self.champion, self.challenger)
            self.score += e.match().value
            self.rounds.append(e)
            self.currentRound += 1
            if self.game_over():
                if self.score > 0:
                    self.champion.historicize(self, Result.Win)
                    self.challenger.historicize(self, Result.Loose)
                elif self.score < 0:
                    self.champion.historicize(self, Result.Loose)
                    self.challenger.historicize(self, Result.Win)
                else:
                    self.champion.historicize(self, Result.Loose)
                    self.challenger.historicize(self, Result.Loose)

    def game_over(self):
        return self.currentRound == self.numberOfRounds

    def pending(self):
        return self.challenger is None

    def ongoing(self):
        return not (self.pending() or self.game_over())

    def get_winner(self):
        if self.game_over():
            if self.score > 0:
                return self.champion
            elif self.score < 0:
                return self.challenger
            else:
                # Nobody wins !
                return None
        else:
            return None

    def to_dict(self, partial):
        dict = {}
        dict["type"] = "chiFouMiChallenge"
        dict["id"] = str(self.id)
        dict["currentRound"] = str(self.currentRound)
        dict["timestamp"] = str(self.timestamp)
        dict["champion"] = self.champion.to_dict_simple()
        dict["link"] = "/chifoumi/challenges/" + self.id
        if self.pending():
            dict["status"] = "pending"
        elif not self.game_over():
            dict["challenger"] = self.challenger.to_dict_simple()
            dict["status"] = "ongoing"
        else:
            dict["challenger"] = self.challenger.to_dict_simple()
            dict["status"] = "over"

        if self.game_over():
            if self.score > 0:
                dict["winner"] = "champion"
            elif self.score < 0:
                dict["winner"] = "challenger"
            else:
                dict["winner"] = "nobody"
        if len(self.rounds) > 0 and not partial:
            rnds = []
            dict["rounds"] = rnds
            for rounds in self.rounds:
                dictr = {}
                dictr["championHandSignal"] = str(rounds.champion_hand_signal)
                dictr["challengerHandSignal"] = str(rounds.challenger_hand_signal)
                rnds.append(dictr)
        return dict
