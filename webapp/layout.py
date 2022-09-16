import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self, view='hHh lpR fFf', **kwargs):                           # kwargs = {
        super().__init__(view=view, **kwargs)                                   #           a:wp,
                                                                                #           view: 'hHh lpR fFf'
                                                                                # }
        ########################################################################
        # structure copied from examples/quasar-layout.html
        ########################################################################
        """
        Qlayout is our base class and it is initialized in
        in the client class, the page class that instantiates
        this class: layout = layout.DefaultLayout(a=wp, view='hHh lpR fFf')
        therefore we get **kwargs and pass them to 
        super().__init
        kwargs in this example is the following dict:
        kwargs = {a: wp, view: 'hHh lpR fFf')
        """
        # layout = jp.QLayout(a=wp, view='hHh lpR fFf')                           # layout
        header = jp.QHeader(a=self)                                             # +- header
        toolbar = jp.QToolbar(a=header)                                         # |    +------------- toolbar
        drawer = jp.QDrawer(                                                    # +- drawer              |
                            a=self,                                             # |    |                 |
                            show_if_above=True,                                 # |    |                 |
                            v_model="left",                                     # |    |                 |
                            bordered=True                                       # |    |                 |
        )                                                                       # |    |                 |
        scroller = jp.QScrollArea(a=drawer, classes='fit')                      # |    +- scroll area    |
        qlist = jp.QList(a=scroller)                                            # |         +- list      |
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'         # |              |       |
        jp.A(a=qlist, text='Home', href='/', classes=a_classes)                 # |              +- a    |
        jp.Br(a=qlist)                                                          # |              +- br   |
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes) # |              +- a    |
        jp.Br(a=qlist)                                                          # |              +- br   |
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)           # |              +- a    |
        jp.Br(a=qlist)                                                          # |              +- br   |
        jp.QBtn(                                                                # |                      +- button
                a=toolbar,                                                      # |                      |
                dense=True, flat=True, round=True,                              # |                      |
                icon="menu",                                                    # |                      |
                click=self.move_drawer,                      # handler           # |                      |
                drawer=drawer                               # object for hndler # |                      |
        )                                                                       # |                      |
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")                  # |                      +- title
                                                                                # |
        """
        the rest of the code is still in homepage.py
        """
        # container = jp.QPageContainer(a=self)                                 # +- container
        # div = jp.Div(a=container, classes='bg-gray-200 h-screen')               #       +- div
        # jp.Div(a=div, text='This is the home page!', classes='text-4xl m-2')    #           +- div
        # jp.Div(a=div, text=cls.loremipsum, classes='text-lg')                   #               +- div
        # return self

    @staticmethod
    def move_drawer(
            widget,                                                             # QBtn with drawer attribute
            msg
    ):
        widget.drawer.value = not widget.drawer.value                           # toggle drawer state


