"""Tests of `Word` class."""

import pytest

from juncaks import Word


def test_word_invalid_parameters():
    with pytest.raises(TypeError):
        Word()


def test_word_build_invalid_parameter():
    chain = {
        "r": [("a", 1)],
        "a": [("n", 1)],
        "n": [("d", 1)],
        "d": [("o", 1)],
        "o": [("m", 1)],
    }

    word = Word(chain=chain)
    with pytest.raises(TypeError):
        word.build()


def test_word_build_one_word():
    corpus = ["random"]
    expected_chain = {
        "r": [("a", 1)],
        "a": [("n", 1)],
        "n": [("d", 1)],
        "d": [("o", 1)],
        "o": [("m", 1)],
    }

    word = Word(corpus=corpus)
    assert expected_chain == word.chain


def test_word_build_no_intersection():
    corpus = ["random", "red"]
    expected_chain = {
        "r": [("a", 1), ("e", 1)],
        "a": [("n", 1)],
        "n": [("d", 1)],
        "d": [("o", 1)],
        "o": [("m", 1)],
        "e": [("d", 1)],
    }

    word = Word(corpus=corpus)
    assert expected_chain == word.chain


def test_word_build_intersection():
    corpus = ["random", "rat"]
    expected_chain = {
        "r": [("a", 2)],
        "a": [("n", 1), ("t", 1)],
        "n": [("d", 1)],
        "d": [("o", 1)],
        "o": [("m", 1)],
    }

    word = Word(corpus=corpus)
    assert expected_chain == word.chain


def test_word_generate():
    corpus = ["random"]
    word = Word(corpus=corpus)
    word.generate()


def test_word_generate_prevent_loop():
    corpus = ["ee"]
    word = Word(corpus=corpus)
    word.generate()


def test_word_generate_min_length():
    corpus = ["random"]
    word = Word(corpus=corpus)
    word.generate(min_length=4)


def test_word_generate_max_length():
    corpus = ["random"]
    word = Word(corpus=corpus)
    word.generate(max_length=1)
