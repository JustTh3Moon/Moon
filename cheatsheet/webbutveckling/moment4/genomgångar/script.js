// Hur man gör en loop med hjälp av timeout

// Skapar en index som kommer räknas uppåt
var i = 0;
function loop() {
    if (++i < 10) {
        // Lägger in en timeout med 1500ms
        setTimeout(loop, 1500);
    }
    // Gör ändringarna
    document.getElementById("paragraph").innerHTML = i
}

// Kör funktionen
loop();