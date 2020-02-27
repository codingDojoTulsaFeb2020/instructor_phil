var data = {
  "orders": [
    {
      "orderno": 784692,
      "date": "June 30, 2088 1:54:23 AM",
      "trackingno": "TN000391",
      "customer": {
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
      }
    },
    {
      "orderno": 784693,
      "date": "March 3, 2088 8:18:14 PM",
      "trackingno": "TN000468",
      "customer": {
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
      }
    }
  ]
}

$('#content').html('<h1>Order numbers</h1>');
$('#content').append('<ul></ul>');

for(var i = 0; i < data.orders.length;i++) {
  console.log(data.orders[i].orderno);
  console.log(Array.isArray(data.orders[i]));
  $('ul').append(`<li>Order #${i+1} is: ${data.orders[i].orderno} by ${data.orders[i].customer.fname} ${data.orders[i].customer.lname}</li>`);
}

/* or

var liBuilder = "";

for(var i = 0; i < data.orders.length;i++) {
  console.log(data.orders[i].orderno);
  liBuilder += `<li>Order #${i+1} is: ${data.orders[i].orderno} by ${data.orders[i].customer.fname} ${data.orders[i].customer.lname}</li>`;
}
$('ul').html(liBuilder);

*/

console.log(typeof(data));
var myArr = [];
console.log(typeof(myArr));
console.log(Array.isArray(myArr));
console.log(Array.isArray(data));

console.log(data['orders']);
console.log(typeof(data.orders));
console.log(Array.isArray(data.orders));
console.log(data['orders'][1]);
console.log(typeof(data.orders[1]));
console.log(Array.isArray(data.orders[1]));
console.log(data['orders'][1].customer.fname);