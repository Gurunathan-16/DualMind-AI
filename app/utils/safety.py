BLOCKED_WORDS = [
    "hack",
    "malware",
    "explosive"
]

def is_safe(user_input):

    for word in BLOCKED_WORDS:

        if word in user_input.lower():
            return False

    return True