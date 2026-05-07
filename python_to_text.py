'''
converts a python file into a text file for ease of sending files (:
'''

name_python = input('name of python file you want to convert (minus the .py extentsion): ')
name_text = input('name of new text file (minus .txt): ')

with open(f'{name_python}.py', 'r') as File:
    python_lines = File.readlines()


with open(f'{name_text}.txt', 'w') as file:
    file.writelines(python_lines)
        
    