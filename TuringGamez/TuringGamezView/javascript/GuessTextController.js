$('#songButton').click(function (evt) {
  console.log('JQuery works')
});

function getInput() {
  var inpy, output;
  inpy = document.getElementById('songChoice').value;
  console.log('Song choice: ' + inpy)
  output = 0

  if (inpy != "") {
    output = "Searching..."
  } else {
    output = "Invalid input type"
  }

  document.getElementById("Choice").innerHTML = output;
}

