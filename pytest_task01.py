import pytest
from Task01 import only_alphabet
text = 'another fine myth'


def test01():
    assert only_alphabet('another fine myth') == text, 'Something wrong'


def test02():
    assert only_alphabet('Another fine myth') == text, 'Something wrong'


def test03():
    assert only_alphabet('another. fine- myth:') == text, 'Something wrong'


def test04():
    assert only_alphabet('anotherрусский fine языкmyth') == text, 'Something wrong'


def test05():
    assert only_alphabet('65_Another 570fine* myth.Русский') == text, 'Something wrong'


if __name__ == '__main__':
    pytest.main(['-v'])
    