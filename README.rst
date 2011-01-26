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

In a Plone buildout add the a line with ``fise.plone`` to your instances 
``eggs`` and `zcml``. 

Run buildout.

(Re)start Zope/Plone.

In Configuration -> Addons: Install ``FISE Plone Integration``.

Changelog
=========

0.2
---

- make fise server configureable through ``portal_properties``. See 
  ``propertiestool.xml`` in the profile for details. - jensens, 2011-01-26

0.1
---
- initial code, tests and documentation

Copyright, License, Contributors
================================

copyright BlueDynamics Alliance, 2010-2011

This package is provided under the OSI-approved OpenSource License 
`GNU General Public License, version 2
<http://opensource.org/licenses/gpl-2.0>`_ (as Plone itself 
is).

Contributors:

- funded by `IKS-Project early adopters program 
  <http://wiki.iks-project.eu/index.php/About>`_
  
- Jens Klein <jens@bluedynamics.com>, Klein & Partner KG: initial code, tests, 
  documentation and first release.