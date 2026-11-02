print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # REQ-04
    if len(arr) == 0:
        return 0

    # REQ-03
    if len(arr) >= 10:
        return 1

    # REQ-05
    for item in arr:
        if not isinstance(item, int):
            return 2

    # Copy input list
    arr_result = arr.copy()

    n = len(arr_result)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:

                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = \
                        arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:

                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = \
                        arr_result[j + 1], arr_result[j]

            else:
                return []

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()


