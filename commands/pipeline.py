class CommandPipeline: 
    def __init__(self): 
        self.commands = [] 

    def add(self, command): 
        self.commands.append(command)
    
    def run(self, data): 
        for command in self.commands: data = command.execute(data) 
        return data 