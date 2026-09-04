import threading
import time

''' Section 1
def worker(name, so):
    while True:
        print(f"hello {name} {so}")
        time.sleep(2)

threading.Thread(target = worker,
                daemon = True, # tự động kết thúc chương trình với daemon
                args = ("ABC",20,) # thêm chuỗi "ABC" vào args của hàm "worker", dấu "," thể hiện kia là 1 tuple --> thêm đủ các biến ở khai báo hàm
                ).start() 
input("nhập gì đó để kết thúc")
'''

''' Section 2
done = False

def worker(name, so):
    while not done:
        print(f"hello {name} {so}")
        time.sleep(2)

t1 = threading.Thread(target = worker, daemon = True, args = ("ABC",20,) )
t2 = threading.Thread(target = worker, daemon = True, args = ("XYZ",20,) )

t1.start()
t2.start()

t1.join() # không thực hiện các lệnh dưới cho đến khi t1 thực hiện xong
t2.join()

input("nhập để kết thúc")
done = True
'''


''' Section 3
done = False

def worker():
    while not done:
        print("hello")
        time.sleep(3)

threading.Thread(target=worker).start()

input("kết thúc ?")
done = True
'''

def ham1():
    tong = 0
    for i in range(1,20):
        time.sleep(0.25)
        tong = tong + i
        print(f"Tổng = {tong}")

def ham2():
    hieu = 3**5
    for i in range(1,20):
        time.sleep(0.25)
        hieu = hieu - i
        print(f'Hiệu = {hieu}')

threading.Thread(target=ham1).start()
threading.Thread(target=ham2).start()