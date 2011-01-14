This is the `Plone <http://www.python.org/>`_ integration of the Semantic 
Engine `Apache Stanbol FISE <http://incubator.apache.org/stanbol/>`_ (see also
the old `IKS-WIKI <http://wiki.iks-project.eu/index.php/FISE>`_). 
  
This package is an outcome of the IKS early adopter programme. It does not aim 
to provide a full-fledged FISE integration in Plone. It's meant as a minimal
example implementation and focal point for future work.

Current features:

- it provides a GenericSetup install step ``FISE Plone Integration``.

- it expects a FISE server running at ``http://localhost:8080``. This is 
  hardcoded for now.

- it passes the ``SearchableText`` of any Plone content to FISE. It depends on
  the Plone configuration whats content is passed to FISE. 
  
- a view available as a document-action fetches the raw enhancement metadata 
  and shows it in Plone.

Installation 
------------

In your Plone buildout add the a line with ``fise.plone`` to your instances 
``eggs`` and `zcml``
