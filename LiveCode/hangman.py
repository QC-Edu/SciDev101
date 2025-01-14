
from os import system
from itertools import chain

def draw_head(border):
	d1 = border+ '*'*9
	d2 = border + '*'+' '*7+'*'
	d3 = border + '*'+' '*2+'|'+' '*2+'|'+' '+'*'
	d4 = border+ '*'+' '*7+'*'
	d5 = border + '*'*9
	
	return iter([d1,d2,d3,d4,d5])

def draw_torso(size,border,flag = None):
	being = []
	print(border)
	mp = len(border)+4

	if flag==None:
		[being.append(border+' '*4 + '*'+ ' '*4) for i in range(6)]

	elif flag == 'r':
		for i in range(6):
			if i<4:
				arml = mp*' '
				armr = (4-i) * ' '+'*'
			else:
				arml, armr='', ''
			string = '*'
			
			being.append(arml+' ' *(mp-len(arml))+ string + armr)

	elif flag == 'l':
		for i in range(6):
			if i<4:
				arml = (len(border)-1 +i) * ' '+'*'
				armr = ' '
			else:
				arml, armr='', ''
			string = '*'
			
			being.append(arml+' ' *(mp-len(arml))+ string + armr)
	else:
		for i in range(6):
			if i<4:
				arml = (len(border)-1 +i) * ' '+'*'
				armr = (4-i) * ' '+'*'
			else:
				arml, armr='', ''
			string = '*'
			
			being.append(arml+' ' *(mp-len(arml))+ string + armr)
	return iter(being)


def draw_legs(size,flag = None):
	legs = []
	if flag =='r':
		for i in range(6):
			if i != 0:
				legs.append(' '*(size//2-i)+' '+' '*(2*i) + '*')
			else:
				legs.append(' '*(size//2-i)+'*')
	elif flag == 'l':
		for i in range(6):
			if i != 0:
				legs.append(' '*(size//2-i)+'*'+' '*(2*i) + ' ')
			else:
				legs.append(' '*(size//2-i)+'*')
	else:
		for i in range(6):
			if i != 0:
				legs.append(' '*(size//2-i)+'*'+' '*(2*i) + '*')
			else:
				legs.append(' '*(size//2-i)+'*')
	return iter(legs)


		
def draw_hangman(size=21, deaths=0):

	if deaths ==0:
		return ''
	
	border = (size-9)//2 * ' '
	total = len(border +' ' *int(9//2)+'_'+ len(border)*3*'_' + '_')

	bi = (size-9)//2 
	funcs = {2:draw_head, 
		     3:draw_torso,
			 4:draw_torso,
			 5:draw_torso,
			 6:draw_legs,
			 7:draw_legs} 
	
	args = {2:{border}, 
		     3:(size,border),
			 4:(size,border),
			 5:(size,border),
			 6:{size},
			 7:{size}} 
	kwargs = {2:{}, 
		     3:{'flag':None},
			 4:{'flag':'r'},
			 5:{'flag':'rl'},
			 6:{'flag':'l'},
			 7:{}} 


	if deaths ==1:
		man = ''
	elif deaths ==2:
		func_args= args.get(deaths,{})
		func_kwargs= kwargs.get(deaths,{})
		man = funcs[deaths](*func_args,**func_kwargs)

	elif deaths <6:
		func_args_h= args.get(2,{})
		func_kwargs_h= kwargs.get(2,{})

		func_args_b= args.get(deaths,{})
		func_kwargs_b= kwargs.get(deaths,{})

		head = funcs[2](*func_args_h,**func_kwargs_h)
		body = funcs[deaths](*func_args_b,**func_kwargs_b)
		man = chain(head,body)
		
		
	else:
		func_args_h= args.get(2,{})
		func_kwargs_h= kwargs.get(2,{})

		func_args_b= args.get(5,{})
		func_kwargs_b= kwargs.get(5,{})

		func_args_l= args.get(deaths,{})
		func_kwargs_l= kwargs.get(deaths,{})

		head = funcs[2](*func_args_h,**func_kwargs_h)
		body = funcs[5](*func_args_b,**func_kwargs_b)
		legs =funcs[deaths](*func_args_l,**func_kwargs_l)
		man = chain(head,body,legs)

	#print(list(man))
	for i in range(21):

		if i==0:
			print(border +' ' *int(9//2)+'_'+ len(border)*3*'_' + '_')
		elif i<=3:
			print(border +' ' *int(9//2)+'^'+border*3 + '|')
		else:
			try:
				it = next(man)

				print( it +(total- len(it)-1)* ' ' + '|')
			except (TypeError,StopIteration):
				man=' '
				print(border +' ' *int(9//2)+ man +(bi*3-(len(man)//2))* ' ' + '|')

	return size,border

def draw_options(option):
	init = {}
	for i in option:
		init[i] = '___'
	print( ' '.join([init[i] for i in init]))
	return init

def draw_update(option, init):
	draw_hangman(option)
	print( ' '.join([init[i] for i in init]))

def random_word():
	import random
	words = ['apple','banana','cherry','date','elderberry', 'fig','grapefruit','honeydew','kiwi','lemon','mango','nectarine','orange','papaya','quince','raspberry','strawberry','tangerine','watermelon']
	return random.choice(words)


if __name__ == '__main__':
	death = 0
	option = random_word()
	print(option)
	#size,border = draw_hangman()
	draw_hangman()
	choices = set()
	init = draw_options(option)
	print(init)
	print(init.values)
	while True:
		guess = input('Enter a letter: ')
		if guess in option and guess not in choices:
			print('Yes')
			choices.add(guess)
			init[guess] = f'_{guess}_'
			clear = lambda: system('clear')
			clear()
			draw_update(option, init)

		elif guess in choices:
			print("YOU ALREADY TRIED THIS")
			
		elif death == 7:
			
			print("you died")
			break

		else:
			print('minus life')
			death +=1
			clear = lambda:system('clear')
			draw_hangman(deaths=death)
o