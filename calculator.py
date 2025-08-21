import math
import re

class ScientificCalculator:
    def __init__(self, angle_mode='DEG'):
        self.memory = 0
        self.angle_mode = angle_mode

    def to_radians(self, x):
        return math.radians(x) if self.angle_mode == 'DEG' else x

    def to_degrees(self, x):
        return math.degrees(x) if self.angle_mode == 'RAD' else x

    # Operations
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return x / y if y != 0 else float('inf')

    # Trigonometric
    def sin(self, x): return math.sin(self.to_radians(x))
    def cos(self, x): return math.cos(self.to_radians(x))
    def tan(self, x): return math.tan(self.to_radians(x))
    def arcsin(self, x): return self.to_degrees(math.asin(x))
    def arccos(self, x): return self.to_degrees(math.acos(x))
    def arctan(self, x): return self.to_degrees(math.atan(x))
    def sinh(self, x): return math.sinh(x)
    def cosh(self, x): return math.cosh(x)
    def tanh(self, x): return math.tanh(x)

    # Exponential & Logarithmic
    def exp(self, x): return math.exp(x)
    def ln(self, x): return math.log(x)
    def log10(self, x): return math.log10(x)
    def pow(self, x, y): return math.pow(x, y)
    def sqrt(self, x): return math.sqrt(x)
    def cbrt(self, x): return x ** (1/3)
    def abs(self, x): return abs(x)
    def factorial(self, n):
        return math.factorial(n) if n >= 0 and int(n) == n else float('nan')

    # Combinatorics
    def nPr(self, n, r):
        return self.factorial(n) // self.factorial(n - r)
    def nCr(self, n, r):
        return self.factorial(n) // (self.factorial(r) * self.factorial(n - r))

    # Miscellaneous
    def percent(self, x): return x / 100.0
    def mod(self, x, y): return x % y
    def reciprocal(self, x): return 1 / x if x != 0 else float('inf')
    def floor(self, x): return math.floor(x)
    def ceil(self, x): return math.ceil(x)
    def pi(self): return math.pi
    def e(self): return math.e

    # Memory
    def store_memory(self, x): self.memory = x
    def recall_memory(self): return self.memory
    def clear_memory(self): self.memory = 0

    # Statistical Functions
    def mean(self, arr): return sum(arr) / len(arr)
    def median(self, arr):
        arr = sorted(arr)
        mid = len(arr) // 2
        return arr[mid] if len(arr) % 2 else (arr[mid - 1] + arr[mid]) / 2
    def stdev(self, arr):
        m = self.mean(arr)
        return math.sqrt(sum((x - m) ** 2 for x in arr) / len(arr))
    def summation(self, arr): return sum(arr)

    # For safe eval: expose only allowed functions
    def safe_eval(self, expr):
        allowed = {
            'sin': self.sin, 'cos': self.cos, 'tan': self.tan,
            'arcsin': self.arcsin, 'arccos': self.arccos, 'arctan': self.arctan,
            'sinh': self.sinh, 'cosh': self.cosh, 'tanh': self.tanh,
            'exp': self.exp, 'ln': self.ln, 'log10': self.log10, 'pow': self.pow,
            'sqrt': self.sqrt, 'cbrt': self.cbrt, 'abs': self.abs,
            'factorial': self.factorial, 'nPr': self.nPr, 'nCr': self.nCr,
            'percent': self.percent, 'mod': self.mod, 'reciprocal': self.reciprocal,
            'floor': self.floor, 'ceil': self.ceil, 'pi': self.pi, 'e': self.e,
            'mean': self.mean, 'median': self.median, 'stdev': self.stdev, 'summation': self.summation,
            'memory': self.memory
        }
        expr = expr.replace('^', '**')
        # Security checks
        if re.search(r'[^\d\w\s\.\,\+\-\*\/\(\)\%\!\^\[\]]', expr):
            raise ValueError("Unsafe expression")
        return eval(expr, {"__builtins__": None}, allowed)