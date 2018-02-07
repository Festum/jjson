JJSON
=======================

jQuery selector liked JSON query tool

- `Source <https://github.com/festum/jjson>`_


Example Usage
-------------

.. code-block:: python

	import jjson

	# Get string from nested JSON
    j = {
		"foo": {
			"bar": {
				"test": "hello world"
			}
		}
	}
    p = "foo.bar.test"
    print jjson.extract(j, p)
	# hello world


Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install git+https://github.com/festum/jjson.git

	# Alternative
    $ pip install jjson


TODO
-------
- CLI
- Change value from certain node


Contributions
-------------

.. _issues: https://github.com/festum/jjson/issues
.. __: https://github.com/festum/jjson/pulls

Issues_ and `Pull Requests`__ are always welcome.


License
-------

.. __: https://github.com/festum/jjson/raw/master/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
