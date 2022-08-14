# Monte Carlo Integral
A Program calculate integral with Monte Carlo method for my course Probility & Statistics.

## mci.py
the mci.py can only calculate non-negative function. It has two way to calculate integral. Suppose we got a integral $\int_a^bf(x)dx$
### method 1
1. generate uniform random numbers $x_i, i=1,2,3,\cdots, n$ in $[a,b]$ .
2. calculate the function value $f(x_i)$
3. you can get the integral by $\int_a^bf(x)dx\approx\frac{b-a}{n}\sum\limits_{i=1}^{n} f(x_i)$

### method 2
1. generate uniform random numbers $x_i,  i=1,2,3,\cdots, n$ in $[a,b]$ .
2. generate uniform random numbers $y_i, i=1,2,3,\cdots, M$ in $[a,b]$ , where $M$ is the up bound of the function $f(x)$ .
3. compare $y_i$ and $f(x_i)$, if $y_i < f(x_i)$, make the counter +1
4. the result is equal to $(b-a)\times \frac{counter}{n} * M$

## extra-2.py
the extra-2.py can calculate both positive and negative function but it has a very low efficiency.


the mc.py is abandoned because of its low efficiency. Just to memorized my first small program :grin:
