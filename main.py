# main.py
from engine import calculate_fun_score
import time

# SIMULATING MOBILENETV2 CONNECTION
def get_mobilenet_prediction(animal_id):
    
    # Here, I have made a 'Mock' output representing what the AI sees
    ai_vision_db = {
        "Buddy": "jumping",
        "Charlie": "play-bow",
        "Max": "standing-alert",
        "Luna": "stretching",
        "Milo": "sleeping"
    }
    return ai_vision_db.get(animal_id, "sitting")

# THE DATA (Only Names and Moods)
animals = [
    {"name": "Buddy", "mood": "sleepy"},
    {"name": "Charlie", "mood": "happy"},
    {"name": "Max", "mood": "alert"},
    {"name": "Luna", "mood": "curious"},
    {"name": "Milo", "mood": "sleepy"}
]

print("--- Initializing MobileNetV2 Inference Stream ---")
time.sleep(1) # Simulates the AI 'loading'

results = []
for a in animals:
    
    detected_posture = get_mobilenet_prediction(a['name'])
    
    score, emoji = calculate_fun_score(detected_posture, a['mood'])
    
    results.append({
        "name": a['name'], 
        "score": score, 
        "emoji": emoji, 
        "posture": detected_posture
    })

# Sort and Print
results.sort(key=lambda x: x['score'], reverse=True)
print(f"{'Rank':<5} | {'Name':<8} | {'Score':<6} | {'Status (AI Detected)'}")
print("-" * 50)
for rank, p in enumerate(results, 1):
    print(f"{rank:<5} | {p['name']:<8} | {p['score']:<6} | {p['emoji']} ({p['posture']})")
