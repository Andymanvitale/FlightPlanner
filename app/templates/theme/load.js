window.onload = () => {
    // copy below to add more pages
    fetch('sidebar.html') // the page we want to use for our sidebar
    .then(data => {
      return data.text()
    })
    .then( data => {
      document.getElementById("wrapper").innerHTML = data; // inserts to element id="navbar"
    })
    // copy end
}