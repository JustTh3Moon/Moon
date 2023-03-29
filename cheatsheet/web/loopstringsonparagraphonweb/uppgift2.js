// Lista med strängar
const strings = [
    "Paragrafen kommer ändras för varannan sekund.", 
    "Så, låt mig lära känna dig!", 
    "Hur är läget?", 
    "Jag hoppas allt är väl.", 
    "För mig går det smidigt.", 
    "Kan bero på att jag bara är text ;)", 
    "Men, det behöver vi inte prata om...", 
    "Det var kul att träffas :)", 
    "Vi syns snart!",
    "Detta är en paragraf."
];

// Event listener som kör koden inuti efter att allt på sidan laddats
document.addEventListener("DOMContentLoaded", function() {
    // En lista med olika strängar
    const strings = [
        "Paragrafen kommer ändras för varannan sekund.", 
        "Så, låt mig lära känna dig!", 
        "Hur är läget?", 
        "Jag hoppas allt är väl.", 
        "För mig går det smidigt.", 
        "Kan bero på att jag bara är text ;)", 
        "Men, det behöver vi inte prata om...", 
        "Det var kul att träffas :)", 
        "Vi syns snart!",
        "Detta är en paragraf."
    ];

    // Hämtar paragrafen som ändras
    var paragraph = document.getElementById("paragraf");
    // Variabel som håller koll på vilken sträng vi är på
    let index = 0;
    // Startar ett intervall som körs för var 2000ms 
    setInterval(() => {
        // Ändrar paragrafen 
        paragraph.textContent = strings[index];
        // Återgår till början av listan om index == längden på listan med strängarna 
        index = (index + 1) % strings.length;
    }, 2000); 
});