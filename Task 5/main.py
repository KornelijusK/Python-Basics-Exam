# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

import modules.numbers.numbers
from modules.math.composition import composition as addition 
from modules.math.division import division as division
from modules.math.subtraction import substraction as substraction
from modules.math.multiplication import multiplication as multiplication

# Kitų failų ir žemiau esančio kodo nekeiskite

a = addition(1, 4);
b = division(4, 2);
c = substraction(3, 2);
d = multiplication(5, 2);

print(a);
print(b);
print(c);
print(d);


