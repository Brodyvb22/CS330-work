console.log("Hello CS330");

var x = 330;
console.log(x);

personName = "Timmy";
personAge = 24;
console.log(personName + " is " + personAge);
personName = "Timothee";
personAge++;
console.log(`${personName} is ${personAge}`);

if (personAge>0) {
    console.log("Welcome to the World");
} else {
    console.log("How did we make it here?");
}

for (let i = 0; i < 10; i++){
    console.log(i);
}

let roster = ["jon", "james", "mike", "nick"];
console.log(roster);
for (let i = 0; i < roster.length; i++){
    console.log(roster[i]);
}

roster.push(11);
roster.push(4);
roster.push(42);
roster.push(100000);

for (let name in roster){
    console.log(name);
}

console.log(roster);
roster.sort();
console.log(roster);

let picks = [7, 21, 70, 9, 86];
console.log(picks);
picks.sort();
console.log(picks);
picks.sort((a, b) => a - b);
console.log(picks);

let grades = {lucy : 90, "doug" : 78}
grades["brad"] = 67;
grades.brody = 96;
console.log(grades);

console.log(greet(personName));

function greet(name){
    return "Hello, " + name;
}

console.log(greet(personName));