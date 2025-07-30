# Ví dụ về các thuật toán sắp xếp trong ViPython-VN

# Import module thuật toán
tu vipython.stdlib.thuat_toan nhap *
tu vipython.stdlib.ngay_gio nhap do_thoi_gian

# Tạo dữ liệu test
danh_sach_goc = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
in_ra("Danh sách gốc:", danh_sach_goc)
in_ra()

# Test các thuật toán sắp xếp
in_ra("=== THUẬT TOÁN SẮP XẾP ===")

# Bubble Sort
@do_thoi_gian
ham test_bubble_sort():
    ket_qua = sap_xep_noi_bot(danh_sach_goc)
    tra_ve ket_qua

in_ra("1. Sắp xếp nổi bọt (Bubble Sort):")
ket_qua_bubble = test_bubble_sort()
in_ra("Kết quả:", ket_qua_bubble)
in_ra()

# Insertion Sort
@do_thoi_gian
ham test_insertion_sort():
    ket_qua = sap_xep_chen(danh_sach_goc)
    tra_ve ket_qua

in_ra("2. Sắp xếp chèn (Insertion Sort):")
ket_qua_insertion = test_insertion_sort()
in_ra("Kết quả:", ket_qua_insertion)
in_ra()

# Selection Sort
@do_thoi_gian
ham test_selection_sort():
    ket_qua = sap_xep_lua_chon(danh_sach_goc)
    tra_ve ket_qua

in_ra("3. Sắp xếp lựa chọn (Selection Sort):")
ket_qua_selection = test_selection_sort()
in_ra("Kết quả:", ket_qua_selection)
in_ra()

# Quick Sort
@do_thoi_gian
ham test_quick_sort():
    ket_qua = sap_xep_nhanh(danh_sach_goc)
    tra_ve ket_qua

in_ra("4. Sắp xếp nhanh (Quick Sort):")
ket_qua_quick = test_quick_sort()
in_ra("Kết quả:", ket_qua_quick)
in_ra()

# Merge Sort
@do_thoi_gian
ham test_merge_sort():
    ket_qua = sap_xep_tron(danh_sach_goc)
    tra_ve ket_qua

in_ra("5. Sắp xếp trộn (Merge Sort):")
ket_qua_merge = test_merge_sort()
in_ra("Kết quả:", ket_qua_merge)
in_ra()

# Heap Sort
@do_thoi_gian
ham test_heap_sort():
    ket_qua = sap_xep_dong(danh_sach_goc)
    tra_ve ket_qua

in_ra("6. Sắp xếp đống (Heap Sort):")
ket_qua_heap = test_heap_sort()
in_ra("Kết quả:", ket_qua_heap)
in_ra()

# So sánh với thuật toán built-in của Python
@do_thoi_gian
ham test_python_sort():
    ket_qua = sorted(danh_sach_goc)
    tra_ve ket_qua

in_ra("7. Sắp xếp built-in Python:")
ket_qua_python = test_python_sort()
in_ra("Kết quả:", ket_qua_python)
in_ra()

# Test với dữ liệu lớn hơn
in_ra("=== TEST VỚI DỮ LIỆU LỚN ===")
tu random nhap randint

# Tạo danh sách 1000 phần tử ngẫu nhiên
danh_sach_lon = []
voi i trong pham_vi(1000):
    danh_sach_lon.them_vao(randint(1, 1000))

in_ra("Đang test với 1000 phần tử ngẫu nhiên...")

# Test Quick Sort với dữ liệu lớn
@do_thoi_gian
ham test_quick_sort_lon():
    ket_qua = sap_xep_nhanh(danh_sach_lon)
    tra_ve len(ket_qua)

in_ra("Quick Sort với 1000 phần tử:")
so_phan_tu = test_quick_sort_lon()
in_ra("Đã sắp xếp", so_phan_tu, "phần tử")
in_ra()

# Test Merge Sort với dữ liệu lớn
@do_thoi_gian
ham test_merge_sort_lon():
    ket_qua = sap_xep_tron(danh_sach_lon)
    tra_ve len(ket_qua)

in_ra("Merge Sort với 1000 phần tử:")
so_phan_tu = test_merge_sort_lon()
in_ra("Đã sắp xếp", so_phan_tu, "phần tử")
in_ra()

# Test Python sort với dữ liệu lớn
@do_thoi_gian
ham test_python_sort_lon():
    ket_qua = sorted(danh_sach_lon)
    tra_ve len(ket_qua)

in_ra("Python built-in sort với 1000 phần tử:")
so_phan_tu = test_python_sort_lon()
in_ra("Đã sắp xếp", so_phan_tu, "phần tử")

in_ra()
in_ra("=== KẾT LUẬN ===")
in_ra("- Bubble Sort, Insertion Sort, Selection Sort: O(n²) - chậm với dữ liệu lớn")
in_ra("- Quick Sort, Merge Sort, Heap Sort: O(n log n) - nhanh hơn")
in_ra("- Python built-in sort (Timsort): Tối ưu nhất cho hầu hết trường hợp")

