'use strict';

const input = document.getElementById('calculation');
const button = document.getElementById('start');
const result = document.getElementById('result');

button.addEventListener("click", function () {
  const text = input.value.trim();
  let num1, num2, anwser;

  if (text.includes('+')) {
     const parts = text.split("+");
     num1 = parseInt(parts[0]);
     num2 = parseInt(parts[1]);
     anwser = num1 + num2;
  }
  else if (text.includes('-')) {
       const parts = text.split("-");
       num1 = parseInt(parts[0]);
       num2 = parseInt(parts[1]);
       anwser = num1 - num2;
  }
  else if (text.includes('*')) {
       const parts = text.split("*");
       num1 = parseInt(parts[0]);
       num2 = parseInt(parts[1]);
       anwser = num1 * num2;
  }
  else if (text.includes('/')) {
    const parts = text.split("/");
    num1 = parseInt(parts[0]);
    num2 = parseInt(parts[1]);
    anwser = num1 / num2;

  }
  else {
    result.textContent = "Error, check input";
    return;
  }
  result.textContent = "Result:" + anwser;
});