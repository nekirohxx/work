class HumanClass:
    def __init__(self):
        print('人間！')
        self.hp = 100

class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.mp = 50
    
    def output_info(self):
        print(f'現在いのHPは{self.hp}で、'
              f'MPは{self.mp}です。')

    def cast_spell(self):
        print('呪文を唱える')

wizard = WizardClass()
wizard.output_info()


class SwordFighterClass:
    def atack_with_sword(self):
        print('物理攻撃！')
        

class MagicSwordFighterClass(WizardClass,SwordFighterClass):
    pass

mfs = MagicSwordFighterClass()
mfs.cast_spell()
mfs.atack_with_sword()  



import cv2
print(cv2.version)      