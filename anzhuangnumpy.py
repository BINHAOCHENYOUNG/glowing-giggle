import numpy as np
x = np.empty([3,2])

y =np.zeros((2,3),dtype=np.int)
print(y)

#
x=np.array([[1,2,3],[2,3,4],[3,4,5]])


x = np.arange(5)
print(x)
y=np.arange(10,20,2,dtype=float)
print(y)

#查看数组类型
print(x.shape)
print(y.shape)
#输出值为m行n列

#改变数组的形状 reshape
print(x.reshape(-1,1))

#数组元素个数 n*m
print(x.size)

#切割新数组
a=np.arange(10)
s=slice(2,7,2)
print(a[s])
#or print(a[2:7:2])

print(x[1])
#所有行的第二列
print(x[:2])

#横列交换
#print(transpose(a))
b=np.array([[1,2],[2,3],[2,4]])
#连接行
print(np.concatenate((a,b)))

print(np.concatenate((a,b),axis=1))


print(np.stack(a,b))
print(np.vstack(a,b))


a=np.array([[1,2,3],[2,3,4],[3,4,5]])
b=np.array([[2,3,4],[3,4,5],[3,5,6]])
a.dot(b)
