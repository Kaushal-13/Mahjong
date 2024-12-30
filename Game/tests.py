# For now this file contains the basic checks to make sure if the game functionality works fine or not.
from tiles import Game, Tile, GameState


gs = GameState()
gs.generatePlayers()
assert (len(gs.tiles) == 83)

assert (Tile("D", 9).unicode() == chr(0x1F021))

game = Game()
game.fullLoop()
