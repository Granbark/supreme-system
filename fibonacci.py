#fibonacci in python

#enter number in terminal for how many numbers to generate

def fibonacci(num_elements):
    num_elements = int(num_elements)
    if num_elements < 1:
        return
    fibonacci_list = [0,1,1]
    for i in range(len(fibonacci_list), num_elements):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    
    print(fibonacci_list)

fibonacci(input())
    