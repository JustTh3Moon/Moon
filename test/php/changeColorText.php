<?php
$selectedColor = $_POST["color"];

echo $selectedColor;

if($selectedColor == 'white')
{
    echo "white";
}
else if($selectedColor == 'black')
{
    echo "black";
}

?>