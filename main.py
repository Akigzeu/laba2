from math import*
def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Радус должен задаваться целым числом или десятичной дробью")
    if radius <0:
        raise ValueError("Радиус не может быть отрицательным")
    return pi*(radius**2)
def area_rectangle(length, width):
    if type(length) not in [int, float] or type(width) not in [int, float]:
        raise TypeError("Длина и ширина должены задаваться целыми числами или десятичными дробями")
    if length <0 or width <0:
        raise ValueError("Длина или ширина не могут быть отрицательными")
    return length * width

