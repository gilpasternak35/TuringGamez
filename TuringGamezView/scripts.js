/* 
  IN THIS FILE YOU SHOULD DEFINE THREE FUNCTIONS:
  incr(), decr(), and dispMessage(). THEY WILL BE HOOKED 
  UP TO THE THREE CORRESPONDING BUTTONS IN YOUR 
  HTML FILE.
  
  incr() WILL TAKE THE CURRENT NUMBER IN YOUR counter
  ELEMENT AND INCREASE IT BY ONE. THERE IS NO LIMIT TO 
  HOW HIGH incr() CAN INCREASE THE NUMBER.
  
  decr() WILL DO THE SAME AS incr() EXCEPT IT WILL 
  DECREASE THE NUMBER. ALSO, YOU SHOULD UTILIZE 
  CONTROL FOLOW IN decr() TO ONLY ALLOW THE USER TO 
  DECREASE THE NUMBER TO 0. IF THEY TRY TO DECREASE 
  LOWER THAN 0, SHOW AN ALERT WARNING THE USER THAT 
  THEY CANNOT DO SO. YOU CAN WRITE WHATEVER YOU'D LIKE
  IN THE ERROR MESSAGE.
  
  dispMessage() WILL DISPLAY A MESSAGE THAT CONTAINS
  THE NAME INPUT BY THE USER (CONCATENATED).
*/

function incr() {
  console.log("pressed Increase");
  let counterNum = document.getElementById("counter");
  counterNum.innerHTML++;

}

function decr() {
  console.log("pressed Increase");
  let counterNum = document.getElementById("counter");
  if (counterNum.innerHTML<1)
    alert("Error: Counter does not go below 0");
  else
    counterNum.innerHTML--;

}

let myImage = document.querySelector('img');

myImage.onclick = function() {
    
    let name = prompt("What is your name?", "John Doe");
  
    msgText.innerHTML = "Hello " + name + ", nice to meet you!"
}

function dispMessage() {

  let name = prompt("What is your name?", "John Doe");
  
  msgText.innerHTML = "Hello " + name + ", I am Alan Turing!";
}

function visitPage(){
        window.location='http://www.google.com';
