"use strict";

function greet(name, selector) {
  const el = document.querySelector(selector);
  el.textContent = `Hello, ${name}!`;
}

function isPrime(number) {
  if (number < 2) return false;
  if (number == 2) return true;
  if (number % 2 == 0) return false;
  for (let i = 3; i <= Math.sqrt(number); i += 2) {
    if (number % i == 0) return false;
  }
  return true;
}

function printNumberInfo(number, selector) {
  const el = document.querySelector(selector);
  const primeStatus = isPrime(number)
  let primeStatus;
  if (isPrime(number)) {
    primeStatus = "is a prime number.";
  } else {
    primeStatus = "is not a prime number.";
  }

  el.textContent = `The number ${number} ${primeStatus}`;
}

function getNPrimes(number) {
  const primes = [];
  let candidate = 2;
  while (primes.length < number) {
    if (isPrime(candidate)) primes.push(candidate);
    candidate++;
  }
  return primes;
}

function printNPrimes(number, selector) {
  const primes = getNPrimes(number);
  const tbody = document.querySelector(selector + " tbody");
  tbody.innerHTML = "";

  for (let i = 0; i < primes.length; i += 10) {
    const row = document.createElement("tr");
    for (let j = i; j < i + 10 && j < primes.length; j++) {
      const cell = document.createElement("td");
      cell.textContent = primes[j];
      row.appendChild(cell);
    }
    tbody.appendChild(row);
  }
}

function displayWarnings(urlParams, selector) {
  // TODO: Implement this function
}

window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  const name = urlParams.get("name") || "student";
  const number = parseInt(urlParams.get("number")) || 330;

  displayWarnings(urlParams, "#warnings");
  greet(name, "#greeting");
  printNumberInfo(number, "#numberInfo");
  printNPrimes(number, "table#nPrimes");
};

document.addEventListener("DOMContentLoaded", () => {
  (document.querySelectorAll(".notification .delete") || []).forEach(
    ($delete) => {
      const $notification = $delete.parentNode;
      $delete.addEventListener("click", () => {
        $notification.parentNode.removeChild($notification);
      });
    }
  );
});

module.exports.isPrime = isPrime;
module.exports.getNPrimes = getNPrimes;
