# -*- coding: utf-8 -*-
import pytest
from core.person import Person, MatchingFlags


@pytest.fixture
def testdata():
    data = []
    tobi = Person(name='Tobi', number=1, email='tobi@gmail.com', phone='0123456789',
                  marked_numbers=set([2, 3]), flags=MatchingFlags.match_all)
    sara = Person(name='Sara Mustermann', number=2, email='', phone='123456789',
                  marked_numbers=set([1, 4, 3]))
    mark = Person(name='Mark', number=3, email='mark@mark.com', phone='987654321',
                  marked_numbers=set([2, 4, 5]))
    luisa = Person(name='Luisa', number=4, email='', phone='49123456789',
                   marked_numbers=set([5, 1]), flags=MatchingFlags.match_all)
    data.append(tobi)
    data.append(sara)
    data.append(mark)
    data.append(luisa)
    return data


@pytest.fixture
def matchmaker():
    from core.matching import SimpleMatchmaker
    return SimpleMatchmaker()


def test_person_that_has_match_all_flag_matches_only_intersections(matchmaker, testdata):
    matchmaker.run(testdata)

    tobi, sara, mark, luisa = testdata
    assert tobi in sara.results.matches
    assert mark in sara.results.matches
    assert sara in mark.results.matches
    assert luisa not in mark.results.matches


def test_person_that_has_not_match_all_flags_matches_only_intersections(matchmaker, testdata):
    matchmaker.run(testdata)

    tobi, sara, mark, luisa = testdata
    assert tobi in sara.results.matches
    assert mark in sara.results.matches
    assert sara in mark.results.matches
    assert luisa not in mark.results.matches
