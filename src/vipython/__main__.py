"""
Entry point cho ViPython-VN REPL
"""

import sys
import traceback
from .lexer.tokenizer import ViPythonLexer
from .parser.parser import ViPythonParser
from .runtime.interpreter import ViPythonInterpreter, ViPythonRuntimeError

def run_file(filename: str):
    """Chạy file ViPython"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Tokenize
        lexer = ViPythonLexer(source)
        tokens = lexer.tokenize()
        
        # Parse
        parser = ViPythonParser(tokens)
        ast = parser.parse()
        
        # Interpret
        interpreter = ViPythonInterpreter()
        interpreter.interpret(ast)
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'")
        sys.exit(1)
    except Exception as e:
        print(f"Lỗi: {e}")
        if "--debug" in sys.argv:
            traceback.print_exc()
        sys.exit(1)

def run_repl():
    """Chạy REPL (Read-Eval-Print Loop)"""
    interpreter = ViPythonInterpreter()
    
    print("ViPython-VN v0.1.0")
    print("Gõ 'thoat()' để thoát REPL")
    print()
    
    while True:
        try:
            # Read
            source = input(">>> ")
            
            if source.strip() == "":
                continue
            
            # Tokenize
            lexer = ViPythonLexer(source)
            tokens = lexer.tokenize()
            
            # Parse
            parser = ViPythonParser(tokens)
            ast = parser.parse()
            
            # Evaluate
            if ast.statements:
                result = None
                for stmt in ast.statements:
                    result = interpreter.execute(stmt)
                
                # Print result if it's an expression
                if result is not None:
                    print(result)
        
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            break
        except EOFError:
            print("\nTạm biệt!")
            break
        except Exception as e:
            print(f"Lỗi: {e}")
            if "--debug" in sys.argv:
                traceback.print_exc()

def main():
    """Main function"""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        run_file(filename)
    else:
        run_repl()

if __name__ == "__main__":
    main()

