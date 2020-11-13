#class Multimedia():
class Multimedia:
    def __init__(self, name, device):
        self.name = name
        self.device = device

agent1 = Multimedia("Taiye", 30)
agent2 = Multimedia("Sonia", 16)

print (agent1.name, "\t", agent2.name)
print (agent1.device, "\t", agent2.device)
