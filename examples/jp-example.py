import justpy as jp


@jp.SetRoute("/home")                                       # use decorator OR jp.Route()
def home():                                                 # request handler
    wp = jp.WebPage()                                       # web page
    jp.Div(                                                 # html element attached to web page
        a=wp,
        text='Hello World!',
        classes="text-green-600 bg-yellow-500 "              # https://tailwindcss.com/docs
                "font-serif text-lg"
    )

    jp.Div(a=wp, text='Hello Again!')
    return wp                                               # must return page


def about():                                                # request handler
    wp = jp.WebPage()                                       # web page
    jp.Div(a=wp, text='Hello Fab!')                         # html element attached to web page
    jp.Div(a=wp, text='Hello Again!')
    return wp                                               # must return page


jp.Route("/about", about)                                   # use jp.Route() OR decorator

jp.justpy()
