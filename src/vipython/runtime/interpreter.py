"""
Interpreter cho ViPython-VN
"""

import sys
from typing import Any, Dict, List, Optional
from ..parser.ast_nodes import *
from ..stdlib.builtin_functions import BUILTIN_FUNCTIONS

class ViPythonRuntimeError(Exception):
    pass

class ReturnValue(Exception):
    """Exception để xử lý return statement"""
    def __init__(self, value):
        self.value = value

class BreakException(Exception):
    """Exception để xử lý break statement"""
    pass

class ContinueException(Exception):
    """Exception để xử lý continue statement"""
    pass

class Environment:
    """Môi trường lưu trữ biến"""
    def __init__(self, parent: Optional['Environment'] = None):
        self.parent = parent
        self.variables: Dict[str, Any] = {}
    
    def define(self, name: str, value: Any):
        """Định nghĩa biến mới"""
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        """Lấy giá trị biến"""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise ViPythonRuntimeError(f"Biến '{name}' chưa được định nghĩa")
    
    def set(self, name: str, value: Any):
        """Gán giá trị cho biến"""
        if name in self.variables:
            self.variables[name] = value
        elif self.parent and self.parent.has(name):
            self.parent.set(name, value)
        else:
            self.variables[name] = value
    
    def has(self, name: str) -> bool:
        """Kiểm tra biến có tồn tại không"""
        return name in self.variables or (self.parent and self.parent.has(name))

class ViPythonFunction:
    """Đại diện cho một hàm ViPython"""
    def __init__(self, name: str, parameters: List[str], body: List[Statement], closure: Environment):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.closure = closure
    
    def call(self, interpreter: 'ViPythonInterpreter', arguments: List[Any]) -> Any:
        """Gọi hàm"""
        if len(arguments) != len(self.parameters):
            raise ViPythonRuntimeError(f"Hàm '{self.name}' mong đợi {len(self.parameters)} tham số, "
                                     f"nhưng nhận được {len(arguments)}")
        
        # Tạo môi trường mới cho hàm
        function_env = Environment(self.closure)
        
        # Bind parameters
        for param, arg in zip(self.parameters, arguments):
            function_env.define(param, arg)
        
        # Lưu môi trường hiện tại
        previous_env = interpreter.environment
        interpreter.environment = function_env
        
        try:
            # Thực thi body
            for stmt in self.body:
                interpreter.execute(stmt)
            return None  # Implicit return None
        except ReturnValue as ret:
            return ret.value
        finally:
            # Khôi phục môi trường
            interpreter.environment = previous_env

class ViPythonClass:
    """Đại diện cho một lớp ViPython"""
    def __init__(self, name: str, methods: Dict[str, ViPythonFunction], attributes: Dict[str, Any]):
        self.name = name
        self.methods = methods
        self.attributes = attributes

