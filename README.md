
# Air Hockey Game

A classic two-player air hockey game built with Python's turtle library.


---

🕹️ How to Play

The game features two paddles, a ball, and a scoreboard. The objective is to score points by getting the ball past your opponent's paddle.

**Player One** (Left Side):
* **Move Up:** `W`
* **Move Down:** `S`

**Player Two** (Right Side):
* **Move Up:** `Up Arrow`
* **Move Down:** `Down Arrow`

**Game Controls:**
* **Quit Game:** `Escape`
* **Start/Reset:** The ball starts in the center and moves automatically. If a goal is scored, the ball resets to the center and serves to the opposite side.

---


📂 Project Structure

The project is organized into several files, with each class handling a specific part of the game.

* `main.py`: Contains the main game loop, sets up the screen, and manages interactions between all the game objects.
* `stick.py`: Defines the `Stick` class, which handles the paddles' movement and boundaries.
* `ball.py`: Defines the `Ball` class, which handles the ball's movement, bouncing, and resetting.
* `scoreboard.py`: Defines the `Scoreboard` class, which manages and displays both players' scores.
* `dividing_line.py`: Defines the `DividingLine` class, which draws the central dividing line on the screen.

---

🔧 Installation and Setup

1.  **Clone the repository** 
2.  **Ensure you have Python installed.** The `turtle` library is a standard part of a Python installation.
3.  **Run the game from your terminal:**

    ```bash
    python main.py
    ```

---

✨ Features

* **Two-Player Gameplay:** Control separate paddles with distinct keys.
* **Collision Detection:** The ball accurately bounces off the walls and paddles.
* **Scoring System:** A live scoreboard tracks points for both players.
* **Simple Graphics:** A clean, retro design using the `turtle` graphics library.

---
