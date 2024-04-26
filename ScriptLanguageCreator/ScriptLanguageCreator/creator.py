#importowanie narzędzi
import keyboard
import ScriptLanguageCreator.tools.errorViewer as ev
import ScriptLanguageCreator.tools.variables
#Tworzenie list, zmiennych, defniowanie obiektów jako globalnych
global langName
global langFormat
langName = "Default Name"
langFormat = "Default Format"
global blockedNamesAndFormates
blockedNamesAndFormates = []
#Definiowane linie z eventami
global lineWithComment
lineWithComment = []
#Skrypty (config.set)
ScriptLanguageCreator.tools.variables.interpreter_start = True
with open("ScriptLanguageCreator/config.set", 'r') as file:
    for line in file:
      # Analizuj każdą linijkę tutaj
      if "{:scriptLanguageCreator.blockedNames.modeContent = True}" in line:
        blockedNamesAndFormates.append("set")
        blockedNamesAndFormates.append("BLOCKED")
      else:
        if "{:scriptLanguageCreator.blockedNames.modeContent = False}" in line:
          blockedNamesAndFormates = []
      


#############################
# Funkcje (oprócz funkcji definicji)
def setLangName(newName):
  '''This function sets the name of your programming language'''
  global langName
  langName = newName


def setLangFormat(newFormat):
  '''This function sets the format of your programming language (after the dot in the file name)'''
  global langFormat
  langFormat = newFormat


def createLanguageWith(place=None):
  '''This function is used to create language files'''
  global langName
  global langFormat
  name = langName
  format = langFormat
  if format in blockedNamesAndFormates:
    format = format.replace(format, "BLOCKED")
    ev.printErrorSystem("The format of your language has been changed, as this format is on the list of blocked file types.", "Tab")
  if " " in name or " " in format or " " in name and " in format":
    pass
  else:
    if place == None:
      with open(f"ScriptLanguageCreator/Window/Languages/{name}.{format}", "w") as writeFile:
         writeFile.write("")
      print(f"The {name}.{format} file was successfully created.")
    else:
      with open(f"ScriptLanguageCreator/{place}/{name}.{format}", "w") as writeFile:
         writeFile.write("")
      print(f"The {name}.{format} file was successfully created.")
  createASettingsFile()
def createASettingsFile():
  '''This function creates settings files for your language interpreter'''
  with open('ScriptLanguageCreator/Window/Settings/config.set', 'w') as config:
    config.write("")
  with open('ScriptLanguageCreator/Window/Settings/setup.set', 'w') as setup:
    setup.write("") 
def writeFile(text, place):
  with open(place, 'w') as newFile:
    newFile.write(text)
#Definicja definicji interpretera

#Comment - komentarz

#Print - pisze
#Variable - tworzy zmienną
#Loop   - pętla
#Loop.For  - pętla For
#Loop.While  - pętla While
#itd.
def defineCode(event, do):
  if event.startswith('$event.start '):
    event = event.replace('$event.start ', '')
    if event.endswith(';'):
      event = event.replace(';', '')
      if event.startswith('%startswith '):
        detectType = "%startswith"
        event = event.replace("%startswith ", "")
        detectText = event
        # Czynność (do)
        if do == "comment":
          textId = do
          aText = "{:scriptDefineCode.whenLineStartswith = asId."
          bText = "}"
          wt = f'\n{aText}{textId} = {detectText}{bText}'
          writeFile(wt,'ScriptLanguageCreator/Window/Languages/setup.set')
      #Do zrobienia !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      elif event.startswith('%endswith'):
        detectType = "%endswith"
        event = event.replace("%endswith", "")
        detectText = event
      else:
        ev.printErrorSystem(f"Unknown event: {event}", "Tab")
    else:
      ev.printErrorSystem(f"Unknown event: {event}", "Tab")
  else:
    ev.printErrorSystem(f"Unknown event: {event}", "Tab")

