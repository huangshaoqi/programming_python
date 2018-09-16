from gui5 import HelloButton


class MyClass(HelloButton):
    def callback(self):
        print("I Going....")


if __name__ == "__main__":
    MyClass(text="Press Down").mainloop()
