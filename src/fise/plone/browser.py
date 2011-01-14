from Products.Five.browser import BrowserView
from fise.plone.utils import get_fise

class RawEnhancementsView(BrowserView):
    
    def enhancements(self):
        fise = get_fise(self.context)
        uid = self.context.UID()
        try:
            md = fise.store.metadata(uid)
        except Exception, e:
            return "Problem while fetching %s from FISE server.\n%s" % (uid, str(e))        
        return str(md)