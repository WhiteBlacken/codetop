"""
题目描述：
给定 n 个正整数组成的数组，求平均数正好等于 k 的最长连续子数组的长度。
如果不存在任何一个连续子数组的平均数等于 k,则输出 -1。

样例：
输入：
5 2
1 3 2 4 1
输出：
3
"""
n, avg_num = map(int,input().split()) # 数组长度，目标平均数
nums = list(map(int, input().split()))
# 前缀和+哈希
prefix = [0]*(n+1)
dict = {}
res = 0
for i in range(n+1):
    prefix[i] = prefix[i-1] + nums[i-1]
    target = prefix[i] - avg_num*i
    if target in dict:
        res = max(res, i-dict[target])
    else:
        dict[target] = i
print(res)
        

