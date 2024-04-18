from typing import Dict

# Define lists of non-inclusive, weak, and filler words
negative_words = ["I", "me", "my", "mine", "myself", "we", "us", "our", "ours", "ourselves"]
weak_words = ["very", "just", "maybe", "actually", "really", "somewhat"]
filler_words = ["um", "uh", "like", "you know", "well", "so"]

def process_transcript(transcript: str):
    # Split transcript into words
    words = transcript.split()

    # Total number of words
    total_words = len(words)

    # Initialize dictionaries to store counts and percentages
    counts = {
        "Negative Words": 0,
        "Weak Words": 0,
        "Filler Words": 0
    }
    percentages = {
        "Non-Inclusive Words": 0,
        "Weak Words": 0,
        "Filler Words": 0
    }

    # Count occurrences of each word category
    for word in words:
        word_lower = word.lower()
        if word_lower in negative_words:
            counts["Negative Words"] += 1
        elif word_lower in weak_words:
            counts["Weak Words"] += 1
        elif word_lower in filler_words:
            counts["Filler Words"] += 1

    # Calculate percentages based on total number of words
    for category in counts:
        counts[category] = counts[category]  # Number of occurrences
        percentages[category] = (counts[category] * 100) // total_words if total_words > 0 else 0  # Percentage as integer

    # Calculate repetition percentage of sentence starter words
    starter_words = [words[0].strip().lower()]  # First word in the transcript
    starter_words_count = sum(1 for word in words[1:] if word.strip().lower() in starter_words)
    starter_words_percentage = (starter_words_count * 100) // (total_words - 1) if (total_words - 1) > 0 else 0

    # Prepare result dictionary
    result = {
        "total_words": total_words,
        "negative_words": counts["Negative Words"],
        "negative_words_percentage": percentages["Negative Words"],
        "weak_words": counts["Weak Words"],
        "weak_words_percentage": percentages["Weak Words"],
        "filler_words": counts["Filler Words"],
        "filler_words_percentage": percentages["Filler Words"],
        "sentence_starters_percentage": starter_words_percentage
    }

    return result
