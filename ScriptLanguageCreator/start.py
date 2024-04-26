import ScriptLanguageCreator.creator as creator
import ScriptLanguageCreator.tools.codeFinder as codeFinder
import ScriptLanguageCreator.interpreter as interpret
interpret.loadInterpreter()
#Podstawowe ustawienia
creator.setLangName("script")
creator.setLangFormat("scp")

#Tworzymy plik interpretacji kodu


#Test 1

creator.defineCode('$event.start %startswith #;', 'comment')
print("test")
creator.ev.printErrorSystem("tekst")