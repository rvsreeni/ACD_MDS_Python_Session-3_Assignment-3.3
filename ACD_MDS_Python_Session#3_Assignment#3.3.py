# Program to print longest word
def longest_word(wdlist):
    maxlen = 0 
    maxwd = ""
    for wd in wdlist:
        if len(wd) > maxlen:
            maxwd = wd
            maxlen= len(wd)
    return(maxwd)        
input_list = ['one','three','four','two']    
print(longest_word(input_list))
 