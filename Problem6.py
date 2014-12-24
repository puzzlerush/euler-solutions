def sumOfSquares(a):
    squares = []
    for x in range(a+1):
        squares.append(x**2)
    return sum(squares)
def squareOfSum(a):
    sums = []
    for x in range(a, 0, -1):
        sums.append(x)
    return sum(sums)**2
print(squareOfSum(100) - sumOfSquares(100))
        
        
