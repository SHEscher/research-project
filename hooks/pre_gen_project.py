#!/usr/bin/env python
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'

if __name__ == '__main__':

    if not re.match(MODULE_REGEX, module_name):
        
        print("\033[31mERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead\033[0m" % module_name)

        #Exit to cancel project
        sys.exit(1)
    
    print("\033[34m\n\nI am creating the research project: %s\n\033[0m" % module_name)