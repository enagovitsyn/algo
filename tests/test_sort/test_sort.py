from sort import BubbleSort, ShakerSort, CombSort, QuickSort, MergeSort
import pytest
import pickle


with open("tests/test_sort/control_arrays.pkl", "rb") as f:
    control_arrays = pickle.load(f)


@pytest.mark.parametrize("arrays", control_arrays)
def test_bubble_sort(arrays):
    assert BubbleSort.apply(arrays[0]) == arrays[1]


@pytest.mark.parametrize("arrays", control_arrays)
def test_shaker_sort(arrays):
    assert ShakerSort.apply(arrays[0]) == arrays[1]


@pytest.mark.parametrize("arrays", control_arrays)
def test_comb_sort(arrays):
    assert CombSort.apply(arrays[0]) == arrays[1]


@pytest.mark.parametrize("arrays", control_arrays)
def test_quick_sort(arrays):
    assert QuickSort.apply(arrays[0]) == arrays[1]


@pytest.mark.parametrize("arrays", control_arrays)
def test_merge_sort(arrays):
    assert MergeSort.apply(arrays[0]) == arrays[1]
