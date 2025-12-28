def get_ai_prediction():
    """
    Simulates the output of an AI model, MobileNetV2.
    """
    # these come from the model that I have used(MobileNetV2)
    detected_animal = "Dog"
    detected_posture = "Play-bow" 
    return detected_animal, detected_posture

def calculate_fun_score(posture, mood):
    """
    Calculates the score and assigns a mood-based emoji.
    """
    base_score = 40
    
    # Postures logic
    posture_weights = {
        "jumping": 45, "running": 40, "play-bow": 35,
        "standing-alert": 20, "sitting": 10, "stretching": 5, "sleeping": -25
    }
    
    score_after_posture = base_score + posture_weights.get(posture.lower(), 0)
    
    # Mood multiplier
    multiplier = 1.0
    if mood == "happy": multiplier = 1.5
    elif mood == "curious": multiplier = 1.3
    elif mood == "sleepy": multiplier = 0.7
        
    final_score = round(max(0, min(score_after_posture * multiplier, 100)), 2)

    # Emoji Selection Logic
    if posture.lower() == "sleeping":
        emoji = "😴"
    elif final_score >= 85:
        emoji = "🚀"
    elif final_score >= 60:
        emoji = "🎾"
    elif final_score >= 40:
        emoji = "🐾"
    else:
        emoji = "☁️"
        
    return final_score, emoji
