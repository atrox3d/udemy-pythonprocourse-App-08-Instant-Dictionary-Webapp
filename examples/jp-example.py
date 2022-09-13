import justpy as jp


@jp.SetRoute("/home")                                           # use decorator OR jp.Route()
def home():                                                     # request handler
    wp = jp.WebPage()

    main_div = jp.Div(                                          # main div
                        a=wp,                                   # belongs to webpage
                        classes='bg-gray-500 h-screen'          # gray, takes entire screen
    )

    header_div = jp.Div(                                        # header div
                        a=main_div,                             # belongs to main div
                        classes='grid '                         # activate grid
                                'grid-cols-3 '                  # a grid with 3 cols
                                'gap-4 '                        # spacing of grid?
                                'p-4 '                          # padding (internal space)
                                'border '                       # activate border
                                'border-black'                  # border color
    )
    input1 = jp.Input(                                          # input
                        a=header_div,                           # belongs to header_div
                        placeholder="Enter first value",        # text placeholder
                        classes='form-input'
    )
    input2 =jp.Input(                                           # input
                        a=header_div,                           # belongs to header div
                        placeholder="Enter second value",
                        classes='form-input'
    )
    result = jp.Div(                                            # sub-div
                    a=header_div,                               # belongs to header div
                    text="Result goes here...",                 # div text
                    classes='text-gray-600'
    )
    jp.Div(                                                     # sub-div
            a=header_div,                                       # belongs to header div
            text="Just another div...",
            classes='text-gray-600'
    )
    jp.Div(                                                     # sub-div
            a=header_div,                                       # belongs to header div
            text="Yet another div",
            classes='text-gray-600'
    )

    footer_div = jp.Div(                                        # footer div
                        a=main_div,                             # belongs to main div
                        classes='grid grid-cols-2 gap-4'        # another grid
    )
    jp.Button(                                                  # button
                a=footer_div,                                   # belongs to footer div
                text='Calculate',                               # button caption
                click=sum_up,                                   # on click function

                input1=input1, input2=input2,                   # add the two inputs as attributes
                result=result,                                  # add the result div as attribute

                classes='border border-blue-500 m-2 p-2 '       # border, spacing, padding
                        'px-4 rounded text-blue-600 '             
                        'hover:bg-red-500 '                     # mouse-over event
                        'hover:text-white'
    )
    jp.Div(
            a=footer_div,
            text='I am a cool interactive div!'
    )
    return wp                                                   # must return page


def sum_up(widget, msg):
    print(f"{widget.text} clicked!")
    sum = float(widget.input1.value or 0) + float(widget.input2.value or 0)
    print(f'setting div result sum: {sum}')
    widget.result.text = sum

jp.justpy()
