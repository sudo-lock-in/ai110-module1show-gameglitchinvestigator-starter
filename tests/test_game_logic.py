from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# ===== check_guess tests =====

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_check_guess_with_string_secret():
    # Test fallback to string comparison when secret can't be coerced to int
    outcome, _ = check_guess("50", "abc")
    assert outcome == "Too Low"  # String comparison: "50" < "abc"

def test_check_guess_edge_case_negative():
    # Test with negative numbers
    outcome, _ = check_guess(-5, -5)
    assert outcome == "Win"
    outcome, _ = check_guess(-3, -5)
    assert outcome == "Too High"
    outcome, _ = check_guess(-7, -5)
    assert outcome == "Too Low"

def test_check_guess_zero():
    # Test with zero
    outcome, _ = check_guess(0, 0)
    assert outcome == "Win"


# ===== get_range_for_difficulty tests =====

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_range_invalid_difficulty_defaults_to_normal():
    # Invalid difficulty should default to Normal range
    low, high = get_range_for_difficulty("InvalidDifficulty")
    assert low == 1
    assert high == 50


# ===== parse_guess tests =====

def test_parse_guess_valid_positive():
    ok, guess_int, err = parse_guess("42")
    assert ok is True
    assert guess_int == 42
    assert err is None

def test_parse_guess_valid_negative():
    ok, guess_int, err = parse_guess("-10")
    assert ok is True
    assert guess_int == -10
    assert err is None

def test_parse_guess_valid_zero():
    ok, guess_int, err = parse_guess("0")
    assert ok is True
    assert guess_int == 0
    assert err is None

def test_parse_guess_valid_with_whitespace():
    ok, guess_int, err = parse_guess("  50  ")
    assert ok is True
    assert guess_int == 50
    assert err is None

def test_parse_guess_empty_string():
    ok, guess_int, err = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."

def test_parse_guess_none_input():
    ok, guess_int, err = parse_guess(None)
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."

def test_parse_guess_float():
    ok, guess_int, err = parse_guess("3.14")
    assert ok is False
    assert guess_int is None
    assert err == "That is not an integer."

def test_parse_guess_scientific_notation():
    ok, guess_int, err = parse_guess("1e3")
    assert ok is False
    assert guess_int is None
    assert err == "That is not an integer."

def test_parse_guess_non_numeric():
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err == "That is not an integer."

def test_parse_guess_mixed_alphanumeric():
    ok, guess_int, err = parse_guess("50abc")
    assert ok is False
    assert guess_int is None
    assert err == "That is not an integer."


# ===== update_score tests =====

def test_update_score_win_first_attempt():
    # First attempt win should give 100 points (100 - 10*(1-1) = 100)
    new_score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert new_score == 100

def test_update_score_win_second_attempt():
    # Second attempt win should give 90 points (100 - 10*(2-1) = 90)
    new_score = update_score(current_score=0, outcome="Win", attempt_number=2)
    assert new_score == 90

def test_update_score_win_tenth_attempt():
    # Tenth attempt win should give 10 points (100 - 10*9 = 10, at minimum)
    new_score = update_score(current_score=0, outcome="Win", attempt_number=10)
    assert new_score == 10

def test_update_score_win_many_attempts():
    # Win after many attempts should not go below MIN_WIN_POINTS (10)
    new_score = update_score(current_score=0, outcome="Win", attempt_number=20)
    assert new_score == 10

def test_update_score_too_high_even_attempt():
    # "Too High" on even attempt should add 5 points
    new_score = update_score(current_score=50, outcome="Too High", attempt_number=2)
    assert new_score == 55

def test_update_score_too_high_odd_attempt():
    # "Too High" on odd attempt should subtract 5 points
    new_score = update_score(current_score=50, outcome="Too High", attempt_number=1)
    assert new_score == 45

def test_update_score_too_low():
    # "Too Low" should always subtract 5 points
    new_score = update_score(current_score=50, outcome="Too Low", attempt_number=1)
    assert new_score == 45
    new_score = update_score(current_score=50, outcome="Too Low", attempt_number=2)
    assert new_score == 45

def test_update_score_too_low_multiple():
    # Multiple "Too Low" outcomes accumulate penalty
    new_score = update_score(current_score=100, outcome="Too Low", attempt_number=1)
    new_score = update_score(current_score=new_score, outcome="Too Low", attempt_number=2)
    new_score = update_score(current_score=new_score, outcome="Too Low", attempt_number=3)
    assert new_score == 85  # 100 - 5 - 5 - 5

def test_update_score_invalid_outcome():
    # Invalid outcome should return score unchanged
    new_score = update_score(current_score=50, outcome="InvalidOutcome", attempt_number=1)
    assert new_score == 50
