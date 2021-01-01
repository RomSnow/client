class ConsoleReader:
    def __init__(self):
        self.is_ready = True

    def get_user_message(self) -> str:
        lines = []
        while True:
            line = input()
            if line == 'exit':
                self.is_ready = False
            lines.append(line)
            if line == '':
                break

        return '\n'.join(lines)
