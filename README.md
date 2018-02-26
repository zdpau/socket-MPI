# socket-MPI

# 一，measure throughput between client and server. 使用socket 和 MPI4py.
## 遇到的问题：
### 1，指定传送的size, 解决方法：使用BUFSIZE = 1024， 然后 test_data = 'x' * (BUFSIZE - 1) + '\n'（相当于发送1024个X）
### 2，num 局部变量，全局变量， 解决方法： 使用 global num
### 3， 如何循环一个函数 ， 解决方法：见代码
### 4， 如何将循环的这么多数据存储，  解决方法： 现在外面定义一个nums=[]数组来存储，然后在函数里面使用， nums.append(num)  具体见代码.
### 5,  如何计算时间：time ,timeit
### 6,  


