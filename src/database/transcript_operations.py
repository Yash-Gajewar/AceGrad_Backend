# Negative words
negative_words = [
    "abysmal",
    "adverse",
    "abrasive",
    "apathetic",
    "atrocious",
    "controlling",
    "dishonest",
    "impatient",
    "betrayed",
    "incompetent",
    "disappointed",
    "jealous",
    "angry",
    "annoyed",
    "cruel",
    "grumpy"
]

# Weak words

weak_words = [
    "almost",
    "apparently",
    "absolutely",
    "actually",
    "a little",
    "sort of",
    "used to"
]


filler_words = [
    "huhh",
    "uh",
    "um",
    "ah",
    "like",
    "you know",
    "okay",
    "so",
    "well",
    "right",
    "actually",
    "basically",
    "essentially",
    "literally",
    "totally",
    "obviously",
    "seriously",
    "definitely",
    "absolutely",
    "honestly",
    "just",
    "you know",
    "you see",
    "I mean",
    "kind of",
    "sort of",
    "I guess",
    "I think",
    "er",
    "ohhh",
    "umm",
    "ahh",
    "um",
    "ah",
    "aah",
    "ohhh",
    "aaahhh"

]

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
        "Negative Words": 0,
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
