import blinker

# Blinker provides a fast dispatching system that
#  allows any number of interested parties to subscribe to events,
#  or “signals”.
#  Signal receivers can subscribe .

frobnicated = blinker.signal('frobnicated')
class Receiver(object):
    
    def __init__(self):
        def handle_frobnicated(sender, **kwargs):
            self.on_frobnicated(sender, **kwargs)
        self.handle_frobnicated = handle_frobnicated
        frobnicated.connect(handle_frobnicated)
    def on_frobnicated(self, sender, **kwargs):
        print (sender,kwargs['message'])
       
if __name__ == '__main__':
         receiver = Receiver()
for i in range(20):
    result= frobnicated.send('Sender %s' % i, message='hello, Mr Albert')
print(result)