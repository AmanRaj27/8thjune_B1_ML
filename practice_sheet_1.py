##question 2 solution
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True * False)
print(True & False)
print(True and False)
print((6>3) and (7<4) or (18==3)) and (9>3)
print(True is False)
print('False' in 'False')
print((True == False) or (False > True)) and (False <= True)

##question 3 solution
s1="Nice to have you"
s2="here"
print(s1+' '+s2)

##question 4 solution
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a.pop(3).pop(1).pop(2))

##question 5 solution
print([s1]+a+[s2])

##question 6 solution
color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"])
print(color_list_1 .difference (color_list_2))

##question 7 solution
def pangram(st):
    import string
    small=set(string.ascii_lowercase)
    return small<=set(st.lower())
s=input('Enter a string: ')
if pangram(s):
    print('it is a pangram')
else:
    print('it is not a pangram')


##question 8 solution
n=input("Enter the number: ")
print(eval('{0}+{0}{0}+{0}{0}{0}'.format(n)))

##question 9 solution
s=['without','hello','bag','world']
s.sort()
print(s)

##question 10 solution
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])

