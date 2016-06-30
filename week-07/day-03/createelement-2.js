var asteroidList = document.querySelector('ul.asteroids');

var newAsteroid = document.createElement('li');
newAsteroid.id = 'b555';
newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);

var newAsteroidlight = document.createElement('li');
newAsteroidlight.id = 'b559';
newAsteroidlight.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroidlight);

var container = document.querySelector('.container');
var newheadings = document.createElement('h1');
newheadings.id = 'b01';
newheadings.textContent = 'I can add elements to the DOM!';
container.appendChild(newheadings);

var anypic = document.createElement('img');
anypic.setAttribute('src', 'https://photo4.lensculture.com/large/e6a18609-fc44-41b0-a442-f8e77415c2d5.jpg');
container.appendChild(anypic);
