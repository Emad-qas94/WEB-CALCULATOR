const display = document.getElementById("calc-display");
const buttonsDiv = document.getElementById("buttons");
const saveBtn = document.getElementById("save-btn");

let currentInput = "";

const buttons = [
    "(", ")", "pi", "e", "^", "sqrt",
    "sin", "cos", "tan", "arcsin", "arccos", "arctan",
    "sinh", "cosh", "tanh", "exp", "ln", "log10",
    "abs", "factorial", "nPr", "nCr", "percent", "mod",
    "reciprocal", "floor", "ceil", "mean", "median", "stdev",
    "summation", "M+", "MR", "MC", "DEG", "RAD",
    "7", "8", "9", "/", "4", "5",
    "6", "*", "1", "2", "3", "-", "0", ".", "+", "C", "="
];

if (buttonsDiv) {
    buttons.forEach(b => {
        let btn = document.createElement("button");
        btn.textContent = b;
        btn.onclick = () => handleInput(b);
        buttonsDiv.appendChild(btn);
    });
}

function handleInput(val) {
    if (val === "C") {
        currentInput = "";
        display.value = "";
        return;
    }
    if (val === "=") {
        calculate();
        return;
    }
    if (val === "DEG" || val === "RAD") {
        fetch('/calculate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({expression: val})
        }).then(() => {
            display.value = `Mode: ${val}`;
            setTimeout(() => display.value = currentInput, 900);
        });
        return;
    }
    currentInput += val === "pi" ? "pi()" :
        val === "e" ? "e()" :
        ["sin","cos","tan","arcsin","arccos","arctan",
         "sinh","cosh","tanh","sqrt","exp","ln","log10",
         "abs","factorial","nPr","nCr","percent","mod",
         "reciprocal","floor","ceil","mean","median","stdev","summation"]
         .includes(val) ? val + "(" :
         val;
    display.value = currentInput;
}

function calculate() {
    fetch('/calculate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({expression: currentInput})
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.result !== undefined) {
            display.value = data.result;
            currentInput = data.result.toString();
        } else {
            display.value = "Error";
            currentInput = "";
        }
    })
    .catch(() => {
        display.value = "Error";
        currentInput = "";
    });
}

if (saveBtn) {
    saveBtn.onclick = function() {
        fetch('/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({expression: currentInput, result: display.value})
        })
        .then(resp => resp.json())
        .then(data => {
            if (data.status === "success") {
                alert("Calculation saved!");
            } else {
                alert("Error saving!");
            }
        });
    };
}