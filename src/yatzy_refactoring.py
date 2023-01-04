class Yatzy:

    @staticmethod
    def chance(listaDeDados):
        total = 0
        for dice in listaDeDados:
            total += dice
        return total

    @staticmethod
    def yatzy(listaDeDados):
        counts = [0]*(len(listaDeDados)+1)
        for dice in listaDeDados:
            counts[dice-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones(listaDeDados):
        sum = 0
        for dice in listaDeDados:
            if dice == 1:
                sum += 1
        return sum

    @staticmethod
    def twos( listaDeDados):
        sum = 0 
        for dice in listaDeDados:
            if dice == 2:
                sum+=2
        return sum
    
    @staticmethod
    def threes(listaDeDados):
        sum = 0
        for dice in listaDeDados:
            if dice == 3:
                sum+=3
        return sum
    
    def __init__(self, listaDeDados):
        self.dice = listaDeDados

    def fours(self):
        sum = 0
        for indice in range(5):
            if (self.dice[indice] == 4): 
                sum += 4
        return sum
    
    def fives(self):
        sum = 0
        for indice in range(len(self.dice)): 
            if (self.dice[indice] == 5):
                sum = sum + 5
        return sum

    def sixes(self):
        sum = 0
        for indice in range(len(self.dice)): 
            if (self.dice[indice] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair( listaDeDados):
        counts = [0]*6
        for dice in listaDeDados:
            counts[dice-1] += 1
        for indice in range(6):
            if (counts[6-indice-1] == 2):
                return (6-indice)*2
        return 0
    
    @staticmethod
    def two_pair( listaDeDados):
        counts = [0]*6
        for dice in listaDeDados:
            counts[dice-1] += 1
        n = 0
        score = 0
        for indice in range(6):
            if (counts[6-indice-1] >= 2):
                n = n+1
                score += (6-indice)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( listaDeDados):
        tallies = [0]*6
        for dice in listaDeDados:
            tallies[dice-1] += 1
        for indice in range(6):
            if (tallies[indice] >= 4):
                return (indice+1) * 4
        return 0
    
    @staticmethod
    def three_of_a_kind( listaDeDados):
        tallies = [0]*6
        for dice in listaDeDados:
            tallies[dice-1] += 1
        for indice in range(6):
            if (tallies[indice] >= 3):
                return (indice+1) * 3
        return 0

    @staticmethod
    def smallStraight( listaDeDados):
        tallies = [0]*6
        for dice in listaDeDados:
            tallies[dice-1] += 1
        
        if tallies.count(1) == 5:
            return 15
        return 0

    @staticmethod
    def largeStraight( listaDeDados):
        tallies = [0]*6
        for dice in listaDeDados:
            tallies[dice-1] += 1
            
        if tallies.count(1) == 5:
            return 20
        return 0

    @staticmethod
    def fullHouse( listaDeDados):
        tallies = []
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        for dice in listaDeDados:
            tallies[dice-1] += 1
        for indice in range(6):
            if (tallies[indice] == 2): 
                _2 = True
                _2_at = indice+1

        for indice in range(6):
            if (tallies[indice] == 3): 
                _3 = True
                _3_at = indice+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0