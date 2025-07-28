window.addEventListener("DOMContentLoaded", () => {
    const speakButton = document.querySelector(".speak");
    const wordText = document.querySelector(".word p");
    const correctSound = new Audio("/static/sounds/correct.mp3");
    speakButton.querySelector("p").style.color = "#7293df";

    let mediaRecorder;
    let audioChunks = [];
    let isRecording = false;

    function playCorrectSound() {
        correctSound.currentTime = 0;
        correctSound.play();
    }

    speakButton.onclick = async () => {
        if (!isRecording) {
            // Start recording
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
                    speakButton.querySelector("p").style.color = "green";
                    speakButton.querySelector("p").textContent = "✅ ถูกต้อง!";
                    correctIndexes.add(currentIndex);
                    if (correctIndexes.size === tcContents.length) {
                        submitButton.disabled = false;
                    }
                    playCorrectSound();
                    onSpeechEvaluated(true);
                } else {
                    speakButton.querySelector("p").style.color = "red";
                    speakButton.querySelector("p").textContent = `❌ ${data.text}`;
                    correctIndexes.delete(currentIndex);
                    onSpeechEvaluated(false);

                    setTimeout(() => {
                        speakButton.querySelector("p").textContent = "🎙️ กดเพื่อพูด";
                        speakButton.querySelector("p").style.color = "#7293df";
                    }, 2999);
                }

                isRecording = false;
            };


            mediaRecorder.start();
            speakButton.querySelector("p").style.color = "#7293df";
            speakButton.querySelector("p").textContent = "⏹️ กดเพื่อหยุด";
            isRecording = true;
        } else {
            // Stop recording
            mediaRecorder.stop();
            speakButton.querySelector("p").textContent = "⏳ กำลังประมวลผล...";
        }
    };

    // Initial label
    speakButton.querySelector("p").textContent = "🎙️ กดเพื่อพูด";
});
