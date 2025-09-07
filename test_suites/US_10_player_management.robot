*** Settings ***
Documentation     Player management.
Library           test_library/ChiFouMiKeyWords.py
Test Setup       Clear Game


*** Test Cases ***
TEST 10-1: player creation
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    ${existence}=  check player exists in system  ${PLAYER_A}
    ${name}=  Get Player Characteristic  ${PLAYER_A}  name
    ${email}=  Get Player Characteristic  ${PLAYER_A}  email
    Should Be Equal  ${existence}  ${True}
    Should Be Equal  ${name}  Alice
    Should Be Equal  ${email}  alice@gmail.com

TEST 10-2: 2 players creation, different emails
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    ${PLAYER_B}=  Create Player  Alice  bob@gmail.com
    ${existenceA}=  check player exists in system  ${PLAYER_A}
    ${existenceB}=  check player exists in system  ${PLAYER_B}
    Should Be Equal  ${existenceA}  ${True}
    Should Be Equal  ${existenceB}  ${True}

TEST 10-3: 2 players creation, same emails
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    ${PLAYER_B}=  Create Player  Bob  alice@gmail.com
    ${existenceA}=  check player exists in system  ${PLAYER_A}
    ${existenceB}=  check player exists in system  ${PLAYER_B}
    Log To Console  ${PLAYER_B}
    Should Be Equal  ${existenceA}  ${True}
    Should Be Equal  ${existenceB}  ${False}

TEST 12-1: player handsignal Stone
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    Player Plays  ${PLAYER_A}  Stone
    ${handSignal}=  Get Player Characteristic  ${PLAYER_A}  handSignal
    Should Be Equal  ${handSignal}  Stone

TEST 12-2: player handsignal Scissors
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    Player Plays  ${PLAYER_A}  Scissors
    ${handSignal}=  Get Player Characteristic  ${PLAYER_A}  handSignal
    Should Be Equal  ${handSignal}  Scissors

TEST 12-3: player handsignal Paper
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    Player Plays  ${PLAYER_A}  Paper
    ${handSignal}=  Get Player Characteristic  ${PLAYER_A}  handSignal
    Should Be Equal  ${handSignal}  Paper

