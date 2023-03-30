// Lista med strängar
const strings = [
    "Wooo! Dance, dance, dance!",
    "It's rockin' here!",
    "May I have this dance?",
    "Move those hips!",
    "Do the moonwalk!",
    "Slaaay, queen",
    "Nice groove!",
    "Drop it like it's hot",
    "Feelin' alive!",
    "You're dancing, right?"
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
    // Byter bakgrund efter 1000ms
    setInterval(() => {
        // Ändrar färg
        document.body.style.backgroundColor = "#" + colors[i];
        i = (i + 1) % colors.length;
    }, 1000);

    // Variabel som håller koll på vilken sträng vi är på
    let y = 0;
    // Ändrar bilden efter 3000ms
    setInterval(() => {
        document.getElementById("my-image").setAttribute("src", images[y]);
        y = (y + 1) % images.length;
    }, 3000);

    // Variabel som håller koll på vilken sträng vi är på
    let x = 0;
    // Ändrar paragrafens innehåll, 
    // när den når slutet av listan kommer den gå baklänges
    setInterval(() => {
        document.getElementById("my-paragraph").textContent = strings[x];
        x = (x + 1) % strings.length;
    }, 2000);
});