def reverse_vowels_bruteforce(s):
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    vowel_indices = []

    # Find indices of vowels in the original string
    for i, char in enumerate(s_list):
        if char in vowels:
            vowel_indices.append(i)

    # Reverse the vowels in the string
    for i in range(len(vowel_indices) // 2):
        left_index = vowel_indices[i]
        right_index = vowel_indices[-i - 1]
        s_list[left_index], s_list[right_index] = s_list[right_index], s_list[left_index]

    return ''.join(s_list)


if __name__=="__main__":
    print(reverse_vowels_bruteforce("leetcode"))