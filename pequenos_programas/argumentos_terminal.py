import argparse
def soma(a, b):
    return a + b
def subtra(a, b):
    return a - b

def main(number, other_number):
    result = number + other_number
    print(f'The result is {result}')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=1)
    parser.add_argument('-n2', type=int, help='Another number', default=1)
    parser.add_argument('-op', type=str, help='Operacao', default='soma')
    args = parser.parse_args()
    if args.op == 'soma':
        print(f'O resultado da operacao {args.op} é: {soma(args.n1, args.n2)}')
    if args.op == 'subtra':
        print(f'O resultado da operacao {args.op} é: {subtra(args.n1, args.n2)}')