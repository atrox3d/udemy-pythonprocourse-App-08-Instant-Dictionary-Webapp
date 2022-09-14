import justpy as jp


class Home:
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

        layout = jp.QLayout(a=wp, view='hHh lpR fFf')                           # copied from examples/quasar-layout.html
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left",
                            bordered=True)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')                      # gray # full screen
        jp.Div(a=div, text='This is the home page!', classes='text-4xl m-2')    # large text # margin: 2
        jp.Div(
            a=div,
            text=cls.loremipsum,
            classes='text-lg'
        )
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value


