# -*- coding: utf-8 -*-

class Singleton:
	
	def __init__(self, cls):
		self._cls = cls

	def Instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self._cls()
			print("create instance: ", self._instance)
			return self._instance

	def __call__(self):
		raise TypeError('Singletons must be accessed through `Instance`.')

	def __instancecheck__(self, inst):
		return isinstance(inst, self._decorated)


@Singleton
class A:

	def __init__(self):
		pass

	def display(self):
		return id(self)

@Singleton
class B:
	def __init__(self):
		pass
	def display(self):
		return id(self)


if __name__ == '__main__':
	s1 = A.Instance()
	s2 = A.Instance()
	print(s1, s1.display())
	print(s2, s2.display())
	print(s1 is s2)
	print("*" * 30)
	b1 = B.Instance()
	b2 = B.Instance()
	print(b1, b1.display())
	print(b2, b2.display())
	print(b1 is b2)
