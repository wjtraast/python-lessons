"""
Self-correcting mechanism for Python lessons.
Provides feedback and validation for student code.
"""

class TestResult:
    """Represents the result of a test."""
    def __init__(self, passed, message, expected=None, actual=None):
        self.passed = passed
        self.message = message
        self.expected = expected
        self.actual = actual
    
    def __str__(self):
        status = "✓ PASS" if self.passed else "✗ FAIL"
        result = f"{status}: {self.message}"
        if not self.passed and self.expected is not None:
            result += f"\n  Expected: {self.expected}"
            result += f"\n  Got: {self.actual}"
        return result


class Checker:
    """Base checker class for assignments."""
    
    def __init__(self, name):
        self.name = name
        self.results = []
    
    def add_test(self, passed, message, expected=None, actual=None):
        """Add a test result."""
        self.results.append(TestResult(passed, message, expected, actual))
    
    def test_value(self, value, expected, test_name):
        """Test if a value matches expected."""
        passed = value == expected
        self.add_test(passed, test_name, expected, value)
        return passed
    
    def test_type(self, value, expected_type, test_name):
        """Test if a value is of expected type."""
        passed = isinstance(value, expected_type)
        self.add_test(passed, test_name, f"type {expected_type.__name__}", type(value).__name__)
        return passed
    
    def test_length(self, value, expected_length, test_name):
        """Test if a value has expected length."""
        try:
            actual_length = len(value)
            passed = actual_length == expected_length
            self.add_test(passed, test_name, f"length {expected_length}", f"length {actual_length}")
            return passed
        except TypeError:
            self.add_test(False, test_name, "has length", "no length attribute")
            return False
    
    def test_condition(self, condition, test_name):
        """Test if a condition is true."""
        self.add_test(condition, test_name)
        return condition
    
    def get_results(self):
        """Get all test results."""
        return self.results
    
    def print_results(self):
        """Print formatted results."""
        print(f"\n{'='*50}")
        print(f"Assignment: {self.name}")
        print(f"{'='*50}")
        
        for i, result in enumerate(self.results, 1):
            print(f"{i}. {result}")
        
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        print(f"\n{'='*50}")
        print(f"Score: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 Excellent! All tests passed!")
        elif passed >= total * 0.8:
            print("👍 Good job! Keep going!")
        elif passed >= total * 0.5:
            print("👀 Getting there! Review the failed tests.")
        else:
            print("💪 Keep trying! Check the hints and try again.")
        print(f"{'='*50}\n")
        
        return passed == total


def run_assignment(assignment_func):
    """Decorator to run an assignment with self-correction."""
    def wrapper():
        try:
            return assignment_func()
        except Exception as e:
            print(f"❌ Error running assignment: {type(e).__name__}: {e}")
            return False
    return wrapper
