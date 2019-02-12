# socket-MPI


## 一，measure throughput between client and server. 使用socket 和 MPI4py.
### 遇到的问题：
1，指定传送的size, 解决方法：使用BUFSIZE = 1024， 然后 test_data = 'x' * (BUFSIZE - 1) + '\n'（相当于发送1024个X）

2，num 局部变量，全局变量， 解决方法： 使用 global num

3， 如何循环一个函数 ， 解决方法：见代码

4， 如何将循环的这么多数据存储，  解决方法： 现在外面定义一个nums=[]数组来存储，然后在函数里面使用， nums.append(num)  具体见代码.

5,  如何计算时间：time ,timeit

6,  float 不能迭代 解决方法：https://stackoverflow.com/questions/25287584/typeerror-float-object-is-not-iterable-3 具体见代码

7, s.sendall(string):完整发送data，将string中data发送到连接的socket
   s.recv(bufsize（要接受MAX数据量）): 接受TCP套接字数据，以字符串返回
   s.connect(address（连接到address处的套接字）)
   s.accept:接受连接，并返回conn（套接字对象和发送数据）,address（连接client的地址）

8，1个英文字母1字节，1024个就是1KB。

9，如何让Server知道datasize。


