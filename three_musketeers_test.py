# The Three Musketeers Game TEST
# by Martha Trevino and Lu Lu.

import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0,0),string_to_location('A1'))
        self.assertEqual((1,2),string_to_location('B3'))
        self.assertEqual((3,4),string_to_location('D5'))
        self.assertEqual((4,1),string_to_location('E2'))
        self.assertEqual((2,2),string_to_location('C3'))
        
    def test_location_to_string(self):
        self.assertEqual('A1',location_to_string((0,0)))
        self.assertEqual('B3',location_to_string((1,2)))
        self.assertEqual('D5',location_to_string((3,4)))
        self.assertEqual('E2',location_to_string((4,1)))
        self.assertEqual('C3',location_to_string((2,2)))

    def test_at(self):
        self.assertEqual('M', at((0,3)))
        self.assertEqual('M', at((1,3)))
        self.assertEqual('R', at((3,1)))
        self.assertEqual('-', at((4,0)))
        self.assertEqual('-', at((4,4)))

    def test_all_locations(self):
        self.assertEqual([(0,0),(0,1),(0,2),(0,3),(0,4),
                          (1,0),(1,1),(1,2),(1,3),(1,4),
                          (2,0),(2,1),(2,2),(2,3),(2,4),
                          (3,0),(3,1),(3,2),(3,3),(3,4),
                          (4,0),(4,1),(4,2),(4,3),(4,4)], all_locations())
        
    def test_adjacent_location(self):
        self.assertEqual((0,2), adjacent_location((0,3), 'left'))
        self.assertEqual((1,3), adjacent_location((1,2), 'right'))
        self.assertEqual((1,2), adjacent_location((2,2), 'up'))
        self.assertEqual((4,1), adjacent_location((3,1), 'down'))
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((1,3), 'left'))
        self.assertTrue(is_legal_move_by_musketeer((2,2), 'left'))
        self.assertTrue(is_legal_move_by_musketeer((2,2), 'right'))
        self.assertFalse(is_legal_move_by_musketeer((0,3), 'left'))
        self.assertFalse(is_legal_move_by_musketeer((1,3), 'right'))
        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((1,2), 'left'))
        self.assertTrue(is_legal_move_by_enemy((2,1), 'left'))
        self.assertTrue(is_legal_move_by_enemy((4,3), 'up'))
        self.assertFalse(is_legal_move_by_enemy((1,2), 'right'))
        self.assertFalse(is_legal_move_by_enemy((2,1), 'down'))

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((1,2), 'left'))
        self.assertTrue(is_legal_move((2,2), 'left'))
        self.assertTrue(is_legal_move((1,3), 'left'))
        self.assertFalse(is_legal_move((0,3), 'left'))
        self.assertFalse(is_legal_move((2,1), 'down'))

    def test_can_move_piece_at(self):
        self.assertTrue(can_move_piece_at((1,3)))
        self.assertTrue(can_move_piece_at((1,2)))
        self.assertTrue(can_move_piece_at((3,1)))
        self.assertFalse(can_move_piece_at((0,3)))
        self.assertFalse(can_move_piece_at((4,1)))

    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))

        set_board([ [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [M, M, _, _, _],
                    [R, M, _, _, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('R'))
        self.assertTrue(has_some_legal_move_somewhere('M'))

    def test_possible_moves_from(self):
        self.assertEqual([],possible_moves_from((0,0)))
        self.assertEqual(['left', 'up'],possible_moves_from((1,2)))
        self.assertEqual(['left', 'right', 'up'],possible_moves_from((2,2)))
        self.assertEqual(['left', 'right', 'down'],possible_moves_from((3,1)))
        self.assertEqual(['left', 'down'],possible_moves_from((1,3)))

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((2,2)))
        self.assertTrue(can_move_piece_at((0,3)))
        self.assertTrue(can_move_piece_at((1,4)))
        self.assertFalse(can_move_piece_at((0,4)))
        self.assertFalse(can_move_piece_at((1,3)))

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((2,4)))
        self.assertTrue(is_legal_location((1,3)))
        self.assertTrue(is_legal_location((2,1)))
        self.assertFalse(is_legal_location((-1,4)))
        self.assertFalse(is_legal_location((2,5)))
        self.assertFalse(is_legal_location((5,0)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((2,4), 'down'))
        self.assertTrue(is_within_board((1,2), 'up'))
        self.assertTrue(is_within_board((0,0), 'right'))
        self.assertFalse(is_within_board((1,4), 'right'))
        self.assertFalse(is_within_board((4,2), 'down'))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual([((0,2), 'left'),((0,2), 'down')], all_possible_moves_for('R'))
        self.assertEqual([((0,3), 'left'),((0,3), 'right'), ((1,4), 'up')], all_possible_moves_for('M'))

    def test_make_move(self):
        make_move((0,3),'left')
        self.assertEqual(at((0,3)), '-')
        self.assertEqual(at((0,2)), 'M')
        make_move((4,3),'up')
        self.assertEqual(at((4,3)), '-')
        self.assertEqual(at((3,3)), 'R')
        
    def test_choose_computer_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, M, _, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [R, _, _, _, _] ] )
        # The computer chooses randomly, so each test will be different
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        self.assertTrue(choose_computer_move('R') in [((0,2),'left'), ((4,0), 'up'), ((4,0), 'right')])
        
        set_board([ [R, _, _, _, R],
                    [_, R, M, _, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [M, _, _, _, _] ] )
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])
        self.assertTrue(choose_computer_move('M') in [((1,4),'up'), ((1,2),'left'), ((1,2),'down')])

    def test_is_enemy_win(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, R, _, R],
                    [_, _, M, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, R, _, R],
                    [_, _, _, _, M],
                    [_, _, _, _, M],
                    [_, _, _, _, M],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())

unittest.main()

