document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('popup-modal');
    const playButton = document.getElementById('play-button');

    // Pause game until play icon is clicked
    let isGameStarted = false;

    // Hide modal and start the game when Play is clicked
    playButton.onclick = () => {
        modal.style.display = 'none'; // Hide the modal
        isGameStarted = true;        // Mark the game as started
        fetchNewRound();             // Start the game
    };

    // Prevent game actions (pause background) until play is clicked
    if (!isGameStarted) {
        optionsElement.innerHTML = ''; // Clear any options
        countdownElement.textContent = 'Time left: 0s'; // Pause timer display
    }
});
