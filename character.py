class Character:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.speed = 133

    def walk(self, direction, time_passed_seconds):
        if direction == "left":
            self.x -= self.speed * time_passed_seconds

        if direction == "right":
            self.x += self.speed * time_passed_seconds

        if direction == "up":
            self.y -= self.speed * time_passed_seconds

        if direction == "down":
            self.y += self.speed * time_passed_seconds
    
    def position(self):
        return (int(self.x / 32) * 32, int(self.y / 32) * 32)
