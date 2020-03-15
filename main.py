import PySimpleGUI as sg
from static.winc_cc64 import iconWindow as iconWindow
from model.linkprovider import LinkProvider
from model.serviceprovider import ServiceProvider

"""
Program allows to choose if it supposed to start and stop the services for the WinCC OA 
or start different projects through links with the same GUI
"""


def createServicesLayout():
	"""
	Method returns tab layout for the Services tab in the GUI
	:return: a list of elements to be visualized inside tab services
	"""
	col1 = [[sg.Text("Project", font=('Segoe',12,'bold'))]]
	col2 = [[sg.Text("      ")]]
	col3 = [[sg.Text("      ")]]
	col4 = [[sg.Text("Status", font=('Segoe',12,'bold'))]]
	for service in services:
		col1 += [[sg.Text(service, pad=(5,6))]]
		col2 += [[sg.Button(button_text='', pad=(5,4), key=("-START_" + services[service].upper()) + "-", image_filename="./static/Start-icon.png", button_color=('#E3F2FD', '#E3F2FD'))]]
		col3 += [[sg.Button(button_text='', pad=(5,4), key=("-STOP_" + services[service].upper()) + "-", image_filename="./static/Stop-red-icon.png", button_color=('#E3F2FD', '#E3F2FD'))]]
		col4 += [[sg.Text(services[service] + " status", pad=(5,6))]]

	return [[sg.Column(col1), sg.Column(col2),
			 sg.Column(col3), sg.Column(col4)]]


def createLinksLayout():
	"""
	Method returns tab layout for the Links tab in the GUI
	:return: a list of the elements to be visualized inside the Links tab
	"""
	col1 = [[sg.Text("Project", font=('Segoe',12,'bold'))]]
	col2 = [[sg.Text("      ")]]

	for link in links:
		col1 += [[sg.Text(link, pad=(5,6))]]
		col2 += [[sg.Button(button_text='', pad=(5,4), key=("-LAUNCH_" + links[link].upper()) + "-", image_filename="./static/Start-icon.png", button_color=('#E3F2FD', '#E3F2FD'))]]

	return [[sg.Column(col1), sg.Column(col2)]]


if __name__ == '__main__':

	sg.theme('LightBlue')
	sg.SetOptions(icon=iconWindow, font="Segoe", text_justification='center')

	services = ServiceProvider.get_services()
	links = LinkProvider.get_links()

	layout = [
			[sg.Text('Win CC OA Console', size=(50, 1), justification='center')]]

	layout += [[sg.TabGroup(
				[[sg.Tab('Services', layout=createServicesLayout()), sg.Tab('Links', layout=createLinksLayout())]])],
			   	[sg.Button('', key='Exit', image_filename="./static/exit.png", button_color=('#E3F2FD', '#E3F2FD'))]]

	window = sg.Window('Win CC OA Console', layout)

	while True:  # Event Loop
		event, values = window.read()
		print(event, values)
		if event in (None, 'Exit'):
			break
		if event == 'Links':
			window['-OUTPUT-'].update(values['-IN-'])

	window.close()
