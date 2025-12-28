from animal_score_logic import calculate_fun_score, get_ai_prediction

def start_project():
    print("Animal playfulness score (powered by MobileNetV2)")
    
    # Simulating a batch of different animals
    test_data = [
        {"name": "Buddy", "mood": "happy", "manual_posture": "jumping"},
        {"name": "Luna", "mood": "curious", "manual_posture": "stretching"},
        {"name": "Charlie", "mood": "happy", "manual_posture": "play-bow"},
        {"name": "Milo", "mood": "sleepy", "manual_posture": "sleeping"}
    ]
    
    results_list = []

    for item in test_data:
        # Calculate score using the 'animal_score_logic' file's logic
        score = calculate_fun_score(item['manual_posture'], item['mood'])
        
        results_list.append({
            "name": item['name'],
            "score": score,
            "posture": item['manual_posture']
        })

    # Create a Leaderboard (Requires: Ranking)
    results_list.sort(key=lambda x: x['score'], reverse=True)
    
    print("\n--- Playfulness Leaderboard ---")
    for rank, p in enumerate(results_list, 1):
        print(f"Rank {rank}: {p['name']} ({p['posture']}) -> Score: {p['score']}/100")

if __name__ == "__main__":
    start_project()
