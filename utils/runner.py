"""
Safe code runner for student assignments.
Executes and validates student code with proper error handling.
"""

import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr


def run_code(code_string, global_vars=None, local_vars=None, timeout=5):
    """
    Safely run code and capture output.
    
    Args:
        code_string: Python code to execute
        global_vars: Global variables for execution
        local_vars: Local variables for execution
        timeout: Maximum execution time (not enforced in this version)
    
    Returns:
        Tuple of (success, output, error_message, variables)
    """
    if global_vars is None:
        global_vars = {}
    if local_vars is None:
        local_vars = {}
    
    # Add built-in functions
    global_vars['__builtins__'] = __builtins__
    
    output = io.StringIO()
    errors = io.StringIO()
    
    try:
        with redirect_stdout(output), redirect_stderr(errors):
            exec(code_string, global_vars, local_vars)
        
        return True, output.getvalue(), "", global_vars
    except Exception as e:
        error_msg = f"{type(e).__name__}: {e}\n"
        error_msg += traceback.format_exc()
        return False, output.getvalue(), error_msg, global_vars


def test_function(func, test_cases):
    """
    Test a function with multiple test cases.
    
    Args:
        func: Function to test
        test_cases: List of (args, expected_result) tuples
    
    Returns:
        List of test results
    """
    results = []
    for args, expected in test_cases:
        try:
            if isinstance(args, tuple):
                result = func(*args)
            else:
                result = func(args)
            
            passed = result == expected
            results.append({
                'passed': passed,
                'args': args,
                'expected': expected,
                'actual': result
            })
        except Exception as e:
            results.append({
                'passed': False,
                'args': args,
                'expected': expected,
                'actual': str(e),
                'error': True
            })
    
    return results


def print_test_results(func_name, test_results):
    """Print formatted test results."""
    print(f"\nTesting {func_name}:")
    print("-" * 50)
    
    for i, result in enumerate(test_results, 1):
        status = "✓" if result['passed'] else "✗"
        print(f"{status} Test {i}:")
        print(f"  Input: {result['args']}")
        print(f"  Expected: {result['expected']}")
        print(f"  Got: {result['actual']}")
        if result.get('error'):
            print(f"  Error occurred!")
        print()
    
    passed = sum(1 for r in test_results if r['passed'])
    total = len(test_results)
    print(f"Result: {passed}/{total} tests passed")
    print("-" * 50)
