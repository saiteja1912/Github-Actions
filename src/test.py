# app.py
#This is a test change
def divide(a, b):
    assert b != 0, "Zero Division Error"
    return a/b

def test_division():
    divide(2, 1) == 2
    print(f'** 1st test passed **\n')
    divide(1, 0) == 1
    print(f'** 2nd test passed **')
test_division()