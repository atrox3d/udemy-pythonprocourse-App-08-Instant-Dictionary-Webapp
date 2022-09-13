import justpy as jp
import definition


class Dictionary:
    path = '/dictionary'

    """
    without class method serve is called as instance method but without the self, because it is registered in the
    Route method as Dictionary.serve
    So it is called without self but it doesnt rise an Exception because justpy passes a request parameter.
    As a result we dont get any error but we have a wrong self variable.
    To solve this we use the classmethod decorator, in this way when serve is called python passes the class
    as 1st argument ad request as the second
    """
    @classmethod                                                                # called from Dictionary.serve, no self
    def serve(cls, request):                                                    # so request doesnt go to 1st param
        wp = jp.QuasarPage(tailwind=True)                                       # enable tailwind css support
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')

        jp.Div(
                a=div,
                text='Get the definition of any English word instantly as you type.',
                classes='text-large'
        )
        input_div = jp.Div(a=div, classes='grid grid-cols-2')
        input_box = jp.Input(
                a=input_div, placeholder='Type in a word here...',
                classes='m-2 '                                                  # margin 2
                        'bg-gray-100 '                                          # gray backgroud
                        'border-2 '                                             # border 2
                        'border-gray-200 '                                      # gray border
                        'rounded '                                              # round borders
                        'w-64 '                                                 # 64 chars width?
                        'focus:bg-white '
                        'focus:outline-none '                                   # no outline when out of focus
                        'focus:border-purple-500 '                              # purple outline when in focus
                        'py-2 '                                                 # padding
                        'px-4 '
        )
        output_div = jp.Div(
                a=div,
                classes='m-2 p-2 text-lg border-2 h-40 '
                        'border-gray-300 '
        )

        jp.Button(
                    a=input_div, text="Get Definition",
                    classes='border-2 border-black '
                            'rounded text-gray-500 ',
                    click=cls.get_definition,                                   # click static handler
                    outputdiv=output_div,                                       # where to write on click
                    inputbox=input_box                                          # where to read from on click
        )
        # print(cls, request)
        return wp

    """
    This time the event handler expects us to declare two params but the handler method is not
    a function, so if we use an instance method we get self as first parameter and if we use
    @classmethod we get the class as first parameter and in the end we always get 3 parameters
    Either way it doesnt work so we need to use @staticmethod to treat the method as a function
    """
    @staticmethod
    def get_definition(widget, msg):                                            # button click handler
        defined = definition.Definition(widget.inputbox.value)                  # get definition of input box
        widget.outputdiv.text = " | ".join(defined.get())                       # write definition on output div



