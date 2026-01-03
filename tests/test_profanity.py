from app.services.profanity_filter import censor_profanity

def test_censors_banned_word():
    out = censor_profanity("This is bloody bad", ["bloody"])
    assert "bloody" not in out.lower()