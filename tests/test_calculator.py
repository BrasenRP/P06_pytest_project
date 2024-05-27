from L06_calculator.Calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # Arrange
        a = 1001
        b = 1000
        cal = Calculator()

        #Act
        res = cal.subtract(a,b)

        #Assert
        expt = 1
        assert res == expt

    def test_multiply(self):
        # Arrange
        a = 10
        b = 5
        cal = Calculator()

        #Act
        res = cal.multiply(a,b)

        #Assert
        expt = 50
        assert res == expt

    def test_divide(self):
        # Arrange
        a = 100
        b = 10
        cal = Calculator()

        #Act
        res = cal.divide(a,b)

        #Assert
        expt = 10
        assert res == expt

