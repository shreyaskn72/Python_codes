from jsonhandling import crudoopsjson

def open_result_file(filename, skip_line, mydict={}):
    with open(filename) as fh:
        for _ in range(skip_line):
            next(fh)

        key = 0

        for line in fh:
            # reading line by line from the text file
            description = list(line.strip().split(None))
            #print(description)
            key = key+1
            mydict[key] = description

    return mydict

if __name__ == "__main__":
      filename = 'example.json'

      a = open_result_file("commands.txt", 0)
      # filename = 'TLT1.json'
      object1 = crudoopsjson(filename)
      object1.addrow('text file', a)