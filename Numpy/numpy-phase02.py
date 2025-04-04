import numpy as np

arr_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Specific Eleent :", arr_2D[2, 2], "\n")
print("Entire Row :", arr_2D[1], "\n")
print("Entire Column :", arr_2D[:1], "\n")

# SORTING
unsorted = np.array([222, 445, 232, 1, 43, 66, 4, 3, 1, 0, 434, 2, 546, 235])
sort = np.sort(unsorted)
print("Sorted array :", sort, "\n")

# If we have 2D array the  how we sort the array ??
arr2D = np.array([[9, 21, 5], [0, 666, 11], [3, 80, 5]])

print(np.sort(arr2D, axis=0))  # -----> they sort the column becasue of axis=0
print(np.sort(arr2D, axis=1), "\n")  # -----> they sort the row becasue of axis=1

# Filtering in array
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
even = numbers[numbers % 2 == 0]
print("Evens numbers of an array :", even, "\n")

# Filter With mask
mask = numbers > 5
print("Mask value of variale numbers :", numbers[mask], "\n")

# Fanccy Indexing
indices = [0, 2, 3]
print(numbers[indices], "\n")

# WHERE in numpy
where_result = np.where(numbers > 5)
print("print the numbers array but ith WHERE :", numbers[where_result])

condition = np.where(numbers > 5, numbers * 2, numbers)
print("Condition in array :", condition, "\n")


# Adding Removing array
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

combine = np.concatenate((arr1, arr2))
print("Combine the array 1 with array 2 :", combine, "\n")

# How to add new elements in array col or row
original = np.array([[1, 2], [3, 4]])
new_row = np.array([[5, 6]])

with_new_row = np.vstack((original, new_row))
print("New Array addition of new Row\n", with_new_row, "\n")

new_col = [[7], [8]]

with_new_col = np.hstack((original, new_col))
print("New Array addition of new Column\n", with_new_col, "\n")
