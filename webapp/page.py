from abc import ABC, abstractmethod


class Page(ABC):
    """
    Abstract class Page could be a normal class, but making
    it a subclass of ABC and using @abstractmethod decorator
    makes it impossible to instantiate it and
    subclassing it without defining the serve method
    """
    @abstractmethod
    def serve(self):
        pass


if __name__ == '__main__':
    try:
        p = Page()                  # TypeError: Can't instantiate abstract class Page with abstract method serve
    except Exception as e:
        print(type(e), e)

    try:
        class X(Page):
                pass

        x = X()                     # TypeError: Can't instantiate abstract class X with abstract method serve
    except Exception as e:
        print(type(e), e)

    try:
        class Y(Page):
            def serve(self):
                pass

        y = Y()
        y.serve()
    except Exception as e:
        print(type(e), e)
    else:
        print('ok')
