"""
Parser cho ViPython-VN
"""

from typing import List, Optional, Union
from ..lexer.tokens import Token, TokenType
from .ast_nodes import *

class ParseError(Exception):
    pass

class ViPythonParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def error(self, message: str):
        if self.current_token:
            raise ParseError(f"Lỗi phân tích cú pháp tại dòng {self.current_token.line}, "
                           f"cột {self.current_token.column}: {message}")
        else:
            raise ParseError(f"Lỗi phân tích cú pháp: {message}")
    
    def advance(self):
        """Di chuyển đến token tiếp theo"""
        if self.position < len(self.tokens) - 1:
            self.position += 1
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None
    
    def peek(self, offset: int = 1) -> Optional[Token]:
        """Xem token tại vị trí hiện tại + offset"""
        pos = self.position + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return None
    
    def match(self, *token_types: TokenType) -> bool:
        """Kiểm tra xem token hiện tại có khớp với các loại token cho trước không"""
        if self.current_token and self.current_token.type in token_types:
            return True
        return False
    
    def consume(self, token_type: TokenType, message: str = None) -> Token:
        """Tiêu thụ token với loại cụ thể"""
        if not self.current_token or self.current_token.type != token_type:
            if message:
                self.error(message)
            else:
                self.error(f"Mong đợi {token_type}, nhưng nhận được {self.current_token.type if self.current_token else 'EOF'}")
        
        token = self.current_token
        self.advance()
        return token
    
    def skip_newlines(self):
        """Bỏ qua các token newline và comment"""
        while self.match(TokenType.XUONG_DONG, TokenType.BINH_LUAN):
            self.advance()
    
    def parse(self) -> Program:
        """Parse toàn bộ chương trình"""
        statements = []
        self.skip_newlines()
        
        while self.current_token and not self.match(TokenType.KET_THUC):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        return Program(statements)
    
    def parse_statement(self) -> Optional[Statement]:
        """Parse một statement"""
        if not self.current_token:
            return None
        
        # Skip indentation tokens and comments
        if self.match(TokenType.THUT_LE, TokenType.BO_THUT_LE, TokenType.BINH_LUAN):
            self.advance()
            return None
        
        if self.match(TokenType.HAM):
            return self.parse_function_def()
        elif self.match(TokenType.LOP):
            return self.parse_class_def()
        elif self.match(TokenType.NEU):
            return self.parse_if_statement()
        elif self.match(TokenType.TRONG_KHI):
            return self.parse_while_statement()
        elif self.match(TokenType.VOI):
            return self.parse_for_statement()
        elif self.match(TokenType.TRA_VE):
            return self.parse_return_statement()
        elif self.match(TokenType.DUNG):
            self.advance()
            return BreakStatement()
        elif self.match(TokenType.TIEP_TUC):
            self.advance()
            return ContinueStatement()
        elif self.match(TokenType.DUNG_LAI):
            self.advance()
            return PassStatement()
        elif self.match(TokenType.NHAP):
            return self.parse_import_statement()
        elif self.match(TokenType.TU):
            return self.parse_from_import_statement()
        elif self.match(TokenType.THU):
            return self.parse_try_statement()
        else:
            return self.parse_expression_statement()
    
    def parse_function_def(self) -> FunctionDef:
        """Parse function definition"""
        self.consume(TokenType.HAM)
        name = self.consume(TokenType.TEN_BIEN, "Mong đợi tên hàm").value
        
        self.consume(TokenType.NGOAC_TRON_MO, "Mong đợi '(' sau tên hàm")
        
        parameters = []
        if not self.match(TokenType.NGOAC_TRON_DONG):
            parameters.append(self.consume(TokenType.TEN_BIEN, "Mong đợi tên tham số").value)
            while self.match(TokenType.PHAY):
                self.advance()
                parameters.append(self.consume(TokenType.TEN_BIEN, "Mong đợi tên tham số").value)
        
        self.consume(TokenType.NGOAC_TRON_DONG, "Mong đợi ')' sau danh sách tham số")
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau định nghĩa hàm")
        
        body = self.parse_block()
        return FunctionDef(name, parameters, body)
    
    def parse_class_def(self) -> ClassDef:
        """Parse class definition"""
        self.consume(TokenType.LOP)
        name = self.consume(TokenType.TEN_BIEN, "Mong đợi tên lớp").value
        
        bases = []
        if self.match(TokenType.NGOAC_TRON_MO):
            self.advance()
            if not self.match(TokenType.NGOAC_TRON_DONG):
                bases.append(self.parse_expression())
                while self.match(TokenType.PHAY):
                    self.advance()
                    bases.append(self.parse_expression())
            self.consume(TokenType.NGOAC_TRON_DONG, "Mong đợi ')' sau danh sách lớp cha")
        
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau định nghĩa lớp")
        body = self.parse_block()
        return ClassDef(name, bases, body)
    
    def parse_if_statement(self) -> IfStatement:
        """Parse if statement"""
        self.consume(TokenType.NEU)
        condition = self.parse_expression()
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau điều kiện if")
        then_body = self.parse_block()
        
        elif_parts = []
        while self.match(TokenType.NEU_KHAC):
            self.advance()
            elif_condition = self.parse_expression()
            self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau điều kiện elif")
            elif_body = self.parse_block()
            elif_parts.append((elif_condition, elif_body))
        
        else_body = []
        if self.match(TokenType.KHAC):
            self.advance()
            self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau else")
            else_body = self.parse_block()
        
        return IfStatement(condition, then_body, elif_parts, else_body)
    
    def parse_while_statement(self) -> WhileStatement:
        """Parse while statement"""
        self.consume(TokenType.TRONG_KHI)
        condition = self.parse_expression()
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau điều kiện while")
        body = self.parse_block()
        return WhileStatement(condition, body)
    
    def parse_for_statement(self) -> ForStatement:
        """Parse for statement"""
        self.consume(TokenType.VOI)
        
        # Parse target as simple identifier, not full expression
        if not self.match(TokenType.TEN_BIEN):
            self.error("Mong đợi tên biến trong vòng lặp for")
        target = Identifier(self.current_token.value)
        self.advance()
        
        self.consume(TokenType.TRONG, "Mong đợi 'trong' trong vòng lặp for")
        iterable = self.parse_expression()
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau vòng lặp for")
        body = self.parse_block()
        return ForStatement(target, iterable, body)
    
    def parse_return_statement(self) -> ReturnStatement:
        """Parse return statement"""
        self.consume(TokenType.TRA_VE)
        value = None
        if not self.match(TokenType.XUONG_DONG, TokenType.KET_THUC):
            value = self.parse_expression()
        return ReturnStatement(value)
    
    def parse_import_statement(self) -> ImportStatement:
        """Parse import statement"""
        self.consume(TokenType.NHAP)
        module = self.consume(TokenType.TEN_BIEN, "Mong đợi tên module").value
        
        alias = None
        if self.match(TokenType.TEN_BIEN) and self.current_token.value == "as":
            self.advance()
            alias = self.consume(TokenType.TEN_BIEN, "Mong đợi alias sau 'as'").value
        
        return ImportStatement(module, alias)
    
    def parse_from_import_statement(self) -> FromImportStatement:
        """Parse from import statement"""
        self.consume(TokenType.TU)
        module = self.consume(TokenType.TEN_BIEN, "Mong đợi tên module").value
        self.consume(TokenType.NHAP, "Mong đợi 'nhap' sau tên module")
        
        names = []
        names.append(self.consume(TokenType.TEN_BIEN, "Mong đợi tên import").value)
        while self.match(TokenType.PHAY):
            self.advance()
            names.append(self.consume(TokenType.TEN_BIEN, "Mong đợi tên import").value)
        
        return FromImportStatement(module, names)
    
    def parse_try_statement(self) -> TryStatement:
        """Parse try statement"""
        self.consume(TokenType.THU)
        self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau 'thu'")
        body = self.parse_block()
        
        except_clauses = []
        while self.match(TokenType.BAT):
            self.advance()
            exception_type = None
            variable = None
            
            if not self.match(TokenType.HAI_CHAM):
                exception_type = self.parse_expression()
                if self.match(TokenType.TEN_BIEN) and self.current_token.value == "as":
                    self.advance()
                    variable = self.consume(TokenType.TEN_BIEN, "Mong đợi tên biến sau 'as'").value
            
            self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau except")
            except_body = self.parse_block()
            except_clauses.append((exception_type, variable, except_body))
        
        else_body = []
        if self.match(TokenType.KHAC):
            self.advance()
            self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau else")
            else_body = self.parse_block()
        
        finally_body = []
        if self.match(TokenType.CUOI_CUNG):
            self.advance()
            self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau finally")
            finally_body = self.parse_block()
        
        return TryStatement(body, except_clauses, else_body, finally_body)
    
    def parse_expression_statement(self) -> Statement:
        """Parse expression statement hoặc assignment"""
        expr = self.parse_expression()
        
        # Kiểm tra assignment
        if self.match(TokenType.GAN, TokenType.CONG_BANG, TokenType.TRU_BANG, 
                     TokenType.NHAN_BANG, TokenType.CHIA_BANG):
            op = self.current_token
            self.advance()
            value = self.parse_expression()
            
            if op.type == TokenType.GAN:
                return Assignment(expr, value)
            else:
                # Compound assignment: a += b -> a = a + b
                binary_op = {
                    TokenType.CONG_BANG: '+',
                    TokenType.TRU_BANG: '-',
                    TokenType.NHAN_BANG: '*',
                    TokenType.CHIA_BANG: '/'
                }[op.type]
                new_value = BinaryOp(expr, binary_op, value)
                return Assignment(expr, new_value)
        
        return ExpressionStatement(expr)
    
    def parse_block(self) -> List[Statement]:
        """Parse một block statements"""
        statements = []
        self.skip_newlines()
        
        # Expect INDENT
        if self.match(TokenType.THUT_LE):
            self.advance()
        
        while (self.current_token and 
               not self.match(TokenType.BO_THUT_LE, TokenType.KET_THUC) and
               not self.match(TokenType.KHAC, TokenType.NEU_KHAC, TokenType.BAT, TokenType.CUOI_CUNG)):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        # Expect DEDENT
        if self.match(TokenType.BO_THUT_LE):
            self.advance()
        
        return statements
    
    def parse_expression(self) -> Expression:
        """Parse expression với precedence"""
        return self.parse_or()
    
    def parse_or(self) -> Expression:
        """Parse logical OR"""
        expr = self.parse_and()
        
        while self.match(TokenType.HOAC):
            op = self.current_token.value
            self.advance()
            right = self.parse_and()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_and(self) -> Expression:
        """Parse logical AND"""
        expr = self.parse_not()
        
        while self.match(TokenType.VA):
            op = self.current_token.value
            self.advance()
            right = self.parse_not()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_not(self) -> Expression:
        """Parse logical NOT"""
        if self.match(TokenType.KHONG):
            op = self.current_token.value
            self.advance()
            expr = self.parse_not()
            return UnaryOp(op, expr)
        
        return self.parse_comparison()
    
    def parse_comparison(self) -> Expression:
        """Parse comparison operators"""
        expr = self.parse_addition()
        
        while self.match(TokenType.BANG, TokenType.KHONG_BANG, TokenType.NHO_HON,
                         TokenType.LON_HON, TokenType.NHO_HON_BANG, TokenType.LON_HON_BANG,
                         TokenType.TRONG, TokenType.LA):
            op = self.current_token.value
            self.advance()
            right = self.parse_addition()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_addition(self) -> Expression:
        """Parse addition and subtraction"""
        expr = self.parse_multiplication()
        
        while self.match(TokenType.CONG, TokenType.TRU):
            op = self.current_token.value
            self.advance()
            right = self.parse_multiplication()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_multiplication(self) -> Expression:
        """Parse multiplication, division, and modulo"""
        expr = self.parse_power()
        
        while self.match(TokenType.NHAN, TokenType.CHIA, TokenType.CHIA_NGUYEN, TokenType.CHIA_DU):
            op = self.current_token.value
            self.advance()
            right = self.parse_power()
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_power(self) -> Expression:
        """Parse exponentiation"""
        expr = self.parse_unary()
        
        if self.match(TokenType.LUY_THUA):
            op = self.current_token.value
            self.advance()
            right = self.parse_power()  # Right associative
            expr = BinaryOp(expr, op, right)
        
        return expr
    
    def parse_unary(self) -> Expression:
        """Parse unary operators"""
        if self.match(TokenType.TRU, TokenType.CONG):
            op = self.current_token.value
            self.advance()
            expr = self.parse_unary()
            return UnaryOp(op, expr)
        
        return self.parse_postfix()
    
    def parse_postfix(self) -> Expression:
        """Parse postfix operations (function calls, attribute access, indexing)"""
        expr = self.parse_primary()
        
        while True:
            if self.match(TokenType.NGOAC_TRON_MO):
                # Function call
                self.advance()
                arguments = []
                if not self.match(TokenType.NGOAC_TRON_DONG):
                    arguments.append(self.parse_expression())
                    while self.match(TokenType.PHAY):
                        self.advance()
                        arguments.append(self.parse_expression())
                self.consume(TokenType.NGOAC_TRON_DONG, "Mong đợi ')' sau danh sách tham số")
                expr = FunctionCall(expr, arguments)
            elif self.match(TokenType.CHAM):
                # Attribute access
                self.advance()
                attr = self.consume(TokenType.TEN_BIEN, "Mong đợi tên thuộc tính").value
                expr = AttributeAccess(expr, attr)
            elif self.match(TokenType.NGOAC_VUONG_MO):
                # Index access
                self.advance()
                index = self.parse_expression()
                self.consume(TokenType.NGOAC_VUONG_DONG, "Mong đợi ']' sau index")
                expr = IndexAccess(expr, index)
            else:
                break
        
        return expr
    
    def parse_primary(self) -> Expression:
        """Parse primary expressions"""
        if self.match(TokenType.SO):
            value = int(self.current_token.value)
            self.advance()
            return NumberLiteral(value)
        
        if self.match(TokenType.THUC):
            value = float(self.current_token.value)
            self.advance()
            return NumberLiteral(value)
        
        if self.match(TokenType.VAN_BAN):
            value = self.current_token.value
            self.advance()
            return StringLiteral(value)
        
        if self.match(TokenType.DUNG_VAY):
            self.advance()
            return BooleanLiteral(True)
        
        if self.match(TokenType.SAI_VAY):
            self.advance()
            return BooleanLiteral(False)
        
        if self.match(TokenType.KHONG_CO):
            self.advance()
            return NoneLiteral()
        
        if self.match(TokenType.TEN_BIEN):
            name = self.current_token.value
            self.advance()
            return Identifier(name)
        
        if self.match(TokenType.NGOAC_TRON_MO):
            self.advance()
            expr = self.parse_expression()
            self.consume(TokenType.NGOAC_TRON_DONG, "Mong đợi ')' đóng ngoặc")
            return expr
        
        if self.match(TokenType.NGOAC_VUONG_MO):
            # List literal
            self.advance()
            elements = []
            if not self.match(TokenType.NGOAC_VUONG_DONG):
                elements.append(self.parse_expression())
                while self.match(TokenType.PHAY):
                    self.advance()
                    if self.match(TokenType.NGOAC_VUONG_DONG):  # Trailing comma
                        break
                    elements.append(self.parse_expression())
            self.consume(TokenType.NGOAC_VUONG_DONG, "Mong đợi ']' đóng danh sách")
            return ListLiteral(elements)
        
        if self.match(TokenType.NGOAC_NHON_MO):
            # Dictionary literal
            self.advance()
            pairs = []
            if not self.match(TokenType.NGOAC_NHON_DONG):
                key = self.parse_expression()
                self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau key trong dictionary")
                value = self.parse_expression()
                pairs.append((key, value))
                
                while self.match(TokenType.PHAY):
                    self.advance()
                    if self.match(TokenType.NGOAC_NHON_DONG):  # Trailing comma
                        break
                    key = self.parse_expression()
                    self.consume(TokenType.HAI_CHAM, "Mong đợi ':' sau key trong dictionary")
                    value = self.parse_expression()
                    pairs.append((key, value))
            
            self.consume(TokenType.NGOAC_NHON_DONG, "Mong đợi '}' đóng dictionary")
            return DictLiteral(pairs)
        
        self.error(f"Token không mong đợi: {self.current_token.type if self.current_token else 'EOF'}")

