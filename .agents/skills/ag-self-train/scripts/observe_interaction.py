import os
import sys
import json

def analyze_transcript(conversation_id):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "../../../.."))
    
    app_data_dir = os.path.expanduser("~/.gemini/antigravity-ide")
    transcript_path = os.path.join(app_data_dir, "brain", conversation_id, ".system_generated", "logs", "transcript.jsonl")
    profile_path = os.path.join(repo_root, "learner_profile.json")
    
    if not os.path.exists(transcript_path):
        print(f"Transcript not found: {transcript_path}")
        return
        
    try:
        with open(profile_path, 'r') as f:
            profile = json.load(f)
    except FileNotFoundError:
        profile = {
            "current_module": 1,
            "persona": "Guide",
            "struggle_score": 0,
            "independence_score": 0
        }
        
    struggle_indicators = ["how do i", "can you just show me", "not working", "error", "what is the code"]
    independence_indicators = ["i fixed it", "i see", "done", "let's move on", "i understand"]
    
    with open(transcript_path, 'r') as f:
        for line in f:
            try:
                event = json.loads(line)
                if event.get("type") == "USER_INPUT":
                    content = event.get("content", "").lower()
                    
                    if any(indicator in content for indicator in struggle_indicators):
                        profile["struggle_score"] += 1
                    if any(indicator in content for indicator in independence_indicators):
                        profile["independence_score"] += 1
            except json.JSONDecodeError:
                continue
                
    # Basic logic to shift persona
    if profile["struggle_score"] > profile["independence_score"] + 2:
        if profile["persona"] in ["Launcher", "Peer"]:
            profile["persona"] = "Collaborator"
        elif profile["persona"] == "Collaborator":
            profile["persona"] = "Guide"
    elif profile["independence_score"] > profile["struggle_score"] + 2:
        if profile["persona"] == "Guide":
            profile["persona"] = "Collaborator"
        elif profile["persona"] == "Collaborator":
            profile["persona"] = "Peer"
        elif profile["persona"] == "Peer":
            profile["persona"] = "Launcher"
            
    with open(profile_path, 'w') as f:
        json.dump(profile, f, indent=2)
        
    print(f"Profile updated. New persona: {profile['persona']} (Struggle: {profile['struggle_score']}, Independence: {profile['independence_score']})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python observe_interaction.py <conversation_id>")
        sys.exit(1)
    analyze_transcript(sys.argv[1])
