"""Word generation."""

import random

from typing import Dict, List, Optional, Tuple


class Word(object):
    """Word generation."""

    def __init__(
        self,
        corpus: Optional[List[str]] = None,
        chain: Optional[Dict[str, List[Tuple[str, int]]]] = None,
    ):
        """Initialization of `Word` class."""
        if not corpus and not chain:
            raise TypeError("Either `corpus` or `chain` parameter is required.")

        self.corpus: Optional[List[str]] = corpus
        self.chain: Dict[str, List[Tuple[str, int]]] = chain if chain else self.build()

    def build(self) -> Dict[str, List[Tuple[str, int]]]:
        """Build the Markov chain."""
        chain: Dict[str, List[Tuple[str, int]]] = {}

        if not self.corpus:
            raise TypeError("`corpus` parameter is required.")

        for word in self.corpus:
            cursor = 0
            current_letter = None
            while cursor < len(word) - 1:
                current_letter = word[cursor]
                next_letter = word[cursor + 1]
                try:
                    suffix_list = chain[current_letter]
                    suffix = None
                    for sf in suffix_list:
                        if sf[0] == next_letter:
                            suffix = sf
                            break
                    if suffix is not None:
                        suffix_list.remove(suffix)
                        new_suffix = (suffix[0], suffix[1] + 1)
                        suffix_list.append(new_suffix)
                    else:
                        chain[current_letter].append((next_letter, 1))
                except KeyError:
                    chain[current_letter] = [(next_letter, 1)]
                cursor += 1
        return chain

    def generate(
        self, min_length: int = 3, max_length: int = 10, max_try: int = 50
    ) -> str:
        """Generate a word."""
        if min_length > max_length:
            min_length = max_length

        word = ""
        try_number = 0

        selected_length = random.randint(min_length, max_length)
        while len(word) < selected_length:
            current_letter = random.choice(list(self.chain.keys()))
            word = current_letter
            while len(word) < selected_length:
                try:
                    letters = [s[0] for s in self.chain[current_letter]]
                    weights = [s[1] for s in self.chain[current_letter]]

                    if set(current_letter) == set(letters):
                        break

                    next_letter = random.choices(letters, weights)[0]
                    word = word + next_letter

                    current_letter = next_letter
                except KeyError:
                    break

            try_number += 1
            if try_number >= max_try:
                break

        return word
