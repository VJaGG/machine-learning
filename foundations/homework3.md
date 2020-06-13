1、$100$ (带入计算即可)  
2、$H^{1126} = H$ （lecture 9 ppt 13）  
3、$\cal err(w) = max(0, 1-\cal yw^{T}x)$  
4、$\cal err(w) = \frac {1}{2}exp(-\cal yw^{T}x)$  
5、$\cal err(w) = max(0, -\cal yw^{T}x)$  
![image](https://github.com/VJaGG/machine-learning/blob/master/foundations/imgs/answer.jpg)  
6、$(-2, 0)$(直接进行计算梯度)  
7、$2.825$[newton](code/newton.py)  
8、$(1.5, 4, -0.5, -1, -2, 0)$  
9、$-(\nabla^{2}E(u, v))^{-1}\nabla E(u, v)$  
10、$2.361$[newton](code/newton.py)  
11、$x_{1},x_{2},x_{3},x_{4},x_{5},x_{6}$(通过画图直接得出结果)  
12、$E_{in}=0.7$  
13、$0.5$
14、$g(x_{1}, x_{2}) = sign(-1-0.05x_{1}+0.08x_{2}+0.13x_{1}x_{2}+1.5x_{1}^{2}+1.5x_{2}^{2})$[newton](code/feature.py)  
15、$0.1$[feature](code/feature.py)  
16、$\frac{1}{N}\sum_{n=1}^N(ln(\sum_{k=1}^Kexp(w_{k}^Tx_{n}))-w_{yn}^Tx_{n})$  
17、$\frac{1}{N}\sum_{n=1}^N((h_{i}(x_{n})-[[y_{n}==i]])x_{n})$  
18-20、[logistic regresssion](code/logistic_regression.py)
