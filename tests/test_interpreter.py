"""
Tests cho ViPython Interpreter
"""

import pytest
from io import StringIO
import sys
from src.vipython.lexer.tokenizer import ViPythonLexer
from src.vipython.parser.parser import ViPythonParser
from src.vipython.runtime.interpreter import ViPythonInterpreter

def run_code(source: str):
    """Helper function để chạy ViPython code"""
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter = ViPythonInterpreter()
    return interpreter.interpret(ast)

def test_simple_assignment():
    """Test assignment và variable access"""
    source = """x = 5
y = x + 3"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("x") == 5
    assert interpreter.environment.get("y") == 8

def test_arithmetic_operations():
    """Test các phép toán số học"""
    source = """a = 10
b = 3
cong = a + b
tru = a - b
nhan = a * b
chia = a / b
chia_nguyen = a // b
chia_du = a % b
luy_thua = a ** b"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("cong") == 13
    assert interpreter.environment.get("tru") == 7
    assert interpreter.environment.get("nhan") == 30
    assert interpreter.environment.get("chia") == 10/3
    assert interpreter.environment.get("chia_nguyen") == 3
    assert interpreter.environment.get("chia_du") == 1
    assert interpreter.environment.get("luy_thua") == 1000

def test_comparison_operations():
    """Test các phép so sánh"""
    source = """a = 5
b = 3
bang = a == b
khong_bang = a != b
nho_hon = a < b
lon_hon = a > b
nho_hon_bang = a <= b
lon_hon_bang = a >= b"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("bang") == False
    assert interpreter.environment.get("khong_bang") == True
    assert interpreter.environment.get("nho_hon") == False
    assert interpreter.environment.get("lon_hon") == True
    assert interpreter.environment.get("nho_hon_bang") == False
    assert interpreter.environment.get("lon_hon_bang") == True

def test_logical_operations():
    """Test các phép logic"""
    source = """a = dung_vay
b = sai_vay
va_op = a va b
hoac_op = a hoac b
khong_op = khong a"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("va_op") == False
    assert interpreter.environment.get("hoac_op") == True
    assert interpreter.environment.get("khong_op") == False

def test_if_statement():
    """Test if statement"""
    source = """x = 10
neu x > 5:
    result = "big"
khac:
    result = "small\""""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("result") == "big"

def test_while_loop():
    """Test while loop"""
    source = """i = 0
total = 0
trong_khi i < 5:
    total = total + i
    i = i + 1"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("total") == 10  # 0+1+2+3+4
    assert interpreter.environment.get("i") == 5

def test_for_loop():
    """Test for loop"""
    source = """total = 0
voi i trong [1, 2, 3, 4, 5]:
    total = total + i"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("total") == 15

def test_function_definition_and_call():
    """Test function definition và call"""
    source = """ham cong(a, b):
    tra_ve a + b

result = cong(3, 4)"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("result") == 7

def test_recursive_function():
    """Test recursive function"""
    source = """ham giai_thua(n):
    neu n <= 1:
        tra_ve 1
    khac:
        tra_ve n * giai_thua(n - 1)

result = giai_thua(5)"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("result") == 120

def test_list_operations():
    """Test list operations"""
    source = """lst = [1, 2, 3]
first = lst[0]
lst[1] = 10
second = lst[1]"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("first") == 1
    assert interpreter.environment.get("second") == 10

def test_builtin_functions():
    """Test built-in functions"""
    source = """length = do_dai([1, 2, 3, 4])
str_num = chuyen_van_ban(42)
int_str = chuyen_so("123")"""
    
    interpreter = ViPythonInterpreter()
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    ast = parser.parse()
    interpreter.interpret(ast)
    
    assert interpreter.environment.get("length") == 4
    assert interpreter.environment.get("str_num") == "42"
    assert interpreter.environment.get("int_str") == 123

