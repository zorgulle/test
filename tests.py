from .main import reply

def test_reply():
    msg = "Foo"
    result = reply(msg=msg)

    assert result == msg
