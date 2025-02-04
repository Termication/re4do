let countdownTimer;
let score = 0;
const countdownElement = document.getElementById('countdown');
const targetEmojiElement = document.getElementById('target-emoji');
const optionsElement = document.getElementById('options');
const scoreElement = document.getElementById('score');
const bannerElement = document.getElementById('banner');

function updateScore(change) {
    if (score + change < 0) {
        score = 0;
    } else {
        score += change;
    }
    scoreElement.textContent = `Score: ${score}`;
}

function showBanner(message, type) {
    bannerElement.textContent = message;
    bannerElement.className = `show ${type}`; // Set the appropriate banner class (correct, wrong, timeout)
    bannerElement.style.display = 'block';

    setTimeout(() => {
        bannerElement.style.display = 'none';
    }, 2000); // Hide the banner after 2 seconds
}

function fetchNewRound() {
    fetch('/new-round')
        .then(response => response.json())
        .then(data => {
            renderGame(data);
            startCountdown(5);
        })
        .catch(err => {
            console.error('Error fetching new round:', err);
        });
}

function renderGame(data) {
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
    clearInterval(countdownTimer);

    let timeLeft = seconds;
    countdownElement.textContent = `Time left: ${timeLeft}s`;

    countdownTimer = setInterval(() => {
        timeLeft -= 1;
        countdownElement.textContent = `Time left: ${timeLeft}s`;

        if (timeLeft <= 0) {
            clearInterval(countdownTimer);

            updateScore(-1);
            
            showBanner('Time\'s up! ⏰', 'timeout');
            fetchNewRound();
        }
    }, 1000);

    
    document.addEventListener("DOMContentLoaded", () => {
        const userModal = document.getElementById('user-modal');
        const userInfoForm = document.getElementById('user-info-form');
    
        userInfoForm.addEventListener("submit", (event) => {
            event.preventDefault();  // Prevent the form from reloading the page
    
            const name = document.getElementById('name').value;
            const country = document.getElementById('country').value;
            const city = document.getElementById('city').value;
    
            fetch('/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, country, city })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    userModal.style.display = 'none';  // Hide the modal
                    fetchNewRound();  // Start the game
                }
            })
            .catch(err => console.error('Error:', err));
        });
    });
    
}

fetchNewRound();
