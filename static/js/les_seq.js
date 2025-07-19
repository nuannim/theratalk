let lists = document.getElementsByClassName("list");
let answerBoxes = document.getElementsByClassName("ans");
let choice = document.getElementById("choice");
let selected = null;

// เพิ่ม event สำหรับลากคำ
for (let item of lists) {
    item.addEventListener("dragstart", function (e) {
        selected = e.target;
    });

    item.addEventListener("click", function (e) {
        selected = e.target;
        moveToAnswerBox(selected);
    });
}

// ฟังก์ชันเคลื่อนคำไปยังกล่องว่างใน answer
function moveToAnswerBox(wordElement) {
    for (let box of answerBoxes) {
        if (!box.hasChildNodes()) {
            box.appendChild(wordElement);
            selected = null;
            return;
        }
    }
}

function attachDragAndClickEvents() {
    let lists = document.getElementsByClassName("list");
    for (let item of lists) {
        item.addEventListener("dragstart", function (e) {
            selected = e.target;
        });

        item.addEventListener("click", function (e) {
            selected = e.target;
            moveToAnswerBox(selected);
        });
    }
}

// กลับไปที่ choice ถ้าวางซ้ำ
choice.addEventListener("dragover", function (e) {
    e.preventDefault();
});

choice.addEventListener("drop", function (e) {
    if (selected) {
        choice.appendChild(selected);
        selected = null;
    }
});

// ตอบรับการวางคำในแต่ละกล่อง ans
for (let box of answerBoxes) {
    box.addEventListener("dragover", function (e) {
        e.preventDefault();
    });

    box.addEventListener("drop", function (e) {
        if (selected) {
            // ถ้ามีก่อนหน้า ให้นำกลับไป choice ก่อน
            if (box.hasChildNodes()) {
                choice.appendChild(box.firstChild);
            }
            box.appendChild(selected);
            selected = null;
        }
    });

    box.addEventListener("click", function (e) {
        if (box.hasChildNodes()) {
            choice.appendChild(box.firstChild);
        }
    });
}
