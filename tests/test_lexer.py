"""
Tests cho ViPython Lexer
"""

import pytest
from src.vipython.lexer.tokenizer import ViPythonLexer
from src.vipython.lexer.tokens import TokenType

def test_basic_tokens():
    """Test tokenization của các token cơ bản"""
    source = "in_ra(\"Hello World\")"
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    expected_types = [
        TokenType.TEN_BIEN,
        TokenType.NGOAC_TRON_MO,
        TokenType.VAN_BAN,
        TokenType.NGOAC_TRON_DONG,
        TokenType.KET_THUC
    ]
    
    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type

def test_keywords():
    """Test tokenization của keywords"""
    source = "neu khac trong_khi voi ham tra_ve"
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    expected_types = [
        TokenType.NEU,
        TokenType.KHAC,
        TokenType.TRONG_KHI,
        TokenType.VOI,
        TokenType.HAM,
        TokenType.TRA_VE,
        TokenType.KET_THUC
    ]
    
    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type

def test_numbers():
    """Test tokenization của số"""
    source = "123 45.67"
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    assert tokens[0].type == TokenType.SO
    assert tokens[0].value == "123"
    assert tokens[1].type == TokenType.THUC
    assert tokens[1].value == "45.67"

def test_operators():
    """Test tokenization của operators"""
    source = "+ - * / == != < > <= >="
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    expected_types = [
        TokenType.CONG,
        TokenType.TRU,
        TokenType.NHAN,
        TokenType.CHIA,
        TokenType.BANG,
        TokenType.KHONG_BANG,
        TokenType.NHO_HON,
        TokenType.LON_HON,
        TokenType.NHO_HON_BANG,
        TokenType.LON_HON_BANG,
        TokenType.KET_THUC
    ]
    
    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type

def test_comments():
    """Test tokenization của comments"""
    source = "# This is a comment\nin_ra(\"Hello\")"
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    assert tokens[0].type == TokenType.BINH_LUAN
    assert tokens[1].type == TokenType.XUONG_DONG
    assert tokens[2].type == TokenType.TEN_BIEN

def test_indentation():
    """Test tokenization của indentation"""
    source = """neu dung_vay:
    in_ra("Hello")
    in_ra("World")"""
    
    lexer = ViPythonLexer(source)
    tokens = lexer.tokenize()
    
    # Tìm INDENT và DEDENT tokens
    indent_found = any(token.type == TokenType.THUT_LE for token in tokens)
    dedent_found = any(token.type == TokenType.BO_THUT_LE for token in tokens)
    
    assert indent_found
    assert dedent_found

