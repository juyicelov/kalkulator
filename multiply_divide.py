class MultiplyDivide:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Pembagi tidak boleh nol!")
        return a / b
