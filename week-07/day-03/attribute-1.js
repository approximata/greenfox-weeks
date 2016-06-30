var picture = document.querySelector('img');
console.log(picture.getAttribute('src'));
picture.setAttribute('src', 'http://deji.chez.com/dessins/pp1.gif');
var linkofit = document.querySelector('a');
console.log(linkofit.getAttribute('href'));
linkofit.setAttribute('href', 'http://www.greenfoxacademy.com/');
var sbutton = document.querySelector('.this-one');
sbutton.setAttribute("disabled", "true");
sbutton.textContent = 'Don\'t click me!'
