import pytest

def test_calc_addition():
  # Fonction test du resultat de 2+4
    output = 2+4
    assert output == 6

def test_calc_substraction():
  # Fonction test du resultat de 2-4
    output = 2-4
    assert output == -2

def test_calc_multiply():
  # Fonction test du resultat de 2*4
    output = 2*4
    assert output == 8

def test_coucou():
  # Fonction test si la resultat renvoie 'hello'
    output='hello'
    assert output == 'hello'

