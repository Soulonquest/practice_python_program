def element_removal(nums_array, value_to_remove):
    k = 0
    for i in range(len(nums_array)):
        if nums_array[i] != value_to_remove:
            nums_array[k] = nums_array[i]
            k += 1

    # Print the array after removal and its length
    print("Array after removal:", nums_array[:k])
    print("Length after removal:", k)
    return k

# Example usage
nums_array = [3, 2, 2, 3]
value_to_remove = 3
element_removal(nums_array, value_to_remove)

    