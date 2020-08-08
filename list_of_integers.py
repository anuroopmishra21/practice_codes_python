arr =   [1, 7, 3, 4]
arr2 = []

def get_products_of_all_ints_except_at_index(arr):
    n=len(arr)
    index=0
    for j in range(0, n):
        result =1
        for i in range(0, n):
            if i == index:
                continue
            else:
                result = result* arr[i]
        arr2.append(result)
        index = index+1
    print(arr2)

get_products_of_all_ints_except_at_index(arr)
