import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    """
    Home is a concrete class of page.Page
    """
    path = '/'
    loremipsum = """
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium 
            doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore 
            veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
            Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, 
            sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
            Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, 
            adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et 
            dolore magnam aliquam quaerat voluptatem. 
            Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis 
            suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? 
            Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam 
            nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
            """

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)                                       # enable tailwind css support

        lay = layout.DefaultLayout(a=wp)                                        # layout
                                                                                # |
        container = jp.QPageContainer(a=lay)                                    # +- container
                                                                                #       |
        div = jp.Div(a=container, classes='bg-gray-200 h-screen')               #       +- div
        jp.Div(a=div, text='This is the home page!', classes='text-4xl m-2')    #           +- div
        jp.Div(a=div, text=cls.loremipsum, classes='text-lg')                   #               +- div

        return wp

    """
    this method has been moved to layout.DefaultLayout
    """
    # @staticmethod
    # def move_drawer(
    #         widget,                                                             # QBtn with drawer attribute
    #         msg
    # ):
    #     widget.drawer.value = not widget.drawer.value                           # toggle drawer state


