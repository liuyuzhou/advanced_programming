x = 30
print(f"1 + 2*3 + {x} = {eval('1 + 2*3 + x')}")
exec('for i in range(5): print(i)')


import ast
ex = ast.parse('2 + 3*4 + x', mode='eval')
print(f'ex: {ex}')
print(f'ast dump ex:\n{ast.dump(ex)}')

top = ast.parse('for i in range(10): print(i)', mode='exec')
print(f'top: {top}')
print(f'ast dump top:\n{ast.dump(top)}')


import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# Sample usage
if __name__ == '__main__':
    # Some Python code
    code = """for i in range(5):
        print(i)
        del i
    """

    # Parse into an AST
    top = ast.parse(code, mode='exec')

    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print(f'Loaded: {c.loaded}')
    print(f'Stored: {c.stored}')
    print(f'Deleted: {c.deleted}')


exec(compile(top,'<stdin>', 'exec'))


import ast
import inspect

# Node visitor that lowers globally accessed names into
# the function body as local variables.
class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        # Compile some assignments to lower the constants
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name)
                            for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')

        # Inject new statements into the function body
        node.body[:0] = code_ast.body

        # Save the function object
        self.func = node

# Decorator that turns global names into locals
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # Skip source lines prior to the @lower_names decorator
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n+1:])
        # Hack to deal with indented code
        if src.startswith((' ','\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        # Transform the AST
        cl = NameLower(namelist)
        cl.visit(top)

        # Execute the modified AST
        temp = {}
        exec(compile(top,'','exec'), temp, temp)

        # Pull out the modified code object
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1
@lower_names('INCR')
def count_down(n):
    while n > 0:
        n -= INCR


def count_down(n):
    __globals = globals()
    INCR = __globals['INCR']
    while n > 0:
        n -= INCR