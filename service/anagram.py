import collections
from typing import List
from models.turn import Solution, Turn
from models.char_ocurrence import CharOccurrence
from core.service import Service

all_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

@Service
class AnagramService:

    def get_words_dict(self,file_):
        """Read a file with words.  Prune out anything with punctuation."""
        result_dict = collections.defaultdict(set)

        for candidate_line in file_:
            candidate_word = candidate_line.lower().rstrip()
            if candidate_word.isalpha():
                length = len(candidate_word)
                result_dict[length].add(candidate_word)

        return result_dict


    def is_word_of_alphabet(self,alphabet, word):
        """Check if a word conforms to our alphabet."""
        words_alphabet = CharOccurrence(word)
        return bool(words_alphabet.is_subset(alphabet))


    def prune_words_dict_for_alphabet(self,words_dict, alphabet):
        """Eliminate words that aren't over the appropriate alphab from our words_dict."""
        result_dict = collections.defaultdict(set)
        for length, words_of_length in words_dict.items():
            for word in words_of_length:
                if self.is_word_of_alphabet(alphabet, word):
                    result_dict[length].add(word)
        return result_dict


    def find_anagrams(self,letter_to_anagram, dict_file='assets/mots.txt'):
        """Find anagrams for a sentence."""
        result_anagrams = []

        list_to_anagram = list(letter_to_anagram)

        sentence_frequencies = CharOccurrence(list_to_anagram)

        with open(dict_file, 'r') as dictionary_file:
            original_dict = self.get_words_dict(dictionary_file)

        prune_dict = self.prune_words_dict_for_alphabet(original_dict, sentence_frequencies)

        # print("Original dict")
        # print(prune_dict)

        for letter in all_alphabets:
            # try another anagram with the letter
            sent_freq = CharOccurrence([lettre for lettre in list_to_anagram] + [letter])
            dict = self.prune_words_dict_for_alphabet(original_dict, sent_freq)
            # print("Dict "+letter)
            # print(dict)
            for length, words in dict.items():
                for word in words:
                    prune_dict[length].add(word)

        # Set to list
        for length, words in prune_dict.items():
            for word in words:
                result_anagrams.append(word)

        anagram_list_with_score = collections.defaultdict(set)

        # Score
        for anagram in result_anagrams:
            score_mot = 0
            for letter_in_anagram in anagram:
                if letter_in_anagram in "aeilnorstu":
                    score_mot += 1
                elif letter_in_anagram in "dgm":
                    score_mot += 2
                elif letter_in_anagram in "bcp":
                    score_mot += 3
                elif letter_in_anagram in "fhv":
                    score_mot += 4
                elif letter_in_anagram in "jq":
                    score_mot += 8
                elif letter_in_anagram in "kwxyz":
                    score_mot += 10
            anagram_list_with_score[score_mot].add(anagram)

        final_anagram_list: List[Solution] = []
        for score, anagrams in anagram_list_with_score.items():
            final_anagram_list.append(Solution(score, list(anagrams)))

        final_anagram_list.sort(reverse=True)

        return Turn(letter_to_anagram, final_anagram_list)


if __name__ == '__main__':
    res = find_anagrams('archozy')
    print(res)
