# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    file=open(filename)
    file_content=file.read()
    
    return file_content

    

def count_words():
    text = read_file_content("./story.txt")

    # clean the text
    import string
    
    permitted_characters=string.digits+string.ascii_letters+'_-'+' '
    cleaned_text="".join(c for c in text if c in permitted_characters)
    
    #convert cleaned text to a list
    text_word_list=cleaned_text.split()

    #count the list
    count={}
    
    for word in text_word_list:
        count.setdefault(word,0)
        count[word]=count[word]+1

    return count

count_words()

#print(count_words("./story.txt"))
