let requestURL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
let request = new XMLHttpRequest();
request.open('GET', requestURL);

request.onload = function() {
    let data = JSON.parse(this.responseText);
    console.log(data);

}
request.send();
console.log(data["result"]["results"]);