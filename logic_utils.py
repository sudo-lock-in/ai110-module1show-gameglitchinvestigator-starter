# FIX: all below methods were refactored from app.py using Copilot Agent mode

# FIX: I asked copilot to fix the difficulty range mismatch
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
    return 1, 50 # FIX: Inline editor was used to set this default return value to that of normal difficulty
# - which was missed by Copilot's initial fix


# FIX: Copilot initially wanted me to continue to allow floats when optimizing this method 
# - But I decided integers would make most sense and requested that implementation instead.
def parse_guess(raw: str):
    """
    Parse user input into an int guess. Accept only integer input (no floats).

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    raw_str = str(raw).strip()
    if raw_str == "":
        return False, None, "Enter a guess."

    # Reject floats and other non-integer formats (e.g. '3.0' or '1e3')
    if "." in raw_str:
        return False, None, "That is not an integer."

    try:
        value = int(raw_str)
    except Exception:
        return False, None, "That is not an integer."

    return True, value, None

# FIX: the logic is updated to compare guess with the secret and suggest accurate hints
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

# FIX: Copilot had initially fixed the method to have clear variables but with the same logic
# - however, after asking Copilot to explain the code I noticed the user cannot recieve max 100 points
# so I requested an appropiate update for the logic around attempts and point calculation for win
def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Return updated score based on outcome and attempt number.

    Notes:
    - `attempt_number` is 1-based (first guess is 1, second is 2, etc.).
    - Win points decay with attempts: points = WIN_BASE - WIN_DECAY * (attempt_number - 1).
      For a win on the first guess (attempt_number=1): 100 - 10*0 = 100 points.
      Minimum points awarded for a win is MIN_WIN_POINTS.
    - For a "Too High" outcome a parity rule is applied: +PARITY_POINTS when
      attempt_number is even, -PARITY_POINTS when odd (keeps original behavior).
    - "Too Low" always subtracts PARITY_POINTS.

    Returns the new score (int).
    """
    WIN_BASE = 100
    WIN_DECAY = 10
    MIN_WIN_POINTS = 10
    PARITY_POINTS = 5

    if outcome == "Win":
        points = WIN_BASE - WIN_DECAY * (attempt_number - 1)
        if points < MIN_WIN_POINTS:
            points = MIN_WIN_POINTS
        return current_score + points

    elif outcome == "Too High":
        # Preserve the original parity-based behavior
        if attempt_number % 2 == 0:
            return current_score + PARITY_POINTS
        return current_score - PARITY_POINTS

    elif outcome == "Too Low":
        return current_score - PARITY_POINTS

    return current_score
