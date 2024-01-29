import pytest
from source.triangles import classify_triangle

def test_equilateral_triangle(capsys):
    classify_triangle(9,9,9)
    captured=capsys.readouterr()
    assert captured.out.strip()=="equilateral triangle"
    classify_triangle(0.001,0.001,0.001)
    captured1=capsys.readouterr()
    assert captured1.out.strip()=="equilateral triangle"
    classify_triangle(1000,1000,1000)
    captured2=capsys.readouterr()
    assert captured2.out.strip()=="equilateral triangle"
    #classify_triangle(11,23.3,343.6)
    #captured3=capsys.readouterr()
    #assert captured3.out.strip()=="equilateral triangle"

def test_isoceles_triangle(capsys):
    classify_triangle(5,5,7)
    captured=capsys.readouterr()
    assert captured.out.strip()=="isosceles triangle"
    classify_triangle(5,12,13)
    captured1=capsys.readouterr()
    assert captured1.out.strip()=="right-angled triangle"
    classify_triangle(1,1,1.4142)
    captured2=capsys.readouterr()
    assert captured2.out.strip()=="isosceles right-angled triangle"

def test_scalene_triangle(capsys):
    classify_triangle(13,14,15)
    captured=capsys.readouterr()
    assert captured.out.strip()=="scalene triangle"

def test_invalid_triangle(capsys):
    classify_triangle(1,1,0)
    captured=capsys.readouterr()
    assert captured.out.strip()=="invalid triangle"
