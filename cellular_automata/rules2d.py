
class Rules2d:
    def __init__(self,input_rule=''):
        self.input_rule = input_rule

    def read_rule(self):
        """
        We will add Generation rules, which is in foramt Bx/Sy/C,where c is the number of all states

        :return:
        """
        last_element = self.input_rule[-1]
        # Check if it's Generation rule
        if len([i for i in self.input_rule if i == '/']) > 1:
            number_of_states = int(''.join([i for i in self.input_rule.split('/')[-1] if i.isdigit()]))
            self.input_rule = '/'.join(self.input_rule.split('/')[:2])
        else:
            # In case we havent multi states but binary two(2) states
            number_of_states = 2
        if last_element == 'V':
            return self.read_rule_von_neumann_neighborhood() + [number_of_states]
        elif last_element == 'H':
            return self.read_rule_hexagonal_neighborhood() + [number_of_states]
        else:
            return self.read_rule_moore_neighborhood() + [number_of_states]

    def read_rule_moore_neighborhood(self):
        """
        Manipulate the input rules which is in format Bxxx/Sxxx,Moore neighborhood
        The x can be numbers for 0 to 8

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
            return [birth, alive ,'M']
        except Exception as e:
            raise Exception(e)

    def read_rule_von_neumann_neighborhood(self):
        """
        Bx/SxV , Von Neuman neighborhood
        The x can be 0 to 6

        :return:
        """
        try:
            self.input_rule =self.input_rule[:-1]
            birth, alive = self.input_rule.split('/')
            birth = [int(i) for i in birth if i.isdigit()]
            alive = [int(i) for i in alive if i.isdigit()]
            """
            First we check if a list is empty so is 0(?)
            And secondly if there is nummber > 6 , in this case 
            raise exception.
            Accept only numbers 0-6
            """
            if len(list(filter(lambda x: x > 6, birth))) > 0 or len(list(filter(lambda x: x > 6, alive))) > 0:
                raise Exception("There is the number >6 inside the rule.Only numbers 0-6 are acceptable.")
            if len(birth) == 0:
                birth.append(0)
            if len(alive) == 0:
                alive.append(0)
            return [birth, alive, 'V']
        except Exception as e:
            raise Exception(e)


    def read_rule_hexagonal_neighborhood(self):
        """
        Bx/SxH
        The x can be 0 to 4

        :return:
        """
        try:
            self.input_rule =self.input_rule[:-1]
            birth, alive = self.input_rule.split('/')
            birth = [int(i) for i in birth if i.isdigit()]
            alive = [int(i) for i in alive if i.isdigit()]
            """
            First we check if a list is empty so is 0(?)
            And secondly if there is nummber > 6 , in this case 
            raise exception.
            Accept only numbers 0-4
            """
            if len(list(filter(lambda x: x > 4, birth))) > 0 or len(list(filter(lambda x: x > 4, alive))) > 0:
                raise Exception("There is the number >4 inside the rule.Only numbers 0-4 are acceptable.")
            if len(birth) == 0:
                birth.append(0)
            if len(alive) == 0:
                alive.append(0)
            return [birth, alive, 'H']
        except Exception as e:
            raise Exception(e)



