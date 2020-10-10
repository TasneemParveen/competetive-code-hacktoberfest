def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
        gap = gap//2
    
    return input_list

if __name__ == "__main__":
    list = input().split()

    for i in range(len(list)):
        list[i] = int(list[i])

    print(shellSort(list))
    
