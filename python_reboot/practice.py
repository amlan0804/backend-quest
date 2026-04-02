# #rint("hello")

# s='hello'
# result=''

# for i,ch in enumerate(s):
#     print (i,ch)
# #     result=ch+result
# # print(result)

# def word_count(s):
#     dict={}
#     for word in s.split():
#         if word in dict:
#             dict[word]+=1
#         else:
#             dict[word]=1
#     print(dict)


# s="hi him"
# word_count(s)


# def max_element(ls):
#     max=0
#     for element in ls:
#         if element > max:
#             max=element
#     return max




# list=[3, 7, 2, 10, 1]
# max=max_element(list)
# print(max)


def word_count(s):
    dict={}
    for word in s.split():
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    print(dict)





s="hi hello him"
word_count(s)

print("test ssh")