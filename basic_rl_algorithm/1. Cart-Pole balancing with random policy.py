# let's create our Cart-Pole environment:
import gym
env = gym.make('CartPole-v0')

#Set the number of episodes and number of time steps in the episode
num_episodes = 100
num_timesteps = 50

#For each episodes
for i in range(num_episodes):	
	#set the return to zero
	Return = 0
	#initialize the state by resetting the environment"
	state = env.reset()
	#For each step in the episode
	for t in range(num_timesteps):
		#Render the environment
		env.render()
		#Randomly select an action by sampling from the environment
		random_action = env.action_space.sample()
		#Perform the randomly selected action:
		next_state, reward, done, info=env.step(random_action)
		#Update the return
		Return = Return + reward
		#If the next state is a terminal state then end the episode:
		if done:
			break
	#For every 10 episodes, print the return(sum of rewards):
	if i%10==0:
		print('Episode: {}, Return: {}'. format(i, Return))

	#Close the envronment:
	env.close
