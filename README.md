# 👤 Face Recognition System  

## 🚀 Giới Thiệu  
Dự án này triển khai một hệ thống nhận diện khuôn mặt sử dụng OpenCV và PyQt5. Hệ thống bao gồm:  
- Thu thập dữ liệu khuôn mặt  
- Đào tạo mô hình nhận diện  
- Nhận diện khuôn mặt trong thời gian thực  
- Ứng dụng giao diện đồ họa với PyQt5  

## 📂 Cấu Trúc Dự Án  
```
face_recognition
├── dataset/                
├── trainer/                
├── haarcascade_frontalface_default.xml  
├── face_dataset.py        
├── face_recognition.py    
├── program.py              
└── README.md              
```

## 🛠 Cài Đặt  

### 1️⃣ Clone repository  
```bash
git clone https://github.com/vinz0369/face_recognition.git
cd face_recognition
```

### 2️⃣ Cài đặt thư viện cần thiết  
```bash
pip install opencv-python numpy pillow pyqt5
```

### 3️⃣ Chạy chương trình  

- **Lưu khuôn mặt mới**:  
  ```bash
  python face_dataset.py
  ```

- **Huấn luyện mô hình**:  
  Khi đã có ảnh trong `dataset/`, hệ thống sẽ tự động huấn luyện bằng `face_recognition.py`.  
  ```bash
  python face_recognition.py
  ```

- **Chạy giao diện GUI**:  
  ```bash
  program.py
  ```

## 📸 Cách Hoạt Động  
1. **Lưu Khuôn Mặt Mới**  
   - Chạy `face_dataset.py` để thu thập ảnh khuôn mặt.
   - Nhập ID của người dùng và chụp 100 ảnh để tăng độ chính xác.
   - Ảnh sẽ được lưu vào thư mục `dataset/`.

2. **Huấn Luyện Mô Hình**  
   - Chạy `face_recognition.py` để huấn luyện dữ liệu.
   - Mô hình sẽ được lưu trong `trainer/trainer.yml`.

3. **Nhận Diện Khuôn Mặt**  
   - Chạy `face_recognition.py` để quét khuôn mặt.
   - Nếu khuôn mặt đã được huấn luyện, chương trình sẽ hiển thị tên.
   - Lưu thời gian điểm danh vào file CSV.

4. **Giao Diện Người Dùng**  
   - Chạy `gui.py` để sử dụng giao diện đồ họa với các nút bấm tiện lợi.

## 🔥 Công Nghệ Sử Dụng  
- **Python** - Ngôn ngữ lập trình chính.
- **OpenCV** - Xử lý hình ảnh và nhận diện khuôn mặt.
- **NumPy** - Hỗ trợ tính toán ma trận và dữ liệu ảnh.
- **Pillow** - Xử lý hình ảnh.
- **PyQt5** - Xây dựng giao diện người dùng.

## 📌 Lưu Ý  
- Hãy đảm bảo webcam hoạt động tốt trước khi chạy chương trình.
- Mô hình càng có nhiều ảnh khuôn mặt thì độ chính xác càng cao.
- Đặt file `haarcascade_frontalface_default.xml` trong cùng thư mục với các script để nhận diện khuôn mặt chính xác.

