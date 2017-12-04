import json
from time import sleep
from multiprocessing import Process, Manager


with open("newfile2.json") as jsonfile:
    data = json.load(jsonfile)

def append_data(json_buffer):
    while True:
        sleep(60)
        if len(json_buffer) < 100:
            json_buffer.append(data)
        else:
            raise Exception("Buffer is full")
        print "Appending data", len(json_buffer)

def delete_data(json_buffer):
    while True:
        sleep(300)
        if len(json_buffer):
            json_buffer.pop(0)
            print "Removing data", len(json_buffer)

if __name__ == '__main__':
    manager = Manager()

    json_buffer_list = manager.list()

    enter_data = Process(target=append_data, args=(json_buffer_list,))
    remove_data = Process(target=delete_data, args=(json_buffer_list,))
    try:
        enter_data.start()
        remove_data.start()
        enter_data.join()
        remove_data.join()
    except Exception, e:
        print e.message
