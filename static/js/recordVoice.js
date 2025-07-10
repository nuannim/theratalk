const speakButton = document.querySelector(".speak");
    const checkButton = document.querySelector("button[type='button']");
    const wordText = document.querySelector(".word p");

    let mediaRecorder;
    let audioChunks = [];

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
            checkButton.disabled = false;
        };

        mediaRecorder.start();
        speakButton.querySelector("p").textContent = "🎙️ พูดได้เลย...";
        setTimeout(() => {
            mediaRecorder.stop();
        }, 3000); // Record for 3 seconds
    };
