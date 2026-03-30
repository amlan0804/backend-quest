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
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    print(dict)


s="hi him"
word_count(s)