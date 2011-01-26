from fise.client import FISE
from Products.CMFCore.utils import getToolByName
SERVER = 'http://localhost:8080/'

def get_fise(context):
    ptool = getToolByName(context, 'portal_properties')
    fiseprops = ptool.get('fise_properties', None)
    if fiseprops is not None:
        return FISE(fiseprops.getProperty('server'))
    return FISE(SERVER)
