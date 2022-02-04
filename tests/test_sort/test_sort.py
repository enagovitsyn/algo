from sort import BubbleSort, ShakerSort, CombSort, QuickSort
import pytest
import pickle


with open("tests/test_sort/test_arrays.pkl", "rb") as f:
    test_arrays = pickle.load(f)


@pytest.mark.parametrize("test_arrs", test_arrays)
def test_bubble_sort(test_arrs):
    assert BubbleSort.apply(test_arrs[0]) == test_arrs[1]


@pytest.mark.parametrize("test_arrs", test_arrays)
def test_shaker_sort(test_arrs):
    assert ShakerSort.apply(test_arrs[0]) == test_arrs[1]


@pytest.mark.parametrize("test_arrs", test_arrays)
def test_comb_sort(test_arrs):
    assert CombSort.apply(test_arrs[0]) == test_arrs[1]


@pytest.mark.parametrize("test_arrs", test_arrays)
def test_quick_sort(test_arrs):
    assert QuickSort.apply(test_arrs[0]) == test_arrs[1]
