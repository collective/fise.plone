from fise.plone.utils import get_fise

def fise_indexer_handler(obj, event):
    fise = get_fise(obj)           
    fise.store[obj.UID()] = obj.SearchableText()