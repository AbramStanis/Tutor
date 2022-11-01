from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_selected_elements(uidoc):
    """Param uidoc: return"""
    selected_elements = []
    
    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)
        
    return selected_elements