import justpy as jp


@jp.SetRoute("/home")                                           # use decorator OR jp.Route()
def home():                                                     # request handler
    wp = jp.WebPage()

    main_div = jp.Div(a=wp,                                     # main div, belongs to webpage
                      classes='bg-gray-500 h-screen')           # gray, takes entire screen

    header_div = jp.Div(a=main_div,
                        classes='grid grid-cols-3 gap-4 '
                                'p-4 border border-black')
    jp.Input(a=header_div, placeholder="Enter first value",     # input, belongs to div
             classes='form-input')
    jp.Input(a=header_div, placeholder="Enter second value",    # input, belongs to div
             classes='form-input')
    jp.Div(a=header_div, text="Result goes here...",            # sub-div, belongs to div
           classes='text-gray-600')
    jp.Div(a=header_div, text="Just another div...",            # sub-div, belongs to div
           classes='text-gray-600')
    jp.Div(a=header_div, text="Yet another div",                # sub-div, belongs to div
           classes='text-gray-600')

    footer_div = jp.Div(a=main_div, classes='grid grid-cols-2 gap-4')
    jp.Button(a=footer_div, text='Calculate',                   # button, belongs to div
              classes='border border-blue-500 m-2 p-2 '         # border, spacing, padding
                      'px-4 rounded text-blue-600 '
                      'hover:bg-red-500 '                       # mouse-over event
                      'hover:text-white')
    jp.Div(a=footer_div, text='I am a cool interactive div!')

    return wp                                                   # must return page


jp.justpy()
