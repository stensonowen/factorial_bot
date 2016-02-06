##Factorial Bot

[factorial_bot](https://reddit.com/user/factorial_bot) does reddit users the favor of evaluating (or approximating) the [factorial](https://en.wikipedia.org/wiki/Factorial)s in their comments. Factorials can be inconvenient to calculate because of how big they get; factorial_bot therefore provides a service that users might not get elsewhere. 21! is too big to fit into any native variable in most programming languages (because 21! > 2<sup>64</sup> (without sacrificing precision with a float, that is), and Wolfram Alpha only gives like 400 digits at a time (bullshit). There are many convenient reddit bots out there to relieve the stress and workload of redditting, but I was appalled at the absense of a bot to evaluate factorials. Redditors deserve to know the exact value of any number that they put an exclamation mark after.

Unfortunately, because of how quickly factorials grow, it's pretty hard to evaluate their exact value. Also the biggest factorial whose value can fit in a reddit comment is 3248! (which is 9998 characters long). Also it can be resource-heavy to do frequently and I'm not made of money. So if your factorial is too big for a reddit comment, its value will instead be estimated by [Stirling's Approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation). It is cheaper and still a very good (the approximation of 3248! is .0025% different from the exact value). 

Also I know you people are not only going to try to evaluate large factorials but also non-integer values, so those will be evaluated by the [gamma function](https://en.wikipedia.org/wiki/Gamma_function). The gamma function is just the smooth equivalent of a factorial such that ![equation](http://bit.ly/1ogazzv). For large factorials, this will be estimated by Stirling's Approximation.

[Also, no negative inputs](https://en.wikipedia.org/wiki/Factorial#Non-extendability_to_negative_integers).

##Code

The bulk of the calculations are done by [mpmath](http://mpmath.org/ "BSD license") using [gmpy](https://github.com/aleaxit/gmpy "LGPL license") arbitrary precision integers. The conversion of written out numbers to integers is based on [this](https://github.com/ghewgill/text2num "MIT license"). 

##License

[GPL](/LICENSE)