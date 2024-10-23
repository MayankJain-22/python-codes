const display = document.querySelector(".display");
const buttons = document.querySelectorAll("button");
const spchar = ["%","*","/","-","+","="];
let output = ""
let historyDisplay = document.querySelector(".history")

const calculate = (btnpress) => {
    display.focus;
    if (btnpress === "=" && output !== ""){
        historyDisplay.innerHTML = output;
        output = eval(output.replace("%","/100"));
    }
    else if (btnpress === "AC") {
        output = "";
        historyDisplay.innerHTML = ""
    }
    else if (btnpress ==="Del") {
        output = output.toString().slice(0,-1);
    }
    else{
        if (output === "" && spchar.includes(btnpress)) return;
        output += btnpress;
    }
    display.value = output;
};

for(let button of buttons){
    button.addEventListener("click",(e) => calculate(e.target.dataset.value));
}