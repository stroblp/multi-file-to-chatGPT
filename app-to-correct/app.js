const screen = document.getElementById("screen");
const clear = document.getElementById("clear");
const equals = document.getElementById("equals");
const numbers = document.querySelectorAll(".number");
const operators = document.querySelectorAll(".operator");
const sqrtButton = document.querySelector(".sqrt");

let currentValue = "";
let currentOperator = "";
let previousValue = "";

function updateScreen() {
  screen.value = currentValue;
}

function clearScreen() {
  currentValue = "";
  currentOperator = "";
  previousValue = "";
  updateScreen();
}

function handleNumberClick(e) {
  currentValue += e.target.value;
  updateScreen();
}

function handleOperatorClick(e) {
  currentOperator = e.target.value;
  previousValue = currentValue;
  currentValue = "";
  updateScreen();
}

function handleEqualsClick() {
  let result;
  switch (currentOperator) {
    case "+":
      result = parseFloat(previousValue) + parseFloat(currentValue);
      break;
    case "-":
      result = parseFloat(previousValue) - parseFloat(currentValue);
      break;
    case "*":
      result = parseFloat(previousValue) * parseFloat(currentValue);
      break;
    case "/":
      result = parseFloat(previousValue) / parseFloat(currentValue);
      break;
    default:
      result = 0;
  }
  currentValue = result.toString();
  currentOperator = "";
  previousValue = "";
  updateScreen();
}

function handleSqrtClick() {
  const num = parseFloat(screen.value);
  console.log(num)
  if (num >= 0) {
    currentValue = Math.sqrt(num).toString();
    updateScreen();
  } else {
    alert("Invalid input for square root operation.");
  }
}

clear.addEventListener("click", clearScreen);

numbers.forEach((number) => {
  number.addEventListener("click", handleNumberClick);
});

operators.forEach((operator) => {
  operator.addEventListener("click", handleOperatorClick);
});

equals.addEventListener("click", handleEqualsClick);

sqrtButton.addEventListener("click", handleSqrtClick);
