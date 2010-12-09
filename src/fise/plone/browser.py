from Products.Five.browser import BrowserView
from fise.plone.utils import get_fise

class RawEnhancementsView(BrowserView):
    
    def enhancements(self):
        fise = get_fise(self.context)
        md = fise.store.metadata(self.context.UID())
        return str(md)