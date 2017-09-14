#Created by: Alireza Teimoori
#Created on: 14 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit0-03
#This program is Address, but with a button :)

import ui

def address_touch_up_inside(sender):
	view['name_lable'].text = ("Alireza Teimoori")
	view['city_lable'].text = ("Ottawa")
	view['province_lable'].text = ("Ontario")
	
view = ui.load_view()
view.present('sheet')
