import time as timer

class hook:
    def __init__(self):
        self.hooks = []

    def Add(self, hookID, uniqueID, callback):
        for i in range(len(self.hooks)):
            values = self.hooks[i]
            if values[0] == hookID and values[1] == uniqueID:
                del self.hooks[i]
                break
        self.hooks.append([hookID, uniqueID, callback])

    def Run(self, hookID, *args):
        for values in self.hooks:
            if values[0] == hookID:
                values[2](*args)
                return
        print("INVALID HOOK")

    def Remove(self, hookID, uniqueID):
        for i in range(len(self.hooks)):
            values = self.hooks[i]
            if values[0] == hookID and values[1] == uniqueID:
                del self.hooks[i]
                break

hook = hook()

def ourFunc():
    print("Called the think hook")
hook.Add("Think", "ourThinkHook", ourFunc)

while True:
    hook.Run("Think")
    timer.sleep(0.1)

# hook.Remove("Think", "ourThinkHook")
