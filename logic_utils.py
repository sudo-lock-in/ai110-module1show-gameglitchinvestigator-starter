def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Rational: Easy = small range, Normal = medium, Hard = largest range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message) as a plain tuple.

    outcome: "Win", "Too High", "Too Low"

    Behavior:
    - Try numeric comparison first by coercing secret to int.
    - If numeric coercion fails, fall back to string comparison.
    - Messages are consistent with outcomes:
        "Too High" -> "📉 Go LOWER!"
        "Too Low"  -> "📈 Go HIGHER!"
    """

    # Try numeric comparison first by coercing secret to int
    try:
        secret_int = int(secret)
    except (TypeError, ValueError):
        # Fallback to string comparison
        g = str(guess)
        s = str(secret)
        if g == s:
            return ("Win", "🎉 Correct!")
        if g > s:
            return ("Too High", "📉 Go LOWER!")
        return ("Too Low", "📈 Go HIGHER!")

    # Numeric comparison
    if guess == secret_int:
        return ("Win", "🎉 Correct!")
    if guess > secret_int:
        return ("Too High", "📉 Go LOWER!")
    return ("Too Low", "📈 Go HIGHER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
