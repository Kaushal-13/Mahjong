import random


class Tile:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value - 1

    def __str__(self):
        # Custom string representation
        return f"{self.value + 1} of {self.suit}"

    def unicode(self):
        dic = {
            "D": "0x1F019",
            "B": "0x1F010",
            "C": "0x1F007",
            "Dr": "0x1F004",
            "W": "0x1F000"
        }
        value = int(dic[self.suit], 16) + self.value
        # print(value)
        return chr(value)


def printHand(list):
    return ','.join(map(lambda x: x.unicode(), list))


class Player:
    # Adding Type check for player initialization here
    def __init__(self, tiles: list[Tile]):
        self.hand = tiles
        self.melds = []
        self.discards = []

    def addTile(self, tile: Tile):
        self.hand.append(tile)

    def discardTile(self, index):
        l = self.hand
        n = len(l)
        l[index], l[n-1] = l[n-1], l[index]
        discardedTile = l.pop()
        print(discardedTile)
        print(discardedTile.unicode())
        self.hand = l
        self.discards.append(discardedTile)

    def __str__(self):
        return f'Hands : {printHand(self.hand)}'


class GameState:
    def __init__(self):

        self.tiles = []
        suits = ["B", "C", "D"]
        for suit in suits:
            for i in range(1, 10):
                for _ in range(4):
                    self.tiles.append(Tile(suit, i))
        directions = [0, 1, 2, 3]  # IN THE ORDER E S W N
        for direction in directions:
            suit = "W"
            for i in range(4):
                self.tiles.append(Tile(suit, direction))

        dragons = [0, 1, 2]  # IN THE ORDER R G W

        for color in dragons:
            suit = "Dr"
            for i in range(4):
                self.tiles.append(Tile(suit, color))
        # Random seed between 1 and 1,000,000 Can be increased as well (later though)
        seed = random.randint(1, 1_000_000)
        random.seed(seed)
        self.seed = seed
        print(len(self.tiles))
        random.shuffle(self.tiles)

    def generatePlayers(self):
        self.players = []
        for i in range(4):
            self.players.append(Player(tiles=self.tiles[i*13: (i+1)*13]))

        random.shuffle(self.players)
        self.dealer = 0
        self.players[self.dealer].addTile(self.tiles[52])
        self.tiles = self.tiles[53:]
        # for player in self.players:
        #     print(player)

    def printState(self):
        for player in self.players:
            print(player)


class Game:
    def __init__(self):
        self.gameState = GameState()
        self.gameState.generatePlayers()
        self.player = 0
        self.tileIndex = 0

    def gameLoop(self):
        tile = self.gameState.tiles[self.tileIndex]
        self.gameState.players[self.player].addTile(tile)
        a = int(input("Enter index of Tile you wish to remove: "))
        assert (a < len(self.gameState.players[self.player].hand))
        self.gameState.players[self.player].discardTile(a)
        self.tileIndex += 1
        self.player = (self.player + 1) % 4

    def fullLoop(self):
        a = 0
        while (a != -1):
            self.gameLoop()
            self.gameState.printState()
            a = int(input("Put -1 to stop game 0 to go on"))
