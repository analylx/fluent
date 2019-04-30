#-- Python实现任意深度的赋值 例如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'
class MyDict(dict):
    def __setitem__(self, key, value):  # 该函数不做任何改动 这里只是为了输出
        print('setitem:', key, value, self)
        super().__setitem__(key, value)

    def __getitem__(self, item):  # 主要技巧在该函数
        print('getitem:', item, self)  # 输出信息
        # 基本思路: a[1][2]赋值时 需要先取出a[1] 然后给a[1]的[2]赋值
        if item not in self:  # 如果a[1]不存在 则需要新建一个dict 并使得a[1] = dict
            temp = MyDict()  # 新建的dict: temp
            super().__setitem__(item, temp)  # 赋值a[1] = temp
            return temp  # 返回temp 使得temp[2] = value有效
        return super().__getitem__(item)  # 如果a[1]存在 则直接返回a[1]


# 例子:
test = MyDict()
test[0] = 'test'
print(test[0])
test[1][2] = 'test1'
print(test[1][2])
test[1][3] = 'test2'
print(test[1][3])
print('-------------the following is the obj help-------------')
print(dir(test))
print(help(test.copy()))