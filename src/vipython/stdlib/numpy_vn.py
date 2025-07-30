"""
Wrapper cho NumPy với tên hàm tiếng Việt
"""

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    np = None

def kiem_tra_numpy():
    """Kiểm tra numpy có sẵn không"""
    if not NUMPY_AVAILABLE:
        raise ImportError("NumPy chưa được cài đặt. Chạy: pip install numpy")

# ===== TẠO MẢNG =====

def tao_mang(du_lieu, kieu_du_lieu=None):
    """Tạo mảng từ dữ liệu"""
    kiem_tra_numpy()
    return np.array(du_lieu, dtype=kieu_du_lieu)

def tao_mang_khong(kich_thuoc, kieu_du_lieu=float):
    """Tạo mảng toàn số 0"""
    kiem_tra_numpy()
    return np.zeros(kich_thuoc, dtype=kieu_du_lieu)

def tao_mang_mot(kich_thuoc, kieu_du_lieu=float):
    """Tạo mảng toàn số 1"""
    kiem_tra_numpy()
    return np.ones(kich_thuoc, dtype=kieu_du_lieu)

def tao_mang_rong(kich_thuoc, kieu_du_lieu=float):
    """Tạo mảng rỗng (không khởi tạo giá trị)"""
    kiem_tra_numpy()
    return np.empty(kich_thuoc, dtype=kieu_du_lieu)

def tao_mang_don_vi(n, kieu_du_lieu=float):
    """Tạo ma trận đơn vị"""
    kiem_tra_numpy()
    return np.eye(n, dtype=kieu_du_lieu)

def tao_day_so(bat_dau, ket_thuc, buoc=1):
    """Tạo dãy số từ bắt đầu đến kết thúc"""
    kiem_tra_numpy()
    return np.arange(bat_dau, ket_thuc, buoc)

def tao_day_tuyen_tinh(bat_dau, ket_thuc, so_diem=50):
    """Tạo dãy số cách đều"""
    kiem_tra_numpy()
    return np.linspace(bat_dau, ket_thuc, so_diem)

def tao_mang_ngau_nhien(kich_thuoc, min_val=0, max_val=1):
    """Tạo mảng số ngẫu nhiên"""
    kiem_tra_numpy()
    return np.random.uniform(min_val, max_val, kich_thuoc)

def tao_mang_ngau_nhien_nguyen(kich_thuoc, min_val=0, max_val=10):
    """Tạo mảng số nguyên ngẫu nhiên"""
    kiem_tra_numpy()
    return np.random.randint(min_val, max_val, kich_thuoc)

# ===== THÔNG TIN MẢNG =====

def kich_thuoc_mang(mang):
    """Lấy kích thước mảng"""
    kiem_tra_numpy()
    return mang.shape

def so_chieu(mang):
    """Lấy số chiều của mảng"""
    kiem_tra_numpy()
    return mang.ndim

def so_phan_tu(mang):
    """Lấy tổng số phần tử"""
    kiem_tra_numpy()
    return mang.size

def kieu_du_lieu(mang):
    """Lấy kiểu dữ liệu của mảng"""
    kiem_tra_numpy()
    return mang.dtype

# ===== THAO TÁC MẢNG =====

def doi_hinh_dang(mang, hinh_dang_moi):
    """Đổi hình dạng mảng"""
    kiem_tra_numpy()
    return mang.reshape(hinh_dang_moi)

def lam_phang(mang):
    """Làm phẳng mảng thành 1 chiều"""
    kiem_tra_numpy()
    return mang.flatten()

def chuyen_vi(mang):
    """Chuyển vị ma trận"""
    kiem_tra_numpy()
    return mang.T

def noi_mang(danh_sach_mang, truc=0):
    """Nối các mảng"""
    kiem_tra_numpy()
    return np.concatenate(danh_sach_mang, axis=truc)

def xep_chong_doc(danh_sach_mang):
    """Xếp chồng mảng theo chiều dọc"""
    kiem_tra_numpy()
    return np.vstack(danh_sach_mang)

def xep_chong_ngang(danh_sach_mang):
    """Xếp chồng mảng theo chiều ngang"""
    kiem_tra_numpy()
    return np.hstack(danh_sach_mang)

def chia_mang(mang, so_phan, truc=0):
    """Chia mảng thành các phần"""
    kiem_tra_numpy()
    return np.split(mang, so_phan, axis=truc)

# ===== TOÁN HỌC =====

def cong_mang(mang1, mang2):
    """Cộng hai mảng"""
    kiem_tra_numpy()
    return np.add(mang1, mang2)

def tru_mang(mang1, mang2):
    """Trừ hai mảng"""
    kiem_tra_numpy()
    return np.subtract(mang1, mang2)

def nhan_mang(mang1, mang2):
    """Nhân hai mảng (element-wise)"""
    kiem_tra_numpy()
    return np.multiply(mang1, mang2)

def chia_mang(mang1, mang2):
    """Chia hai mảng"""
    kiem_tra_numpy()
    return np.divide(mang1, mang2)

def luy_thua_mang(mang, so_mu):
    """Lũy thừa mảng"""
    kiem_tra_numpy()
    return np.power(mang, so_mu)

def can_bac_hai(mang):
    """Căn bậc hai"""
    kiem_tra_numpy()
    return np.sqrt(mang)

def gia_tri_tuyet_doi(mang):
    """Giá trị tuyệt đối"""
    kiem_tra_numpy()
    return np.abs(mang)

