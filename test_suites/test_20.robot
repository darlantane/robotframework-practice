*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game

*** Test Cases ***
Test 20 - Créer un défi en 3 rounds
    [Setup]    Clear Game
    ${playerA_id}=    Create Player    Alice    alice@test.com
    ${challenge_id}=    Player Initiates Challenge In Rounds    ${playerA_id}    3

    ${exists}=    Check Challenge Exists In System    ${challenge_id}
    Should Be True    ${exists}

    ${status}=    Get Challenge Characteristic    ${challenge_id}    status
    Should Be Equal    ${status}    pending

    ${champion}=    Get Challenge Characteristic    ${challenge_id}    champion
    Should Be Equal    ${champion}    ${playerA_id}

Test 21 - Rejoindre un défi
    [Setup]    Clear Game
    ${playerA_id}=    Create Player    Alice    alice@test.com
    ${challenge_id}=    Player Initiates Challenge In Rounds    ${playerA_id}    3

    ${playerB_id}=    Create Player    Bob    bob@test.com
    Player Joins Challenge    ${playerB_id}    ${challenge_id}

    ${status}=    Get Challenge Characteristic    ${challenge_id}    status
    Should Be Equal    ${status}    ongoing

    ${challenger}=    Get Challenge Characteristic    ${challenge_id}    challenger
    Should Be Equal    ${challenger}    ${playerB_id}

