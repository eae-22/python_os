import time
from datetime import timedelta, datetime

print(time.ctime()) # Hiện thời gian ở thời điểm hiện tại
time.sleep(1) # chờ 1s sau đó mới tiếp tục chương trình.

# Giờ địa phương --> Giúp lấy từng giá trị so với ctime()
t0 = time.localtime() 
print(t0.tm_year)  # năm
print(t0.tm_mon)   # tháng
print(t0.tm_mday)  # ngày
print(t0.tm_hour)  # giờ
print(t0.tm_min)   # phút
print(t0.tm_sec)   # giây

# Giờ UTC
t5 = time.gmtime()
print("Năm:", t5.tm_year)
print("Tháng:", t5.tm_mon)
print("Ngày:", t5.tm_mday)
print("Giờ:", t5.tm_hour)
print("Phút:", t5.tm_min)
print("Giây:", t5.tm_sec)
print("Thứ:", t5.tm_wday)
print("Ngày thứ:", t5.tm_yday, "trong năm")
print("Daylight Saving Time:", t5.tm_isdst) # Giờ mùa hè 
#--> VN ko dùng --> trả về 0, đang dùng --> 1; không xác định --> -1

# Đo thời gian chạy 1 lệnh/ tập lệnh (có trễ)
t1 = time.time()
for i in range(100):
    time.sleep(0.25)
t2 = time.time()
print(t2-t1)

# Đo thời gian chạy 1 lệnh/ tập lệnh (không trễ)
t3 = time.perf_counter()
for i in range(100):
    time.sleep(0.25)
t4 = time.perf_counter()
print(t4-t3)


# Cộng/ trừ thời gian
dt = datetime.now()
print(dt + timedelta(days=7))    # 7 ngày sau
print(dt - timedelta(hours=2))   # 2 giờ trước

# Khoảng thời gian giữa 2 thời điểm
# --> datetime(năm, tháng, ngày, giờ, phút, giây, microsecond)
t1 = datetime(2026, 8, 25, 10, 30, 0)
t2 = datetime(2026, 8, 30, 15, 45, 30)
print(t2 - t1)