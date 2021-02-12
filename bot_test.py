from bot import Bot


def test_process_input():
    b = Bot()
    assert b.process_input("Is this a good example?") == [
        "Is",
        "this",
        "a",
        "good",
        "example",
    ]
    assert b.process_input("How:/about{{#@}} this    one ?") == [
        "How",
        "about",
        "this",
        "one",
    ]
