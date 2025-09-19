isAnagram = lambda s, t: sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
