#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].
def biggie(lst):
    for i in range(len(lst)):
        if lst[i]>0:
            lst[i]=("big")
    print (lst)
#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values. Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in the list.  For example sum_total([1,2,3,4]) should return 10
def sumlist(lst):
    if len(lst)==0:
        return false
    else:
        return sum(lst)


#Average - Create a function that takes a list as an argument and returns the average of all the values in the list.  For example multiples([1,2,3,4]) should return #2.5
def sumof_lst(lst):
    return sum(lst)/len(lst)
#Length - Create a function that takes a list as an argument and returns the length of the list.  For example length([1,2,3,4]) should return 4
def lstlength(lst):
    if len(lst) ==0:
        return False
    else:
        if len(lst) >0:
            return len(lst)
#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list.  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min_in_list(lst):
    Min=lst[0]
    if len(lst) ==0:
        return False
    else: 
        for element in lst:
            if element<min:
                min =element
        return min



#
#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maxnumber(lst):
    maxnum=lst[0]
    if len(lst)==0:
        return False
    else:
        for num in lst:
            if num> maxnum:
                maxnum=num
        return maxnum

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum ad length of the list.

dict ={}
def ultimate(lst):
  for i in range(len(lst)):
    sumTotal= sum(lst)
    average =sumTotal/len(lst)
    maximum =max(lst)
    minimum =min(lst)
    lst_length= len(lst)
    dict[ 'SumTotal']=sumTotal
    dict['Average'] =average
    dict['Maximum_in_lst']=maximum
    dict['Minimum_in_lst']=minimum
    dict['List_length']=lst_length
  print (dict)

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order.  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.


for number in range(1, 101):
  if number%3 ==0 and number%5==0:
      print(f"{number}Fizz-Buzz")
  elif number%3==0:
    print(f"{number} fizz")
    
  elif number%5==0:
      print(f"{number} Buzz")
  else:
    print(number)
  



#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
 
#Create a function that accepts any number and will create a sequence based on the fibonacci sequence

def fibonacci(n):
    if n <0:
        return 0
    elif n ==1 or n==2:
        return 1
    else: 
        for x in range(2,n):
            return fibonacci(n-1)+(n-2)

input_value=int(input("Enter a number value"))
for i in range(0,input_value):
    print(fibonacci(i))
