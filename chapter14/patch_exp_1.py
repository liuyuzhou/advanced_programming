from unittest.mock import patch
from chapter14 import example_exp

@patch('example_exp.func')
def test1(x, mock_func):
    example_exp.func(x)
    mock_func.assert_called_with(x)


with patch('example_exp.func') as mock_func:
    example_exp.func(x)
    mock_func.assert_called_with(x)


p = patch('example.func')
mock_func = p.start()
example_exp.func(x)
mock_func.assert_called_with(x)
p.stop()