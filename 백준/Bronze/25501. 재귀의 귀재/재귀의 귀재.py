def recursion(word: str, left_idx, right_idx):
    if left_idx >= right_idx:
        return 1, left_idx + 1
    elif word[left_idx] != word[right_idx]:
        return 0, left_idx + 1
    else:
        return recursion(word, left_idx + 1, right_idx - 1)


def isPalindrome(word: str):
    return recursion(word, 0, len(word) - 1)


N = int(input())
for i in range(N):
    print(*isPalindrome(input()))
