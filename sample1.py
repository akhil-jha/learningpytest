"""
Default maths values
Using a class SampleClass, returning the maths constants
"""


class SampleClass:
    def value_pi(self):
        return 3.141

    def value_e(self):
        return 2.718

    def value_gamma(self):
        return 0.577

    def value_goldenratio(self):
        return 1.618


def main_fun():
    value = SampleClass()
    print(f'{value.value_e()}\n{value.value_gamma()}\
        \n{value.value_goldenratio()}\n{value.value_pi()}')

if __name__ == "__main__":
        main_fun()
