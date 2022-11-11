from src import app
from src.config import PORT, DEBUG

#from babel.messages.frontend import CommandLineInterface

#CommandLineInterface().run(['pybabel','extract','-F','babel.cfg','-k','lazy_gettext','-o','messages.pot','--input-dirs=.'])
#CommandLineInterface().run(['pybabel','update','-i','messages.pot','-d','./translations','-l','de'])
#CommandLineInterface().run(['pybabel','compile','-d','translations'])

if __name__ == "__main__":
    print("Start server ....")
    if DEBUG:
        app.run(port=PORT, debug=True)
    else:
        app.run('0.0.0.0', port=PORT, debug=False)