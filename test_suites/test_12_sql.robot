*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Library           DatabaseLibrary
Test Setup        setup du test
Test Teardown     teardown du test

*** Variables ***
${database_adress}  sakila.db

*** Test Cases ***
test 12-1 signe de la main d’un joueur de chi fou mi Stone
    Create Player Alice
    Alice plays  Stone
    ${handSignal}=  get player characteristic  ${ID_ALICE}  handSignal
    should be equal  Stone  ${handSignal}

test 12-2 signe de la main d’un joueur de chi fou mi Scissors
    Create Player Alice
    Alice plays  Scissors
    ${handSignal}=  get player characteristic  ${ID_ALICE}  handSignal
    should be equal  Scissors  ${handSignal}

test 12-3 signe de la main d’un joueur de chi fou mi Paper
    Create Player Alice
    Alice plays  Paper
    ${handSignal}=  get player characteristic  ${ID_ALICE}  handSignal
    should be equal  Paper  ${handSignal}


*** Keywords ***
setup du test
    Clear Game
    # connection à la base
    Connect To Database   sqlite3   ${database_adress}

teardown du test
    # déconnexion à la fin
    Disconnect From All Databases

Create Player Alice
    # le résultat de la requête va dans dans la variable ${resultat}, c'est un TABLEAU
    ${resultat}=  Query    select first_name, email from customer where first_name like 'ALICE%';
    # 1ère ligne 1ère colonne
    Log To Console    ${resultat}[0][0]
    # 1ère ligne 2ème colonne
    Log To Console    ${resultat}[0][1]
    # on crée le joueur à partir du résultat
    ${id}=      Create Player     ${resultat}[0][0]  ${resultat}[0][1]
    set test variable  ${ID_ALICE}  ${id}
    Log To Console    ${ID_ALICE}

Alice plays
    [Arguments]  ${hand}
    Player plays  ${ID_ALICE}  ${hand}

