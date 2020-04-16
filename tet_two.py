import pygame
import random


class SetupGame:
    """ This class will setup and handle the running of the game. """

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        # The timer is used to regulate the speed of gameplay.
        # self.gameplay_speed can be diminished to increase the speed of gameplay.
        self.time = pygame.time.get_ticks()
        self.gameplay_speed = 500

        # Defining size of application window; includes peripherals eg, score and upcoming Tetromino
        self.main_window_size = (14*self.block_size, 19*self.block_size)
        self.main_window = pygame.display.set_mode(self.main_window_size)

        # Creating surfaces for gameplay and the display window for the next Tetromino.
        # todo - create these surfaces

        # The block size is the size of each individual block of the Tetromino
        self.block_size = 40

        # Defining colours used for the background of the games windows
        self.bg_colours = {"off_white": (240, 240, 240),
                           "light_grey": (192, 192, 192),
                           "dark_grey": (10, 10, 10)}
        # Defining colours - { "colour": ((dark), (light)) }
        self.colours = {"blue": ((40, 63, 128), (156, 182, 255)),
                        "purple": ((77, 48, 128), (202, 171, 255)),
                        "pink": ((128, 29, 93), (255, 135, 213)),
                        "orange": ((204, 65, 18), (255, 138, 99)),
                        "grey": ((10, 10, 10), (192, 192, 192))}

        # Attributes to hold the appropriate Tetromino
        self.current_tet = None
        self.next_tet = None
        # A group to hold all the blocks once they become static
        # -- After the Tetromino is stationary the Blocks will be removed and the Tetromino will be discarded.
        self.static_blocks = pygame.sprite.Group()
        # A group to hold any sprite that has been discarded (blocks, tetrominoes, hitboxes).
        # -- Anything in this group will be deleted during each iteration of the loop.
        self.discarded_sprites = pygame.sprite.Group()

        # An integer attribute to hold the points for the current game
        # A list attribute to control the increasing difficulty of the game
        # -- Integers will be used as the self.gameplay_speed attribute.
        # todo - think through the logistics of points and increasing difficulty
        points = 0
        difficulty = [500, 450, 400, 350, 300, 250, 200, 150, 50]

        def loop():
            return

        def gameplay():
            return

        def event_handling():
            return

        def gravity():
            return


class XHitbox(pygame.sprite.Sprite):
    """ Used for X-Axis collision detection. """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 20))
        self.image.fill((152, 251, 152))
        self.rect = self.image.get_rect()

        self.set_x(x)
        self.set_y(y)

    def draw(self):
        return

    def set_x(self, x):
        return

    def set_y(self, y):
        return


class YHitbox(XHitbox):
    """ Used for Y-Axis collision detection. """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((20, 60))


class Block(pygame.sprite.Sprite):

    def __init__(self, colour, identification):
        pygame.sprite.Sprite.__init__(self)
        # self.ID used to identify blocks when they're being drawn.
        self.ID = identification

        # Block is (39, 39) so that there is a 2px gap between each block.
        self.image = pygame.Surface((39, 39))
        # self.center is filled with a different colour to self image to create a border.
        self.center = pygame.Surface((35, 35))
        self.rect = self.image.get_rect()
        # Unpacking the colour tuple and filling the two surfaces.
        self.dark, self.light = colour
        self.image.fill(self.dark)
        self.center.fill(self.light)

        # Create the hitboxes.
        # -- Adjusted X and Y for their initialisation, so they're in the correct position.
        self.x_hitbox = XHitbox(self.rect.x-20, self.rect.y+20)
        self.y_hitbox = YHitbox(self.rect.x+20, self.rect.y-20)

    def draw(self, surface, x_and_y=None):
        """ Draws the block on the given surface and at the given co-ordinates.
            --- If the x_and_y argument is None, the block is no longer part of a Tetromino,
                and should be drawn at the co-ordinates it currently occupies. """

        # todo - maybe the parameter, when this method is called, should be surface.blit

        if x_and_y is None:
            # Drawing the center surface onto the image surface to create the border.
            self.image.blit(self.center, (2, 2))
            # Now draw the whole image to the given surface.
            surface.blit(self.image, self.rect)
        else:
            self.image.blit(self.center, (2, 2))
            surface.blit(self.image, x_and_y)

    def move_down(self):
        return

    def get_x(self) -> int:
        # todo - do division to return gameplay grid co-ordinate.
        return self.rect.x

    def get_y(self) -> int:
        # todo - do division to return gameplay grid co-ordinate.
        return self.rect.y

    def set_x(self):
        # todo - Add multiplication to convert to real co-ordinate.
        return

    def set_y(self):
        # todo - Add multiplication to convert to real co-ordinate.
        return

    def get_block_id(self):
        return self.ID


