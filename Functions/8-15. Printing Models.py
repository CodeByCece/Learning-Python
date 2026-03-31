"""Utilzing functions from printing_models.py in a
separate file called printing_functions.py. Use an import statement 
at the top of printing_models.py, and modify the file to 
use the imported functions""" 

import printing_functions
# pyright: ignore[reportMissingImports] 
# printing_functions module is on local drive

unprinted_designs = ['guitar case', 'robots', 'hexagon']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
