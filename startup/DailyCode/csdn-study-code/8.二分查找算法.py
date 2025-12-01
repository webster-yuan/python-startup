arr_list = [5, 7, 11, 22, 27, 33, 39, 52, 58]

# 查找的算法是11
seek_number =11
# 保存一共查找了多少次
count =0
left =0
right =len(arr_list)-1

# 递归算法
def binary_search(arr_list, seek_number, left, right):
    if left > right:
        return -1
    else:
        mid = (left+right)//2
        if arr_list[mid] > seek_number:
            right =mid-1
        elif arr_list[mid]<seek_number:
            left =mid+1
        else:
            return mid
    # 递归调用
    return binary_search(arr_list, seek_number, left, right)
print("查找的数字为%s,索引为%s "% (seek_number,binary_search(arr_list, seek_number, left, right)))

# 非递归算法
# while left<=right:
#     mid= (left+right)//2
#     count+=1
#     if seek_number >arr_list[mid]:
#         left =mid+1
#     elif seek_number < arr_list[mid]:
#         right =mid-1
#     else:
#         print("找到了,查找了%d次"%count)
#         break
# else:
#     print("没有找到,查找了%d次"%count)
# print("查找的次数为%d"%count)
