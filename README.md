# Animal-Score-Logic
"A Python project that uses Image Classification to identify animal actions (like playing or sitting etc.) and calculates a 'Fun Score' using a custom-weighted logic."

## Project Description
This project is a Python tool that calculates a "Playfulness Score" for animals based on their actions and mood. It is designed to work as the logic layer for an AI-powered camera system.

## Features Implemented
- **Size Scaling:** Differentiates between big and small animals for score weighting.
- **Posture Detection:** Identifies 'Standing', 'Sitting', 'Lying', or 'Playful' states.
- **Social Logic:** Includes a bonus for multiple animals interacting.
- **Output:** Generates a Fun Score (0-100) and mood-based emojis.

### How it Works:
1. **Input:** The system receives an animal's posture (like "Jumping" or "Sleeping").
2. **Scoring Logic:** In `engine.py`, points are added based on the action's energy level. 
3. **Safety Check:** A math rule ensures scores stay between 0 and 100.
4. **Display:** In `main.py`, the animals are ranked and displayed in a neat table with emojis.

## The Logic engine
The project uses a **Heuristic Scoring Model**. 
- **Base Score:** Derived from the posture (e.g., Playful = 50 pts).
- **Multipliers:** Small animals receive a +20 point bonus.
- **Social Bonus:** Interactions between animals add +30 points to the total.

### Why use two files?
I used a **Modular Design**. `engine.py` handles the "math and rules," while `main.py` handles the "display and ranking."

## How to Run
1. Have Python installed.
2. Run `python animal_score_logic.py`.

'''### Sample Output:
--- Animal Analytics: Playfulness Leaderboard ---

Rank  | Name     | Score  | Status
-----------------------------------
1     | Buddy    | 100.0  | 🚀 (jumping)
2     | Charlie  | 100.0  | 🚀 (play-bow)
3     | Max      | 66.0   | 🎾 (standing-alert)
4     | Luna     | 58.5   | 🐾 (stretching)
5     | Milo     | 10.5   | 😴 (sleeping)'''

'''### Sample Output:
```text
--- Animal Analytics: Playfulness Leaderboard ---

Rank  | Name     | Score  | Status
-----------------------------------
1     | Buddy    | 100.0  | 🚀 (jumping)
2     | Charlie  | 100.0  | 🚀 (play-bow)
3     | Max      | 66.0   | 🎾 (standing-alert)
4     | Luna     | 58.5   | 🐾 (stretching)
5     | Milo     | 10.5   | 😴 (sleeping)
'''
```markdown
### Sample Output:

| Rank | Name | Score | Status |
| :--- | :--- | :--- | :--- |
| 1 | Buddy | 100.0 | 🚀 (jumping) |
| 2 | Charlie | 100.0 | 🚀 (play-bow) |
| 3 | Max | 66.0 | 🎾 (standing-alert) |
| 4 | Luna | 58.5 | 🐾 (stretching) |
| 5 | Milo | 10.5 | 😴 (sleeping) |
