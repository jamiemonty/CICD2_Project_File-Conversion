from app.services.spellchecker import spellcheck_text

def test_marks():
    dictionary = {"this", "is", "good"}
    text, suggestions = spellcheck_text("this is goood", dictionary)
    assert "*goood*" in text
    assert "goood" in suggestions