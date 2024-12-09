import re

text = "The cat sat on the caterpillar."

# Using \b to match whole word 'cat'
pattern_b = r"\bcat\b"
matches_b = re.findall(pattern_b, text)
print("Using \\b:", matches_b)

# Using [^\w]cat[^\w] to match 'cat' surrounded by non-word characters
pattern_non_word = r"[^\w]cat[^\w]"
matches_non_word = re.findall(pattern_non_word, text)
print("Using [^\\w]cat[^\\w]:", matches_non_word)


print('*'*10)
def foo(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:
            result += lst[i]
        else:
            result -= lst[i]
        result *= 2    
    return result
nums = [1,2,3,4,5]
print(foo(nums))