class ViPythonInterpreter:
    def __init__(self):
        self.global_env = Environment()
        self.environment = self.global_env
        
        # Thêm built-in functions
        for name, func in BUILTIN_FUNCTIONS.items():
            self.global_env.define(name, func)
    
    def interpret(self, program: Program) -> Any:
        """Thực thi chương trình"""
        result = None
        for statement in program.statements:
            result = self.execute(statement)
        return result
    
    def execute(self, node: Statement) -> Any:
        """Thực thi một statement"""
        if isinstance(node, Assignment):
            return self.execute_assignment(node)
        elif isinstance(node, ExpressionStatement):
            return self.evaluate(node.expression)
        elif isinstance(node, IfStatement):
            return self.execute_if(node)
        elif isinstance(node, WhileStatement):
            return self.execute_while(node)
        elif isinstance(node, ForStatement):
            return self.execute_for(node)
        elif isinstance(node, FunctionDef):
            return self.execute_function_def(node)
        elif isinstance(node, ClassDef):
            return self.execute_class_def(node)
        elif isinstance(node, ReturnStatement):
            return self.execute_return(node)
        elif isinstance(node, BreakStatement):
            raise BreakException()
        elif isinstance(node, ContinueStatement):
            raise ContinueException()
        elif isinstance(node, PassStatement):
            return None
        elif isinstance(node, ImportStatement):
            return self.execute_import(node)
        elif isinstance(node, FromImportStatement):
            return self.execute_from_import(node)
        elif isinstance(node, TryStatement):
            return self.execute_try(node)
        else:
            raise ViPythonRuntimeError(f"Statement không được hỗ trợ: {type(node)}")
    
    def evaluate(self, node: Expression) -> Any:
        """Đánh giá một expression"""
        if isinstance(node, NumberLiteral):
            return node.value
        elif isinstance(node, StringLiteral):
            return node.value
        elif isinstance(node, BooleanLiteral):
            return node.value
        elif isinstance(node, NoneLiteral):
            return None
        elif isinstance(node, Identifier):
            return self.environment.get(node.name)
        elif isinstance(node, BinaryOp):
            return self.evaluate_binary_op(node)
        elif isinstance(node, UnaryOp):
            return self.evaluate_unary_op(node)
        elif isinstance(node, FunctionCall):
            return self.evaluate_function_call(node)
        elif isinstance(node, ListLiteral):
            return [self.evaluate(elem) for elem in node.elements]
        elif isinstance(node, DictLiteral):
            return {self.evaluate(key): self.evaluate(value) for key, value in node.pairs}
        elif isinstance(node, AttributeAccess):
            return self.evaluate_attribute_access(node)
        elif isinstance(node, IndexAccess):
            return self.evaluate_index_access(node)
        else:
            raise ViPythonRuntimeError(f"Expression không được hỗ trợ: {type(node)}")
    
    def execute_assignment(self, node: Assignment) -> None:
        """Thực thi assignment"""
        value = self.evaluate(node.value)
        
        if isinstance(node.target, Identifier):
            self.environment.set(node.target.name, value)
        elif isinstance(node.target, IndexAccess):
            obj = self.evaluate(node.target.object)
            index = self.evaluate(node.target.index)
            obj[index] = value
        elif isinstance(node.target, AttributeAccess):
            obj = self.evaluate(node.target.object)
            setattr(obj, node.target.attribute, value)
        else:
            raise ViPythonRuntimeError(f"Target assignment không hợp lệ: {type(node.target)}")
    
    def execute_if(self, node: IfStatement) -> None:
        """Thực thi if statement"""
        condition = self.evaluate(node.condition)
        if self.is_truthy(condition):
            for stmt in node.then_body:
                self.execute(stmt)
        else:
            # Kiểm tra elif parts
            for elif_condition, elif_body in node.elif_parts:
                if self.is_truthy(self.evaluate(elif_condition)):
                    for stmt in elif_body:
                        self.execute(stmt)
                    return
            
            # Thực thi else body
            for stmt in node.else_body:
                self.execute(stmt)
    
    def execute_while(self, node: WhileStatement) -> None:
        """Thực thi while loop"""
        try:
            while self.is_truthy(self.evaluate(node.condition)):
                try:
                    for stmt in node.body:
                        self.execute(stmt)
                except ContinueException:
                    continue
        except BreakException:
            pass
    
    def execute_for(self, node: ForStatement) -> None:
        """Thực thi for loop"""
        iterable = self.evaluate(node.iterable)
        
        if not hasattr(iterable, '__iter__'):
            raise ViPythonRuntimeError(f"Đối tượng không thể lặp: {type(iterable)}")
        
        try:
            for item in iterable:
                if isinstance(node.target, Identifier):
                    self.environment.set(node.target.name, item)
                else:
                    raise ViPythonRuntimeError("For loop target phải là identifier")
                
                try:
                    for stmt in node.body:
                        self.execute(stmt)
                except ContinueException:
                    continue
        except BreakException:
            pass
    
    def execute_function_def(self, node: FunctionDef) -> None:
        """Thực thi function definition"""
        function = ViPythonFunction(node.name, node.parameters, node.body, self.environment)
        self.environment.define(node.name, function)
    
    def execute_class_def(self, node: ClassDef) -> None:
        """Thực thi class definition"""
        # Tạo môi trường cho class
        class_env = Environment(self.environment)
        previous_env = self.environment
        self.environment = class_env
        
        try:
            # Thực thi body của class
            for stmt in node.body:
                self.execute(stmt)
            
            # Thu thập methods và attributes
            methods = {}
            attributes = {}
            
            for name, value in class_env.variables.items():
                if isinstance(value, ViPythonFunction):
                    methods[name] = value
                else:
                    attributes[name] = value
            
            # Tạo class object
            cls = ViPythonClass(node.name, methods, attributes)
            previous_env.define(node.name, cls)
        
        finally:
            self.environment = previous_env
    
    def execute_return(self, node: ReturnStatement) -> None:
        """Thực thi return statement"""
        value = None
        if node.value:
            value = self.evaluate(node.value)
        raise ReturnValue(value)
    
    def execute_import(self, node: ImportStatement) -> None:
        """Thực thi import statement"""
        # Placeholder - sẽ implement sau
        pass
    
    def execute_from_import(self, node: FromImportStatement) -> None:
        """Thực thi from import statement"""
        # Placeholder - sẽ implement sau
        pass
    
    def execute_try(self, node: TryStatement) -> None:
        """Thực thi try statement"""
        try:
            for stmt in node.body:
                self.execute(stmt)
        except Exception as e:
            # Tìm except clause phù hợp
            for exception_type, variable, except_body in node.except_clauses:
                # Simplified exception handling
                if variable:
                    self.environment.define(variable, e)
                
                for stmt in except_body:
                    self.execute(stmt)
                break
        else:
            # Thực thi else body nếu không có exception
            for stmt in node.else_body:
                self.execute(stmt)
        finally:
            # Thực thi finally body
            for stmt in node.finally_body:
                self.execute(stmt)
    
    def evaluate_binary_op(self, node: BinaryOp) -> Any:
        """Đánh giá binary operation"""
        left = self.evaluate(node.left)
        
        # Short-circuit evaluation cho logical operators
        if node.operator == 'va':
            if not self.is_truthy(left):
                return left
            return self.evaluate(node.right)
        elif node.operator == 'hoac':
            if self.is_truthy(left):
                return left
            return self.evaluate(node.right)
        
        right = self.evaluate(node.right)
        
        if node.operator == '+':
            return left + right
        elif node.operator == '-':
            return left - right
        elif node.operator == '*':
            return left * right
        elif node.operator == '/':
            if right == 0:
                raise ViPythonRuntimeError("Chia cho 0")
            return left / right
        elif node.operator == '//':
            if right == 0:
                raise ViPythonRuntimeError("Chia cho 0")
            return left // right
        elif node.operator == '%':
            return left % right
        elif node.operator == '**':
            return left ** right
        elif node.operator == '==':
            return left == right
        elif node.operator == '!=':
            return left != right
        elif node.operator == '<':
            return left < right
        elif node.operator == '>':
            return left > right
        elif node.operator == '<=':
            return left <= right
        elif node.operator == '>=':
            return left >= right
        elif node.operator == 'trong':
            return left in right
        elif node.operator == 'la':
            return left is right
        else:
            raise ViPythonRuntimeError(f"Toán tử không được hỗ trợ: {node.operator}")
    
    def evaluate_unary_op(self, node: UnaryOp) -> Any:
        """Đánh giá unary operation"""
        operand = self.evaluate(node.operand)
        
        if node.operator == '-':
            return -operand
        elif node.operator == '+':
            return +operand
        elif node.operator == 'khong':
            return not self.is_truthy(operand)
        else:
            raise ViPythonRuntimeError(f"Toán tử unary không được hỗ trợ: {node.operator}")
    
    def evaluate_function_call(self, node: FunctionCall) -> Any:
        """Đánh giá function call"""
        function = self.evaluate(node.function)
        arguments = [self.evaluate(arg) for arg in node.arguments]
        
        if isinstance(function, ViPythonFunction):
            return function.call(self, arguments)
        elif callable(function):
            # Built-in function
            return function(*arguments)
        else:
            raise ViPythonRuntimeError(f"Đối tượng không thể gọi: {type(function)}")
    
    def evaluate_attribute_access(self, node: AttributeAccess) -> Any:
        """Đánh giá attribute access"""
        obj = self.evaluate(node.object)
        return getattr(obj, node.attribute)
    
    def evaluate_index_access(self, node: IndexAccess) -> Any:
        """Đánh giá index access"""
        obj = self.evaluate(node.object)
        index = self.evaluate(node.index)
        return obj[index]
    
    def is_truthy(self, value: Any) -> bool:
        """Kiểm tra giá trị có truthy không"""
        if value is None or value is False:
            return False
        elif value == 0 or value == "" or value == []:
            return False
        else:
            return True

