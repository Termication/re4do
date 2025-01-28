document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('popup-modal');
    const playButton = document.getElementById('play-button');

    let isGameStarted = false;

    playButton.onclick = () => {
        fetch('/start-game', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                console.log("Start Game Response:", data);  // Debugging line
                if (data.status === "Game started") {
                    modal.style.display = 'none';
                    fetchNewRound();
                }
            })
            .catch(error => console.error("Error starting game:", error));
    };
    
    // Ensure the game stays paused initially
    if (!isGameStarted) {
        optionsElement.innerHTML = '';
        targetEmojiElement.textContent = '🎮'; // Placeholder emoji before game starts
        countdownElement.textContent = 'Time left: 0s';
    }
});
