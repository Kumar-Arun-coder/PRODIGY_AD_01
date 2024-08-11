from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the window size

Window.size=(400,500)


class The_CalculatorApp(App):
    pass

class BoxLayoutCal(BoxLayout):
    #for clear all the text at a time 
    def clear(self):
        self.ids.display_label.text = '0'

    #for clearing text one at a timee
    def clear_entry(self):
        self.ids.display_label.text=self.ids.display_label.text[:-1]
        value=self.ids.display_label.text #display value
        if(len(value)==0):
            value=self.ids.display_label.text = '0'

    #creating a button pressing function
    def button_press(self, button):
        #create a variable that contains whatever was in the text box already
        value = self.ids.display_label.text

        # determine if 0 is already there
        if value == "0":
            self.ids.display_label.text = ""
            self.ids.display_label.text = f"{button}"
        else:
            self.ids.display_label.text = f"{value}{button}"
            
            
    #creating addition function
    def math_sign(self,sign):
        value = self.ids.display_label.text
        # adding  a sign to the text
        self.ids.display_label.text = f"{value}{sign}"
        
    #creating a squareroot function
    def squareroot(self):
        value = self.ids.display_label.text
        #adding a squareroot sign to the text
        self.ids.display_label.text = f"{value}^(1/2)"  
        
    #creating percentage function
    def percentage(self):
        value = self.ids.display_label.text
        #performing percentage fuction
        percent = eval(value)/100
        self.ids.display_label.text = f"{percent}"
        
    #creating a rational function
    def rational(self):
        value = eval(self.ids.display_label.text)
        #performing rational fuction
        if(value!=0):
            rationalno = 1/value
            self.ids.display_label.text = f"{rationalno}"
        else:
            self.ids.display_label.text ='Zero Error'
            
    #creating a square function
    def square(self):
        value = self.ids.display_label.text
        #performing squaring fuction
        squareno = eval(value)**2
        self.ids.display_label.text = f"{squareno}"
        
    #creating a sign function
    def sign(self):
        value = eval(self.ids.display_label.text)
        if(value>=0):
            self.ids.display_label.text=f"{-value}"
        elif(value<0):
            self.ids.display_label.text=f"{abs(value)}"
            
    #creating a point adding function
    def dot(self):
        value=self.ids.display_label.text
        self.ids.display_label.text=f"{value}."
            

        
    #creating evaluating function
    def equals(self):
        value=self.ids.display_label.text
        def evaluate_expression(value):
            # Replace 'x' with '*' and '÷' with '/'
            value = value.replace("x", "*").replace("÷", "/").replace("^(1/2)", "**(1/2)")
            
            return value
        value=evaluate_expression(value)
        
        # Evaluate the expression
        try:
            answer = eval(value)
            self.ids.display_label.text=f"{answer}"
        except Exception as e:
            self.ids.display_label.text=f"Error: {str(e)}"
        
            
    
            
            
        
    
      


The_CalculatorApp().run()