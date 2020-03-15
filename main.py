import PySimpleGUI as sg
from model.linkprovider import LinkProvider
from model.serviceprovider import ServiceProvider

"""
Program allows to choose if it supposed to start and stop the services for the WinCC OA 
or start different projects through links with the same GUI
"""

if __name__ == '__main__':

	sg.theme('BluePurple')

	services = ServiceProvider.get_services()
	links = LinkProvider.get_links()

	layout = [
		[sg.Text('Win CC OA Console', size=(50, 1), font=("Helvetica", 12), justification='center')],
		[sg.Radio('Services', group_id=1, default=True), sg.Radio('Links', default=False, group_id=1)]
	]

	col1 = [[sg.Text("Project")]]
	col2 = [[sg.Text("      ")]]
	col3 = [[sg.Text("      ")]]
	col4 = [[sg.Text("Status")]]

	for service in services:
		col1 += [[sg.Text(service)]]
		col2 += [[sg.Button(button_text='Start', key=("_START_" + services[service].upper()))]]
		col3 += [[sg.Button(button_text='Stop', key=("_STOP_" + services[service].upper()))]]
		col4 += [[sg.Text(services[service] + " status")]]

		#test
		#layout += [[sg.Column(sg.Text(service)), sg.Column(sg.Button(button_text='Start', key=("_START_" + services[service].upper()))),
		#			sg.Column(sg.Button(button_text='Stop', key=("_STOP_" + services[service].upper())))]]

	layout += [[sg.Column(col1, background_color="red"), sg.Column(col2, background_color='blue'),
			    sg.Column(col3, background_color='white'), sg.Column(col4, background_color='yellow')]]

	layout += [[sg.Button('Exit')]]

	window = sg.Window('Win CC OA Console', layout)

	while True:  # Event Loop
		event, values = window.read()
		print(event, values)
		if event in (None, 'Exit'):
			break
		if event == 'Links':
			window['-OUTPUT-'].update(values['-IN-'])

	window.close()
