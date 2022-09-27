import pygame
from sys import exit
from random import randint, choice


# LEVEL -------------------------------------------------------------------------------------------------

class Level:
    def __init__(self):
        # Surfaces
        self.sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
        self.ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

        
        self.ground_height = 300

        self.player_x_position = 200
        self.player_spawn_position = (self.player_x_position,self.ground_height)

        self.obstacle_x_position = randint(900, 1200)
        
        # Background music
        self.background_music = pygame.mixer.Sound("audio/music.wav")
        self.background_music.set_volume(0.2)


# PLAYER -----------------------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.level = Level()

        # All surfaces
        self.jump_surface = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        walk_1_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        walk_2_surface = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()

        # Walking animation
        self.frames = [walk_1_surface, walk_2_surface]
        self.frame_index = 0

        # Sprite
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom = self.level.player_spawn_position)

        # Sound
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.2)

        # Variables
        self.gravity = 0
        self.score = 0


    def is_jumping(self):
        # if player is above the ground
        return self.rect.bottom < self.level.ground_height


    def jump(self):
        self.gravity = -20
        self.jump_sound.play()

    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.is_jumping():
            self.jump()


    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if not self.is_jumping():
            self.rect.bottom = self.level.ground_height

    
    def animation_state(self):
        # Jump animation
        if self.is_jumping():
            self.image = self.jump_surface
        # Walking animation
        else:
            self.frame_index += 0.1

            if int(self.frame_index) >= len(self.frames):
                self.frame_index = 0

            self.image = self.frames[int(self.frame_index)]


    def update(self):
        self.get_input()
        self.apply_gravity()
        self.animation_state()


# OBSTACLE ---------------------------------------------------------------------------------------------

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        self.level = Level()

        if type == 'snail':
            # Snail surfaces
            surface_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            surface_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            # Snail variables
            self.y_position = self.level.ground_height
            self.velocity = 6

        elif type == 'fly':
            # Fly surfaces
            surface_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            surface_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            # Fly variables
            self.y_position = self.level.ground_height - 90
            self.velocity = randint(10, 15)
        
        # Animation
        self.frames = [surface_1, surface_2]
        self.frame_index = 0
        
        # Sprite
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom = (self.level.obstacle_x_position, self.y_position))


    def move(self):
        self.rect.x -= self.velocity


    def destroy(self):
        # if the obstacle is not visible on the screen, delete it
        if self.rect.right <= 0:
            self.kill()


    def animation_state(self):
        # Walking animation
        self.frame_index += 0.1

        if int(self.frame_index) >= len(self.frames):
            self.frame_index = 0
        
        self.image = self.frames[int(self.frame_index)]


    def update(self):
        self.animation_state()
        self.move()
        self.destroy()


# GAME CLASS -------------------------------------------------------------------------------------------

class PixelRunner:
    def __init__(self):
        # Game window setup
        pygame.init()

        WIDTH = 800
        HEIGHT = 400
        TITLE = "Pixel Runner 1.0"
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        # Text
        self.text_font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.big_text_font = pygame.font.Font("font/Pixeltype.ttf", 70)

        self.game_name_surface = self.big_text_font.render("Pixel  Runner", False, (111, 196, 169))
        self.game_name_rect = self.game_name_surface.get_rect(center=(400, 80))

        self.game_over_msg_surface = self.big_text_font.render("You  died!", False, (180, 64, 64))
        self.game_over_msg_rect = self.game_over_msg_surface.get_rect(center=(400, 80))

        self.start_game_surface = self.text_font.render("Press  [SPACE]  to  run", False, (111,196,169))
        self.start_game_rect = self.start_game_surface.get_rect(center=(400, 320))

        # Images
        self.game_image_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        self.game_image_rect = self.game_image_surface.get_rect(center=(400,200))

        # Game objects
        self.level = Level()
        self.level.background_music.play()

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())

        self.obstacle_group = pygame.sprite.Group()

        # User events
        self.obstacle_spawn_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_spawn_timer, 1500)

        # Game varibles
        self.game_active = False
        self.start_time = 0
        self.gameplay_time = 0
    

    @staticmethod
    def quit():
        pygame.quit()
        exit()


    def spawn_obstacle(self):
        # Add a new Obstacle to the sprite obstacle sprite group 
        self.obstacle_group.add(Obstacle(choice(["snail", "snail", "fly"])))


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if self.game_active:
                if event.type == self.obstacle_spawn_timer:
                    self.spawn_obstacle()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.start_game()


    def check_sprite_collision(self):
        # Check if the player sprite collided in any Obstcale of the obstacle group
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False): return True
        else: return False


    def update_game_state(self):
        if self.check_sprite_collision():
            self.game_active = False
        else:
            self.game_active = True


    def start_game(self):
        # Delete all Obstacles of the obstacle sprite group
        self.obstacle_group.empty()
        # Place player on the ground
        self.player.sprite.rect.bottom = self.level.ground_height

        self.game_active = True
        self.start_time = int(pygame.time.get_ticks() / 100)

    
    def update_player_score(self):
        self.gameplay_time = int(pygame.time.get_ticks() / 100)
        print(self.start_time, self.gameplay_time)
        self.player.sprite.score = self.gameplay_time - self.start_time


    def display_score(self):
        score_surface = self.text_font.render(str(self.player.sprite.score), False, (64,64,64))
        score_rect = score_surface.get_rect(center = (400,60))
        self.screen.blit(score_surface, score_rect)


    def display_final_score(self):
        score_surface = self.text_font.render(f"Score: {self.player.sprite.score}", False, (64,64,64))
        score_rect = score_surface.get_rect(center = (400,320))
        self.screen.blit(score_surface, score_rect)


    def display_game_over(self):
        self.screen.blit(self.game_over_msg_surface, self.game_over_msg_rect)
        self.display_final_score()


    def display_game_intro(self):
        self.screen.blit(self.game_name_surface, self.game_name_rect)
        self.screen.blit(self.start_game_surface, self.start_game_rect)


    def run(self):
        while True:
            # Track events
            self.event_loop()

            if self.game_active:
                # Background 
                self.screen.blit(self.level.sky_surface, (0,0))
                self.screen.blit(self.level.ground_surface, (0,300))

                # Score
                self.update_player_score()
                self.display_score()

                # Player
                self.player.draw(self.screen)
                self.player.update()


                # Obstacles
                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()

                self.update_game_state()

            else:
                self.screen.fill((94, 129, 162))
                self.screen.blit(self.game_image_surface, self.game_image_rect)

                if self.player.sprite.score == 0:
                    self.display_game_intro()

                else:
                    self.display_game_over()


            # Update game window
            pygame.display.update()
            self.clock.tick(60)

# ------------------------------------------------------------------------------------------------------

game = PixelRunner()

if __name__ == "__main__":
    game.run()