import PySimpleGUI as sg

def main():
  layout=[[sg.Button("button1"),
     sg.Button('button2',key='b2')]]
  window=sg.Window("Gui",location=(20,20))
  window.Layout(layout).Finalize()
  while True:
    event,values=window.Read()
    if event == 'button1':
     sg.Popup("button 1 pressed")
    if event == 'b2':
     sg.Popup("button 2 pressed")
    if event == sg.WIN_CLOSED:
     break



main()
