document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('popup-modal');
    const playButton = document.getElementById('play-button');

    // Hide modal and start the game when Play is clicked
    playButton.onclick = () => {
        modal.style.display = 'none';
        fetchNewRound(); // Start the game
    };
});
