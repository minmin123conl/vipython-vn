"""
Module thuật toán cho ViPython-VN
"""

import random
import heapq
from collections import deque, defaultdict

# ===== THUẬT TOÁN SẮP XẾP =====

def sap_xep_noi_bot(danh_sach):
    """Thuật toán sắp xếp nổi bọt (Bubble Sort)"""
    arr = danh_sach.copy()
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def sap_xep_chen(danh_sach):
    """Thuật toán sắp xếp chèn (Insertion Sort)"""
    arr = danh_sach.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def sap_xep_lua_chon(danh_sach):
    """Thuật toán sắp xếp lựa chọn (Selection Sort)"""
    arr = danh_sach.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def sap_xep_nhanh(danh_sach):
    """Thuật toán sắp xếp nhanh (Quick Sort)"""
    if len(danh_sach) <= 1:
        return danh_sach
    
    pivot = danh_sach[len(danh_sach) // 2]
    trai = [x for x in danh_sach if x < pivot]
    giua = [x for x in danh_sach if x == pivot]
    phai = [x for x in danh_sach if x > pivot]
    
    return sap_xep_nhanh(trai) + giua + sap_xep_nhanh(phai)

def sap_xep_tron(danh_sach):
    """Thuật toán sắp xếp trộn (Merge Sort)"""
    if len(danh_sach) <= 1:
        return danh_sach
    
    giua = len(danh_sach) // 2
    trai = sap_xep_tron(danh_sach[:giua])
    phai = sap_xep_tron(danh_sach[giua:])
    
    return tron_hai_mang(trai, phai)

def tron_hai_mang(trai, phai):
    """Trộn hai mảng đã sắp xếp"""
    ket_qua = []
    i = j = 0
    
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            ket_qua.append(trai[i])
            i += 1
        else:
            ket_qua.append(phai[j])
            j += 1
    
    ket_qua.extend(trai[i:])
    ket_qua.extend(phai[j:])
    return ket_qua

def sap_xep_dong(danh_sach):
    """Thuật toán sắp xếp đống (Heap Sort)"""
    arr = danh_sach.copy()
    n = len(arr)
    
    # Xây dựng max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Trích xuất từng phần tử từ heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Hàm heapify cho heap sort"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# ===== THUẬT TOÁN TÌM KIẾM =====

def tim_kiem_tuyen_tinh(danh_sach, gia_tri):
    """Tìm kiếm tuyến tính (Linear Search)"""
    for i, item in enumerate(danh_sach):
        if item == gia_tri:
            return i
    return -1

def tim_kiem_nhi_phan(danh_sach, gia_tri):
    """Tìm kiếm nhị phân (Binary Search) - yêu cầu mảng đã sắp xếp"""
    trai, phai = 0, len(danh_sach) - 1
    
    while trai <= phai:
        giua = (trai + phai) // 2
        
        if danh_sach[giua] == gia_tri:
            return giua
        elif danh_sach[giua] < gia_tri:
            trai = giua + 1
        else:
            phai = giua - 1
    
    return -1

def tim_kiem_noi_suy(danh_sach, gia_tri):
    """Tìm kiếm nội suy (Interpolation Search)"""
    trai, phai = 0, len(danh_sach) - 1
    
    while trai <= phai and gia_tri >= danh_sach[trai] and gia_tri <= danh_sach[phai]:
        if trai == phai:
            if danh_sach[trai] == gia_tri:
                return trai
            return -1
        
        # Công thức nội suy
        pos = trai + int(((float(gia_tri - danh_sach[trai]) / 
                          (danh_sach[phai] - danh_sach[trai])) * (phai - trai)))
        
        if danh_sach[pos] == gia_tri:
            return pos
        elif danh_sach[pos] < gia_tri:
            trai = pos + 1
        else:
            phai = pos - 1
    
    return -1

# ===== CẤU TRÚC DỮ LIỆU =====

class Ngan_xep:
    """Cấu trúc dữ liệu ngăn xếp (Stack)"""
    
    def __init__(self):
        self.items = []
    
    def day_vao(self, item):
        """Đẩy phần tử vào ngăn xếp"""
        self.items.append(item)
    
    def lay_ra(self):
        """Lấy phần tử ra khỏi ngăn xếp"""
        if self.rong():
            raise IndexError("Ngăn xếp rỗng")
        return self.items.pop()
    
    def xem_dinh(self):
        """Xem phần tử ở đỉnh ngăn xếp"""
        if self.rong():
            raise IndexError("Ngăn xếp rỗng")
        return self.items[-1]
    
    def rong(self):
        """Kiểm tra ngăn xếp có rỗng không"""
        return len(self.items) == 0
    
    def kich_thuoc(self):
        """Lấy kích thước ngăn xếp"""
        return len(self.items)

class Hang_doi:
    """Cấu trúc dữ liệu hàng đợi (Queue)"""
    
    def __init__(self):
        self.items = deque()
    
    def them_vao(self, item):
        """Thêm phần tử vào hàng đợi"""
        self.items.append(item)
    
    def lay_ra(self):
        """Lấy phần tử ra khỏi hàng đợi"""
        if self.rong():
            raise IndexError("Hàng đợi rỗng")
        return self.items.popleft()
    
    def xem_dau(self):
        """Xem phần tử đầu hàng đợi"""
        if self.rong():
            raise IndexError("Hàng đợi rỗng")
        return self.items[0]
    
    def rong(self):
        """Kiểm tra hàng đợi có rỗng không"""
        return len(self.items) == 0
    
    def kich_thuoc(self):
        """Lấy kích thước hàng đợi"""
        return len(self.items)

class Hang_doi_uu_tien:
    """Cấu trúc dữ liệu hàng đợi ưu tiên (Priority Queue)"""
    
    def __init__(self):
        self.heap = []
    
    def them_vao(self, item, uu_tien):
        """Thêm phần tử với độ ưu tiên"""
        heapq.heappush(self.heap, (uu_tien, item))
    
    def lay_ra(self):
        """Lấy phần tử có độ ưu tiên cao nhất"""
        if self.rong():
            raise IndexError("Hàng đợi ưu tiên rỗng")
        return heapq.heappop(self.heap)[1]
    
    def xem_dau(self):
        """Xem phần tử có độ ưu tiên cao nhất"""
        if self.rong():
            raise IndexError("Hàng đợi ưu tiên rỗng")
        return self.heap[0][1]
    
    def rong(self):
        """Kiểm tra hàng đợi có rỗng không"""
        return len(self.heap) == 0
    
    def kich_thuoc(self):
        """Lấy kích thước hàng đợi"""
        return len(self.heap)

# ===== THUẬT TOÁN ĐỒ THỊ =====

def duyet_theo_chieu_rong(do_thi, dinh_bat_dau):
    """Duyệt đồ thị theo chiều rộng (BFS)"""
    da_tham = set()
    hang_doi = deque([dinh_bat_dau])
    ket_qua = []
    
    while hang_doi:
        dinh = hang_doi.popleft()
        if dinh not in da_tham:
            da_tham.add(dinh)
            ket_qua.append(dinh)
            
            for lang_gieng in do_thi.get(dinh, []):
                if lang_gieng not in da_tham:
                    hang_doi.append(lang_gieng)
    
    return ket_qua

def duyet_theo_chieu_sau(do_thi, dinh_bat_dau):
    """Duyệt đồ thị theo chiều sâu (DFS)"""
    da_tham = set()
    ngan_xep = [dinh_bat_dau]
    ket_qua = []
    
    while ngan_xep:
        dinh = ngan_xep.pop()
        if dinh not in da_tham:
            da_tham.add(dinh)
            ket_qua.append(dinh)
            
            for lang_gieng in reversed(do_thi.get(dinh, [])):
                if lang_gieng not in da_tham:
                    ngan_xep.append(lang_gieng)
    
    return ket_qua

def duong_di_ngan_nhat_dijkstra(do_thi, dinh_bat_dau):
    """Thuật toán Dijkstra tìm đường đi ngắn nhất"""
    khoang_cach = defaultdict(lambda: float('inf'))
    khoang_cach[dinh_bat_dau] = 0
    hang_doi_uu_tien = [(0, dinh_bat_dau)]
    da_tham = set()
    
    while hang_doi_uu_tien:
        kc_hien_tai, dinh_hien_tai = heapq.heappop(hang_doi_uu_tien)
        
        if dinh_hien_tai in da_tham:
            continue
        
        da_tham.add(dinh_hien_tai)
        
        for lang_gieng, trong_so in do_thi.get(dinh_hien_tai, []):
            kc_moi = kc_hien_tai + trong_so
            
            if kc_moi < khoang_cach[lang_gieng]:
                khoang_cach[lang_gieng] = kc_moi
                heapq.heappush(hang_doi_uu_tien, (kc_moi, lang_gieng))
    
    return dict(khoang_cach)

# ===== THUẬT TOÁN KHÁC =====

def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_de_quy(n):
    """Tính số Fibonacci bằng đệ quy"""
    if n <= 1:
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

def gcd(a, b):
    """Tìm ước chung lớn nhất (GCD)"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Tìm bội chung nhỏ nhất (LCM)"""
    return abs(a * b) // gcd(a, b)

def la_so_nguyen_to(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def sang_eratosthenes(n):
    """Sàng Eratosthenes tìm tất cả số nguyên tố <= n"""
    if n < 2:
        return []
    
    la_nguyen_to = [True] * (n + 1)
    la_nguyen_to[0] = la_nguyen_to[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if la_nguyen_to[i]:
            for j in range(i*i, n + 1, i):
                la_nguyen_to[j] = False
    
    return [i for i in range(2, n + 1) if la_nguyen_to[i]]

def dao_nguoc_danh_sach(danh_sach):
    """Đảo ngược danh sách"""
    return danh_sach[::-1]

def xao_tron(danh_sach):
    """Xáo trộn danh sách"""
    arr = danh_sach.copy()
    random.shuffle(arr)
    return arr

def lay_mau_ngau_nhien(danh_sach, k):
    """Lấy k phần tử ngẫu nhiên từ danh sách"""
    return random.sample(danh_sach, k)

def tim_phan_tu_xuat_hien_nhieu_nhat(danh_sach):
    """Tìm phần tử xuất hiện nhiều nhất"""
    dem = {}
    for item in danh_sach:
        dem[item] = dem.get(item, 0) + 1
    
    return max(dem, key=dem.get) if dem else None

def loai_bo_trung_lap(danh_sach):
    """Loại bỏ phần tử trùng lặp"""
    return list(dict.fromkeys(danh_sach))

def giao_hai_tap(tap1, tap2):
    """Tìm giao của hai tập hợp"""
    return list(set(tap1) & set(tap2))

def hop_hai_tap(tap1, tap2):
    """Tìm hợp của hai tập hợp"""
    return list(set(tap1) | set(tap2))

def hieu_hai_tap(tap1, tap2):
    """Tìm hiệu của hai tập hợp"""
    return list(set(tap1) - set(tap2))

