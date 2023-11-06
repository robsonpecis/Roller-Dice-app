from  tkinter import *
from playsound import playsound
from random import randint

class RollerDice:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')

        self.create_app()
    
    def play(self):
        playsound('roll_dice.mp3')

    def roll_dice(self, dice):
        rolled_dice = randint(1, dice)
        if self.is_int(self.modifier_var.get()):
            exibition = (f"Dado rolado: d{dice} \n"
            f"Você rolou {rolled_dice} + {self.modifier_var.get()}. \n"
            f"Total: {rolled_dice + int(self.modifier_var.get())}")
            self.play()
        else:
            exibition = 'Insira apenas valores númericos'
            print(f'informação recebida: {self.modifier_var.get()}')

        self.text_exibition['text'] = exibition
    
    def is_int(self, modifier):
        try:
            int(modifier)
            return True
        except ValueError:
            return False

    def create_app(self):
        self.head = Label(root, text='Roller Dice')
        self.head.grid(column=1, row=0)

        dices = [4, 6, 8, 10, 12, 20, 100]

        self.modifier_var = StringVar()
        self.modifier_var.set('0')

        for indice, dice in enumerate(dices):
            self.button = Button(root, text=(f'D{dice}'), command=lambda d=dice: self.roll_dice(d))
            self.button.grid(column=0, row=indice+1, padx=2, pady=2)
        
            self.text_modifier = Label(root, text='+')
            self.text_modifier.grid(column=1, row=indice+1, padx=2, pady=2)

            self.modifier = Entry(root, textvariable=self.modifier_var, width=5)
            self.modifier.grid(column=2, row=indice+1, padx=2, pady=2)

        self.text_exibition = Label(root, text='')
        self.text_exibition.grid(column=1, row=9, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    app = RollerDice(root)
    root.title('Roller Dice')
    root.mainloop()
