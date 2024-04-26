import ScriptLanguageCreator.tools.variables as var
def loadInterpreter():    
    with open("ScriptLanguageCreator/config.set" , 'a') as configurer:
        if not var.interpreter_start:
            configurer.write("\n{:scriptLanguageCreator.interpreterCanLoaded = False}")
        else:
            configurer.write("\n{:scriptLanguageCreator.interpreterCanLoaded = True}")
