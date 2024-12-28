# Tokenizes the input source code into meaningful lexemes.
import re

def lexical_analysis(code):
    token_specification = [
        ('NUMBER',   r'\d+'),          # Integer
        ('IDENT',    r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifiers
        ('OP',       r'[=+*/-]'),      # Arithmetic operators
        ('SKIP',     r'[ \t]+'),      # Skip spaces and tabs
        ('NEWLINE',  r'\n'),          # Line breaks
        ('MISMATCH', r'.'),            # Any other character
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    line_number = 1
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NEWLINE':
            line_number += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character {value} on line {line_number}')
        else:
            tokens.append((kind, value))
    return tokens

code = ' x = 42'
    

tokens = lexical_analysis(code)
print("Tokens:", tokens)
