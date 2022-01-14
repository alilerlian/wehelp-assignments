let requestURL = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
    const datafile = request.response;
    newdata(datafile)

    console.log(datafile)


}

function newdata(obj) {
    let n = obj['result']["results"].length;
    let spot_list = [];
    for (var i = 0; i < n; i++) {
        let photo_split = obj['result']["results"][i]["file"].split("https://");
        console.log(photo_split);
        let photo_site = "https://" + photo_split[1];
        let newtitle = obj["result"]["results"][i]["stitle"];

        let singlespot = new Object();
        singlespot.spottitle = newtitle;
        singlespot.photosite = photo_site;
        spot_list.push(singlespot);

    }

    console.log(spot_list)

    for (var j = 0; j < spot_list.length; j++) {
        const gallery = document.createElement('div');
        gallery.className = "gallery";

        const newdiv = document.createElement('div');
        newdiv.className = "photoblock";

        const newimg = document.createElement('img');
        newimg.src = spot_list[j]["photosite"];
        newimg.className = "photo";
        const div2 = document.createElement('div');
        div2.className = "photointro";
        const textNode = document.createTextNode(spot_list[j]["spottitle"]);

        document.body.appendChild(gallery);
        gallery.appendChild(newdiv);
        newdiv.appendChild(newimg);
        newdiv.appendChild(div2);
        div2.appendChild(textNode);


    }




}