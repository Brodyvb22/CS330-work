function greetName(){
    const queryStr = window.location.search;
    const urlParams = new URLSearchParams(queryStr);
    console.log(urlParams); /*#delete this*/
    let greetingElement = document.querySelector("h2");
    greetingElement.innerHTML = "Hello" + urlParams.get("name");
}
window.onload=function(){
    console.log("Hello"); /*delete this*/
    greetName();
}