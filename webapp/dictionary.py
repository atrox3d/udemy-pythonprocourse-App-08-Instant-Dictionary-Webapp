import justpy as jp


class Dictionary:
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)                                       # enable tailwind css support
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')

        jp.Div(
                a=div,
               text='Get the definition of any English word instantly as you type.',
               classes='text-large'
        )
        jp.Input(
                a=div, placeholder='Type in a word here...',
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
        jp.Div(
                a=div,
                classes='m-2 p-2 text-lg border-2 h-40 '
                        'border-gray-300 '
        )
        return wp


# jp.Route(Home.path, Home.serve)
# jp.justpy(port=8001)

