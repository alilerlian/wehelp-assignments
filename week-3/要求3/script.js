let requestURL = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
    const datafile = request.response;
    newdata(datafile)
}

function newdata(obj) {
    let n = obj['result']["results"].length;
    let spot_list = [];
    for (var i = 0; i < n; i++) {
        let photo_split = obj['result']["results"][i]["file"].split("https://");
        let photo_site = "https://" + photo_split[1];
        let newtitle = obj["result"]["results"][i]["stitle"];

        let singlespot = new Object();
        singlespot.spottitle = newtitle;
        singlespot.photosite = photo_site;
        spot_list.push(singlespot);

    }
    addblock(spot_list);

}

function addblock(spots) {

    const gallery = document.createElement('div');
    gallery.className = "gallery";
    document.body.appendChild(gallery);


    for (var j = 0; j < spots.length; j++) {


        const newdiv = document.createElement('div');
        newdiv.className = "photoblock";

        const newimg = document.createElement('img');
        newimg.src = spots[j]["photosite"];
        newimg.className = "photo";
        const div2 = document.createElement('div');
        div2.className = "photointro";
        const textNode = document.createTextNode(spots[j]["spottitle"]);

        gallery.appendChild(newdiv);
        newdiv.appendChild(newimg);
        newdiv.appendChild(div2);
        div2.appendChild(textNode);

    }
    addbtn();
}

function addbtn() {
    const bottonblock = document.createElement('div');
    const morebtn = document.createElement('button');
    const btntext = document.createTextNode('MORE');
    bottonblock.className = "btnb";
    document.body.appendChild(bottonblock);
    bottonblock.appendChild(morebtn);
    morebtn.appendChild(btntext);

}