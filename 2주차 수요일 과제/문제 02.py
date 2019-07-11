import random

class Character:
    def __init__(self):
        self.name()
        self.status()
        self.info()

    def name(self):
        self.user=input('캐릭터의 이름을 입력하세요: ')

    def status(self):
        self.strenth=random.randint(6,8)
        self.brain=random.randint(6,8)
        
        if self.strenth>self.brain:
            self.job='전사'
        elif self.strenth==self.brain:
            self.job='궁수'
        elif self.strenth<self.brain:
            self.job='법사'
        
    def info(self):
        print('캐릭터 이름:',self.user)
        print('캐릭터 정보: 힘(%d), 지력(%d)' % (self.strenth,self.brain))
        print('캐릭터 직업:',self.job)

user=Character()
