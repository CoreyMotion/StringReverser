#Project created to satisfy exercise requirements of "Write a code that reverses a string"
#https://github.com/bregman-arie/devops-exercises/blob/master/exercises/python/reverse_string.md


str1 = input("Please enter some text you'd like to reverse:\n")
for x in range(len(str1)):
    print(str1[len(str1)-1-x], end = '')
print()


# This code would also reverse the string str1[::-1], however the above is a more visual representation
# Note the visual code run in this script is more time consuming than str1[::-1]