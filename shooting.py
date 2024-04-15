import random

# Define target and bullet classes (simplified)
class Target:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def is_hit(self, bullet_x, bullet_y):
        return abs(self.x - bullet_x) <= self.size // 2 and abs(self.y - bullet_y) <= self.size // 2

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction  # Up, down, left, right

# Function to handle user input for adjusting aim
def get_user_aim():
    while True:
        direction = input("Enter direction (e,w,n,s) or 'fire': ")
        if direction in ("e", "w", "n", "s", "fire"):
            return direction
        else:
            print("Invalid direction. Try again.")

# Main game loop
def main():
    # Set up target and player position
    target = Target(random.randint(50, 100), random.randint(50, 100), 20)
    player_x = 50
    player_y = 50

    while True:
        # Display game state (text-based)
        print(f"Player at ({player_x}, {player_y})")
        print(f"Target at ({target.x}, {target.y})")

        # Get user input
        direction = get_user_aim()

        if direction == "fire":
            # Simulate bullet movement (simple example)
            bullet = Bullet(player_x, player_y, direction)
            if direction == "e":
                bullet.y -= 5
            elif direction == "w":
                bullet.y += 5
            elif direction == "n":
                bullet.x -= 5
            elif direction == "s":
                bullet.x += 5

            # Check if bullet hits target
            if target.is_hit(bullet.x, bullet.y):
                print("Hit!")
                break
            else:
                print("Miss!")
        else:
            # Adjust player aim based on direction
            if direction == "e":
                player_y -= 2
            elif direction == "w":
                player_y += 2
            elif direction == "n":
                player_x -= 2
            elif direction == "s":
                player_x += 2

            # Prevent going off-screen
            player_x = max(0, min(player_x, 100))
            player_y = max(0, min(player_y, 100))

    print("Game Over!")

if __name__ == "__main__":
    main()
