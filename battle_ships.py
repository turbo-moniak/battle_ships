from game import Game
from game_operations import start_game, sink_ships
from ship import coordinates_mapping


game = Game()
start_game(game)
sink_ships(game, coordinates_mapping)
