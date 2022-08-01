'''
More Frequent Item

Let’s go back to our factory example. 
We have a conveyor belt of items where each item is represented by a different number. 
We want to know, out of two items, which one shows up more on our belt.+
To solve this, we can use a function with three parameters.
 One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

1. Define the function to accept three parameters: the list, the first item, and the second item
2. Count the number of times item1 shows up in our list
3. Count the number of times item2 shows up in our list
4. If item1 shows up more, return item1. Otherwise, return item2

Question:
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
'''
#Write your function here



#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3)) # ouput: 3


'''
Middle Item

For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements. Here is what we need to do:

1. Define the function to accept one parameter for our list of numbers
2. Determine if the length of the list is even or odd
3. If the length is even, then return the average of the middle two numbers
4. If the length is odd, then return the middle number

Question:
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. 
If there are an even number of elements, the function should return the average of the middle two elements.

Hint: 
Remember to use modulus % to determine if a number is divisible by 2. If len(lst) % 2 == 0 then the number is even. 
If we divide the length of the list by 2 we can get the middle element index. 
We then need to convert that value into an integer and access element at that index. This will look something like: lst[int(len(lst)/2)].
'''








'''
Create a function named double_index that has two parameters: a list named lst and a single number named index.

The function should return a new list where all elements are the same as in lst except for the element at index. 
The element at index should be double the value of the element at index of the original lst.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4, 5, 6], 2)
After writing your function, un-comment the call to the function that we’ve provided for you to test your results.
'''
def double_index(lst, index):
    # your code here



    return new_list