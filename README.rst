Read the Docs Git Stress Test
=============================

This is a repository intended to stress Read the Docs' git abstractions.

It has:

- Over 35k commits
- Over 35k tags


Generate documentation
----------------------

.. code-block:: bash

    $ pip install -r requirements.txt
    $ cd docs && make html
