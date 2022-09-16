import inspect

import justpy as jp

from webapp import page
# from webapp.about import About
# from webapp.home import Home
# from webapp.dictionary import Dictionary

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

imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)


jp.justpy(port=8001)
