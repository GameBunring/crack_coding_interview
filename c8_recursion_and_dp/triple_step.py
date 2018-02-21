def triple_step(n):
    dp = [1,2,4]
    if n == 0:
        return 0
    if n < 3:
        return dp[n - 1]
    for i in range(3, n):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    return dp[-1]
    
if __name__=="__main__":
    print(triple_step(3))
    print(triple_step(4))
    print(triple_step(5))
    print(triple_step(10))
