def save_to_file(content, filename):
    with open(filename,'w+') as f:
        f.write(content)

def read_file(filename):
    with open(filename,'r') as f:
        print(f.readlines())

print(__name__)
