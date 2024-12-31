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

code = ' x = 42 '

tokens = lexical_analysis(code)

def syntax_analysis(tokens):
    if len(tokens) != 3 or tokens[1][1] != '=':
        raise SyntaxError("Invalid syntax")
    if tokens[0][0] != 'IDENT' or tokens[2][0] != 'NUMBER':
        raise SyntaxError("Invalid tokens")
    return {'type': 'assignment', 'var': tokens[0][1], 'value': int(tokens[2][1])}

syntax_tree = syntax_analysis(tokens)

def semantic_analysis(syntax_tree):

    if not syntax_tree['var'].isidentifier():
        raise ValueError(f"Invalid variable name: {syntax_tree['var']}")
    return True

semantic_analysis(syntax_tree)

# Intermediate Code Generation
def generate_ir(syntax_tree):
    return [{'op': 'assign', 'target': syntax_tree['var'], 'value': syntax_tree['value']}]

ir = generate_ir(syntax_tree)
print("Intermediate Representation:", ir)