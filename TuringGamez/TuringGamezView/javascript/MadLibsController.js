function getInput() {
  var inpy, output;
  inpy = document.getElementByID('songChoice').value;
  output = 0
  if(typeof(inpy) == "string") {
  	output = "Searching..."
  } else {
  	output = "Invalid input type"
  }

  document.getElementByID("Choice").innerHTML = output;