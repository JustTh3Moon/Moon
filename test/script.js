function colorOfText()
{
    img = document.getElementById('image');
    currentColor = document.getElementById('landing_page').color;
    console.log(currentColor)
    
    
    const radioButtons = document.querySelectorAll('input[name="color"]');
    
    let selectedColor;
    for (const radioButton of radioButtons) 
    {
        if(radioButton.checked)
        {
            selectedColor = radioButton.value;
            break;
        }
    }

    if(selectedColor == 'white')
    {
        document.getElementById('landing_page').color = '#FFF';
        img.src = 'img/white.png';
    }
    else if(selectedColor == 'black')
    {
        document.getElementById('landing_page').color = '#000';
        img.src = 'img/black.png';
    }
}