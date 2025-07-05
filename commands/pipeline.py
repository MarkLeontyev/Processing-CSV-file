class CommandPipeline:
    def __init__(self):
        """
        Инициализирует пустой конвейер команд.
        """
        self.commands = []

    def add(self, command):
        """
        Добавляет команду в конвейер.
        """
        self.commands.append(command)
    
    def run(self, data):
        """
        Последовательно выполняет все команды конвейера над данными.
        """
        for command in self.commands:
            data = command.execute(data)
        return data
