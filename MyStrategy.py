from model.action import Action
from model.game import Game
from model.robot import Robot
from model.rules import Rules

ROBOT_MIN_RADIUS = 1
ROBOT_MAX_RADIUS = 1.05
ROBOT_MAX_JUMP_SPEED = 15
ROBOT_ACCELERATION = 100
ROBOT_NITRO_ACCELERATION = 30
ROBOT_MAX_GROUND_SPEED = 30
ROBOT_ARENA_E = 0
ROBOT_RADIUS = 1
ROBOT_MASS = 2
TICKS_PER_SECOND = 60
MICROTICKS_PER_TICK = 100
RESET_TICKS = 2 * TICKS_PER_SECOND
BALL_ARENA_E = 0.7
BALL_RADIUS = 2
BALL_MASS = 1
MIN_HIT_E = 0.4
MAX_HIT_E = 0.5
MAX_ENTITY_SPEED = 100
MAX_NITRO_AMOUNT = 100
START_NITRO_AMOUNT = 50
NITRO_POINT_VELOCITY_CHANGE = 0.6
NITRO_PACK_X = 20
NITRO_PACK_Y = 1
NITRO_PACK_Z = 30
NITRO_PACK_RADIUS = 0.5
NITRO_PACK_AMOUNT = 100
NITRO_PACK_RESPAWN_TICKS = 10 * TICKS_PER_SECOND
GRAVITY = 30

class MyStrategy:
    def act(self, me, rules, game, action):
    	dist_to_ball = ((me.x - game.ball.x)**2 + (me.y - game.ball.y)**2 + (me.z - game.ball.z)**2)**0.5

    	jump = dist_to_ball < BALL_RADIUS + ROBOT_MAX_RADIUS and me.z < game.ball.z

    	if me.id == 1:
        	for i in range(1,101):
        		t = i * 0.1
        		ball_x = game.ball.x
        		ball_z = game.ball.z
        		ball_velocity_x = game.ball.velocity_x
        		ball_velocity_z = game.ball.velocity_z
       			
       			pos_x = ball_x + ball_velocity_x * t
       			pos_z = ball_z + ball_velocity_z * t

       			speed_x = (pos_x - me.x)/t
       			speed_z = (pos_z - me.z)/t

       			speed = (speed_x**2 + speed_z**2)**0.5

       			if 0.5 * ROBOT_MAX_GROUND_SPEED < speed and speed < ROBOT_MAX_GROUND_SPEED:
       				action.target_velocity_x = speed_x
       				action.target_velocity_z = speed_z
       				action.jump_speed = ROBOT_MAX_JUMP_SPEED if jump else 0.0

    	
    	elif me.id == 2:
    		for i in range(1,101):
        		t = i * 0.1
        		ball_x = game.ball.x
        		
        		ball_velocity_x = game.ball.velocity_x
        		
       			
       			pos_x = ball_x + ball_velocity_x * t
       			pos_z = -40

       			speed_x = (pos_x - me.x)/t
       			speed_z = (pos_z - me.z)/t

       			speed = (speed_x**2 + speed_z**2)**0.5

       			if 0.5 * ROBOT_MAX_GROUND_SPEED < speed and speed < ROBOT_MAX_GROUND_SPEED:
       				action.target_velocity_x = speed_x
       				action.target_velocity_z = speed_z
       				action.jump_speed = ROBOT_MAX_JUMP_SPEED if jump else 0.0
