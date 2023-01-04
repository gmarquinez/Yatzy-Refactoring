from src.yatzy_refactoring import Yatzy
import pytest

def test_chance_scores_sum_of_all_dice():
        expected = 15
        actual = Yatzy.chance(2,3,4,5,1)
        assert expected == actual
        assert 16 == Yatzy.chance(3,3,4,5,1)
  

def test_yatzy_scores_50():
        expected = 50
        actual = Yatzy.yatzy([4,4,4,4,4])
        assert expected == actual
        assert 50 == Yatzy.yatzy([6,6,6,6,6])
        assert 0 == Yatzy.yatzy([6,6,6,6,3])
  

@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
               ([1,2,3,4,5], 1),
               ([1,2,1,4,5], 2),
               ([6,2,2,4,5], 0),
               ([1,2,1,1,1], 4)
        ]
)
def test_1s(listaDeDados, resultado):
        assert Yatzy.ones(listaDeDados) == resultado
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([1,2,3,2,6], 4),
                ([2,2,2,2,2], 10)
        ]
)
def test_2s(listaDeDados, resultado):
        assert Yatzy.twos(listaDeDados) == resultado
  
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([1,2,3,2,3], 6),
                ([2,3,3,3,3], 12)
        ]
)
def test_threes(listaDeDados, resultado):
        assert Yatzy.threes(listaDeDados) == resultado

  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([4,4,4,5,5], 12),
                ([4,4,5,5,5], 8),
                ([4,5,5,5,5], 4)
        ]
)
def test_fours_test(listaDeDados, resultado):
        assert Yatzy(listaDeDados).fours() == resultado
   
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([4,4,4,5,5], 10),
                ([4,4,5,5,5], 15),
                ([4,5,5,5,5], 20)
        ]
)
def test_fives(listaDeDados, resultado):
        assert Yatzy(listaDeDados).fives() == resultado
    
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([4,4,4,5,5], 0),
                ([4,4,6,5,5], 6),
                ([6,5,6,6,5], 18)
        ]
)
def test_sixes_test(listaDeDados, resultado):
        assert Yatzy(listaDeDados).sixes() == resultado
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([3,4,3,5,6], 6),
                ([5,3,3,3,5], 10),
                ([5,3,6,6,5], 12)
        ]
)
def test_one_pair(listaDeDados, resultado):
        assert Yatzy.score_pair(listaDeDados) == resultado

  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([3,3,5,4,5], 16),
                ([3,3,6,6,6], 18),
                ([3,3,6,5,4], 0)
        ]
)
def test_two_Pair(listaDeDados, resultado):
        assert Yatzy.two_pair(listaDeDados) == resultado
       
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([3,3,3,4,5], 9),
                ([5,3,5,4,5], 15),
                ([3,3,3,3,5], 9)
        ]
)
def test_three_of_a_kind(listaDeDados, resultado):
        assert Yatzy.three_of_a_kind(listaDeDados) == resultado
       
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([3,3,3,3,5], 12),
                ([5,5,5,4,5], 20),
                ([3,3,3,3,3], 12),
                ([3,3,3,2,1], 0)
        ]
)
def test_four_of_a_knd(listaDeDados, resultado):
        assert Yatzy.four_of_a_kind(listaDeDados) == resultado
       
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([1,2,3,4,5], 15),
                ([2,3,4,5,1], 15),
                ([1,2,2,4,5], 0)
        ]
)
def test_smallStraight(listaDeDados, resultado):
        assert Yatzy.smallStraight(listaDeDados) == resultado
  
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([6,2,3,4,5], 20),
                ([2,3,4,5,6], 20),
                ([1,2,2,4,5], 0)
        ]
)
def test_largeStraight(listaDeDados, resultado):
        assert Yatzy.largeStraight(listaDeDados) == resultado
     
@pytest.mark.parametrize(
        "listaDeDados, resultado",
        [
                ([6,2,2,2,6], 18),
                ([2,3,4,5,6], 0)
        ]
)
def test_fullHouse(listaDeDados, resultado):
        assert Yatzy.fullHouse(listaDeDados) == resultado
      
   