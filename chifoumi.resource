*** Settings ***
Library           test_library/ChiFouMiKeyWords.py

*** Keywords ***
Create a 1 round challenge between player A and player B
    ${idA}=  Create Player    A  a@a.com
    ${idB}=  Create Player    B  b@a.com
    Set Test Variable    ${PLAYER_A}  ${idA}    
    Set Test Variable    ${PLAYER_B}  ${idB}
    ${id_challenge}=  Player Initiates Challenge In Rounds    ${idA}  1
    Player Joins Challenge    ${idB}  ${id_challenge}
    Set Test Variable  ${GAME}  ${id_challenge}
    
Player A end B play a round
    [Arguments]    ${hand_A}  ${hand_B}
    Player Plays    ${PLAYER_A}  ${hand_A} 
    Player Plays    ${PLAYER_B}  ${hand_B}
    Play A Round Of    ${GAME}