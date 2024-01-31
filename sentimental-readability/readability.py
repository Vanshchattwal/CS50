# get input string isalpha
string = input("Text: ")
# i am a boy
# no of letters
charlen = 0
for l in string:
    if l.isalpha() == True:
        charlen = charlen + 1
    else:
        charlen = charlen
# no of words
wlen = 1
for l in string:
    if l == " ":
        wlen = wlen + 1
    else:
        wlen = wlen
# no of sentences
slen = 0
news = [".", "!", "?"]
for l in string:
    if l in news:
        slen = slen + 1
    else:
        slen = slen

L = (charlen / wlen) * 100
S = (slen / wlen) * 100

index = 0.0588 * L - 0.296 * S - 15.8
index = round(index)

# sepetated by space " " is word
# occurence of . ! ?
# 20, 7, 2
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
