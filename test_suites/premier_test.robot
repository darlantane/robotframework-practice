*** Settings ***
Library           test_library/ChiFouMiKeyWords.py
*** Variables ***
${ID_JOUEUR}
*** Test Cases ***
premier test
    Should Be Equal    ${True}  ${True}
    
creation joueur
    ${ID_JOUEUR}=  create player    Babacar  babacar@gmail.com
    Log To Console    ${ID_JOUEUR}
    