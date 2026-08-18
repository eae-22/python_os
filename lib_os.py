import os
import datetime

print(os.getcwd()) # in ra thư mục chứa file Python hiện tại

os.chdir("C:\\Users\\txd04\\OneDrive\\Desktop\\Python\\tools") # chuyển sang làm việc tại thư mục như đường dẫn
print(os.getcwd())

files = os.listdir(r"C:\Users\txd04\OneDrive\Desktop\Python") # list ra các file có trong thư mục theo đường dẫn
print(files)

#os.mkdir("TEST") # tạo thư mục có tên "TEST" trong thư mục hiện đang làm việc
#os.makedirs("A/ B/ C", exist_ok = True) # tạo thư mục C trong thư mục B trong thư mục A và trng thư mục hiện đang làm việc, nếu có trùng thì không báo lỗi

#os.rmdir("TEST") # xóa thư mục có tên "TEST"

file1 = 'file1.txt'
add = os.path.join(os.getcwd(), file1) # ghép đường dẫn với thư mục hiện tại để có đường dẫn đến file1.txt
print(add)
# nếu có nhiều folder thì os.path.join(os.getcwd(), "folder1", "folder2", file)

print(os.path.exists(add)) # kiểm tra đường dẫn có tồn tại
print(os.path.isfile(add)) # kiểm tra đường dẫn có phải là file
print(os.path.isdir(add)) # kiểm tra đường dẫn có phải là folder


info = os.stat(r"C:\Users\txd04\OneDrive\Desktop\Python\tools") # lấy thông tin đường dẫn
print("Thông tin file/folder:", info)
print("Loại & quyền truy cập:", info.st_mode)
print("Số hiệu inode:", info.st_ino)
print("ID thiết bị:", info.st_dev)
print("Số hard link:", info.st_nlink)
print("ID người dùng:", info.st_uid)
print("ID nhóm:", info.st_gid)
print("Kích thước:", info.st_size, "byte")
print("Thời gian truy cập:", datetime.datetime.fromtimestamp(info.st_atime))
print("Thời gian sửa đổi:", datetime.datetime.fromtimestamp(info.st_mtime))
print("Thời gian tạo:", datetime.datetime.fromtimestamp(info.st_ctime))

v1 = os.environ.get("PATH") # danh sách các PATH mà window có thể tìm
print(v1)

print(os.getlogin()) # tên tài khoản window đang đăng nhập

os.chdir("C:\\Users\\txd04\\OneDrive\\Desktop\\Python") # Phải ở thư mục chứa thư mục muốn đổi tên
#os.rename("tools", "TOOLS") # đổi tên folder
#os.rename("test.py", "demo.py") # đổi tên file

print(os.path.splitext("demo.py")) # tách tên file và phần mở rộng

print(os.path.basename(r"C:\Users\txd04\OneDrive\Desktop\Python\demo.py")) # lấy tên file từ đường dẫn

print(os.path.abspath("TOOLS")) # lấy đường dẫn tuyệt đối (từ ổ đĩa đến vị trí file) từ tên file 

for root, dir, file in os.walk("C:\\Users\\txd04\\OneDrive\\Desktop"): # duyệt tất cả các đường dẫn -> thự mục -> file 
    print(root)
    print(dir)
    print(file)