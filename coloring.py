# 贪婪算法（贪心法）伪代码：
# 输入：图G                   # 记录图中的顶点连接关系
# 集合verts保存G中所有顶点      # 建立初始状态
# 设置集合groups为空集         # 记录得到的分组，元素是顶点集合
# while 存在未着色顶点：
#     选一种新颜色
#     在未着色顶点中给尽量多的无互连边的点着色(构建一个分组)
#     记录新着色的顶点组

# 算法结束时集合groups里记录着一种分组方式
# 算法细节还需要进一步考虑

# 操作情况：# 1、选第一种颜色构造第一个分组：顺序选出相互不冲突的AB、AC、AD，以及与任何方向都不冲突的BA、DC和ED，做成一组；
# 2、选出BC、BD和与它们不冲突的EA作为第二组；
# 3、选出DA和DB作为第三组；
# 4、剩下的EA和EB作为第四组。

# 以上算法有重要的细节缺失：一种新颜色的着色处理。现在考虑这个问题。
# 假设图G保存需着色图中顶点的领接信息，集合verts是图中所有未着色的顶点的集合。显然算法开始时verts应该是G中所有顶点的集合。
# 用另一个变量new_group记录正在构造的用当前新颜色着色的顶点(一个集合)，在上面算法的每次迭代中重新构造，每次开始做分组时
# 将这个集合重新设置为空集。
# 在上面安排的基础上，找出verts中可用新颜色着色的顶点集的算法是：
# new_group = 空集
# for v in verts:
#     if v与new_group中所有顶点之间都没有边：
#         从verts中去掉v
#         把v加入new_group

# 循环结束时new_group是可以用一种新颜色着色的顶点集合
# 用这段代替前面程序框架中主循环体里的一部分

# Python的集合数据类型不支持元素遍历，但上述算法中需要遍历集合元素，还要在遍历中修改集合。处理这个问题的方法是在每次需要遍历时
# 从当时的verts生成一个表，而后对表做遍历(并不直接对集合遍历)
# 算法中需要的图操作依赖于图的表示，需要考虑如何在Python中实现图数据结构。图是一种复杂数据结构，应该支持一些操作。这里假定两个与
# 图结构有关的操作(依赖于图的表示)：
# 1、函数vertices(G)得到G中所有顶点的集合
# 2、谓词not_adjacent_with_set(v, group, G)检查顶点v与顶点集group中各项点在图G中是否有边连接
# 程序(算法)：

def coloring(G):
    color = 0
    groups = set()
    verts = vertices(G)
    while verts:
        new_group = set()
        for v in list(verts):
            if not_adjacent_with_set(v, newgroup, G):
                new_group_add(v)
                verts.remove(v)
        group.add((color, new_group))
        color += 1
    return groups