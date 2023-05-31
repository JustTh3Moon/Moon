// Funktion som byter bakgrundsfärg
function changeBackgroundColor() {
    document.body.style.backgroundColor = "#DC143C";
}

// Funktion som ändrar färgen på header1
function changeHeader1Color() {
    document.getElementById("head1").style.color = "red";
}

// Funktion som gör headern större
function biggerHeader() {
    var headElement = document.getElementById("head1");
    headElement.style.fontSize = "70px";
}

// Funktion som gör header mindre
function smallerHeader() {
    document.getElementById("head1").style.fontSize = "20px";
}

// Funktion som tillåter en bakgrund att läggas till eller ändras
function paragraphBackground() {
    var paragraph = document.getElementById("para");
    if(paragraph.style.backgroundColor == "orange") {
        paragraph.style.backgroundColor = "blue";
    }
    else {
        paragraph.style.backgroundColor = "orange";
    }   
}

// Funktion som gör bilden mindre
function smallerImage() {
    myImage = document.getElementById("grumpy");
    // Hämtar nuvarande storlek
    currentHeight = myImage.clientHeight;
    currentWidth = myImage.clientWidth;
    // Minskar med 50
    myImage.style.height = (currentHeight - 50) + "px";
    myImage.style.width = (currentWidth - 50) + "px";
}

// Funktion som animerar grumpy cat bilden
function animateElement() {
    let id = null;
    // Definierar element att animera
    const myImage = document.getElementById("grumpy");
    // Definierar startposition
    let pos = 0;
    clearInterval(id);
    id = setInterval(frame, 5);
    function frame() {
        // Ifall position kommer till 200 stannar animation
        if(pos == 200) {
            clearInterval(id)
        }
        // Annars fortsätter den med att animera
        else {
            pos++;
            myImage.style.left = pos + "px";
        }
    }
}

// Expanderar de olika options
function expand() {
    // Definierar div
    options = document.getElementById("options");
    // Definierar knapp
    btn = document.getElementById("expand");
    // Är det redan gömt, så ändras det så det visar
    if (options.style.visibility == "hidden") {
        options.style.position = "relative";
        options.style.visibility = "visible";
        // Ändrar knappen till att stå kollapsa 
        btn.textContent = "Collapse Options";
    }
    // Är det redan öppet kommer det istället att gömmas
    else {
        options.style.position = "absolute";
        options.style.visibility = "hidden";
        // Ändrar knappen till att stå expandera
        btn.textContent = "Expand Options";
    }
}

// --------------------

// Funktioner som låter användaren välja en egen färg på texter
let colorPicker;
defaultColor = "#000";

// Startar event listener för vår färgen
window.addEventListener("load", startup, false)

// Får färgelementet, sätter default value och skapar en event listener för färgen
function startup() {
    // Definierar färghjulet 
    colorPicker = document.getElementById("colorPicker");
    // Sätter standard färg färghjulet
    colorPicker.value = defaultColor;
    // Skapar en eventlistener för vårt färghjul
    colorPicker.addEventListener("input", update, false);
}

// Funktion som uppdaterar beroende på vilken knapp som trycks
function update(event) {
    // Hämtar id för knappen som blir tryckt
    document.querySelectorAll('button').forEach(occurence => {
        // Lagrar id för knappen som blir tryckt
        let id = occurence.getAttribute('id');
        occurence.addEventListener('click', function() {
            if (id == "ownBackground") {
                document.body.style.backgroundColor = event.target.value;
            }
                
            else if (id == "ownHeader") {
                document.getElementById("head1").style.color = event.target.value;
            }

            else if (id == "ownParagraph") {
                document.getElementById("para").style.backgroundColor = event.target.value;
            }
        });
    });
}

// --------------------

// Funktioner för att ändra font size

// Ändra storlek på header
function textHeader() {
    // Hämtar angedda storleken
    value = document.getElementById("textHeader").value;
    document.getElementById("head1").style.fontSize = value + "px";
}

// Ändra storlek på paragrafer
function textParagraph() {
    // Hämtar angedda storleken
    value = document.getElementById("textParagraph").value;
    document.getElementById("para").style.fontSize = value + "px";
}

function resetHeader() {
    document.getElementById("head1").style.fontSize = "32px";
    document.getElementById("textHeader").value = "";
}

function resetParagraph() {
    document.getElementById("para").style.fontSize = "13px";
    document.getElementById("textParagraph").value = "";
}

// --------------------

function ownImgSize() {
    ownHeight = document.getElementById("imgWidth").value;
    ownWidth = document.getElementById("imgHeight").value;
    myImage.style.height = ownHeight + "px";
    myImage.style.width = ownWidth + "px";
}

// Återställer bilden fullständigt (storlek och position)
function resetImg() {
    myImage.style.width = "auto";
    myImage.style.height = "auto";
    myImage.style.left = "0px";
    document.getElementById("imgWidth").value = "";
    document.getElementById("imgHeight").value = "";
}