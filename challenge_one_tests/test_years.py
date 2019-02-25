from dayOneChallengeOne.challenge_one.years import Years
import pytest

years_instance = Years()

def test_year_is_invalid():
    assert years_instance.get_year("2025") == "Invalid year of birth"

def test_year_is_not_integer():
    assert years_instance.get_year("dgdgd") == "You must provide an integer" 

def test_is_minor():
    assert years_instance.get_year("2005") == "You are a minor"

def test_is_youth():
    assert years_instance.get_year("1997") == "You are a youth"

def test_is_elder():
    assert years_instance.get_year("1980") == "You are an elder"