from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
import json

class RawEnhancementsView(BrowserView):
    
    def enhancements(self):
        records = []
        md = getattr(self.context, '_fise_enhancements', None)
        if not md:
            return records
        md = json.loads(md)
        for enhkey in md:
            data = md[enhkey]
            record = {}
            if u'http://purl.org/dc/terms/type' in data:
                record['from'] = 'dc'
                record['rawtypes'] = [_['value'] for _ in data[u'http://purl.org/dc/terms/type']]                
                record['name'] =  data[u'http://fise.iks-project.eu/ontology/selected-text'][0][u'value']
                record['confidence'] = float(data[u'http://fise.iks-project.eu/ontology/confidence'][0][u'value'])
                record['url'] = None
            elif u'http://fise.iks-project.eu/ontology/entity-type' in data:
                record['from'] = 'iksontology'                
                record['rawtypes'] = [_['value'] for _ in data[u'http://fise.iks-project.eu/ontology/entity-type']]                
                record['url'] = data[u'http://fise.iks-project.eu/ontology/entity-reference'][0][u'value']
                record['name']  = data[u'http://fise.iks-project.eu/ontology/entity-label'][0][u'value']
                record['confidence'] = float(data[u'http://fise.iks-project.eu/ontology/confidence'][0][u'value'])
            else:
                continue
            record['types'] = list()
            for raw in record['rawtypes']:
                short = raw.rpartition('/')[2].rpartition('#')[2]
                record['types'].append([short, raw])
            records.append(record)
        return sorted(records, key=lambda item: item['confidence'], reverse=True)                                   
