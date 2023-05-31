// Lista med strängar
const strings = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
];

// En for loop som börjar på noll och körs till listan 
// med strängar är slut, 
// adderar med en för varje gång loopens kod är körd
for (let i = 0; i < strings.length; i++) {
    console.log(strings[i]);
}

// Loopar genom listan baklänges 
// då den börjar på listans sista index och går sedan 
// baklänges tills den når noll
for (let i = (strings.length - 1); i >= 0; i--) {
    console.log(strings[i]);
}

// Tar bort en sträng med parameter som anger position att ta bort
function removeString(removeIndex) {
    strings.splice(removeIndex, 1);
}

// Lägger till en sträng i listan
function addString(string) {
    strings.splice(strings.length, 0, string);
}

// ----------------

// Lista på färger
const colors = ["0A2463", "3E92CC", "D8315B", "B5B682", "FEDC97", "8C1C13",]

const images = ["img/dance1.gif", "img/dance2.gif", "img/dance3.gif", "img/dance4.gif", "img/dance5.gif",]

// Event listener som kör koden inuti efter att allt på sidan laddats
document.addEventListener("DOMContentLoaded", function() {
    // Variabel som håller koll på vilken sträng vi är på
    let i = 0;
    let y = 0;
    // Byter bakgrund efter 1000ms
    setInterval(() => {
        // Ändrar färg
        document.body.style.backgroundColor = "#" + colors[i];
        // 
        i = (i + 1) % colors.length;
    }, 1000);

    setInterval(() => {
        document.getElementById("my-image").setAttribute("src", images[y]);
        y = (y + 1) % images.length;
    }, 3000);
});