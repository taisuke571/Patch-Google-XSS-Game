function startTimer(seconds) {
  console.log("startTimer function has been executed with seconds:", seconds); // This line logs the message

  seconds = parseInt(seconds) || 3;
  setTimeout(function() { 
      window.confirm("Time is up!");
      window.history.back();
  }, seconds * 1000);
}

document.addEventListener('DOMContentLoaded', function() {
  var img = document.getElementById('loading-gif');
  img.addEventListener('load', function() {
      console.log("Image has loaded.");
      startTimer(img.getAttribute('data-timer')); // Call the startTimer function when the image loads
  });
  // Check if the image is already loaded (e.g., from cache)
  if (img.complete) {
      console.log("Image was already loaded from cache.");
      startTimer(img.getAttribute('data-timer'));
  }
});
