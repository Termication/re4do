let countdownTimer;
let score = 0;
let isGameStarted = false; // Ensure game is paused initially

const countdownElement = document.getElementById('countdown');
const targetEmojiElement = document.getElementById('target-emoji');
const optionsElement = document.getElementById('options');
const scoreElement = document.getElementById('score');
const bannerElement = document.getElementById('banner');

function updateScore(change) {
    score += change;
    scoreElement.textContent = `Score: ${score}`;
}

function showBanner(message, type) {
    bannerElement.textContent = message;
    bannerElement.className = `show ${type}`;
    bannerElement.style.display = 'block';

    setTimeout(() => {
        bannerElement.style.display = 'none';
    }, 2000);
}

function fetchNewRound() {
    if (!isGameStarted) return; // Ensure game doesn’t start before play is clicked

    fetch('/new-round')
        .then(response => {
            if (!response.ok) {
                console.warn("Game is not started yet.");
                return;
            }
            return response.json();
        })
        .then(data => {
            if (data) {
                renderGame(data);
                startCountdown(5);
            }
        })
        .catch(err => console.error('Error fetching new round:', err));
}

function renderGame(data) {
    if (!isGameStarted) return; // Ensure game is paused

    const { target, options } = data;

    targetEmojiElement.textContent = target;
    optionsElement.innerHTML = '';

    options.forEach(emoji => {
        const emojiButton = document.createElement('div');
        emojiButton.className = 'emoji-option';
        emojiButton.textContent = emoji;

        emojiButton.onclick = () => {
            if (emoji === target) {
                updateScore(5);
                showBanner('Correct! 🎉', 'correct');
            } else {
                updateScore(-2);
                showBanner('Wrong! 😢', 'wrong');
            }
            fetchNewRound();
        };

        optionsElement.appendChild(emojiButton);
    });
}

function startCountdown(seconds) {
    if (!isGameStarted) return; // Ensure countdown doesn’t start before play is clicked

    clearInterval(countdownTimer);
    let timeLeft = seconds;
    countdownElement.textContent = `Time left: ${timeLeft}s`;

    countdownTimer = setInterval(() => {
        if (!isGameStarted) {
            clearInterval(countdownTimer);
            return;
        }

        timeLeft -= 1;
        countdownElement.textContent = `Time left: ${timeLeft}s`;

        if (timeLeft <= 0) {
            clearInterval(countdownTimer);
            updateScore(-1);
            showBanner("Time's up! ⏰", "timeout");
            fetchNewRound();
        }
    }, 1000);
}

// Prevent game from starting automatically
optionsElement.innerHTML = '';
targetEmojiElement.textContent = '🎮'; // Placeholder before game starts
countdownElement.textContent = 'Time left: 0s';
