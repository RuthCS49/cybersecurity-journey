
# the first one
#  it calculates the sum of numbers
"""

def sum_to(n):
    if n <= 0 :
        return 0
    else:
        return n + sum_to(n-1)
print(sum_to(-9))    

"""
# the second one
# to get the reverse of a text 

"""

def reverse(text):
    if len(text) <= 1:
        return text
    return text[:: -1]
    
print(reverse("How are you!"))

"""

# the third one
# to reverse a text using recursion only 
"""

def reverse(text):
    print ("Called with", text)
    if len(text) <= 1 :
        return text
    first = text[0]
    rest = text[1:]
    return reverse(rest) + first
print(reverse("python"))
"""

# the forth one 
# the palidrome check
"""

def reverse(text):
  
    if len(text) <= 1 :
        return text
    first = text[0]
    rest = text[1:]
    return reverse(rest) + first


def is_palindrome(text):

    return reverse(text) == text
word = "madam"

print(f"Is {word} palindrome to {reverse(word)} ? ", is_palindrome(word))

"""

# the fifth one
# the count item in  a list (a nested one)

def count_items (data):
    total = 0
    for  i in  data:
        if  isinstance( i, list):
        
           total += count_items(i)
        else:
            total += 1

    return total
    
print(count_items([1,2,[90,76,66,3,],[100,300]]))    
print(count_items(["Apple", "mango," ,"banana", ["mercedz", "audi","porche"],["cup", "spoon", "plate"], "pen", "eraser", "book" ]))
print(count_items([[], [],[[]]]))


    
   