<<<<<<< HEAD
"use strict"

function paint(newColor){
    let labelElement = document.querySelector("#ageLabel");
    //labelElement.style.color = newColor;
    labelElement.setAttribute("style", `color: ${newColor}`);

    let ageInputElement = document.querySelector("#ageInput");
    console.log(ageInputElement.value);
    if(newColor == "Red"){
        ageInputElement.remove();
    }
=======
"use strict";

function paint(newColor) {
  let labelElement = document.querySelector("#ageLabel");
  //   labelElement.style.color = newColor;
  labelElement.setAttribute("style", `color: ${newColor}`);

  let ageInputElement = document.querySelector("#ageInput");
  if (newColor === "red") {
    ageInputElement.remove();
  }
>>>>>>> bec812f1035e3fd70ddc9fc720e83eb2a8832196
}
