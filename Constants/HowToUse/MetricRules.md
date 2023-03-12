Metric Input format: 
                        
* Use square brackets to represent tensor: $[[a, b], [c, d]]$
* Use star if you are multiplying: $$ a * b = ab $$
* Use double star if you are exponentiating: $$ a * *  b = a^b$$
* Use normal brackets if you want to encapsulate expressions: $$y*e**(x + y) = ye^{(x + y)}$$
                        
If you want to define a function, place normal brakets following a single letter: $$ F( $$

* In this case, the symbol $$F$$ will be treated as a function.
* Whatever comes after $$F$$ will be trated as its arguments: $$ f(x) $$ or $$ G(x,y)$$ for instance, will have $$x$$ and $$(x,y)$$ as their varibles respectively.