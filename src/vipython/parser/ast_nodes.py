"""
Định nghĩa các node AST cho ViPython-VN
"""

from abc import ABC, abstractmethod
from typing import List, Any, Optional

class ASTNode(ABC):
    """Base class cho tất cả AST nodes"""
    pass

class Expression(ASTNode):
    """Base class cho các expression"""
    pass

class Statement(ASTNode):
    """Base class cho các statement"""
    pass

# Literals
class NumberLiteral(Expression):
    def __init__(self, value: float):
        self.value = value

class StringLiteral(Expression):
    def __init__(self, value: str):
        self.value = value

class BooleanLiteral(Expression):
    def __init__(self, value: bool):
        self.value = value

class NoneLiteral(Expression):
    def __init__(self):
        pass

# Identifiers
class Identifier(Expression):
    def __init__(self, name: str):
        self.name = name

# Binary Operations
class BinaryOp(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

# Unary Operations
class UnaryOp(Expression):
    def __init__(self, operator: str, operand: Expression):
        self.operator = operator
        self.operand = operand

# Function Call
class FunctionCall(Expression):
    def __init__(self, function: Expression, arguments: List[Expression]):
        self.function = function
        self.arguments = arguments

# List/Array
class ListLiteral(Expression):
    def __init__(self, elements: List[Expression]):
        self.elements = elements

# Dictionary
class DictLiteral(Expression):
    def __init__(self, pairs: List[tuple]):
        self.pairs = pairs  # List of (key, value) tuples

# Attribute Access
class AttributeAccess(Expression):
    def __init__(self, object: Expression, attribute: str):
        self.object = object
        self.attribute = attribute

# Index Access
class IndexAccess(Expression):
    def __init__(self, object: Expression, index: Expression):
        self.object = object
        self.index = index

# Assignment
class Assignment(Statement):
    def __init__(self, target: Expression, value: Expression):
        self.target = target
        self.value = value

# If Statement
class IfStatement(Statement):
    def __init__(self, condition: Expression, then_body: List[Statement], 
                 elif_parts: List[tuple] = None, else_body: List[Statement] = None):
        self.condition = condition
        self.then_body = then_body
        self.elif_parts = elif_parts or []  # List of (condition, body) tuples
        self.else_body = else_body or []

# While Loop
class WhileStatement(Statement):
    def __init__(self, condition: Expression, body: List[Statement]):
        self.condition = condition
        self.body = body

# For Loop
class ForStatement(Statement):
    def __init__(self, target: Expression, iterable: Expression, body: List[Statement]):
        self.target = target
        self.iterable = iterable
        self.body = body

# Function Definition
class FunctionDef(Statement):
    def __init__(self, name: str, parameters: List[str], body: List[Statement]):
        self.name = name
        self.parameters = parameters
        self.body = body

# Class Definition
class ClassDef(Statement):
    def __init__(self, name: str, bases: List[Expression], body: List[Statement]):
        self.name = name
        self.bases = bases
        self.body = body

# Return Statement
class ReturnStatement(Statement):
    def __init__(self, value: Optional[Expression] = None):
        self.value = value

# Break Statement
class BreakStatement(Statement):
    def __init__(self):
        pass

# Continue Statement
class ContinueStatement(Statement):
    def __init__(self):
        pass

# Pass Statement
class PassStatement(Statement):
    def __init__(self):
        pass

# Expression Statement
class ExpressionStatement(Statement):
    def __init__(self, expression: Expression):
        self.expression = expression

# Import Statement
class ImportStatement(Statement):
    def __init__(self, module: str, alias: Optional[str] = None):
        self.module = module
        self.alias = alias

# From Import Statement
class FromImportStatement(Statement):
    def __init__(self, module: str, names: List[str]):
        self.module = module
        self.names = names

# Try Statement
class TryStatement(Statement):
    def __init__(self, body: List[Statement], except_clauses: List[tuple], 
                 else_body: List[Statement] = None, finally_body: List[Statement] = None):
        self.body = body
        self.except_clauses = except_clauses  # List of (exception_type, variable, body) tuples
        self.else_body = else_body or []
        self.finally_body = finally_body or []

# Program (Root node)
class Program(ASTNode):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

