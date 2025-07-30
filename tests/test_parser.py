"""
Tests cho ViPython Parser
"""

import pytest
from src.vipython.lexer.tokenizer import ViPythonLexer
from src.vipython.parser.parser import ViPythonParser
from src.vipython.parser.ast_nodes import *

def parse_source(source: str):
    """Helper function để parse source code"""
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    parser = ViPythonParser(tokens)
    return parser.parse()

def test_simple_assignment():
    """Test parsing assignment đơn giản"""
    source = "x = 5"
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, Assignment)
    assert isinstance(stmt.target, Identifier)
    assert stmt.target.name == "x"
    assert isinstance(stmt.value, NumberLiteral)
    assert stmt.value.value == 5

def test_function_definition():
    """Test parsing function definition"""
    source = """ham test(a, b):
    tra_ve a + b"""
    
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, FunctionDef)
    assert stmt.name == "test"
    assert stmt.parameters == ["a", "b"]
    assert len(stmt.body) == 1

def test_if_statement():
    """Test parsing if statement"""
    source = """neu x > 5:
    in_ra("Big")
khac:
    in_ra("Small")"""
    
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, IfStatement)
    assert isinstance(stmt.condition, BinaryOp)
    assert len(stmt.then_body) == 1
    assert len(stmt.else_body) == 1

def test_for_loop():
    """Test parsing for loop"""
    source = """voi i trong [1, 2, 3]:
    in_ra(i)"""
    
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, ForStatement)
    assert isinstance(stmt.target, Identifier)
    assert stmt.target.name == "i"
    assert isinstance(stmt.iterable, ListLiteral)

def test_while_loop():
    """Test parsing while loop"""
    source = """trong_khi x < 10:
    x = x + 1"""
    
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, WhileStatement)
    assert isinstance(stmt.condition, BinaryOp)
    assert len(stmt.body) == 1

def test_function_call():
    """Test parsing function call"""
    source = "in_ra(\"Hello\", \"World\")"
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, ExpressionStatement)
    expr = stmt.expression
    assert isinstance(expr, FunctionCall)
    assert isinstance(expr.function, Identifier)
    assert expr.function.name == "in_ra"
    assert len(expr.arguments) == 2

def test_binary_operations():
    """Test parsing binary operations"""
    source = "result = a + b * c"
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, Assignment)
    assert isinstance(stmt.value, BinaryOp)
    # Kiểm tra precedence: a + (b * c)
    assert stmt.value.operator == "+"
    assert isinstance(stmt.value.right, BinaryOp)
    assert stmt.value.right.operator == "*"

def test_list_literal():
    """Test parsing list literal"""
    source = "lst = [1, 2, 3]"
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, Assignment)
    assert isinstance(stmt.value, ListLiteral)
    assert len(stmt.value.elements) == 3

def test_dict_literal():
    """Test parsing dictionary literal"""
    source = "d = {\"key\": \"value\", \"num\": 42}"
    ast = parse_source(source)
    
    assert len(ast.statements) == 1
    stmt = ast.statements[0]
    assert isinstance(stmt, Assignment)
    assert isinstance(stmt.value, DictLiteral)
    assert len(stmt.value.pairs) == 2

