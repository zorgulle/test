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

    def test_empty_sentence(self):
        """test empty sentence
        """

        sentence = ""
        expected = ""

        result = lower_case(sentence=sentence)

        assert result == expected

    def test_basic_sentence(self):
        """Sentence without number or ponctuation
        """

        sentence = "I am Foo"
        expected = "i am foo"


        result = lower_case(sentence=sentence)

        assert result == expected

    def test_already_lower_case(self):
        """test sentence in lower case
        """
        sentence = "i am foo"
        expected = "i am foo"

        result = lower_case(sentence=sentence)

        assert result == expected



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

    def test_upper_case_sentence(self):
        """Sentence with lower case
        """

        sentence = "I am Foo"
        expected  = ['i', 'am', 'foo']

        result = split(sentence=sentence)
        assert result == expected


def test_void():
    assert True
