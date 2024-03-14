import collections


class CharOccurrence(object):
    """Collection of char occurrence in a sentence"""

    def __init__(self, sentence):
        """Initialize a CharOccurrence."""
        self.frequencies = collections.Counter(sentence)
        if ' ' in self.frequencies:
            del self.frequencies[' ']

    def __sub__(self, other):
        """Subtract two CharOccurrence"""
        result = CharOccurrence('')

        result.frequencies = self.frequencies - other.frequencies

        return result

    def is_subset(self, other):
        """Return True if self is a subset of others."""
        self_keys = set(self.frequencies)
        other_keys = set(other.frequencies)

        if self_keys <= other_keys:
            for key in self_keys:
                if self.frequencies[key] > other.frequencies[key]:
                    return False
            return True

        return False

