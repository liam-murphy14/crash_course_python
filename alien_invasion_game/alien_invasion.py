"""Module to manage the whole alien invasion game"""

# stdlib modules
import sys 
from time import sleep

# downloaded modules
import pygame 

# my modules
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall game asset and behavior management class"""

    def __init__(self):
        """Initialize the game, and create resources"""
        pygame.init()
        
        # settings object
        self.settings = Settings()
        # screen object
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # gamestats object
        self.stats = GameStats(self)
        # ship object
        self.ship = Ship(self)
        # container for bullets
        self.bullets = pygame.sprite.Group()
        # container for aliens
        self.aliens = pygame.sprite.Group()
        # scoreeeeeeboaaaarrrddd
        self.sb = Scoreboard(self)

        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Listen for key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start new game when the player presses play"""
        clicked = self.play_button.rect.collidepoint(mouse_pos)
        if clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True 
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _handle_keydown_event(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_d:
            # set right moving flag to true
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            # set left moving flag to true
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            # fires a bullet
            self._fire_bullet()
        elif event.key == pygame.K_q:
            # quit the game
            sys.exit()

    def _handle_keyup_event(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_d:
            # set right moving flag to false
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            # set left moving flag to false
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create and fire new bullet"""
        if len(self.bullets) < self.settings.number_bullets_allowed:
            new_bul = Bullet(self)
            self.bullets.add(new_bul)

    def _update_bullets(self):
        """Handle bullet updating"""
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self._check_collisions()

    def _check_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Create alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        ship_height = self.ship.rect.height 
        available_space_x = self.settings.screen_width - (alien_width * 2)
        available_space_y = self.settings.screen_height - ((3 * alien_height) + ship_height)
        num_aliens = available_space_x // (alien_width * 2)
        num_rows = available_space_y // (2 * alien_height)
        for row_num in range(num_rows): 
            for num in range(num_aliens):
                self._make_alien(num, row_num)

    def _make_alien(self, num, row_num):
        """Create an alien instance for a row and collumn"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * num)
        alien.rect.x = alien.x 
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_num)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond if aliens reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        """Drop entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty() 
            self._create_fleet()
            self.ship.center_ship()
            self.sb.prep_ships()
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == "__main__":
    # Make instance and run
    ai = AlienInvasion()
    ai.run_game()