import sys
import random
handle='C'
while handle=='C' :
    
    computer = random.randint(0, 2)
    user = int(input('请根据对应编号出拳：0.剪刀，1.石头，2.布'))
    if computer == 0:
        computer = '剪刀'
    elif computer == 1:
        computer = '石头'
    else:
        computer = '布'   
    if user == 0:
        user = '剪刀'
    elif user == 1:
        user = '石头'
    else:
        user = '布'
    print('电脑出的是%s,用户出的是%s' % (computer, user))
    if ((computer == '剪刀' and user == '石头')
        or (computer == '石头' and user == '布')
        or (computer == '布' and user == '剪刀')):
        print('用户获胜') 
    elif user == computer:
        print('双方平局')
    else:
        print('电脑获胜')
    handle = input('用户是否选择继续：C.继续，E.结束')
       
    if handle == 'E':
        print('游戏结束')
        sys.exit()
    elif handle != 'C' and handle != 'E':
          print('输入有误，请重新输入')
          handle = input()
