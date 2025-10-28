# Sample string utilities module
"""
string_utils.py - A collection of string utility functions
"""

def capitalize_words(text):
    """Capitalize the first letter of each word"""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def remove_duplicates(text):
    """Remove duplicate characters from a string"""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Module constants
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"