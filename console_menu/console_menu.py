class ConsoleMenu:
    """
    A simple console menu allows you to easily implement a basic user interface.
    You can find a sample below.
    """
    def __init__(self, title, items: dict):
        """
        :param title: This title will be displayed
        :param items: pairs of strings and function references
        """
        self.items = items
        self.title = title

    def __display(self):
        print("\n")
        print(self.title)
        i = 1
        for key in self.items:
            print(str(i) + ") " + str(key))
            i += 1
        print(str(i) + ") " + "exit")

    def execute(self):
        while True:
            self.__display()

            try:
                argument = int(input("run: "))
            except (TypeError, ValueError):
                print("Error: Invalid input type")
                continue
            except KeyboardInterrupt:
                exit()

            if argument not in range(1, len(self.items) + 2):
                print("Error: No such item in menu")
                continue

            if argument == len(self.items) + 1:
                exit()

            try:
                list(self.items.values())[argument - 1]()
            except Exception:
                print("Error: Failed to run item '{}'".format(list(self.items.keys())[argument - 1]))
