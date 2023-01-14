import pygame

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        pygame.init()
        self.offset = board.properties["offset"]
        self.win_size = [board.size[0] + self.offset[0]*1.3, board.size[1] + self.offset[1]]
        self.screen = pygame.display.set_mode(self.win_size)
        self.clock = pygame.time.Clock()

        for player in self.players:
            player.set_avatar("madeline")
    
    def run(self):
        continue_ = True
        # --- Get events init
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                continue_ = False
            if event.type == pygame.KEYDOWN:
                # for more info https://www.pygame.org/docs/ref/key.html
                if event.key == pygame.K_SPACE:
                    #roll dice
                    pass
            if event.type == pygame.KEYUP:
                pass
    
        # mouse_pos = pygame.mouse.get_pos()
        # --- Get events end

        # --- Draw Board init
        self.board.draw(self.screen, self.offset)
        # --- Draw Board end

        # --- Draw players init

        # Draw stats
        for player in self.players:
            player.draw(self.screen)

        
        # --- Draw players end

        # update screen
        pygame.display.flip()
        self.clock.tick(60) # Frames Per Second
        return continue_