def nhan_ma_tran(ma_tran1, ma_tran2):
    """Nhân ma trận"""
    kiem_tra_numpy()
    return np.dot(ma_tran1, ma_tran2)

# ===== THỐNG KÊ =====

def tong(mang, truc=None):
    """Tính tổng"""
    kiem_tra_numpy()
    return np.sum(mang, axis=truc)

def trung_binh(mang, truc=None):
    """Tính trung bình"""
    kiem_tra_numpy()
    return np.mean(mang, axis=truc)

def trung_vi(mang, truc=None):
    """Tính trung vị"""
    kiem_tra_numpy()
    return np.median(mang, axis=truc)

def do_lech_chuan(mang, truc=None):
    """Tính độ lệch chuẩn"""
    kiem_tra_numpy()
    return np.std(mang, axis=truc)

def phuong_sai(mang, truc=None):
    """Tính phương sai"""
    kiem_tra_numpy()
    return np.var(mang, axis=truc)

def gia_tri_nho_nhat(mang, truc=None):
    """Tìm giá trị nhỏ nhất"""
    kiem_tra_numpy()
    return np.min(mang, axis=truc)

def gia_tri_lon_nhat(mang, truc=None):
    """Tìm giá trị lớn nhất"""
    kiem_tra_numpy()
    return np.max(mang, axis=truc)

def vi_tri_nho_nhat(mang, truc=None):
    """Tìm vị trí giá trị nhỏ nhất"""
    kiem_tra_numpy()
    return np.argmin(mang, axis=truc)

def vi_tri_lon_nhat(mang, truc=None):
    """Tìm vị trí giá trị lớn nhất"""
    kiem_tra_numpy()
    return np.argmax(mang, axis=truc)

# ===== SẮP XẾP VÀ TÌM KIẾM =====

def sap_xep(mang, truc=-1):
    """Sắp xếp mảng"""
    kiem_tra_numpy()
    return np.sort(mang, axis=truc)

def chi_so_sap_xep(mang, truc=-1):
    """Lấy chỉ số sắp xếp"""
    kiem_tra_numpy()
    return np.argsort(mang, axis=truc)

def tim_kiem_nhi_phan(mang_da_sap_xep, gia_tri):
    """Tìm kiếm nhị phân"""
    kiem_tra_numpy()
    return np.searchsorted(mang_da_sap_xep, gia_tri)

def phan_tu_duy_nhat(mang):
    """Lấy các phần tử duy nhất"""
    kiem_tra_numpy()
    return np.unique(mang)

# ===== ĐIỀU KIỆN =====

def dieu_kien(dieu_kien, gia_tri_dung, gia_tri_sai):
    """Chọn giá trị dựa trên điều kiện"""
    kiem_tra_numpy()
    return np.where(dieu_kien, gia_tri_dung, gia_tri_sai)

def tat_ca_dung(mang, truc=None):
    """Kiểm tra tất cả phần tử đều đúng"""
    kiem_tra_numpy()
    return np.all(mang, axis=truc)

def co_phan_tu_dung(mang, truc=None):
    """Kiểm tra có phần tử nào đúng không"""
    kiem_tra_numpy()
    return np.any(mang, axis=truc)

# ===== HÀNG LƯỢNG GIÁC =====

def sin(mang):
    """Hàm sin"""
    kiem_tra_numpy()
    return np.sin(mang)

def cos(mang):
    """Hàm cos"""
    kiem_tra_numpy()
    return np.cos(mang)

def tan(mang):
    """Hàm tan"""
    kiem_tra_numpy()
    return np.tan(mang)

def arcsin(mang):
    """Hàm arcsin"""
    kiem_tra_numpy()
    return np.arcsin(mang)

def arccos(mang):
    """Hàm arccos"""
    kiem_tra_numpy()
    return np.arccos(mang)

def arctan(mang):
    """Hàm arctan"""
    kiem_tra_numpy()
    return np.arctan(mang)

# ===== HÀNG MŨ VÀ LOGARIT =====

def exp(mang):
    """Hàm e^x"""
    kiem_tra_numpy()
    return np.exp(mang)

def log(mang):
    """Hàm logarit tự nhiên"""
    kiem_tra_numpy()
    return np.log(mang)

def log10(mang):
    """Hàm logarit cơ số 10"""
    kiem_tra_numpy()
    return np.log10(mang)

def log2(mang):
    """Hàm logarit cơ số 2"""
    kiem_tra_numpy()
    return np.log2(mang)

# ===== HẰNG SỐ =====

def lay_pi():
    """Lấy hằng số π"""
    kiem_tra_numpy()
    return np.pi

def lay_e():
    """Lấy hằng số e"""
    kiem_tra_numpy()
    return np.e

# ===== TIỆN ÍCH =====

def luu_mang(ten_file, mang):
    """Lưu mảng ra file"""
    kiem_tra_numpy()
    np.save(ten_file, mang)

def tai_mang(ten_file):
    """Tải mảng từ file"""
    kiem_tra_numpy()
    return np.load(ten_file)

def luu_van_ban(ten_file, mang, dinh_dang='%.6f'):
    """Lưu mảng ra file văn bản"""
    kiem_tra_numpy()
    np.savetxt(ten_file, mang, fmt=dinh_dang)

def tai_van_ban(ten_file):
    """Tải mảng từ file văn bản"""
    kiem_tra_numpy()
    return np.loadtxt(ten_file)

def in_mang(mang, do_chinh_xac=3):
    """In mảng với độ chính xác chỉ định"""
    kiem_tra_numpy()
    with np.printoptions(precision=do_chinh_xac, suppress=True):
        print(mang)

