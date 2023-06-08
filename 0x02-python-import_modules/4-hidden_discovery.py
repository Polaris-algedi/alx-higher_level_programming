#!/usr/bin/python3
"""Program that prints all the names defined
by the compiled module hidden_4.pyc"""
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if not name.startswith("__"):
            print(name)
