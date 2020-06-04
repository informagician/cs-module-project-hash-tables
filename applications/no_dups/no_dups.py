def no_dups(s):
    # Your code here
    string = s.split()
    print(string)
    cache = []
    for w in string:
        if w not in cache:
            cache.append(w)
    print(cache)
    new_str = ''
    for w in cache:
        new_str += w
        new_str += " "
    
    final = new_str[:-1]
    print(final)
    return(final)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))