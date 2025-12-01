# 查找一个列表中的重复元素
def find_duplicates(list_to_search):
    counts={}
    for item in list_to_search:
        if item in counts:
            counts[item]+=1
        else:
            counts[item]=1
    duplicates={item : count for item ,count in counts.items() if count>1}
    # for item, count in counts.items()：这是一个循环，遍历上述返回的元组列表。
    # {item: count ...}：这部分定义了新字典的键和值。
    # 如果条件满足（元素出现次数大于1），则将 item 作为键，count 作为值添加到新字典 duplicates 中。
    return duplicates

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
duplicates=find_duplicates(sample_list)
if duplicates:
    print("Duplicates found:", duplicates)
    for item,count in duplicates.items():
        print(f"Item {item} appears {count} times")
else:
    print("No duplicates found")