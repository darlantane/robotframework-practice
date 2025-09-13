*** Settings ***
Documentation     Challenge management.
...               Keywords are defined in the suite file.
Library           test_library/ChiFouMiKeyWords.py
Test Setup       Clear Game


*** Test Cases ***
TEST 20: challenge is created
    [Documentation]    Créer un défi chi fou mi
    Create player Alice
    ${AB_CHALLENGE}=  Player Initiates Challenge In Rounds   ${ALICE}  3
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${True}
    ${status}=  Get Challenge Characteristic  ${AB_CHALLENGE}  status
    ${champion}=  Get Challenge Characteristic  ${AB_CHALLENGE}  champion
    Should Be Equal  ${status}  pending
    Should Be Equal  ${champion}  ${ALICE}

TEST 21: challenge is joined
    [Documentation]    Rejoindre un défi chi fou mi
    Create player Alice
    ${AB_CHALLENGE}=  Player Initiates Challenge In Rounds   ${ALICE}  3
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${True}
    Create player Bob
    Player Joins Challenge  ${BOB}  ${AB_CHALLENGE}
    ${status}=  Get Challenge Characteristic    ${AB_CHALLENGE}  status
    ${challenger}=  Get Challenge Characteristic    ${AB_CHALLENGE}  challenger
    Should Be Equal  ${status}  ongoing
    Should Be Equal  ${challenger}  ${BOB}


TEST 22-1: challenge is cancelled
    [Documentation]    Annuler un défi chi fou mi
    Create player Alice
    ${AB_CHALLENGE}=  Player Initiates Challenge In Rounds   ${ALICE}  3
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${True}
    Player Cancels Challenge  ${ALICE}  ${AB_CHALLENGE}
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${False}

TEST 22-2: challenge is not cancelled
    [Documentation]    Annuler un défi chi fou mi
    Create player Alice
    ${AB_CHALLENGE}=  Player Initiates Challenge In Rounds   ${ALICE}  3
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${True}
    Create player Bob
    Player Joins Challenge  ${BOB}  ${AB_CHALLENGE}
    Player Cancels Challenge  ${ALICE}  ${AB_CHALLENGE}
    ${existenceC}=  Check Challenge Exists In System  ${AB_CHALLENGE}
    Should Be Equal    ${existenceC}  ${True}

*** Keywords ***
Create player Alice
    ${PLAYER_A}=  Create Player  Alice  alice@gmail.com
    Set Test Variable     ${ALICE}  ${PLAYER_A}

Create player Bob
    ${PLAYER_B}=  Create Player  Bob  bob@gmail.com
    Set Test Variable     ${BOB}  ${PLAYER_B}
