# 题目：自动驾驶车辆能耗最优路径规划
# 一辆自动驾驶配送车需要从起点到达终点，道路被划分成 n 个路段，每个路段有两种行驶模式可选：
# 模式 A：能耗为 a[i]，但只能在连续不超过 k 个路段使用（避免电池过热）
# 模式 B：能耗为 b[i]，无使用次数限制
# 请计算从第 1 段到第 n 段的最小总能耗。


def min_energy_consumption_memo_dfs(a: list[int], b: list[int], k):
    """
    dfs
    状态定义：我希望有个函数告诉我，在第i个路段的起点开始选择怎么走以及后续路段选择时，可以获得最低的能耗
    边界条件：当i == n时，说明所有路段都已经走完了，那后续的能耗就是0
    状态转移：
        dfs(i) = min(a[i], b[i])
        注意：选择a之后，影响第k+1次的选择，只能选b方案
    可变参数有两个，i， cnt(已经连续用了几次A) ,
    当 cnt = k 之后这一段，只能选择b方案，选择之后将 cnt 重置为0之后，继续下一路段的选择
    """
    n = len(a)
    memo = {}

    def memo_dfs(i: int, cnt: int):
        if i == n:
            return 0

        if (i, cnt) in memo:
            return memo[(i, cnt)]

        res = float("inf")
        if cnt < k:
            # 选A，但是有条件
            res = min(res, a[i] + memo_dfs(i + 1, cnt + 1))

        # 选b但是要注意重置连续使用A的次数
        res = min(res, b[i] + memo_dfs(i + 1, 0))
        memo[(i, cnt)] = res
        return memo[(i, cnt)]

    return memo_dfs(0, 0)


# 测试用例
a = [1, 2, 3]
b = [3, 2, 1]
k = 2
print(min_energy_consumption_memo_dfs(a, b, k))  # 预期输出：4

a = [2, 1, 3, 2]  # 各路段模式A能耗
b = [3, 4, 2, 5]  # 各路段模式B能耗
k = 2  # 模式A连续使用上限
print(min_energy_consumption_memo_dfs(a, b, k))  # 预期输出：7


def min_energy_consumption_dp(a: list[int], b: list[int], k):
    """
    dp
    状态定义： dp[i][cnt]代表的就是从第i次开始选择，A选择已经连续使用了cnt次的，到达终点的最低能耗
    状态转移：dp[i][cnt] = min(
                        a[i]+dp[i+1][cnt+1] if cnt <k,
                        b[i]+dp[i+1][0]
                        )
    初始化： if i == m: 也就是选完最后一次之后，最小能耗是0，这个本不属于整体逻辑计算之内，
        但是为了避免单独对最后一次进行处理，所以多开一行，并将最后一行设置为0

    依赖关系：i：上依赖于下，所以是从下往上遍历，
    dp[i][cnt] 依赖于dp[i+1][0]，dp[i+1][cnt+1]，不存在同行依赖，只需要保证是从下往上的，那么下面那一行的肯定都是算好的
    所以遍历顺序随便
    注意：cnt属于[0,k],所以要开k+1个空间
    """
    m = len(a)
    dp = [[0] * (k + 1) for _ in range(m + 1)] # 初始化的是第m行
    for i in range(m - 1, -1, -1):
        for j in range(k + 1):
            if j >= k:
                # 选b
                dp[i][j] = dp[i + 1][0] + b[i]
            else:
                dp[i][j] = min(a[i] + dp[i + 1][j + 1], b[i] + dp[i + 1][0])

    return dp[0][0]

# 测试用例
a = [1, 2, 3]
b = [3, 2, 1]
k = 2
print(min_energy_consumption_dp(a, b, k))  # 预期输出：4

a = [2, 1, 3, 2]  # 各路段模式A能耗
b = [3, 4, 2, 5]  # 各路段模式B能耗
k = 2  # 模式A连续使用上限
print(min_energy_consumption_dp(a, b, k))  # 预期输出：7


def min_energy_consumption_dp_plus(a: list[int], b: list[int], k):
    """
    由依赖关系，i只依赖于下一行，那么只需要保证从下到上遍历就行
    状态变更： dp[j]表示的就是已经选择了j次a之后，到达终点的最小油耗是多少
    状态转移： dp[j] = min(dp[j+1] + a[i], dp[0]+b[i])
    初始化：dp[n] = 0
    """
    n = len(a)
    dp = [0]*(k+1)
    for i in range(n-1,-1,-1):
        # 临时数组，
        # dp 保存的是上一行的值
        # new_dp 用来计算当前行的值
        # 这样保证 每一次计算都用的都是上一行的完整状态
        # 最后再把 new_dp 赋给 dp 以供下一行使用
        new_dp = [0] * (k + 1)
        for j in range(k+1):
            if j >=k:
                new_dp[j] = dp[0]+b[i]
            else:
                new_dp[j] = min(dp[j+1] + a[i], dp[0]+b[i])
        
        dp = new_dp
    
    return dp[0]

# 测试用例
a = [1, 2, 3]
b = [3, 2, 1]
k = 2
print(min_energy_consumption_dp_plus(a, b, k))  # 预期输出：4

a = [2, 1, 3, 2]  # 各路段模式A能耗
b = [3, 4, 2, 5]  # 各路段模式B能耗
k = 2  # 模式A连续使用上限
print(min_energy_consumption_dp_plus(a, b, k))  # 预期输出：7
