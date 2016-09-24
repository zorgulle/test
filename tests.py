from .main import reply

def test_reply():
    msg = "Foo"
    result = main.reply(msg=msg)

    assert result == msg
