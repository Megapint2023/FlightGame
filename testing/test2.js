'use strict';

const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const operation = document.getElementById('operation');
const button = document.getElementById('start');
const result = document.getElementById('result');


function operate(num1, num2, operation) {
  let result;
  if (operation === 'add') {
    result = num1 + num2;
  }
  else if (operation === 'sub') {
    result = num1 - num2;
  }
  else if (operation === 'multi') {
    result = num1 * num2;
  }
  else if (operation === 'div') {
    result = num1 / num2;
  }
  return result;
}

button.onclick = function () {
  const number1 = Number(num1.value);
  const number2 = Number(num2.value);
  const selection = operation.value
  const calculation = operate(number1, number2, selection);
  result.textContent = calculation;
};