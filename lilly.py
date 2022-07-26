class Composable:

	def __init__(self, callable):

		self.callable = callable
		self.__call__ = lambda _, x: callable(x)
		self.__or__ = lambda _, other: Composable(lambda x: other.callable(callable(x)))
