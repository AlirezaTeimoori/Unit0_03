import ui

def hello_world_touch_up_inside(sender):
	view['hello_world_lable'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')
