const input1 = document.getElementById("input1");
const input2 = document.getElementById('input2');
const result = document.getElementById('result');

function calculateSum() {
  const num1 = parseFloat(input1.value);
  const num2 = parseFloat(input2.value);
  const sum = num1 + num2;
  result.value = sum;
}

const button = document.getElementById('calculateBtn');
button.addEventListener('click', calculateSum);
