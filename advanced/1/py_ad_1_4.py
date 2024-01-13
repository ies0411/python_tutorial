"""
    magic method, with
    context manager(1)
    keyword - contextlib, __enter__,__exit__,exception
"""


# close :  resource 반환, memory leak방지
# context manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
# 대표적으로 with 구문

# 1
file = open("./testfile1.txt", "w")
try:
    file.write("context manager\nlib test1.")
finally:
    file.close()

# 2
with open("./testfile2.txt", "w") as f:
    f.write("context manager\nlib test1.")


# 3 : class 안에 enter, exit
class MyFileWriter:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        if exc_type:
            print(f"logging exception {exc_type,value,trace_back}")
        self.file_obj.close()


with MyFileWriter("./testfile3.txt", "w") as f:
    f.write("test3")


# 4
