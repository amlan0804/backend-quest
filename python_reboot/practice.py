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
from os import eventfd



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
#print (ch)


#name=input()
#print ("Hello",name)

def odd_even(n):
    if (n%2==0):
        return "even"
    else: 
        return "odd"

#n= input()
#print(type(n))
#print (odd_even(n))

#x, y = input("Enter two numbers: ")
#print(x)

initial_list= [1, 2, 2, 3, 1]

#input_list=input().split(',')
#duplicate_list=[]
#for num in input_list:
#    if num not in duplicate_list:
#        duplicate_list.append(num)
#print (duplicate_list)

def word_count(s):
    freq={}
    for word in s.split():
        if word not in freq:
            freq[word]=1
        else:
            freq[word]+=1
    print (freq)


#s="hi hello hi"
#word_count(s)


'''s='hello'
rev=s[::-1]
print (rev)'''

def word_counts(s):
    my_dict={}
    for word in s.split():
        if word not in my_dict:
            my_dict[word]=1
        else:
            my_dict[word]+=1
    print (my_dict)


#s='hi hello hi'
#word_counts(s)

def check_palindrome(s):
    print (s==s[::-1])
        
s='heleh'
#check_palindrome(s)

def rem_duplicate(my_list):
    duplicate=[]
    for num in my_list:
        if num not in duplicate:
            duplicate.append(num)
    print (duplicate)

my_list=[1,2,3,2,4]
#rem_duplicate(my_list)

def first_non_repeat_char(s):
    dup={}
    for char in s:
        if char not in dup:
            dup[char]=1
        else :
            dup[char]+=1

    for char in s:
        if dup[char] ==1:
            return (char)


s='hello'
print(first_non_repeat_char(s))




