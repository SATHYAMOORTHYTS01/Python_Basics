letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
# letters_tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
# letters_set = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
# filter the vowels from a string
## a,e,i,o,u

def vowels_given(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

# result = filter_vowel('p')
# #print(result)

filtered_vowels = filter(vowels_given,letters_list)
print(list(filtered_vowels))
