---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
自然指数函数（特殊）
求导结果是自己
积分结果是自己 ^5CKaJEJy

求积分的方法
定义，求黎曼和的极限
微积分基本定理，先求原函数
用函数的特值求积分 ^xtiqsOMA

复分析 留数定理
用积分求函数的特值 ^PEsX0IgC

应用：工程数学 计算差值积分 ^OpYBtWcZ

被积函数 ^304aUZI8

被积函数的原函数 ^e8WVoHQk

x无初等原函数 ^AGVTLddL

t有初等原函数 ^vmE4jkQG

f(ax)  f(bx)

a b 系数
x 自变量 ^oc6RaFA2

f(xy)

a b 自变量 y
x 自变量 ^MGiLlDmH

二元函数一般形式 g(x, y)
二元函数特殊形式 f(xy) 乘积形式 ^6brKt173

函数差的形式总是可以
转换为定积分的形式
（可以一般化） ^Xa85CdI3

## Embedded Files
787f59348c327f985c7e9c786d2b09f10624187d: $$\begin{aligned}
e^x: \quad & (e^x)' = e^x & \int e^x \, dx &= e^x + C \\
e^{ax}: \quad & (e^{ax})' = a e^{ax} & \int e^{ax} \, dx &= \frac{1}{a} e^{ax} + C
\end{aligned}$$

3d32bd0c51751924df0589aee9368924465c67d8: $$\begin{aligned}
\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x} \, dx 
&= \int_0^\infty \int_a^b e^{-tx} \, dt \, dx 
= \int_a^b \int_0^\infty e^{-tx} \, dx \, dt \\

&= \int_a^b \left(-\frac{1}{t}e^{-tx}\right)\Bigg|_0^\infty dt 
= \int_a^b \frac{1}{t} \, dt 
= \ln t \Big|_a^b = \ln\frac{b}{a}
\end{aligned}$$

7258902fb7d567e02076130f537453d81807bf62: $$\begin{aligned}
\color{blue}\frac{e^{-ax} - e^{-bx}}{x}\color{black} = -\frac{e^{-bx}}{x} + \frac{e^{-ax}}{x} &= \color{blue}\left[-\frac{1}{x}e^{-tx}\right]_{t=a}^{t=b}\color{black} \\
&= \int_a^b e^{-tx} \, dt \quad \color{red}\Rightarrow \frac{e^{-ax} - e^{-bx}}{x} = \int_a^b e^{-tx} \, dt\color{black}
\end{aligned}$$

530c18937d8a065cecc2f0320b0f6265263e4430: $$(e^{-tx})'_t = -xe^{-tx}, \quad 
\left(-\frac{e^{-tx}}{x}\right)'_t = e^{-tx}$$

c8c9b261fbaca8314f540736597d3f1f4da3b50f: $$\begin{aligned}
&g(x,y) = f(xy), \quad u = xy \\
&\frac{\partial g}{\partial x} = f'(u) \cdot \frac{\partial u}{\partial x} = f'(u) \cdot y \quad \Rightarrow \quad f'(u) = \frac{1}{y}\frac{\partial g}{\partial x} \\
&\frac{\partial g}{\partial y} = f'(u) \cdot \frac{\partial u}{\partial y} = f'(u) \cdot x \quad \Rightarrow \quad f'(u) = \frac{1}{x}\frac{\partial g}{\partial y} \\
& \color{red}{\Rightarrow \quad \frac{1}{x}\frac{\partial g}{\partial x} = \frac{1}{y}\frac{\partial g}{\partial y}}
\end{aligned}$$

d74d1405a7e594d5d55d1c93fcc860146c39e628: $$\begin{aligned}
&\int_0^\infty \frac{1}{x}[f(ax) - f(bx)] \, dx 
= \int_0^\infty \frac{1}{x} f(xy)\Big|_{y=b}^{y=a} \, dx 
= \int_0^\infty \frac{1}{x} \int_b^a \frac{\partial}{\partial y}f(xy) \, dy \, dx \\

&\qquad = \int_0^\infty \int_b^a \frac{1}{x} \frac{\partial}{\partial y}f(xy) \, dy \, dx 
= \int_b^a \int_0^\infty \frac{1}{x} \frac{\partial g}{\partial y} \, dx \, dy 
= \int_b^a \frac{1}{y} \int_0^\infty \frac{\partial g}{\partial x} \, dx \, dy \\

&\qquad = \int_b^a \frac{1}{y} [g(\infty, y) - g(0, y)] \, dy 
= \int_b^a \frac{1}{y} [f(\infty) - f(0)] \, dy 
= [f(\infty) - f(0)] \int_b^a \frac{1}{y} \, dy \\

&\qquad = [f(\infty) - f(0)] \ln y \Big|_b^a 
= [f(\infty) - f(0)] (\ln a - \ln b) 
= [f(0) - f(\infty)] \ln\frac{b}{a}
\end{aligned}$$

d2f0a40e4f5731078c94fd82c1ce4e37641b2aec: $$\boxed{
\color{red}\int_0^\infty \frac{f(ax) - f(bx)}{x} \, dx = [f(0) - f(\infty)] \ln\frac{b}{a}
}$$

575d6d250a9c2d14cd073fb17b7e736c1b83e5d9: $$\boxed{
\color{red}\int_0^\infty \frac{f(ax) - f(bx)}{x} \, dx = [f(0) - f(\infty)] \ln\frac{b}{a}
}$$

400cc2043bfe353c978dbdcd5d719a3a8a37f480: $$\boxed{
\color{red}\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x} \, dx = \ln\frac{b}{a}
}$$

4bfd8d07246366643561541873a8013cd9ece9f3: $$\boxed{
\color{red}\int_0^\infty \frac{e^{-ax} - e^{-bx}}{x} \, dx = \ln\frac{b}{a}
}$$

%%
## Drawing
```compressed-json
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=
```
%%