from console_menu import ConsoleMenu

if __name__ == "__main__":
    def func1():
        print("Im func1")

    def func2():
        print("Im func2")

    def func3():
        print("Im func3")
        raise Exception

    menu = ConsoleMenu(
        "This is a test menu",
        {
            "call func1": func1,
            "call func2": func2,
            "call func3": func3,
        }
    )
    menu.execute()
