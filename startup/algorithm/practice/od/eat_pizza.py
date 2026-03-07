# 题干描述：https://renjie.blog.csdn.net/article/details/135297269

# dfs(l , rr)的意思是：在剩下的披萨是pizzas[l...r]的情况下，吃货能够吃到的最大披萨数量
# 吃货先吃，保证初识披萨个数是奇数，那么剩下偶数个的时候是馋嘴吃
# 馋嘴是贪心的吃，每次吃掉剩下披萨中最大的那块，那么吃货只能在剩下的披萨中选择
# 如果馋嘴是使坏的吃，那么吃货的选择就是馋嘴让他达到的效果，拿到的是选择之后最小的值即min(dfs(l+1,r), dfs(l ,r-1))

def max_pizza_dfs(pizzas):
    n = len(pizzas)
    memo = {}
    def dfs(l ,r):
        if l > r:
            return 0
        
        if (l ,r) in memo:
            return memo[(l,r)]
        
        # 判断当前是 吃货 还是 馋嘴 选择
        # 吃货是当此时剩下的披萨个数是奇数的时候选择
        # r-l+1 代表的是剩下的披萨个数，剩下的如果是奇数个，应该吃货选择；减去之后如果是偶数，吃货选择，如果是奇数，馋嘴选择
        is_eater_turn  = (n - (r-l+1)) % 2 == 0
        if is_eater_turn:
            # 吃货选择
            chose_left = pizzas[l] + dfs(l+1, r)
            chose_right = pizzas[r] + dfs(l ,r-1)
            res = max(chose_left, chose_right)
        else:
            # 馋嘴选择: 选择左右中最大的那块，那吃货只能在剩下的披萨中选择
            if pizzas[l] > pizzas[r]:
                res = dfs(l+1, r)
            else:
                res = dfs(l, r-1)
        
        memo[(l,r)] = res
        return res

    return dfs(0, n-1)

if __name__ == "__main__":
    N = int(input())
    pizzas = []
    for i in range(N):
        num = int(input().split("\n")[0]) # split("\n") 是为了去掉分割符拿到纯数字 [0] 是因为split方法拿到的是列表，我们需要拿到第一个元素，也就是纯数字
        pizzas.append(int(num))

    print(f"{pizzas}")
    print(max_pizza_dfs(pizzas))
