"""
The goal of this exercise is to convert a string to a new string where each
character in the new string is "(" if that character appears only once in
the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""

def duplicate_encode(word):
    new_word = []
    word_low = word.lower()
    for i in range(len(word_low)):
        if word_low.count(word_low[i]) > 1:
            new_word.append(")")
        else:
            new_word.append("(")
    return "".join(new_word)
print(duplicate_encode("TPkxxFduJwvbIckvckFPcmTGax"))
