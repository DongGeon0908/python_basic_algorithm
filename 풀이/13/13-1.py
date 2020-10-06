def palindrome(s):
    qu = []
    st =[]
    for i in s:
        if i.isalpha():
            qu.append(i.lower())
            st.append(i.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True

print(palindrome("Wow"))
print(palindrome("Woa"))
