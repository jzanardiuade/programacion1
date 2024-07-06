"""
-----------------------------------------------------------------------------------------------
Título: TP06-04 | REGISTRO DE PRECIPITACIONES
Fecha:
Autor: Joaquin Zanardi

Descripción: TP06-03 | ELIMINAR COMENTARIOS 
Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta 
que  los  comentarios  comienzan  con  el  signo  #  (siempre  que  éste  no  se  encuentre  encerrado  entre  comillas  simples  o 
dobles) y que también se considera comentario a las cadenas de documentación (docstrings).
-----------------------------------------------------------------------------------------------
"""

def remove_python_comments(file_path):
    in_docstring = False
    cleaned_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            # Check for docstring start or end
            if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
                in_docstring = not in_docstring
                continue  # Skip docstring lines
            if in_docstring:
                continue  # Skip lines inside docstrings
                # Check for inline comments not inside strings    
            else:
                in_string = False
                for i, char in enumerate(stripped_line):
                    if char == '"' or char == "'":
                        in_string = not in_string
                    if char == '#' and not in_string:
                        line = line.split('#')[0] + '\n'
                        break
                cleaned_lines.append(line)

    # Write the cleaned lines to a new file or overwrite the original
    with open(file_path, 'w') as file:
        file.writelines(cleaned_lines)

# Example usage
remove_python_comments("TP06-03.py")