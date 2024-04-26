import keyboard
def printErrorSystem(content="No defined Error", button="Tab", place="ScriptLanguageCreator/config.set"):
  with open(place, 'r') as globalConfiguration:
    if "{:scriptLanguageCreator.textPrintedClass = get.allClassObject}" in globalConfiguration:
      print(f"  Press the {button} to display the error (1 error)")
      rclicked = True
      while rclicked:
        if keyboard.is_pressed(button):
          print(f"   {content}")
          rclicked = False
    else:
      pass