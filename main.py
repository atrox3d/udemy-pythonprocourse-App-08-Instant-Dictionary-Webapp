import justpy as jp

from webapp.aboutpage import About
from webapp.homepage import Home
from webapp.dictionary import Dictionary

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary .serve)

jp.justpy(port=8001)
