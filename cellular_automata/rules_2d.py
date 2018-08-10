
class rules_2d:
    def __init__(self,input_rule=''):
        self.input_rule = input_rule

    def read_rule(self):
        """
        Manipulate the inpute rules which is in format Bxxx/Sxxx

        :return: A list of two lists which include numbers from 0-8
        """
        try:
            birth, alive = self.input_rule.split('/')
            birth = [int(i) for i in birth if i.isdigit()]
            alive = [int(i) for i in alive if i.isdigit()]
            """
            First we check if a list is empty so is 0(?)
            And secondly if there is the number 9 , in this case 
            raise exception.
            Accept only numbers 0-8
            """
            if 9 in birth or 9 in alive:
                raise Exception("There is the number 9 inside the rule.Only numbers 0-8 are acceptable.")
            if len(birth) == 0:
                birth.append(0)
            if len(alive) == 0:
                alive.append(0)
            return [birth, alive]
        except Exception as e:
            raise Exception(e)

