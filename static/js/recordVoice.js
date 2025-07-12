const speakButton = document.querySelector(".speak");
    const checkButton = document.getElementById("check-button");
    const wordText = document.querySelector(".word p");
    const correctIndexes = new Set();
    const correctSound = new Audio("/static/sounds/correct.mp3");
    speakButton.querySelector("p").style.color = "#7293df";

    let mediaRecorder;
    let audioChunks = [];

    function playCorrectSound() {
        correctSound.currentTime = 0; // Reset if played before
        correctSound.play();
    }

    speakButton.onclick = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = async () => {
            const blob = new Blob(audioChunks, { type: "audio/webm" });
            const formData = new FormData();
            formData.append("file", blob, "speech.webm");

            speakButton.querySelector("p").textContent = "⏳ กำลังประมวลผล...";

            const res = await fetch("/patient/transcribe/", {
                method: "POST",
                body: formData
            });
            const data = await res.json();

            speakButton.querySelector("p").textContent = `📄 ${data.text}`;

            const check = await fetch("/patient/check_answer/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    answer: data.text,
                    word: wordText.textContent
                })
            });

            if (check.ok) {
                // 200 OK – Correct
                speakButton.querySelector("p").style.color = "green";
                speakButton.querySelector("p").textContent = "✅ ถูกต้อง!";
                correctIndexes.add(currentIndex);
                playCorrectSound();
            } else {
                // Wrong or error
                speakButton.querySelector("p").style.color = "red";
                correctIndexes.delete(currentIndex);
            }
        };

        mediaRecorder.start();
        speakButton.querySelector("p").textContent = "🎙️ พูดได้เลย...";
        setTimeout(() => {
            mediaRecorder.stop();
        }, 3000); // Record for 3 seconds
    };
