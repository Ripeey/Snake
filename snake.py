import tkinter
import random

class game:
	def __init__(self):
		self.engine = tkinter.Tk()
		self.engine.title("Snake")
		self.world_width=800
		self.world_height=500
		self.world = tkinter.Canvas(self.engine, bg="black",bd=0, width=self.world_width, height=self.world_height, highlightthickness=7, highlightbackground="red")
		self.score=0
		self.stat = self.world.create_text(self.world_width/2,20,text="Score : 0",fill="white",font="Times 15 bold")
		self.step=10 # distance
		x,y,r=50,50,10
		self.food=self.world.create_oval(x, y, x+r, y+r, fill="deeppink")
		x,y,r=100,100,10
		self.snake=[]
		self.create_snake(x,y,r,20)
		self.heading='d'
	def create_snake(self,x,y,r,steroid=10):
		for i in range(steroid):
			self.snake.append(self.world.create_rectangle(x+(r*i), y, x+(r*i)+r, y+r, fill="green"))
	def spawn_food(self,r=10):
		x,y=random.randint(1,self.world_width/10)*10,random.randint(1,self.world_height/10)*10
		self.world.coords(self.food, x, y, x+r, y+r)
	def move_snake(self):
		if self.check_obstacle():
			tail=self.snake[0]
			head=self.world.coords(self.snake[len(self.snake)-1])
			if self.heading == 'w':
				self.world.coords(tail, head[0], head[1]-self.step, head[2], head[3]-self.step)
			elif self.heading == 'a':
				self.world.coords(tail, head[0]-self.step, head[1], head[2]-self.step, head[3])
			elif self.heading == 's':
				self.world.coords(tail, head[0], head[1]+self.step, head[2], head[3]+self.step)
			elif self.heading == 'd':
				self.world.coords(tail, head[0]+self.step, head[1], head[2]+self.step, head[3])
			else:
				pass
			
			self.snake.append(self.snake.pop(0))
			self.world.update()
			self.engine.after(70,self.move_snake)
		else:
			pass
		print(self.heading)
		print(self.world.coords(self.snake[len(self.snake)-1]))
		#endgame
	def check_obstacle(self):
		head_loc=self.world.coords(self.snake[len(self.snake)-1])
		tail_loc=self.world.coords(self.snake[0])
		food_loc=self.world.coords(self.food)
		if head_loc == food_loc:
			print("found food")
			self.snake.insert(0,self.world.create_rectangle(tail_loc[0],tail_loc[1],tail_loc[2],tail_loc[3], fill="green"))
			self.spawn_food()
			self.update_score()
			self.world.update()
		elif head_loc[0]>self.world_width-self.step or head_loc[1] > self.world_height-self.step or head_loc[0] < self.step or head_loc[1] < self.step:
			print("hit border")
			self.update_score(False)
			return False
		else:
			for piece in range(len(self.snake)-1):
				if head_loc == self.world.coords(self.snake[piece]):
					print("eat self")
					self.update_score(False)
					return False
				else:
					continue
		return True
	def key_press(self, _):
		if _.char in ('w','a','s','d') and (_.char not in ('w','s') or self.heading not in ('w','s')) and  (_.char not in ('a','d') or self.heading not in ('a','d')):
			self.heading = _.char
		else:
			pass
	def update_score(self,bonus=1):
		if not bonus:
			self.world.itemconfig(self.stat, text="Gamw Over, Score : {}".format(self.score))
		else:
			self.score+=bonus
			self.world.itemconfig(self.stat, text="Score : {}".format(self.score))
	def run(self):
		self.engine.bind('<Key>', self.key_press)
		self.world.pack()
		self.engine.after('1000',self.move_snake)
		self.engine.mainloop()

ob=game()
ob.run()