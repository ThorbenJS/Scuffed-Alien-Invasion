


class GameStats:

    def __init__ (self, ai):
        self.settings = ai.settings
        self.score = 0
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        """Reset the game statistics"""
        self.settings.health = 500
        self.settings.movement_speed = 0.5
        self.settings.alien_speed = 0.08
        self.settings.fleet_drop_speed = 18
        self.settings.fleet_direction = 1
        self.settings.collision = False
        self.score = 0
        self.settings.alien_kill_score = 50
