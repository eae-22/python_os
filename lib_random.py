import random

print(random.random()) # in ra ngẫu nhiên số (0,1)

print(random.randint(-10, 10)) # in ra ngẫu nhiên số nguyên [-10, 10]

print("===",random.randrange(0,20,2)) # Tạo ra 1 số nguyên thoe khoảng (0, 20) với bước là 2

print(random.uniform(-10,10)) # in ra ngẫu nhiên số thực [-10, 10]

L1 = ("A", "B", "C", "D")
print(random.choice(L1)) # Chọn ngẫu nhiện 1 phần tử trong set (có thể thay list, dict, tuple)
print(random.sample(L1,2)) # Lấy ngẫu nhiên 2 phần tử khác nhau trong L1
print(random.choices(L1,k=2)) # Lấy ngẫu nhiên 2 phần tử (có thể trùng) trong L1

L2 = ["Tom", "Jerry", "Hug", "Timi"]
random.shuffle(L2) # đảo ngẫu nhiên vị trí các phần tử trong list 
print(L2)

print("\n")

# tạo ra các bộ mã ngẫu nhiên cố định
random.seed(1)
print(random.random()) 
print(random.randint(-10, 10)) 
print(random.uniform(-10,10)) 

print("\n")

random.seed(2)
print(random.random()) 
print(random.randint(-10, 10)) 
print(random.uniform(-10,10)) 