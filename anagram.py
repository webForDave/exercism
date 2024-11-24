def find_anagrams(word, candidates):
    new_word = sorted(list(word.lower()))
    anagrams = []

    for index, char in enumerate(candidates):
        if char.lower() == word.lower():
            candidates.pop(index)
        
    for char in candidates:
        if sorted(list(char.lower())) == new_word:
            anagrams.append(char)
    return anagrams


print(find_anagrams("ΑΒΓ", ["ΒΓΑ", "ΒΓΔ", "γβα", "αβγ"]))
