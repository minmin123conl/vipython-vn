"""
Lexer (Tokenizer) cho ViPython-VN
"""

import re
from typing import List, Iterator
from .tokens import Token, TokenType, KEYWORDS

class ViPythonLexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        self.indent_stack = [0]  # Stack để theo dõi mức thụt lề
    
    def error(self, message: str):
        raise SyntaxError(f"Lỗi cú pháp tại dòng {self.line}, cột {self.column}: {message}")
    
    def peek(self, offset: int = 0) -> str:
        """Xem ký tự tại vị trí hiện tại + offset"""
        pos = self.position + offset
        if pos >= len(self.source):
            return ''
        return self.source[pos]
    
    def advance(self) -> str:
        """Di chuyển đến ký tự tiếp theo"""
        if self.position >= len(self.source):
            return ''
        
        char = self.source[self.position]
        self.position += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Bỏ qua khoảng trắng (trừ newline)"""
        while self.peek() and self.peek() in ' \t\r':
            self.advance()
    
    def read_string(self, quote: str) -> str:
        """Đọc chuỗi văn bản"""
        value = ''
        self.advance()  # Bỏ qua dấu ngoặc mở
        
        while self.peek() and self.peek() != quote:
            char = self.advance()
            if char == '\\':
                # Xử lý escape sequences
                next_char = self.advance()
                if next_char == 'n':
                    value += '\n'
                elif next_char == 't':
                    value += '\t'
                elif next_char == 'r':
                    value += '\r'
                elif next_char == '\\':
                    value += '\\'
                elif next_char == quote:
                    value += quote
                else:
                    value += next_char
            else:
                value += char
        
        if not self.peek():
            self.error("Chuỗi không được đóng")
        
        self.advance()  # Bỏ qua dấu ngoặc đóng
        return value
    
    def read_number(self) -> Token:
        """Đọc số (integer hoặc float)"""
        start_line, start_col = self.line, self.column
        value = ''
        is_float = False
        
        while self.peek() and (self.peek().isdigit() or self.peek() == '.'):
            char = self.advance()
            if char == '.':
                if is_float:
                    self.error("Số thực không hợp lệ")
                is_float = True
            value += char
        
        token_type = TokenType.THUC if is_float else TokenType.SO
        return Token(token_type, value, start_line, start_col)
    
    def read_identifier(self) -> Token:
        """Đọc identifier hoặc keyword"""
        start_line, start_col = self.line, self.column
        value = ''
        
        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            value += self.advance()
        
        # Kiểm tra xem có phải keyword không
        token_type = KEYWORDS.get(value, TokenType.TEN_BIEN)
        return Token(token_type, value, start_line, start_col)
    
    def read_comment(self) -> Token:
        """Đọc comment"""
        start_line, start_col = self.line, self.column
        value = ''
        
        while self.peek() and self.peek() != '\n':
            value += self.advance()
        
        return Token(TokenType.BINH_LUAN, value, start_line, start_col)
    
    def handle_indentation(self, line_start: int) -> List[Token]:
        """Xử lý thụt lề"""
        tokens = []
        indent_level = 0
        
        # Đếm số khoảng trắng/tab ở đầu dòng
        pos = line_start
        while pos < len(self.source) and self.source[pos] in ' \t':
            if self.source[pos] == ' ':
                indent_level += 1
            else:  # tab
                indent_level += 4  # Tab = 4 spaces
            pos += 1
        
        current_indent = self.indent_stack[-1]
        
        if indent_level > current_indent:
            # Tăng thụt lề
            self.indent_stack.append(indent_level)
            tokens.append(Token(TokenType.THUT_LE, '', self.line, 1))
        elif indent_level < current_indent:
            # Giảm thụt lề
            while self.indent_stack and self.indent_stack[-1] > indent_level:
                self.indent_stack.pop()
                tokens.append(Token(TokenType.BO_THUT_LE, '', self.line, 1))
            
            if not self.indent_stack or self.indent_stack[-1] != indent_level:
                self.error("Thụt lề không khớp")
        
        return tokens
    
    def tokenize(self) -> List[Token]:
        """Tokenize toàn bộ source code"""
        tokens = []
        line_start = True
        
        while self.position < len(self.source):
            # Xử lý thụt lề ở đầu dòng
            if line_start:
                line_start = False
                if self.peek() not in '\n#':  # Không phải dòng trống hoặc comment
                    indent_tokens = self.handle_indentation(self.position)
                    tokens.extend(indent_tokens)
            
            char = self.peek()
            
            if not char:
                break
            
            # Khoảng trắng
            if char in ' \t\r':
                self.skip_whitespace()
                continue
            
            # Newline
            if char == '\n':
                tokens.append(Token(TokenType.XUONG_DONG, char, self.line, self.column))
                self.advance()
                line_start = True
                continue
            
            # Comment
            if char == '#':
                comment_token = self.read_comment()
                tokens.append(comment_token)
                continue
            
            # String literals
            if char in '"\'':
                value = self.read_string(char)
                tokens.append(Token(TokenType.VAN_BAN, value, self.line, self.column))
                continue
            
            # Numbers
            if char.isdigit():
                number_token = self.read_number()
                tokens.append(number_token)
                continue
            
            # Identifiers and keywords
            if char.isalpha() or char == '_':
                identifier_token = self.read_identifier()
                tokens.append(identifier_token)
                continue
            
            # Operators and delimiters
            start_line, start_col = self.line, self.column
            
            if char == '+':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.CONG_BANG, '+=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.CONG, '+', start_line, start_col))
            elif char == '-':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.TRU_BANG, '-=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.TRU, '-', start_line, start_col))
            elif char == '*':
                self.advance()
                if self.peek() == '*':
                    self.advance()
                    tokens.append(Token(TokenType.LUY_THUA, '**', start_line, start_col))
                elif self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.NHAN_BANG, '*=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.NHAN, '*', start_line, start_col))
            elif char == '/':
                self.advance()
                if self.peek() == '/':
                    self.advance()
                    tokens.append(Token(TokenType.CHIA_NGUYEN, '//', start_line, start_col))
                elif self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.CHIA_BANG, '/=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.CHIA, '/', start_line, start_col))
            elif char == '%':
                self.advance()
                tokens.append(Token(TokenType.CHIA_DU, '%', start_line, start_col))
            elif char == '=':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.BANG, '==', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.GAN, '=', start_line, start_col))
            elif char == '!':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.KHONG_BANG, '!=', start_line, start_col))
                else:
                    self.error(f"Ký tự không hợp lệ: {char}")
            elif char == '<':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.NHO_HON_BANG, '<=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.NHO_HON, '<', start_line, start_col))
            elif char == '>':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    tokens.append(Token(TokenType.LON_HON_BANG, '>=', start_line, start_col))
                else:
                    tokens.append(Token(TokenType.LON_HON, '>', start_line, start_col))
            elif char == '(':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_TRON_MO, '(', start_line, start_col))
            elif char == ')':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_TRON_DONG, ')', start_line, start_col))
            elif char == '[':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_VUONG_MO, '[', start_line, start_col))
            elif char == ']':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_VUONG_DONG, ']', start_line, start_col))
            elif char == '{':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_NHON_MO, '{', start_line, start_col))
            elif char == '}':
                self.advance()
                tokens.append(Token(TokenType.NGOAC_NHON_DONG, '}', start_line, start_col))
            elif char == ',':
                self.advance()
                tokens.append(Token(TokenType.PHAY, ',', start_line, start_col))
            elif char == ':':
                self.advance()
                tokens.append(Token(TokenType.HAI_CHAM, ':', start_line, start_col))
            elif char == ';':
                self.advance()
                tokens.append(Token(TokenType.CHAM_PHAY, ';', start_line, start_col))
            elif char == '.':
                self.advance()
                tokens.append(Token(TokenType.CHAM, '.', start_line, start_col))
            else:
                self.error(f"Ký tự không hợp lệ: {char}")
        
        # Thêm DEDENT tokens cho các indent còn lại
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            tokens.append(Token(TokenType.BO_THUT_LE, '', self.line, self.column))
        
        tokens.append(Token(TokenType.KET_THUC, '', self.line, self.column))
        return tokens

