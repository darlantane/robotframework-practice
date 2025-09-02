*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
Test Setup        Clear Game

*** Test Cases ***
test 12-1 signe de la main d’un joueur de chi fou mi Stone
    ${ID}=  Create Player Alice

*** Keywords ***
Create Player Alice
    ${id_alice}=      Create Player    Alice  alice@gmail.com
    Log To Console    ${id_alice}
    [Return]  ${id_alice}

#Babacar joue Stone
#    ${id_babacar}=      Create Player    Babacar  b@gmail.com
#    Player Plays    ${id_babacar}  Stone

