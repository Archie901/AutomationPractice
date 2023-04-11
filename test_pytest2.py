'''Example of pytest module'''

from test_pytest import total, join


def test_total_empty() -> None:
    '''Total of empty list should be 0.0'''
    assert total([]) == 0.0

def test_total_single() -> None:
    '''Total of single item list should be the first item value'''
    assert total([111.0]) == 111.0

def test_total_many() -> None:
    '''Total of many items list should be their sum'''
    assert total([1.0, 2.0, 3.0]) == 6.0

########################

def test_join_usecase() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"

def test_join_edge_singitem() -> None:
    assert join([1], ", ") == "1"

def test_join_edge_emptydelimiter() -> None:
    assert join([1, 2, 3], "") == "123"