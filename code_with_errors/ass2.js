function calculateCircleArea(radius) {
    const pi = 3.14;
    let area = pi * radius ** 2;
    return area
}

function greetUser(name) {
    let greeting = "Hello, " + name;
    console.log(greeting)
}

function findMaximum(numbers) {
    let maxNum = -Infinity;
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > maxNum {
            maxNum = numbers[i];
        }
    }
    return maxNum;
}

let numbers = [1, 2, 3, 4, 5];
let total = numbers.reduce((a, b) => a + b, 0);
console.log("The total is " + total;

function checkEvenOdd(number) {
    if (number % 2 == 0) {
        console.log("The number is even");
    else {
        console.log("The number is odd");
    }
}

console.log(calculateCircleArea(5));
greetUser("Alice");
console.log("The maximum number is: " + findMaximum(numbers));
checkEvenOdd(7);
