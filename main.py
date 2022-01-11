import turtle
import time
import random
import winsound

player_dx = 15

def move_left():
    x = player.xcor() - player_dx
    if x < -190:
        x = -190
    player.setx(x)

def move_right():
    x = player.xcor() + player_dx
    if x > 190:
        x = 190
    player.setx(x)

def fire_bullet():
    winsound.PlaySound('sounds/laser_sound.wav', winsound.SND_ASYNC)
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y + 30)
    bullet.showturtle()

# set up window
wn = turtle.Screen()
wn.setup(width=540, height=540)
wn.bgcolor('black')
wn.title("Space Invader")

# register shapes
turtle.register_shape('images/alien.gif')
turtle.register_shape('images/rocket.gif')

# Draw border, 400x400 square
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.up()
border.setposition(-200, -200)
border.down()
border.pensize(3)
for side in range(4):
    border.fd(400)
    border.lt(90)
border.hideturtle()

# Score
score = 0

# Draw score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.up()
score_pen.setposition(-200, 210)
score_pen.write('Score: %s' % score)
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.shape('images/rocket.gif')
player.up()
player.speed(0)
player.setposition(0, -180)
player.setheading(90)

# Create player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# create invader turtle
invader = turtle.Turtle()
invader.shape('images/alien.gif')
invader.up()
invader.speed(0)
invader.setposition(-180, 180)

# Create keyboard binding
turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(fire_bullet, 'space')

invader_speed = 2
bullet_speed = 10
while True:
    invader.fd(invader_speed)

    # check border
    if invader.xcor() > 190 or invader.xcor() < -190:
        invader.right(180)
        invader.fd(invader_speed)

        # fire the bullet
    bullet.fd(bullet_speed)

    # check for collision
    if abs(bullet.xcor() - invader.xcor()) < 15 and \
            abs(bullet.ycor() - invader.ycor()) < 15:
        # Sound
        winsound.PlaySound('sounds/explosion_sound.wav', winsound.SND_ASYNC)

        # update the score
        score = score + 1
        score_pen.clear()
        score_pen.write('Score: %s' % score)

        # reset invader and player
        bullet.hideturtle()
        invader.hideturtle()
        time.sleep(2)

        invader.showturtle()
        x = random.randint(-180, 180)
        invader.setposition(x, 180)

        player.setposition(0, -180)