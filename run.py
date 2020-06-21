#!/usr/bin/python3

import os
import sys
import subprocess

def c(file):
    filename, _ = file.split('.')
    subprocess.call(['gcc', '-g', '-o', f'./bin/{filename}', f'./src/{file}'])
    return [f'./bin/{filename}']

def cpp(file):
    filename, _ = file.split('.')
    subprocess.call(['g++', '-g', '-o', f'./bin/{filename}', f'./src/{file}'])
    return [f'./bin/{filename}']

def python(file):
    return ['python3', f'./src/{file}']

def rust(file):
    filename, _ = file.split('.')
    subprocess.call(['rustc', '-g', '-o', f'./bin/{filename}', f'./src/{file}'])
    return [f'./bin/{filename}']

behaviour = {
    'c': c,
    'cpp': cpp,
    'py': python,
    'rs': rust,
}

def main(argv):
    try:
        if len(argv) == 1:
            print(f'Usage: {argv[0]} <filename> [args]')
            exit(0)
        else:
            if not os.path.isfile(f'./src/{argv[1]}'):
                print('[i] 파일이 존재하지 않습니다.')
                exit(-1)

            if '.' not in argv[1]:
                print('[i] 확장자가 존재하지 않습니다.')
                exit(-1)
            
            _, extension = argv[1].split('.')

            if extension not in behaviour:
                print('[!] 언어를 감지하지 못했습니다.')
                exit(-1)

            subprocess.call('clear')

            command = []
            command.extend(behaviour[extension](argv[1]))
            command.extend(argv[2:])

            subprocess.run(command)
    except:
        exit(-1)

if __name__ == "__main__":
    main(sys.argv)