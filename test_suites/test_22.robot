*** Settings ***
Library           test_library/ChiFouMiKeyWords.py

*** Test Cases ***
test 22_1 Challenge 1 round
    [Setup]  Clear Game
    ${playerA_id}=  Create Player  louis  l@gmail.com
    ${challenge_id}=  Player Initiates Challenge In Rounds    ${playerA_id}  1
    ${cancel}=  Player Cancels Challenge    ${playerA_id}  ${challenge_id}
    Should Be True       ${cancel}
    ${exists}=    Check Challenge Exists In System    ${challenge_id}
    Should Not Be True   ${exists}

test 22_2 Challenge 1 round 2 joueurs
    [Setup]  Clear Game
    ${playerA_id}=  Create Player  louis  l@gmail.com
    ${challenge_id}=  Player Initiates Challenge In Rounds    ${playerA_id}  1
    ${playerB_id}=  Create Player  Thaïs  t@gmail.com
    ${playerB_accept}=  Player Joins Challenge    ${playerB_id}  ${challenge_id}
    ${cancel}=  Player Cancels Challenge    ${playerA_id}  ${challenge_id}
    Should Not Be True    ${cancel}
    ${exists}=    Check Challenge Exists In System    ${challenge_id}
    Should Be True    ${exists}

