from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self): #객체의 상호작용, 행위
        pass
    def draw(self):
        self.image.draw(400,30)
        pass

class boy:
    def __init__(self):
        self.x = random.randint(100,400)
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.x += 5
        self.frame = (self.frame +1) % 8
        pass
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,90)
        pass

class Zombie:
    def __init__(self):
        self.x, self.y = 0, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')
        pass
    def update(self):
        self.x += 4
        self.frame = (self.frame +1) % 10
        pass
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width,0,frame_width,frame_height, self.x, self.y, frame_width // 2, frame_height // 2)
        pass

class Ball:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = 599
        self.speed = random.randint(5,10)
        if random.randint(0,1) == 0:
            self.image = load_image('ball21x21.png')
            self.r = 21
        else:
            self.image = load_image('ball41x41.png')
            self.r = 41
        pass
    def update(self):
        if self.y > self.r //2 + 50:
            self.y -= self.speed
        pass
    def draw(self):
        self.image.draw(self.x,self.y)
        pass
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()



def reset_world():
    #객체들을 생성
    global running
    running = True

    global world # 모든 객체를 포함하는 변수

    world = []

    grass = Grass()
    world.append(grass)

    team = [boy() for i in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    ball = [Ball() for i in range(20)]
    world += ball

reset_world()

def update_world():
    for game_object in world:
        game_object.update()

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()
    pass


while running:
    handle_events()
    update_world() #객체들의 상호작용을 시뮬레이션, 계산
    render_world()
    delay(0.05)



close_canvas()