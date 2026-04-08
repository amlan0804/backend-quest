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


# def word_count(s):
#     dict={}
#     for word in s.split():
#         if word in dict:
#             dict[word]+=1
#         else:
#             dict[word]=1
#     print(dict)





# s="hi hello him"
# word_count(s)
def checkPalindrome(s):
    return s==s[::-1]

str="madam"
flag=checkPalindrome(str)
#print(flag)

my_list= [1, 2, 2, 3, 4, 1]
for i, element in enumerate(my_list):
    for j, next_element in enumerate(my_list[i + 1:], start=i + 1):
        if next_element ==element:
            my_list.pop(j)

result=[]
for element in my_list:
    if element not in result:
        result.append(element)

#print (result)


# def non_repeating_ch(str):
#     for i, ch in enumerate(str):
#         if ch not in str[i+1:]:
#             return ch

def non_repeating_ch(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in s:
        if freq[ch]==1:
            return ch
    return None
        
my_str= "leetcode"
ch=non_repeating_ch(my_str)
print (ch)