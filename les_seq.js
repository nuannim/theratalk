let lists = document.getElementsByClassName("list");
let answer = document.getElementsByClassName("ans");
let choice = document.getElementById("choice");
let selected = null;
for(let i of lists){
    i.addEventListener("dragstart", function(e){
        selected = e.target;
    });
    i.addEventListener("click", function(e){
        selected = e.target;
    });

    // i.addEventListener("dragover", function(e){
    //     e.preventDefault();
    // });

    // i.addEventListener("drop", function(e){
    //     e.preventDefault();
    //     if(selected && selected !== e.target){
    //         e.target.parentNode.insertBefore(selected, e.target);
    //         selected = null;
    //     }
    // });
}
choice.addEventListener("dragover", function(e){
    e.preventDefault();
});

choice.addEventListener("drop", function(e){
    if(selected){
        choice.appendChild(selected);
        selected = null;
    }
});

for(let j of answer){
    j.addEventListener("dragover", function(e){
        e.preventDefault();
    });
    
    j.addEventListener("drop", function(e){
        if(j.firstChild){
            choice.appendChild(j.firstChild);
        }
        j.appendChild(selected);
        selected = null;
    });
}
