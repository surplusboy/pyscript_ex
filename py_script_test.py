import random
from time import sleep


print('py_script_test.py 진입')

number_input = Element('number_input')
result = Element('result')

input_btn = Element('input_btn')

def test_func(*args):
    user_input = number_input.value
    random_output = random.randint(1, 10)

    if int(user_input) == random_output:
        result.elemnet.innerText = 'True'
    else:
        result.elemnet.innerText = f'False, Why ? result = {random_output}'

    number_input.clear()

def test_func1(*args):
    result.elemnet.innerText = 'test'

input_btn.element.onclick = test_func1
