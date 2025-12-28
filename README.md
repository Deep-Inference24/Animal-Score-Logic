# Animal-Score-Logic
"A Python project that uses Image Classification to identify animal actions (like playing or sitting etc.) and calculates a 'Fun Score' using a custom-weighted logic."

## Project Description
This is a **Vision-Based Fun Score Predictor** designed to analyze animal images and quantify their playfulness. The system extracts features like posture, size, and social interaction to generate a standardized score.

## Features Implemented
- **Size Scaling:** Differentiates between big and small animals for score weighting.
- **Posture Detection:** Identifies 'Standing', 'Sitting', 'Lying', or 'Playful' states.
- **Social Logic:** Includes a bonus for multiple animals interacting.
- **Output:** Generates a Fun Score (0-100) and mood-based emojis.

## The Logic Engine
The project uses a **Heuristic Scoring Model**. 
- **Base Score:** Derived from the posture (e.g., Playful = 50 pts).
- **Multipliers:** Small animals receive a +20 point bonus.
- **Social Bonus:** Interactions between animals add +30 points to the total.

## How to Run
1. Have Python installed.
2. Run `python animal_score_logic.py`.
