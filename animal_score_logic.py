import json

def calculate_playfulness(posture, mood, size):
    """Calculates a numerical score based on 7 distinct behavioral postures."""
    # Base score
    score = 40
    
    # 1. Postures
    # Each posture has a unique weightage depends on energy levels
    if posture == "jumping":
        score += 45
    elif posture == "running":
        score += 40
    elif posture == "play-bow": 
        score += 35
    elif posture == "standing-alert":
        score += 20
    elif posture == "sitting":
        score += 10
    elif posture == "stretching":
        score += 5
    elif posture == "sleeping":
        score -= 25
        
    # 2. Mood Multiplier
    multiplier = 1.0
    if mood == "happy":
        multiplier = 1.5
    elif mood == "curious":
        multiplier = 1.3
    elif mood == "alert":
        multiplier = 1.1
    elif mood == "sleepy":
        multiplier = 0.7
        
    final_score = score * multiplier
    
    # Ensuring that the score stays between 0 and 100
    if final_score > 100: final_score = 100
    if final_score < 0: final_score = 0
        
    return round(final_score, 2)

def generate_emoji(score, posture):
    """Suggests an emoji based on score and specific posture."""
    if posture == "sleeping": return "💤"
    if score >= 85: return "🚀"
    if score >= 60: return "🎾"
    if score >= 40: return "👀"
    return "🐾"
