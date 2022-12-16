import pytest
from airflow.dags.solution import nb_year


# can calculate the population for the first year
def test_nb_year_CurrentYear():

    number_of_years = nb_year(p0 = 1000, percent=5, aug=50, p=1000)
    assert number_of_years == 0

# can calculate the population for the second year

def test_nb_year_FirstYear():

    number_of_years = nb_year(p0 = 1000, percent=5, aug=50, p=1100)
    assert number_of_years == 1

def test_nb_year_SecondYear():

    number_of_years = nb_year(p0 = 1000, percent=5, aug=50, p=1200)
    assert number_of_years == 2

def test_nb_year_Tenth():

    number_of_years = nb_year(1500000, 2.5, 10000, 2000000)
    assert number_of_years == 10

def test_nb_year_nth():

    number_of_years = nb_year(1500000, 0.25, 1000, 2000000)
    assert number_of_years == 94

def test_nb_year_WeirdUseCase():

    number_of_years = nb_year(1000, 2, 50, 1214)
    assert number_of_years == 3