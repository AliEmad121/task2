class StringOperations:
    def reverse(self, *, to_be_reversed: str = None):
        raise NotImplemented('This method need to be implemented')

class ReversedString(StringOperations):
  def reverse(x):
    return x[::-1]

x = ReversedString
x.reverse('hi')
