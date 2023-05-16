def longest(s1, s2):
    distinct_letters = sorted(set(s1 + s2))
    return ''.join(distinct_letters)
