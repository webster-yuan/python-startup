# def word_count(nums):
#     dict={}
#     for it in nums:
#         if it not in dict:
#             dict[it]=1
#         else:
#             dict[it]+=1
#     return dict


lis_num=list(map(int,input().split()))
dict={}
for it in lis_num:
    if it not in dict:
        dict[it]=1
    else:
        dict[it]+=1
lis_dict=sorted(dict.items(),key=lambda x: x[0])
for key,val in lis_dict:
    print("{:<5} {:}".format(key,val))
