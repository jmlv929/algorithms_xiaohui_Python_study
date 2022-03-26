'''

挖金矿 每个近况黄金储量不同 需要参与挖掘的工人也不同

每座金矿要么全挖 要么不挖 不能挖一半 要求算出 怎样得到尽可能多的金矿

贪婪算法： 只能得到局部最优解

动态规划问题：把复杂的问题简化成规模较小的子问题 再从简单的子问题自底向上一步一步递推  最终得到问题的复杂解

要点：确定全局最优解和最优子结构之间的关系，以及问题的边界  ！！！ 状态转移方程式 ！！！
边界：0个工人 或者 0个金矿

空间复杂度 时间复杂度 O(2^n)
'''


# 递归 ：函数调用栈

# 递归  将一个大问题划分为 最优子结构
def get_best_gold_mining(w, n, p=[], g=[]):
    '''
        :param w:工人数量
        ：param n ：可选金矿数量
        ：param p：金矿开采所需工人数量
        ：param g: 金矿储量
    '''
    #临界条件
    if w == 0 or n == 0:    #边界条件
        return 0
    if w < p[n-1]:   #如果可用工人数量小于 当前需要人数 跳过
        return get_best_gold_mining(w,n-1,p,g)
    return max(get_best_gold_mining(w,n-1,p,g),get_best_gold_mining(w-p[n-1],n-1,p,g)+g[n-1])
#将问题分解为 选与不选当前这个金矿  无所谓 返回其中最大的  选择范围： 选：当前价值加上除去这些工人在剩下金矿最大值 不选 ：当前数量工人在剩下金矿价值最大

if __name__ == '__main__':
    w = 10
    n = 5
    p=[3,4,3,5,5]
    g=[200,300,350,400,500]
    print(get_best_gold_mining(w,n,p,g))




