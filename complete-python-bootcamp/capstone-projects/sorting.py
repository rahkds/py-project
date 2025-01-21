
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(0, n):
        for j in range(0,n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

def selection_sort(numbers):
    n = len(numbers)
    for i in range(0,n):
        j = i
        max_value = numbers[i]
        for k in range(i,n):
            if numbers[k] > max_value:
                max_value = numbers[k]
                j = k

        numbers[i],numbers[j] = numbers[j],numbers[i]
    return numbers




print(bubble_sort([1,56,7,23,56,4,19,10]))
print(selection_sort([1,56,7,23,56,4,19,10]))




