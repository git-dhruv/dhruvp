/*
let modalBtn = document.getElementById("acrylic")
//let modal = document.querySelector(String(modalBtn.id))
let modal = document.querySelector(".modal")
let closeBtn = document.querySelector(".close-btn")
modalBtn.onclick = function(){
  modal.style.display = "block"
}
closeBtn.onclick = function(){
  modal.style.display = "none"
}
window.onclick = function(e){
  if(e.target == modal){
    modal.style.display = "none"
  }
}*/

var modal = document.getElementsByClassName('modal');

// Get the button that opens the modal
var btn = document.getElementsByClassName("image fit");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-btn");

// When the user clicks the button, open the modal 
for(let i=0;i<btn.length;i++){
  btn[i].onclick = function(){
    modal[i].style.display = "block";
  }

  span[i].onclick = function() {
    modal[i].style.display = "none";
}

}
btn[0].onclick = function() {
    modal[0].style.display = "block";
}

btn[1].onclick = function() {
    modal[1].style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span[0].onclick = function() {
    modal[0].style.display = "none";
}

span[1].onclick = function() {
    modal[1].style.display = "none";
}

window.onclick = function(e){
  if(e.target == modal){
    modal.style.display = "none"
  }
}