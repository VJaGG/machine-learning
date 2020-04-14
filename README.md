1、**(ii),(iv) and (v)**  
2、**reinforcement learning**  
3、**unsupervised learning**  
4、**supervised learning**  
5、**activate learning**  
6、$\frac{1}{L}\times\left(\lfloor\frac{N+1}{2}\rfloor-\lfloor\frac{N}{2}\rfloor\right)$（主要是计算偶数的个数，偶数是错误的）  
7、$2^L$  
8、$\Bbb{E}_{f}$
 
9、**0.24**  
&emsp;&emsp;解：题目中$\mu=0.5$为了保证采样的10个弹珠中$\nu=0.5$则进行排列组合${C_{10}^{5}}\left(\frac{1}{2}\right)^{10}=0.24$  
10、**0.39**  
&emsp;&emsp;解：计算方式同上$C_{10}^{9}\left(\frac{9}{10}\right)^9\left(\frac{1}{10}\right)^1=0.3874$  
11、$9.1\times10^{-9}$  
&emsp;&emsp;解：$P(\nu\le0.1)=C_{10}^{9}\left(\frac{1}{10}\right)^9\left(\frac{1}{10}\right)^1+0.1^{10}=9.1\times10^{-9}$  
12、$5.52\times10^{-6}$  
&emsp;&emsp;解：根据Hoeffding不等式进行带入计算$\mu=0.9,\nu\le0.1$则$\nu-\mu\le-0.8$所以$|\nu-\mu|\ge0.8$得到的$\epsilon=0.8$  
&emsp;&emsp;&emsp;&emsp;带入到Hoeffding不等式右边计算出结果为$2exp\left(-2\times(0.8)^2\times10\right)=5.52\times10^{-6}$  
&emsp;&emsp;&emsp;&emsp;**Hoeffding's Inequality**  
<p align="center">
$\Bbb{P}\left[|\nu-\mu|\gt\epsilon\right]\le2exp\left(-2\epsilon^2N\right)$
</p>


13、$\frac{8}{256}$  
&emsp;&emsp;解：1的一面为橙色的有B和C两种骰子，在一次抽样中抽到橙色的概率为$\frac{1}{2}$，所以总的概率为$\left(\frac{1}{2}\right)^{5}=\frac{1}{32}=\frac{8}{256}$  
14、$\frac{31}{256}$  
&emsp;&emsp;解：1全部为橙色只能是选B和C，2全部为橙色只能选A和C，3全部为橙色只能选B和C，4全部为橙色只能选A和  
&emsp;&emsp;D，5全部为橙色只能选B和D，6全部为橙色只能选A和D。所以共有4种选择方式。总共的选择方式  
&emsp;&emsp;为$\left(4\right)^{5}$，其中为纯色的有，对于1来说纯色只能在B和C中选共有$\left(2\right)^{5}$中可能上述一  
&emsp;&emsp;共有$4\times\left(2\right)^{5}$其中AA多计算一次同理其他都多计算一次所以有$4$个重复的，则最后的结果  
&emsp;&emsp;为$\frac{4\times\left(2\right)^{5}-4}{\left(4\right)^{5}}=\frac{31}{256}$  
15、算法的实现在code中
