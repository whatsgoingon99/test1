# def countline(var):
#     with open(var,'r') as f:
#         lines = f.readlines() #reads all lines from the file and returns a list where each element is a line from the file.
#         lines_count = len(lines) ## count the number oflines

#         word_count = 0 ## initialize a counter
#         for line in lines: ## loops throught the list created (lines)
#             words = line.split() ## each line will have hte split() method  that breaks it down to words. Every words will be saved on this var
#             word_count += len(words)  ## length of the words will be added to the counter
#         return f'the file has {lines_count} lines and {word_count} words.'
    

# print(countline('obama_speech.txt'))

x = 0 
while True:
    x = x+1
    if x < 100:
        print(str(x))
        print('<100')
        break
    if x < 200:
        print(str(x))
        print('<200')
        break
    else:
        break
    break