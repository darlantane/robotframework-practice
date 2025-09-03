*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game

*** Test Cases ***
Test 12-1 Joueur choisit Stone
    ${player_id}=    Create Player    Alice    alice@test.com
    Player Plays    ${player_id}    Stone
    ${hand}=    Get Player Characteristic    ${player_id}    handSignal
    Should Be Equal    ${hand}    Stone

Test 12-2 Joueur choisit Scissors
    ${player_id}=    Create Player    Bob    bob@test.com
    Player Plays    ${player_id}    Scissors
    ${hand}=    Get Player Characteristic    ${player_id}    handSignal
    Should Be Equal    ${hand}    Scissors

Test 12-3 Joueur choisit Paper
    ${player_id}=    Create Player    Charlie    charlie@test.com
    Player Plays    ${player_id}    Paper
    ${hand}=    Get Player Characteristic    ${player_id}    handSignal
    Should Be Equal    ${hand}    Paper
