# ViPython-VN

Ngôn ngữ lập trình "ViPython-VN" - phiên bản Việt hoá không dấu theo phong cách Python kèm trình IDLE chuyên dụng.

## Mục tiêu

- **Ngôn ngữ**: Cú pháp "thuần Việt không dấu", khối lệnh thụt lề (indentation) như Python, động-hình (dynamic), tập trung vào giải thuật.
- **IDLE**: Môi trường viết-chạy-gỡ lỗi một chạm, đa nền tảng (Win/macOS/Linux).
- **Đối tượng**: Học sinh, sinh viên, giáo viên, người mới bắt đầu lập trình tại Việt Nam.

## Cấu trúc dự án

```
vipython-vn/
├── src/vipython/          # Mã nguồn chính
│   ├── lexer/            # Phân tích từ vựng
│   ├── parser/           # Phân tích cú pháp
│   ├── runtime/          # Thời gian chạy
│   └── stdlib/           # Thư viện chuẩn
├── tests/                # Bộ kiểm thử
├── docs/                 # Tài liệu
├── examples/             # Ví dụ mã nguồn
├── ide/                  # IDLE ViPy-Studio
└── tools/                # Công cụ hỗ trợ
```

## Cài đặt

```bash
# Clone repository
git clone https://github.com/minmin123conl/vipython-vn.git
cd vipython-vn

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy REPL
python -m vipython
```

## Ví dụ cú pháp

```vipython
# Chào thế giới
in_ra("Xin chao the gioi!")

# Hàm tính giai thừa
ham giai_thua(n):
    neu n <= 1:
        tra_ve 1
    khac:
        tra_ve n * giai_thua(n - 1)

# Sử dụng
ket_qua = giai_thua(5)
in_ra(f"Giai thua cua 5 la: {ket_qua}")
```

## Đóng góp

- Chúng tôi hoan nghênh mọi đóng góp! Vui lòng đọc [bao_cao_giai_doan_3.md](bao_cao_giai_doan_3.md) và [bao_cao_trien_khai.md](bao_cao_trien_khai.md) để biết chi tiết về các phiên bản và nội dung những thử nghiệm và thống kê.
- Chi tiết vấn đề bản quyền và đóng góp chi tiết cho dự án vui long liên hệ qua email sau: hoanganh1mw@gmail.com

## Giấy phép

Dự án này được phát hành dưới giấy phép Apache License 2.0. Xem [LICENSE](LICENSE) để biết thêm chi tiết.

