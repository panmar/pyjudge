class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class judge:
    def __init__(self, reference, tests, test_gen=None):
        self.reference = reference
        self.tests = tests
        self.test_gen = test_gen

    def __call__(self, func):
        ref_results = []
        results = []

        success_header = f"{Color.OKGREEN}SUCCESS{Color.ENDC}"
        failure_header = f"{Color.FAIL}FAILURE{Color.ENDC}"

        for test in self.tests:
            ref_result = self.reference(*test)
            result = func(*test)
            ref_results += [ref_result]
            results += [result]

            if ref_result == result:
                print(f"{success_header}")
            else:
                print(
                    f"{failure_header} {test} - expected: {ref_result}, got: {result}"
                )

        if self.test_gen:
            failures, successes = 0, 0
            for test in self.test_gen():
                ref_result = self.reference(*test)
                result = func(*test)
                if ref_result != result:
                    failures += 1
                else:
                    successes += 1
            total = failures + successes
            if failures == 0:
                print(f"{success_header} - Random tests: {successes}/{total} passed.")
            else:
                print(f"{failure_header} - Random tests: {successes}/{total} passed.")

        return func

    def compare(self, results1, results2):
        print(f"Brute force: {results1}")
        print(f"Solution: {results2}")
        return results1 == results2