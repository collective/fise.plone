from fise.plone.utils import get_fise
from Products.statusmessages.interfaces import IStatusMessage

def fise_indexer_handler(obj, event):
    obj._fise_enhancements = None
    fise = get_fise(obj)
    try:           
        obj._fise_enhancements = fise.engines(obj.SearchableText(), 'rdfjson')
    except Exception, e:
        msg = "Problem while using FISE server for automatic "+\
              "enhancement.\n%s" % str(e)
        IStatusMessage(obj.REQUEST).addStatusMessage(msg, type='error')