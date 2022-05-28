
def find_anagram(word, anagram):
    # [assignment] Add your code here

    word_list=list(word)
    word_list.sort()
    
    anagram_list=list(anagram)
    anagram_list.sort()
    
    if  word_list == anagram_list:
        return True
    else:
        return False