class Tetromino(pygame.sprite.Sprite):

    def __init__(self, block_size, colours):
        pygame.sprite.Sprite.__init__(self)
        self.block_size = block_size

        # Surface is (160, 160) because the shape templates are that big.
        self.image = pygame.Surface((160, 160))
        self.rect = self.image.get_rect()

        # Pick a random colour for the Tetromino
        self.colour = random.choice(list(colours.keys()))

        # Integer to hold current rotation of Tetromino.
        self.current_rotation = 0

        # Group to hold the blocks with make up the Tetromino
        self.blocks = pygame.sprite.Group()

        # Randomly assign the shape of the Tetromino.
        self.shape = random.choice(["L", "J", "I", "T", "S", "Z", "O"])

        # Dictionary containing Tetromino shapes, and their rotations.
        self.shape_dictionary = {"L": [["-----",
                                        "-B---",
                                        "-B---",
                                        "-BB--",
                                        "-----"],
                                       ["-----",
                                        "BBB--",
                                        "B----",
                                        "-----",
                                        "-----"],
                                       ["-----",
                                        "-BB--",
                                        "--B--",
                                        "--B--",
                                        "-----"],
                                       ["-----",
                                        "---B-",
                                        "-BBB-",
                                        "-----",
                                        "-----"]],
                                 "J": [["-----",
                                        "---B-",
                                        "---B-",
                                        "--BB-",
                                        "-----"],
                                       ["-----",
                                        "-----",
                                        "B----",
                                        "BBB--",
                                        "-----"],
                                       ["-----",
                                        "-BB--",
                                        "-B---",
                                        "-B---",
                                        "-----"],
                                       ["-----",
                                        "-----",
                                        "-BBB-",
                                        "---B-",
                                        "-----"]],
                                 "I": [["-----",
                                        "--B--",
                                        "--B--",
                                        "--B--",
                                        "--B--"],
                                       ["-----",
                                        "-----",
                                        "-----",
                                        "-BBBB",
                                        "-----"]],
                                 "T": [["-----",
                                        "-BBB-",
                                        "--B--",
                                        "-----",
                                        "-----"],
                                       ["-----",
                                        "--B--",
                                        "-BB--",
                                        "--B--",
                                        "-----"],
                                       ["-----",
                                        "--B--",
                                        "-BBB-",
                                        "-----",
                                        "-----"],
                                       ["-----",
                                        "--B--",
                                        "--BB-",
                                        "--B--",
                                        "-----"]],
                                 "S": [["-----",
                                        "--BB-",
                                        "-BB--",
                                        "-----",
                                        "-----"],
                                       ["-B---",
                                        "-BB-",
                                        "--B--",
                                        "-----",
                                        "-----"]],
                                 "Z": [["-----",
                                        "-BB--",
                                        "--BB-",
                                        "-----",
                                        "-----"],
                                       ["---B-",
                                        "--BB-",
                                        "--B--",
                                        "-----",
                                        "-----"]],
                                 "O": [["-----",
                                        "-BB--",
                                        "-BB--",
                                        "-----",
                                        "-----"]]
                                 }

        # Create the blocks
        self.create_blocks()

    def create_blocks(self):
        """ Creates a block and give it an ID. """
        for i in range(4):
            new_block = Block(self.colour, i)
            self.blocks.add(new_block)

    def collision_detection(self):
        return

    def rotate(self):
        """ Increases and resets the current_rotation integer accordingly. """
        if self.create_blocks() == len(self.shape_dictionary.get(self.shape)) - 1:
            self.current_rotation = 0
        else:
            self.current_rotation += 1

    def move_left(self):
        """ Moves the Tetromino to the left on the grid. """
        self.rect.x -= 1 * self.block_size

    def move_right(self):
        """ Moves the Tetromino to the right ont the grid. """
        self.rect.x += 1 * self.block_size

    def move_down(self, movement_amount):
        """ Moves the Tetromino down the grid. """
        # todo - try using the argument to speed up the descent
        self.rect.y += movement_amount * self.block_size

    def draw(self, surface):
        """ Calculates the where to draw each block, and then calls the blocks own draw() method. """

        # i will be iterated, and will draw the correct block according to each block's ID.
        i = 0
        x, y = self.get_x(), self.get_y()

        for string in self.shape_dictionary.get(self.shape)[self.current_rotation]:
            for char in string:
                if char == '-':
                    x += self.block_size
                elif char == 'B':
                    for block in self.blocks:
                        if i == block.get_block_id():
                            block.draw(surface, (x, y))
                    i += 1
            y += self.block_size

    def set_x(self, x):
        """ Sets the X co-ordinate of the Tetromino. """
        # todo - Add multiplication to convert to real co-ordinate.
        self.rect.x = x

    def set_y(self, y):
        """ Sets the Y co-ordinate of the Tetromino. """
        # todo - Add multiplication to convert to real co-ordinate.
        self.rect.y = y

    def get_x(self) -> int:
        """ Returns the X co-ordinate. """
        # todo - Add the division so that the return Int relates to the gameplay grid.
        return self.rect.x

    def get_y(self) -> int:
        """ Returns the Y co-ordinate. """
        # todo - Add the division so that the return Int relates to the gameplay grid.
        return self.rect.y


if __name__ == "__main__":
    pass
