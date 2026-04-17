def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
    for record_id in record_ids:
        if record_id % 2 != 0:
            record_ids.remove(record_id)
    return record_ids
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]

# Answers
# Task 2
# a). OBSERVATION:
# The first skip occurs at index 0, when the value 1 is removed at index 0, then the list shifts left and becomes: [3, 4, 6, 7, 9, 10], the loop then moves to index 1, skipping the value 3, which has shifted to index 0.

# b). WHY:
# When an item is removed from a list while iterating forward, all the remaining elements shift one position to the left, however, the loop index continues to move forward, this causes the next element to be skipped because it has moved, into the current index, but the loop has already advanced. Therefore, the pointer becomes "blind" to that element.moving backward prevents skipping because deleted elements do not affect the indexes we are going to visit next.

def clean_database_new_list(record_ids):
    new_list = []

    for num in record_ids:
        if num % 2 == 0:
            new_list.append(num)

    return new_list
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database_new_list(data)

print(cleaned)





