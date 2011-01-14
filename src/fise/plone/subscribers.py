from fise.plone.utils import get_fise

def fise_indexer_handler(obj, event):
    fise = get_fise(obj)
    #try:           
    fise.store[obj.UID()] = obj.SearchableText()
    #except Exception, e:
    #    raise Exception, \
    #          "FISE server wasn't able to store or process.\n%s" % str(e)