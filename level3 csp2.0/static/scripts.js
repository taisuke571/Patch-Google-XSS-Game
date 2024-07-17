function chooseTab(num) {
  var html = "Image " + parseInt(num) + "<br>";
  html += "<img src='/static/level3/cloud" + num + ".jpg' />";
  document.getElementById('tabContent').innerHTML = html;

  window.location.hash = num;

  var tabs = document.querySelectorAll('.tab');
  for (var i = 0; i < tabs.length; i++) {
      if (tabs[i].id == "tab" + parseInt(num)) {
          tabs[i].className = "tab active";
      } else {
          tabs[i].className = "tab";
      }
  }

  top.postMessage(self.location.toString(), "*");
}

window.onload = function() { 
  chooseTab(unescape(self.location.hash.substr(1)) || "1");
}

window.addEventListener("message", function(event){
  if (event.source == parent) {
      chooseTab(unescape(self.location.hash.substr(1)));
  }
}, false);

document.addEventListener('DOMContentLoaded', function() {
  var tabs = document.querySelectorAll('.tab');
  tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
          var num = this.id.replace('tab', '');
          chooseTab(num);
      });
  });
});
