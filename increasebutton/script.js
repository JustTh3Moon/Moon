function incrementValue()
{
    var value = parseInt(document.getElementById('number').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('number').value = value;
}

function resetValue()
{
    document.getElementById('number').value = 0;
}

function getMultiTable()
{
    var base = parseInt(document.getElementById('base').value, 10);
    var topValue = parseInt(document.getElementById('topValue').value, 10);
    var multiTable = [];
    var para = document.getElementById('multiplicationTable');
    
    for (let i = 1; i <= topValue ;i++)
    {
        res = i / base;
        if (!(res % 1))
        {
            multiTable.push(i);
        }
    }

    para.innerHTML = multiTable;
}

function resetMultiply()
{
    document.getElementById('base').value = '';
    document.getElementById('topValue').value = '';
    document.getElementById('multiplicationTable').innerHTML = '';
}