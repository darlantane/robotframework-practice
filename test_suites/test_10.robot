*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game
*** Test Cases ***

test 10-1 Créer un joueur avec un nom et un email
    [Documentation]  documentation
    ${id_darlan}=    Create Player    Darlan  d@.com
    Log To Console    ${id_darlan}
    ${player_exist}=  Check Player Exists In System  ${id_darlan}
    Should Be True    ${player_exist}

test 10-2 Créer deux joueurs avec deux emails différents
    ${id_darlan}=    Create Player    Darlan  d@.com
    Log To Console    ${id_darlan}
    ${player_exist}=  Check Player Exists In System  ${id_darlan}
    Should Be True    ${player_exist}

    ${id_willy}=      Create Player    Darlan  w@.com
    Log To Console    ${id_willy}
    ${player_exist}=  Check Player Exists In System  ${id_willy}
    Should Be True    ${player_exist}


test 10-3 Créer deux joueurs avec deux emails identiques
    [Documentation]    La création du 2ème joueur doit être refusée
    ${id_darlan}=    Create Player    Darlan   d@.com
    Log To Console    ${id_darlan}
    ${player_exist_v}=  Check Player Exists In System  ${id_darlan}

    ${id_willy}=      Create Player    Guillaume  d@.com
    Log To Console    ${id_willy}
    ${player_exist_w}=  Check Player Exists In System  ${id_willy}
    Should Not Be True    ${player_exist_v} and ${player_exist_w}

    Should Be Equal  ${id_willy}  (409, 'A user with this email already exists')
    
test 10-4 Cloner un joueur
    [Documentation]  documentation
    ${id_vincent}=    Create Player    Vincent  a@.com
    Log To Console    ${id_vincent}
    ${clone_id}=   Clone Player    ${id_vincent}
    ${clone_exist}=  Check Player Exists In System    ${clone_id}
    ${clone_name}=  Get Player Characteristic    ${clone_id}  name
    ${vincent_name}=  Get Player Characteristic    ${id_vincent}  name
    Should Be Equal    ${clone_name}  ${vincent_name}
    ${clone_email}=  Get Player Characteristic    ${clone_id}  email
    ${vincent_email}=  Get Player Characteristic    ${id_vincent}  email
    ${new_vincent_email}=  Catenate     SEPARATOR=  clone-  ${vincent_email}
    Should Be Equal    ${clone_email}  ${new_vincent_email}