'use strict';
var button = document.querySelector('button');
var xhr = new XMLHttpRequest();
     xhr.onload = function() {
       console.log(JSON.parse(xhr.response).season);
     };
     xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/06');
     xhr.send();
 function viewData () {
   document.querySelector('.weekday').textContent = JSON.parse(xhr.response).weekday;
   document.querySelector('.celebrations').textContent = JSON.parse(xhr.response).celebrations.length;
 }
 button.addEventListener('click', viewData);
