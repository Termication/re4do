# Emoji Match Game

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [How to Play](#how-to-play)
6. [Project Structure](#project-structure)
7. [Future Enhancements](#future-enhancements)

---

## Introduction
The Emoji Match Game is a fun and interactive browser-based game where players match a randomly displayed target emoji with one of the emojis displayed in a grid. The game is designed to test reflexes and attention to detail, offering an enjoyable experience for all ages.

---

## Features
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.
- **Dynamic Gameplay**: A new target emoji and options grid are generated for each round.
- **Scoring System**:
  - Correct matches: +5 points
  - Incorrect matches: -2 points
- **Countdown Timer**: Players must make a match before the time runs out.
- **Feedback Banner**:
  - Displays messages for correct, incorrect, and timeout events.
  - Smooth fade-in and fade-out animations.
- **Interactive Emoji Grid**: Hover effects and responsive layout for a better user experience.

---

## Technologies Used
- **HTML5**: For structuring the webpage.
- **CSS3**: For styling and animations.
- **JavaScript (Vanilla)**: For game logic and interactivity.
- **Fetch API**: To simulate backend interactions for generating new game rounds.

---

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/emoji-match-game.git
   cd emoji-match-game
   ```

2. **Set Up Backend (Optional)**:
   If using a backend to generate new rounds, ensure your backend server provides the `/new-round` endpoint that returns JSON data in the following format:
   ```json
   {
     "target": "😄",
     "options": ["😀", "😃", "😄", "😁"]
   }
   ```

3. **Run the Project**:
   Open the `index.html` file in any modern web browser.

---

## How to Play
1. The game starts by displaying a target emoji above the grid.
2. A timer starts counting down from 5 seconds.
3. Click on the emoji in the grid that matches the target emoji.
   - **Correct Match**: Gain 5 points, and the next round begins.
   - **Incorrect Match**: Lose 2 points, and the next round begins.
   - **Timeout**: If time runs out, no points are awarded, and the next round begins.
4. The score is displayed at the top of the screen.

---

## Project Structure
```
emoji-match-game/
├── index.html        # Main HTML file for the game
├── style.css         # Embedded or external CSS styles
├── script.js         # Game logic and interactivity
├── README.md         # Project documentation
```

---

## Future Enhancements
1. **Multiplayer Mode**: Add support for real-time competition between players.
2. **Leaderboard**: Display high scores to encourage competitive play.
3. **Difficulty Levels**: Introduce varying grid sizes and timer durations.
4. **Custom Emojis**: Allow players to select or upload their own emoji sets.
5. **Mobile Optimization**: Enhance the layout for small-screen devices.
6. **Sound Effects**: Add audio feedback for correct, incorrect, and timeout events.

---

Enjoy the game and feel free to contribute or suggest improvements!

