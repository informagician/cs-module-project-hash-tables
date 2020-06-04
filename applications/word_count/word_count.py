def word_count(s):
    # Your code here
    punc = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    punc_list = punc.split()
    punc_dict = {i:'' for i in punc}
    s = s.lower()
    # print(s)
    string_list = s.split()
    new_string_list = []
    for word in string_list:
        new_word = ""
        for c in word:
            if c not in punc_dict:
                new_word += c
        if len(new_word) > 0:
            new_string_list.append(new_word)
    print(new_string_list)
    string_dict = {}
    for word in new_string_list:
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    print(string_dict)
    return string_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))