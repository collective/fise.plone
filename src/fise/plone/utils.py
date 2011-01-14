from fise.client import FISE
fise = FISE('http://localhost:8080/')

def get_fise(context):
    # XXX this need improvement
    return fise