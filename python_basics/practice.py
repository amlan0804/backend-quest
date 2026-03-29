# #rint("hello")

# s='hello'
# result=''

# for i,ch in enumerate(s):
#     print (i,ch)
# #     result=ch+result
# # print(result)

def word_count(s):
    dict={}
    for word in s.split():
        dict[word]=s.count(word)
    print(dict)


s="hi hi hello"
word_count(s)