import pytest
from main import BubbleSort


@pytest.fixture()
def sort_obj():
    b = BubbleSort()
    return b


def test_bubblesort_1(sort_obj):
    data = [4, 3, 2, 1]
    sort_obj.set_data(data)
    sort_obj.sort()
    assert sort_obj.get_data() == [1, 2, 3, 4]


def test_bubblesort_2(sort_obj):
    data = [1]
    sort_obj.set_data(data)
    sort_obj.sort()
    assert sort_obj.get_data() == [1]


def test_bubblesort_3(sort_obj):
    data = []
    with pytest.raises(ValueError):
        sort_obj.set_data(data)


def test_bubblesort_4(sort_obj):
    data = ['a', 1, 2, 3]
    with pytest.raises(ValueError):
        sort_obj.set_data(data)


def test_bubblesort_5(sort_obj):
    data = 'James'
    with pytest.raises(ValueError):
        sort_obj.set_data(data)


def test_bubblesort_6(sort_obj):
    data = None
    with pytest.raises(ValueError):
        sort_obj.set_data(data)
