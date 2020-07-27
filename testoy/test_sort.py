import pytest

SORT_FUNC = {}

edge_cases = [([], [])]
small_cases = [([1], [1]), ([2, 1], [1, 2])] # length 1 ~ 4
mid_cases = [([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])] # length 5 ~ 100
# large_cases = [([], [])] # length 100 ~

# Will be used as a Decorator for users 
# --> Saves the function to SORT_FUNC variable and execute pytesting.
def decorator_sort(f):
    global SORT_FUNC
    SORT_FUNC[f.__name__] = f
    pytest.main(["-v"]) # Execute: >pytest -v
    return f

# Fixture that will be used for testing functions
# --> This fixture gives test functions the sorting function we were to test with
@pytest.fixture
def fixture_sort():
    return list(SORT_FUNC.values())[0]

# Test Case for Edge cases
@pytest.mark.parametrize("test_case, sorted", edge_cases)
def test_edge_cases(fixture_sort, test_case, sorted):
    assert fixture_sort(test_case) == sorted 

# Test Case for small test cases
@pytest.mark.parametrize("test_case, sorted", small_cases)
def test_small_cases(fixture_sort, test_case, sorted):
    assert fixture_sort(test_case) == sorted 
    
# Test Case for mid-sized test cases
@pytest.mark.parametrize("test_case, sorted", mid_cases)
def test_mid_cases(fixture_sort, test_case, sorted):
    assert fixture_sort(test_case) == sorted 

# Test Case for large-sized test cases
@pytest.mark.parametrize("test_case, sorted", large_cases)
def test_large_cases(fixture_sort, test_case, sorted):
    assert fixture_sort(test_case) == sorted 