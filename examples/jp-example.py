import justpy as jp


@jp.SetRoute("/home")                                       # use decorator OR jp.Route()
def home():                                                 # request handler
    wp = jp.WebPage()

    div = jp.Div(a=wp,                                      # main div, belongs to webpage
                 classes='bg-gray-500 h-screen')            # gray, takes entire screen

    jp.Input(a=div, placeholder="Enter first value",        # input, belongs to div
             classes='form-input')

    jp.Input(a=div, placeholder="Enter second value",       # input, belongs to div
             classes='form-input')

    jp.Div(a=div, text="Result goes here...",               # sub-div, belongs to div
           classes='text-gray-600')

    jp.Button(a=div, text='Calculate',                      # button, belongs to div
              classes='border border-blue-500 m-2 p-2 '     # border, spacing, padding
                      'px-4 rounded text-blue-600 '
                      'hover:bg-red-500 '                   # mouse-over event
                      'hover:text-white')
    return wp                                               # must return page


jp.justpy()
