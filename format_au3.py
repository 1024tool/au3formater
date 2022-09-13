#!/usr/bin/env python3.7.6
#-*- coding: utf-8 -*-
  
_AU3 = './sample.au3'
_AU3_OUT = './format_UPER.au3'
_INDENT = ' ' * 4
  
def au3formater(line, indent):
    line = line.strip()#.lower()
    
    next_indent = indent
    if line.startswith('END') or line.startswith('UNTIL') or line in ('NEXT', 'WEND'):
        indent -= 1
        next_indent -= 1
    elif line.startswith('IF') and line.endswith('THEN'):
        next_indent += 1
    elif (line.startswith('FUNC') or
        line.startswith('FOR') or
        line.startswith('SELECT') or
        line.startswith('SWITCH') or
        line.startswith('WHILE') or
        line == 'DO'):
        next_indent += 1
    elif line.startswith('ELSE') or line.startswith('CASE'):
        indent -= 1
    new_line = _INDENT * indent + line
    
    return new_line, next_indent
  
def main():
    with open(_AU3, 'r') as fp:
        with open(_AU3_OUT, 'w') as fpw:
            indent = 0
            line = fp.readline()
            while line:
                new_line, indent = au3formater(line, indent)
                if 'ENDFUNC' in new_line:
                    fpw.write('%s\n\n' % new_line)
                else:
                    fpw.write('%s\n' % new_line)
                line = fp.readline()
  
if __name__ == '__main__':
  main()
