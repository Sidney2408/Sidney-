from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import Button
from kivy.graphics import Color, Rectangle



class GuiKivy(App):

	def build(self):
	    self.lbl_Red = Label(text = "Red LED",color= [0,1,1,1] , halign ="left")
	    
	    self.lbl_Red.canvas.before.add(Color(1,0,0,1))
	    #canvas is where you draw things on, aka put pictures on it 
	    rect = Rectangle()
	    self.rect = rect #debug
	    #rect is a reference to rectangle
            self.lbl_Red.canvas.before.add(rect)
            #Add rectangle to canvas 
	    def res_rect(instance, val,color):
	        print "resizing"
	        rect.pos = instance.pos
	        rect.size = instance.size
	        # create rectangle no size defined. rect.pos is the position of the instance(label)
	    color = Color(0,0,0,1)
	    def redrawer(i,val):
	        return res_rect(i,val,color)
	    redrawer = lambda i,val:res_rect(i,val,color)
	    self.lbl_Red.bind(pos=redrawer, size=redrawer)
	    # pos is a value, when the value changes(pos), callback(res_rect) activates.
	    # Resizes rectangle to fit the button
	    
	    new = self.lbl_Red
	    #a is alpha
	    return new
	def changecolour(self,instance):
	    self.btn.fill = "yellow"
	    
x=GuiKivy()
x.run()