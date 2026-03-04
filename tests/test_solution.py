"""自动评分测试 - 请勿修改此文件"""
import pytest
from src.solution import reverse_string, count_vowels, find_max


class TestReverseString:
    def test_basic(self):
        assert reverse_string("hello") == "olleh"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_single_char(self):
        assert reverse_string("a") == "a"

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_uppercase(self):
        assert count_vowels("APPLE") == 2

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_empty(self):
        assert count_vowels("") == 0


class TestFindMax:
    def test_basic(self):
        assert find_max([1, 3, 2]) == 3

    def test_negative(self):
        assert find_max([-1, -5, -2]) == -1

    def test_single(self):
        assert find_max([42]) == 42

    def test_empty(self):
        assert find_max([]) is None

    def test_duplicates(self):
        assert find_max([5, 5, 5]) == 5
