*** Settings ***
Library           test_library/ChiFouMiKeyWords.py

*** Test Cases ***
*** Test Cases ***
Test 40-1 Joueur A gagne tout
    [Setup]    Clear Game
    ${A}=    Create Player    A    a@mail.com
    ${challenge}=    Player Initiates Challenge In Rounds    ${A}    3
    ${B}=    Create Player    B    b@mail.com
    Player Joins Challenge    ${B}    ${challenge}

    # Round 1
    Player Plays    ${A}    Stone
    Player Plays    ${B}    Scissors
    Play A Round Of    ${challenge}

    # Round 2
    Player Plays    ${A}    Stone
    Player Plays    ${B}    Scissors
    Play A Round Of    ${challenge}

    # Round 3
    Player Plays    ${A}    Stone
    Player Plays    ${B}    Scissors
    Play A Round Of    ${challenge}

    Should Be Equal    ${challenge_state}=    Get Challenge Characteristic    ${challenge}    handsignal
    Should Be Equal    ${champion}=    Get Challenge Characteristic    ${challenge}    champion    ${A}
    Should Be Equal As Integers    ${ranking_A}=    Get Player Characteristic    ${A}    ranking    1
    Should Be Equal As Integers    ${ranking_B}=    Get Player Characteristic    ${B}    ranking    -1


Test 40-2 Joueur B gagne tout
    [Setup]    Clear Game
    ${A}=    Create Player    A    a@mail.com
    ${challenge}=    Player Initiates Challenge In Rounds    ${A}    3
    ${B}=    Create Player    B    b@mail.com
    Player Joins Challenge    ${B}    ${challenge}

    # B gagne toujours
    Player Plays    ${A}    SCISSORS
    Player Plays    ${B}    ROCK
    Play A Round Of    ${challenge}
    Player Plays    ${A}    SCISSORS
    Player Plays    ${B}    ROCK
    Play A Round Of    ${challenge}
    Player Plays    ${A}    SCISSORS
    Player Plays    ${B}    ROCK
    Play A Round Of    ${challenge}

    Should Be Equal    ${challenge_state}=    Get Challenge Characteristic    ${challenge}    state    over
    Should Be Equal    ${champion}=    Get Challenge Characteristic    ${challenge}    champion    ${B}
    Should Be Equal As Integers    ${ranking_A}=    Get Player Characteristic    ${A}    ranking    -1
    Should Be Equal As Integers    ${ranking_B}=    Get Player Characteristic    ${B}    ranking    1


Test 40-3 Égalité
    [Setup]    Clear Game
    ${A}=    Create Player    A    a@mail.com
    ${challenge}=    Player Initiates Challenge In Rounds    ${A}    2
    ${B}=    Create Player    B    b@mail.com
    Player Joins Challenge    ${B}    ${challenge}

    # A gagne le premier round
    Player Plays    ${A}    ROCK
    Player Plays    ${B}    SCISSORS
    Play A Round Of    ${challenge}

    # B gagne le deuxième round
    Player Plays    ${A}    SCISSORS
    Player Plays    ${B}    ROCK
    Play A Round Of    ${challenge}

    Should Be Equal    ${challenge_state}=    Get Challenge Characteristic    ${challenge}    state    over
    Should Be Equal    ${champion}=    Get Challenge Characteristic    ${challenge}    champion    nobody
    Should Be Equal As Integers    ${ranking_A}=    Get Player Characteristic    ${A}    ranking    -1
    Should Be Equal As Integers    ${ranking_B}=    Get Player Characteristic    ${B}    ranking    -1