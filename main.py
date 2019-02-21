import pygame, random

class Game:
    def __init__(self):
        self.widht = 500
        self.height = 400
        self.screen = pygame.display.set_mode((self.widht, self.height))
        pygame.display.set_caption('SNAKE')
        pygame.font.init()
        go_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.go_surf = go_font.render('Game over', True, pygame.Color(255, 255, 255))
        self.restart = go_font.render('Press R to restart', True, pygame.Color(255, 255, 255))

    def draw_game_over(self):
        self.screen.blit(self.go_surf, (self.widht/2.8, self.height / 3))
        self.screen.blit(self.restart, (self.widht/4, self.height / 2))

    def draw(self):
        game.screen.fill((43, 43, 43))
        food.drawFood(game.screen)
        snake.drawSnake(game.screen)

        if game_over:
            game.draw_game_over()

        pygame.display.flip()


class Food:
    def __init__(self):
        self.FoodColor = pygame.Color(255, 0, 0)
        self.Update()

    def Update(self):
        self.Food_x = random.randint(0, 490 / 10) * 10
        self.Food_y = random.randint(0, 390 / 10) * 10

    def drawFood(self, screen):
        pygame.draw.rect(screen, self.FoodColor, pygame.Rect(self.Food_x, self.Food_y, 10, 10))


class Snake:
    def __init__(self):
        self.SnakeColor = pygame.Color(255, 255, 255)
        self.reset()

    def updateSnake(self):
        if self.Snake_direction == 'LEFT': self.Snake_x -= 10
        if self.Snake_direction == 'RIGHT': self.Snake_x += 10
        if self.Snake_direction == 'DOWN': self.Snake_y += 10
        if self.Snake_direction == 'UP': self.Snake_y -= 10

        self.count_block_coord.insert(0, [self.Snake_x, self.Snake_y])
        self.count_block_coord.pop()

    def drawSnake(self, screen):
        for i in self.count_block_coord:
            pygame.draw.rect(screen, self.SnakeColor, pygame.Rect(i[0], i[1], 10, 10))

    def change_direction(self, direction):
        if (direction == 'RIGHT' and self.Snake_direction != 'LEFT') or (
                direction == 'LEFT' and self.Snake_direction != 'RIGHT') or (
                direction == 'UP' and self.Snake_direction != 'DOWN') or (
                direction == 'DOWN' and self.Snake_direction != 'UP'):

            self.Snake_direction = direction

    def add_block(self):
        index = len(self.count_block_coord) - 1
        self.count_block_coord.insert(index, self.count_block_coord[index])

    def reset(self):
        self.Snake_x = 150
        self.Snake_y = 200
        self.count_block_coord = [[self.Snake_x, self.Snake_y + (10 * i)] for i in range(5)]
        self.Snake_direction = "UP"


if __name__ == '__main__':
    game = Game()
    snake = Snake()
    food = Food()

    game_over = False
    app_running = True

    while app_running:

        print('....')

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                app_running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                    break

                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                    break

                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                    break

                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                    break

                elif event.key == pygame.K_r and game_over:
                    game_over = False
                    snake.reset()
                    food.Update()

        if not game_over:
            snake.updateSnake()

        # eat snake
        if snake.Snake_x == food.Food_x and snake.Snake_y == food.Food_y:
            food.Update()
            snake.add_block()


        # game over
        if (snake.Snake_x >= game.widht or snake.Snake_x < 0) or (
                snake.Snake_y >= game.height or snake.Snake_y < 0):
            game_over = True

        for i in snake.count_block_coord[1:]:
            if snake.count_block_coord[0] == i:
                game_over = True

        game.draw()


        pygame.time.delay(300)
