*** Settings ***
Documentation   Fuel Consumption Calculator
Library    SeleniumLibrary

*** Test Cases ***
Fuel Consumption Calculator
    Open browser    https://calcus.ru/kalkulyator-rashoda-topliva
    Input text    name:average_consumption      12
    Input text    name:distance     420
    Input text    name:cost     49,75
    Click button    class:calc-submit
    Sleep   3 seconds
    Close browser

