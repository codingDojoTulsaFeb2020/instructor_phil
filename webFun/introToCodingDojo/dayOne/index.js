// let/const
var myString = "Hello World";
var myString = 'Second string';
var myNum = 4;

console.log(myNum);
// => undefined
var myBool = false;
console.log(myBool);
// => false

if(myBool ==  true) {
  console.log('its true')
} else {
  console.log('its false');
}

if(myNum == 1) {
  console.log('it one');
} else if(myNum == 2) {
  console.log('it two');
}
else {
  console.log('its not one or two');
}
if((myNum == 2 || myBool == false) && true) {
  console.log('its all good');
}

// AND condition
// t = t && t
// f = t && f
// f = f && t
// f = f && f

// OR condition
// t = t || t
// t = t || f
// t = f || t
// f = f || f

console.log(Math.round(3.5));
console.log(Math.floor(3.5));
console.log(Math.ceil(3.5));
console.log(Math.trunc(3.5));
