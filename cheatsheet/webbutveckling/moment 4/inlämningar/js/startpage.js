function darkmode() {
    let btn = document.getElementById("darkmode")
    if (btn.textContent == "Dark Mode") {
        document.body.style.background = "#0F110C";
        document.getElementById("welcome").style.color = "#fbf7f5";
        btn.textContent = "Light Mode";
    }
    else {
        document.body.style.background = "#fbf7f5";
        document.getElementById("welcome").style.color = "#424B54";
        btn.textContent = "Dark Mode";
    }
}