from xml.dom import minidom

import cherrypy

from chi_fou_mi.game import HandSignal
from server.data_model import makeGetFilter, players_dict, challenges_dict


class PlayersList(object):
    @cherrypy.expose
    def default(self, *vpath, **params):
        cherrypy.response.headers['Content-Type'] = 'text/xml;charset=utf-8'
        return players_list_xml(**params)


class ChallengesList(object):
    @cherrypy.expose
    def default(self, *vpath, **params):
        cherrypy.response.headers['Content-Type'] = 'text/xml;charset=utf-8'
        return challenges_list_xml(**params)

def players_list_xml(**kwargs):
    root = minidom.Document()
    xml = root.createElement('PLAYERS')
    root.appendChild(xml)
    filtered = filter(makeGetFilter(**kwargs), players_dict.values())
    for p in filtered:
        player = root.createElement('PLAYER')
        player.setAttribute('id', p.id)
        nam = root.createElement('NAME')
        nam.appendChild(root.createTextNode(p.name))
        player.appendChild(nam)
        emel = root.createElement('EMAIL')
        emel.appendChild(root.createTextNode(p.email))
        player.appendChild(emel)
        handS = root.createElement('HANDSIGNAL')
        handS.appendChild(root.createTextNode(textHandSignal(p.hand_signal)))
        player.appendChild(handS)
        hist = root.createElement('HISTORY')

        for (c, r) in p.history:
            ch = root.createElement('CHALLENGE')
            ch.setAttribute('id', c.id)
            hist.appendChild(ch)

        player.appendChild(hist)
        xml.appendChild(player)
    return root.toprettyxml(indent="\t")

def challenges_list_xml(**kwargs):
    root = minidom.Document()
    xml = root.createElement('CHALLENGES')
    root.appendChild(xml)
    filtered = filter(makeGetFilter(**kwargs), challenges_dict.values())
    for c in filtered:
        challenge = root.createElement('CHALLENGE')
        challenge.setAttribute('id', c.id)
        rounds = root.createElement('ROUNDS')
        rounds.appendChild(root.createTextNode(str(c.numberOfRounds)))
        challenge.appendChild(rounds)

        crounds = root.createElement('CURRENTROUND')
        crounds.appendChild(root.createTextNode(str(c.currentRound)))
        challenge.appendChild(crounds)

        ts = root.createElement('TIMESTAMP')
        ts.appendChild(root.createTextNode(str(c.timestamp)))
        challenge.appendChild(ts)

        P2 = root.createElement('PLAYER')
        P2.setAttribute('id', c.champion.id)
        P2.setAttribute('playertype', "champion")
        challenge.appendChild(P2)

        if c.pending():
            st = root.createElement('STATUS')
            st.appendChild(root.createTextNode("PENDING"))
            challenge.appendChild(st)
        elif not c.game_over():
            P1 = root.createElement('PLAYER')
            P1.setAttribute('id', c.challenger.id)
            P1.setAttribute('playertype', "challenger")
            challenge.appendChild(P1)
            st = root.createElement('STATUS')
            st.appendChild(root.createTextNode("ONGOING"))
            challenge.appendChild(st)
        else:
            P1 = root.createElement('PLAYER')
            P1.setAttribute('id', c.challenger.id)
            P1.setAttribute('playertype', "challenger")
            challenge.appendChild(P1)
            st = root.createElement('STATUS')
            st.appendChild(root.createTextNode("OVER"))
            challenge.appendChild(st)

        if c.game_over():
            if c.score > 0:
                P1 = root.createElement('PLAYER')
                P1.setAttribute('id', c.champion.id)
                P1.setAttribute('playertype', "winner")
                challenge.appendChild(P1)
            elif c.score < 0:
                P1 = root.createElement('PLAYER')
                P1.setAttribute('id', c.challenger.id)
                P1.setAttribute('playertype', "winner")
                challenge.appendChild(P1)

        xml.appendChild(challenge)
    return root.toprettyxml(indent="\t")

def textHandSignal(hs:HandSignal):
    if hs is None: return "Null"
    if hs.Scissors: return "Scissors"
    if hs.Paper: return "Paper"
    if hs.Stone: return "Stone"
