---
layout: scribbles
title: Scribbles on kinematics
buttonStyle: fg-guide-note
backgroundStyle: bg-guide-note
---

# Scribbles on kinematics

## Equations of motion

### Uniform acceleration

For a uniformly accelerating body, moving in 1D space, the velocity \\( v_x \\) at time \\( t \\) can be calculated as:

$$
v_x = v_{x, 0}+ a_x t
$$

The position \\( x \\) of an uniformly accelerating body with initial velocity \\( v_{x, 0} \\) at time \\( t \\) can be calculated as:

$$
x = x_0 + v_{x, 0} t + \frac{1}{2} a_x t^2,
$$
where \\( x_0 \\) is the initial position.

From the two relations above, we can calculate a body's velocity \\( v_x \\) at any position \\( x \\), without knowing the time spent since the initial condition.
$$
\begin{eqnarray}
t &=& \frac{v_x - v_{x, 0}}{a_x} \Rightarrow \\
x - x_0 &=& v_{x, 0} \left( \frac{v_x - v_{x, 0}}{a}\right) + \frac{1}{2} \frac{(v_x - v_{x, 0})^2}{a} \\
2 a (x - x_0) &=& \cancel{2 v_x v_{x, 0}} - 2 v_{x, 0}^2 + v_x^2 + v_{x, 0}^2 - \cancel{2 v_x v_{x, 0}} \\
v_x^2 &=& v_{x, 0}^2 + 2a (x - x_0)
\end{eqnarray}
$$

Using these equations of motion, we can calculate the average distance moved as:
$$
\begin{eqnarray}
x - x_0 &=& t \left( v_{x, 0} + \frac{1}{2} a t \right) \\
&=& t \left( v_{x, 0} + \frac{v_x - v_{x, 0}}{2} \right) \\
&=& t \left( \frac{v_{x, 0} + v_x}{2} \right) \\
\bar{x} &=& t \bar{v}_x
\end{eqnarray}
$$

### Non-uniform acceleration

