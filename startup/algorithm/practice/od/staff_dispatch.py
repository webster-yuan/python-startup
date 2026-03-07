# 题干描述：https://renjie.blog.csdn.net/article/details/135318935
# 二分查找 使用前提
# 答案可以确定在一个有序区间内，可以确定区间的范围
import math

def get_min_count_staff(x, y, cntx, cnty):
    l , r = 1, 10**18
    while l<r:
        mid = l+(r-l)//2
        # 需要一个函数判定，在mid个员工的情况下，是否能够满足要求
        if can_dispatch(mid , x ,y ,cntx, cnty):
            r = mid
        else:
            l = mid+1

    return l # 我们要的是满足区间的最小值，所以返回左边界

def can_dispatch(staff_num, x, y, cntx, cnty):
    lcm  = math.lcm(x, y)

    not_x = staff_num // x # 不能分配给x的员工数量 staff_num =20 x =4 那么不能去x的数有 4 8 12 16 20 = 20 // 4 = 5
    not_y = staff_num // y # 不能分配给y的员工数量
    not_both = staff_num // lcm

    only_y = not_x - not_both
    only_x = not_y - not_both
    free = staff_num - not_x - not_y + not_both # 两个国家都能去的人的个数

    need_x = max(0, cntx - only_x) # 还需要多少人去x
    need_y = max(0, cnty - only_y) # 还需要多少人去y

    return free - need_x - need_y >= 0 # 如果剩余的员工数量能够满足还需要的人数，那么就说明在staff_num个员工的情况下能够满足要求


if __name__ == "__main__":
    x, y ,cntx, cnty = map(int, input().split())
    print(f"x={x}, y={y}, cntx={cntx}, cnty={cnty}")
    print(get_min_count_staff(x, y, cntx, cnty))