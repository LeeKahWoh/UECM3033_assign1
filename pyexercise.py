import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (8/9)*sy.exp(4*sy.sin(x**4)+5), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array([[1,2,2,8,6,8,1,2,4,7], [5,2,0,0,0,0,2,5,5,5],
                  [2,5,6,7,8,4,5,6,3,4], [2,3,5,7,9,5,3,3,6,7],
                  [4,6,7,8,2,4,5,6,5,3], [4,6,7,8,4,3,2,5,6,8],
                  [5,6,7,8,9,4,3,2,5,6], [2,4,5,6,7,7,8,8,4,9],
                  [0,0,0,0,2,3,5,5,6,7], [9,9,8,8,6,6,4,4,0,0]])
    b = np.array([3,1,1,7,8,2,5,7,2,7])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1404656
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
