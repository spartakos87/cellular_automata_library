import numpy as np
from json import dump

from cecullar_automata.rules import *
from cecullar_automata.rules_2d import rules_2d
from cecullar_automata.generations_creators import generations_creators
from cecullar_automata.gif_creator import gif_creator
# https://en.wikipedia.org/wiki/Life-like_cellular_automaton

class cecullar_automata:
    def __init__(self, width=10,height=10, input_array='', generations=10, save_image=False,
                 save_data=False, filename=''):
        self.width = width
        self.height = height
        # self.random_array = random_array
        self.input_array = input_array
        self.first_generation = self.random_or_input_array()
        self.generations = generations
        self.save_image = save_image
        self.save_data = save_data
        self.filename = filename
        self.universe=''


    def game_of_life(self):
        """
        Call the game of life rule
        :return:
        """
        self._create_new_universe(rules_2d_dict['game_of_life'])


    def replicator(self):
        """
        Rule:B1357/S1357
        Name:Replicator
        Description:Edward Fredkin's replicating automaton: every pattern is eventually replaced by
        multiple copies of itself

        :return:
        """
        self._create_new_universe(rules_2d_dict['replicator'])

    def seeds(self):
        """
        Rule:B2/S
        Name:Seeds
        Description:All patterns are phoenixes, meaning that every live cell immediately dies, and many patterns
        lead to explosive chaotic growth. However, some engineered patterns with complex behavior are known.


        :return:
        """
        self._create_new_universe(rules_2d_dict['seeds'])

    def life_without_death(self):
        """
        Rule:B3/S012345678
        Name:Life without Death
        Description:Also known as Inkspot or Flakes. Cells that become alive never die. It combines chaotic growth with
        more structured ladder-like patterns that can be used to simulate arbitrary Boolean circuits


        :return:
        """
        self._create_new_universe(rules_2d_dict['life_without_death'])

    def life(self):
        """
        Rule: B3/S23
        Name: Life
        Description:Highly complex behavior

        :return:
        """
        self._create_new_universe(rules_2d_dict['life'])

    def life_34(self):
        """
        Rule:B34/S34
        Name:34 Life
        Description:Was initially thought to be a stable alternative to Life, until computer simulation found that
         larger patterns tend to explode. Has many small oscillators and spaceships.


        :return:
        """
        self._create_new_universe(rules_2d_dict['life_34'])

    def diamoeba(self):
        """
        Rule:B35678/S5678
        Name:Diamoeba
        Description:Forms large diamonds with chaotically fluctuating boundaries. First studied by Dean Hickerson, who
        in 1993 offered a $50 prize to find a pattern that fills space with live cells; the prize was won in 1999 by David Bell
        :return:
        """
        self._create_new_universe(rules_2d_dict['diamoeba'])

    def rule_2x2(self):
        """
        Rule:B36/S125
        Name:2x2
        Description:If a pattern is composed of 2x2 blocks, it will continue to evolve in the same form; grouping these
         blocks into larger powers of two leads to the same behavior, but slower. Has complex oscillators of high
         periods as well as a small glider.

        :return:
        """
        self._create_new_universe(rules_2d_dict['rule_2x2'])

    def highlife(self):
        """
        Rule:B36/S23
        Name:HighLife
        Decription:Similar to Life but with a small self-replicating pattern.

        :return:
        """
        self._create_new_universe(rules_2d_dict['highlife'])

    def day_and_night(self):
        """
        Rule:B3678/S34678
        Name:Day & Night
        Description:Symmetric under on-off reversal. Has engineered patterns with highly complex behavior.

        :return:
        """
        self._create_new_universe(rules_2d_dict['day_and_night'])

    def morley(self):
        """
        Rule:B368/S245
        Name:Morley
        Description:Named after Stephen Morley; also called Move. Supports very high-period and slow spaceships.

        :return:
        """
        self._create_new_universe(rules_2d_dict['morley'])

    def anneal(self):
        """
        Rule:B4678/S35678
        Name:Anneal
        Description:Also called the twisted majority rule. Symmetric under on-off reversal. Approximates the
        curve-shortening flow on the boundaries between live and dead cells.


        :return:
        """
        self._create_new_universe(rules_2d_dict['anneal'])



    def specify_rule_2d(self, rule):
        """
        User can input his/her rule

        :param rule:Must be in format Bxxx/Sxxx the x's should be numbers fo 0-8
        :return:
        """
        self._create_new_universe(rule)

    def store_data(self):
        """

        :return:
        """
        with open(self.filename) as ouput:
            dump(self.universe,ouput)


    def create_random_array(self):
        return np.random.randint(2,size=(self.width,self.height))

    def random_or_input_array(self):
        if self.input_array == '':
            self.input_array = self.create_random_array()
        return self.input_array

    def _create_new_universe(self,rule):
        self.universe = generations_creators(self.first_generation, rules_2d(rule).read_rule()
                                             ,self.generations ).create_generations()
        gif_creator(self.universe,save=self.save_image,filename=self.filename).create_fig()
        if self.save_data:
            self.store_data()


