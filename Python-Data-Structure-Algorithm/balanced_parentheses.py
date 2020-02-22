from stack import Stack

def balanced_parentheses(parentheses):
    s = Stack()
    for p in parentheses:
        if p == '(':
            s.push(p)
        elif p == ')':
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parentheses domonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
