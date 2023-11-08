import re

class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a, self.b, self.c = a, b, c

    @property
    def discrt(self):
        return self.b**2 - 4 * self.a * self.c

    @property
    def x1(self):
       return (-self.b - (self.discrt) ** 0.5) / (2 * self.a) if self.discrt >= 0 else 'No real roots'

    @property
    def x2(self):
        return (-self.b + (self.discrt) ** 0.5) / (2 * self.a) if self.discrt >= 0 else 'No real roots'

    @property
    def view(self):
        expression = f'{self.a}x^2'
        exp_b_c = [f'{abs(self.b)}x', f'{abs(self.c)}']
        for sym in range(2):
            if re.fullmatch(r'-\d+', [str(self.b), str(self.c)][sym]):
                expression += f' - {exp_b_c[sym]}'
            else:
                expression += f' + {exp_b_c[sym]}'
        return expression

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)
    
    @coefficients.setter
    def coefficients(self, abc: tuple):
        self.a, self.b, self.c = abc

