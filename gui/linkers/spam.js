
function check_spam() {
  var python = require("python-shell")
  var path = require("path")

  var text = document.getElementById("text").value
  document.getElementById("text").value = "";

  var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [text]
  }

  var result = new python('detector.py', options);

  result.on('message', function(message) {
    swal(message);
  })
}
