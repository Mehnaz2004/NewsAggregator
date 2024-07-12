let button = document.querySelector("#ChangeMode");
let body = document.querySelector("body");
let articlescontainer = document.querySelector(".articles-container");

button.onclick = changeMode;

function changeMode() {
    if (button.innerText == "🌑") {
        body.style.backgroundColor = "rgb(50, 50, 50)";
        button.innerText = "☀";
        articlescontainer.style.backgroundColor = "rgb(73,73,73)";
    } else {
        body.style.backgroundColor = "rgb(145, 142, 142)";
        button.innerText = "🌑";
        articlescontainer.style.backgroundColor = "rgb(172, 174, 173)";
    }
}
