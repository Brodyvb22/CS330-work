/* jshint esversion: 8 */
/* jshint browser: true */
'use strict';

var outputScreen;
var clearOnEntry;


/**
 * Display a digit on the `outputScreen`
 * 
 * @param {number} digit digit to add or display on the `outputScreen`
 */
function enterDigit(digit) {
    if (clearOnEntry) {
        outputScreen.textContent = "";
        clearOnEntry = false;
    }

    outputScreen.textContent += digit;
}


/**
 * Clear `outputScreen` and set value to 0
 */
function clear_screen() {
    outputScreen.textContent = "0";
    clearOnEntry = true;
}


/**
 * Evaluate the expression and display its result or *ERROR*
 */
function eval_expr() {
    try {
        let result = eval(outputScreen.textContent);
        outputScreen.textContent = result;
    } catch (e) {
        outputScreen.textContent = "ERROR";
    }
    clearOnEntry = true;
}


/**
 * Display an operation on the `outputScreen`
 * 
 * @param {string} operation to add to the expression
 */
function enterOp(operation) {
    if (clearOnEntry) {
        clearOnEntry = false;
    }

    let lastChar = outputScreen.textContent.slice(-1);

    outputScreen.textContent += operation;
}


window.onload = function () {
    outputScreen = document.querySelector("#result");
    clearOnEntry = true;
    outputScreen.textContent = "0";
};
