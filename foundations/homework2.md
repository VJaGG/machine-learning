
1、  $\lambda\times\mu+(1-\lambda)\times(1-\mu)$  
&emsp;&emsp;解：在有noise的情况下，也就是在某一点x的值不再是Deterministic的了，不是确定的，存在着一定的概率值。  
&emsp;&emsp;比如在x点，有0.7的概率y=1，有0.3的概率y=0，即y是按照P(y|x)分布的。  因为$h$在没有噪声的数据集下，  
&emsp;&emsp;训练出的模型错误率为$\mu$，根据题意加噪声的意思是有$1-\lambda$的比例$(x, y)$变成$(x, -y)$。当  
&emsp;&emsp;$y=f(x)$时候，$h$对$f$的错误率为$\mu$，$y=f(x)$的概率为$\lambda$所以这部分的错误率为$\lambda\times\mu$  
2、
&emsp;&emsp;

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
