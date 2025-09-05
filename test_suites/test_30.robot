*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game
Resource    chifoumi.resource

*** Test Cases ***
TEST 30 : jouer une manche de chi fou mi / test 30-1 scissors vs paper
    Create a 1 round challenge between player A and player B
    Player A end B play a round  Scissors  Paper
    ${winner}=  get challenge characteristic  ${GAME}  winner
    Should Be Equal    champion   ${winner}

TEST 30 : jouer une manche de chi fou mi / test 30-2 scissors vs stone
    Create a 1 round challenge between player A and player B
    Player A end B play a round  Scissors  Stone
    ${winner}=  get challenge characteristic  ${GAME}  winner
    Should Be Equal    challenger   ${winner}

TEST 30 : jouer une manche de chi fou mi / test 30-3 paper vs stone
    Create a 1 round challenge between player A and player B
    Player A end B play a round  Paper  Stone
    ${winner}=  get challenge characteristic  ${GAME}  winner
    Should Be Equal    champion   ${winner}

TEST 30 : jouer une manche de chi fou mi / test 30-4 draw
    Create a 1 round challenge between player A and player B
    Player A end B play a round  Paper  Paper
    ${winner}=  get challenge characteristic  ${GAME}  winner
    Should Be Equal    nobody   ${winner}
