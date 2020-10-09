from chapter12.actor_exp_1 import Actor

class TaggedActor(Actor):
    def run(self):
        while True:
             tag, *payload = self.recv()
             getattr(self,'do_'+tag)(*payload)

    # Methods correponding to different message tags
    def do_A(self, x):
        print(f'Running A {x}')

    def do_B(self, x, y):
        print(f'Running B {x} {y}')

# Example
a = TaggedActor()
a.start()
a.send(('A', 1))
a.send(('B', 2, 3))
a.close()
a.join()