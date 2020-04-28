
1、$\lambda\times\mu+(1-\lambda)\times(1-\mu)$  
&emsp;&emsp;解：在有noise的情况下，也就是在某一点x的值不再是Deterministic的了，不是确定的，存在着一定的概率值。  
&emsp;&emsp;比如在x点，有0.7的概率y=1，有0.3的概率y=0，即y是按照P(y|x)分布的。  因为$h$在没有噪声的数据集下，  
&emsp;&emsp;训练出的模型错误率为$\mu$，根据题意加噪声的意思是有$1-\lambda$的比例$(x, y)$变成$(x, -y)$。当  
&emsp;&emsp;$y=f(x)$时候，$h$对$f$的错误率为$\mu$，$y=f(x)$的概率为$\lambda$所以这部分的错误率为$\lambda\times\mu$  
2、0.5  
&emsp;&emsp;解：题意为$\lambda$为什么值的时候$h$与$\mu$无关，所以消去第一题中的$\mu$，$\lambda=0.5$  
4、$Devroye$  
&emsp;&emsp;解：按着题意将$d_{vc}=50, \sigma=0.05, N=10000$带入下面各式计算结果  
&emsp;&emsp;$Original=0.632174915200836,Radmacher=0.3282912038471584,Parrondo=0.2236982936807856,$  
&emsp;&emsp;$Devroye=0.21522850732079352,Variant=0.8604259707062739$左右两边都有未知数$\epsilon$按二元一次方程组来  
&emsp;&emsp;解。  
5、$Parrondo$  
&emsp;&emsp;解：按着题意将$d_{vc}=50, \sigma=0.05, N=5$带入下面各式计算结果  
&emsp;&emsp;$Original=13.828161484991483,Radmacher=7.048776564183685,Parrondo=5.101361981989992,$  
&emsp;&emsp;$Devroye=5.599525295062205,Variant=16.264111061012045$左右两边都有未知数$\epsilon$按二元一次方程组来  
&emsp;&emsp;解。  
6、$N^{2}-N+2$
&emsp;&emsp;解：对于$N$个点一共有$N+1$个位置，从中选择两个位置一共有$C_{N+1}^{2}$，其中重复的共有$2\times(N-1)$，这里  
&emsp;&emsp;重复的计算对应着两种不同的开口方向（类比二次曲线），左边开口向下对应着右边一种开口向上，左边一种开口向上对应  
&emsp;&emsp;右边一种开口向上。所以总共$C_{N+1}^{2}-2\times(N-1)=N^{2}-N+2$
