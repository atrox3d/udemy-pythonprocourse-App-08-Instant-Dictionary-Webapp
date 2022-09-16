import inspect

import justpy as jp

from webapp import page

"""
imports are grayed out in pycharm but removing them will
cause the program to fail, because they would not be into
globals()
"""
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary

# """
# Abstract Classes: first test and error
# """
# imports = globals()
# for key, value in imports.items():                              # RuntimeError: dictionary changed size during iteration
#     if hasattr(key, 'path'):                                    # because key and values are globals and are therefore
#         jp.Route(value.path, value.serve)                       # added to the globals dict
#
# """
# Abstract Classes: second test and error
# """
# imports = list(globals().values())
# for obj in imports:                                             # AttributeError: 'SourceFileLoader' object has no attribute 'serve'
#     if hasattr(obj, 'path'):                                    # the SourceFilellLoader object has a path attribute
#         jp.Route(obj.path, obj.serve)                           # but not a serve method
#
#
# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary .serve)

imports = list(globals().values())                                              # get list of values from globals (imports)
for obj in imports:                                                             # iter through objects in globals
    if inspect.isclass(obj):                                                    # check if obj is indeed a class
        if (
                issubclass(obj, page.Page) and                                  # check if we have a subclass of abstract Page
                obj is not page.Page                                            # must not be the abstract class, if imported
        ):
            jp.Route(obj.path, obj.serve)                                       # automatically create routes


jp.justpy(port=8001)
