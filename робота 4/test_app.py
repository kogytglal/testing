from app import Figure

def test_app_triangle():
    fig = "triangle"
    triangle = Figure(fig, 4)
    assert triangle.type == fig

def test_get_angles():
    triangle = Figure("triangle", 1)
    square = Figure("square", 2)
    rectangle = Figure("rectangle", 5)
    assert triangle.get_angles == 3
    assert square.get_angles == 4
    assert rectangle.get_angles == 4

def test_invalid_figure():
    import pytest
    with pytest.raises(AssertionError):
        Figure("circle", 1)

def test_invalid_length():
    import pytest
    with pytest.raises(AssertionError):
        Figure("square", 0)
