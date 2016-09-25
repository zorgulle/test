import pytest

from .translator import split
from .translator import lower_case

class TestLowerCase:
    """Test case for lowercase
    """

    def test_none_sentence(self):
        """Test the none sentence args
        """
        with pytest.raises(Exception) as e:
            sentence = lower_case()

class TestSplit:
    """Unit test case for split

    split function split sentence into words
    """

    def test_basic_split(self):
        """basic sentence no ponctuation no numbers
        """

        sentence = "i am foo"
        expected  = ['i', 'am', 'foo']

        result = split(sentence=sentence)
        assert result == expected

def test_void():
    assert True
