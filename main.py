def palindrome(n):
    c = 1
    for num in range(len(n)):
        if n[num].lower() == n[-num-1].lower():
            pass
        else:
            c = 0
            break
    if c == 0:
        return False
    if c == 1:
        return True

print(palindrome('гг'))
