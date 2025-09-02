*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game
*** Test Cases ***

test 10-1 Créer un joueur avec un nom et un email
    [Documentation]  documentation
    ${id_vincent}=    Create Player    Vincent  a@.com
    Log To Console    ${id_vincent}
    ${player_exist}=  Check Player Exists In System  ${id_vincent}
    Should Be True    ${player_exist}

test 10-2 Créer deux joueurs avec deux emails différents
    ${id_vincent}=    Create Player    Vincent  a@.com
    Log To Console    ${id_vincent}
    ${player_exist}=  Check Player Exists In System  ${id_vincent}
    Should Be True    ${player_exist}

    ${id_willy}=      Create Player    Vincent  bc@.com
    Log To Console    ${id_willy}
    ${player_exist}=  Check Player Exists In System  ${id_willy}
    Should Be True    ${player_exist}


test 10-3 Créer deux joueurs avec deux emails identiques
    [Documentation]    La création du 2ème joueur doit être refusée
    ${id_vincent}=    Create Player    Vincent   bc@.com
    Log To Console    ${id_vincent}
    ${player_exist_v}=  Check Player Exists In System  ${id_vincent}

    ${id_willy}=      Create Player    Guillaume  bc@.com
    Log To Console    ${id_willy}
    ${player_exist_w}=  Check Player Exists In System  ${id_willy}
    Should Not Be True    ${player_exist_v} and ${player_exist_w}

    Should Be Equal  ${id_willy}  (409, 'A user with this email already exists')