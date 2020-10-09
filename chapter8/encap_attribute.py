class A:
    def __init__(self):
        # internal attribute
        self._internal = 0
        # public attribute
        self.public = 1

    def public_method(self):
        """
        public method
        :return:
        """
        pass

    def _internal_method(self):
        """
        private method
        :return:
        """
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        # not override B.__private
        self.__private = 1

    # not override B.__private_method()
    def __private_method(self):
        pass


lambda_ = 'Hello' # Trailing _ to avoid clash with lambda keyword
