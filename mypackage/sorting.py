def bubble_sort(items):

    '''
        Returns array of items, sorted in ascending order:
        This function makes multiple passes through the items.
        And then compares adjacent items and exchanges those that are out of order.
        Each pass through the list places the next largest value in its proper place.
        In essence, each item “bubbles” up to the location where it belongs.


        Args:
        items (int): the items must be in a list or array as int items

        Examples:
        >>>bubble_sort([10,2,88,549,247,42,77])
            [2, 10, 42, 77, 88, 247, 549]

        >>>bubble_sort([64, 34, 25, 12, 22, 11, 90])
            [11, 12, 22, 25, 34, 64, 90]

    '''

    length_of_items = len(items) -1

    for i in range(length_of_items):

        for a in range(length_of_items - i):
            if items[a] > items[a + 1]:
                items[a], items[a+1]=items[a + 1],items[a]

    return items

def merge_sort(items):

    '''
        Returns array of items, sorted in ascending order:

        The items in the list are divided into two roughly equal halves.
        Then the items from the left half are sorted.
        And also the items from the right half are sorted.
        Lastly the two sorted halves are merged into one sorted list.

        Args:
        items (int): the items must be in a list or array as int items

        Examples:
        >>>merge_sort([100,698,5,88,17,26])
            [5, 17, 26, 88, 100, 698]

        >>>merge_sort([3,455,231,21,11,95,9])
            [3, 9, 11, 21, 95, 231, 455]

    '''

    if len(items) < 2:
        return items


    half_lst = len(items) // 2
    left_half = merge_sort(items[:half_lst])
    right_half = merge_sort(items[half_lst:])
    merged_lst = []
    left_side = right_side = 0


    while True:
        if left_side >= len(left_half):
            merged_lst.extend(right_half[right_side:])
            break
        if right_side >= len(right_half):
            merged_lst.extend(left_half[left_side:])
            break
        if left_half[left_side] < right_half[right_side]:
            merged_lst.append(left_half[left_side])
            left_side += 1
        else:
            merged_lst.append(right_half[right_side])
            right_side += 1

    return merged_lst


def quick_sort(items):

    '''
        Returns array of items, sorted in ascending order:

        This function takes the first index of the elements in the items and places the index of the element at its correct position in sorted array.

        Therefore, placing all smaller (smaller than index number) to the left of the index and all greater elements to the right of the index.


        Args:
        items (int): the items must be in a list or array as int items

        Examples:
        >>> quick_sort([20,98,8,55,16,19])
            [8, 16, 19, 20, 55, 98]

        >>> quick_sort([10,2,88,549,247,42,77])
            [2, 10, 42, 77, 88, 247, 549]


    '''

    if len(items) < 2:
        return items
    else:
        index_num= items[0]

        smaller_nums = [i for i in items[1:] if i <= index_num]

        bigger_nums = [i for i in items[1:] if i > index_num]

        return quick_sort(smaller_nums) + [index_num] + quick_sort(bigger_nums)
    
