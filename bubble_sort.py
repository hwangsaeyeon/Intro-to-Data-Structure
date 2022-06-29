def bubble_sort(items):
    long=len(items)
    for i in range(long -1):
        change=False
        for k in range(long-i-1):
            if items[k] > items[k+1]:
                items[k], items[k+1] = items[k+1], items[k]
                change=True
        if change==False:
            break
    return items

items = [40,70,60,30,10,50]
print('정렬 전: ',end='')
print(items)
bubble_sort(items)
print('정렬 후: ',end='')
print(items)
