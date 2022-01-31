def func1():
    print("Calling func 1")


if __name__ == "__main__":
    print("file is being executed directly")
    func1()
else:
    print("file is imported")
