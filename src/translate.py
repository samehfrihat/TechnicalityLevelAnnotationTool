from babel.messages.frontend import CommandLineInterface

print(1)
CommandLineInterface().run(['pybabel','extract','-F','babel.cfg','-k','lazy_gettext','-o','messages.pot','--input-dirs=.'])
print(2)
CommandLineInterface().run(['pybabel','update','-i','messages.pot','-d','./translations','-l','de'])
print(3)
CommandLineInterface().run(['pybabel','compile','-d','translations'])
print(4)