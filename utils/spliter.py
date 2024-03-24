# def split_string(s):
#     length = len(s)
#     midpoint = length // 2
#     first_half = s[:midpoint]
#     second_half = s[midpoint:]
#     return first_half, second_half

def split_string(s, p):
    n = len(s) // p
    parts = [s[i:i+n] for i in range(0, len(s), n)]
    return parts