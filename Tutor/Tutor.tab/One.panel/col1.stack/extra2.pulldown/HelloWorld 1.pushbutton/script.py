__title__ = 'DOC'
__author__ = 'Stanislav Abramenkov'
__doc__ = 'This is good'

uidoc = __revit__.ActiveUIDocument
#CUSTOM IMPORT 

from Snippets.selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))