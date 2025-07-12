document.querySelector('.listen-box').addEventListener('click', () => {
    const text = document.getElementById('question').innerText;

    fetch(`/api/tts?text=${encodeURIComponent(text)}`)
        .then(response => response.blob())
        .then(blob => {
            const audioUrl = URL.createObjectURL(blob);
            const audio = new Audio(audioUrl);
            audio.play();
        })
        .catch(error => {
            console.error('TTS error:', error);
        });
});

