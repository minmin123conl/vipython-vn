# Danh sách các hàm trong Thư viện chuẩn ViPython-VN

Đây là danh sách tổng hợp các hàm có sẵn trong thư viện chuẩn của ViPython-VN, bao gồm tên tiếng Việt, tên gốc (Python tương đương) và chú thích về chức năng của từng hàm.

## 1. Module `builtin_functions.py` (Hàm dựng sẵn)

| Tên tiếng Việt | Tên gốc (Python) | Chức năng |
|-----------------|------------------|-----------|
| `in_ra`         | `print`          | In ra màn hình console. |
| `nhap_vao`      | `input`          | Nhập dữ liệu từ bàn phím. |
| `do_dai`        | `len`            | Trả về độ dài của đối tượng (chuỗi, danh sách, tuple, từ điển). |
| `kieu`          | `type`           | Trả về kiểu dữ liệu của đối tượng. |
| `chuyen_so`     | `int`, `float`   | Chuyển đổi chuỗi hoặc đối tượng sang kiểu số nguyên hoặc số thực. |
| `chuyen_van_ban`| `str`            | Chuyển đổi đối tượng sang kiểu chuỗi. |
| `chuyen_so_nguyen`| `int`          | Chuyển đổi đối tượng sang kiểu số nguyên. |
| `chuyen_so_thuc`| `float`          | Chuyển đổi đối tượng sang kiểu số thực. |
| `pham_vi`       | `range`          | Tạo một dãy số. |
| `sap_xep`       | `sorted`         | Sắp xếp các phần tử trong một iterable. |
| `dao_nguoc`     | `reversed`       | Đảo ngược thứ tự các phần tử trong một iterable. |
| `tong`          | `sum`            | Tính tổng các phần tử trong một iterable. |
| `nho_nhat`      | `min`            | Tìm giá trị nhỏ nhất trong một iterable. |
| `lon_nhat`      | `max`            | Tìm giá trị lớn nhất trong một iterable. |
| `tat_ca`        | `all`            | Kiểm tra xem tất cả các phần tử trong iterable có phải là True không. |
| `bat_ky`        | `any`            | Kiểm tra xem có bất kỳ phần tử nào trong iterable là True không. |
| `dem`           | `count`          | Đếm số lần xuất hiện của một giá trị trong iterable. |
| `tim_vi_tri`    | `index`          | Tìm vị trí (chỉ số) đầu tiên của một giá trị trong iterable. |
| `la_so`         | `isinstance`     | Kiểm tra xem đối tượng có phải là số (int hoặc float) không. |
| `la_chuoi`      | `isinstance`     | Kiểm tra xem đối tượng có phải là chuỗi không. |
| `la_danh_sach`  | `isinstance`     | Kiểm tra xem đối tượng có phải là danh sách không. |
| `la_tu_dien`    | `isinstance`     | Kiểm tra xem đối tượng có phải là từ điển không. |
| `nhap_module`   | `__import__`     | Import một module. |
| `nhap_tu_module`| `getattr`        | Import một hàm cụ thể từ một module. |
| `liet_ke_ham_module`| `dir`        | Liệt kê các hàm có sẵn trong một module. |
| `dung_vay`      | `True`           | Hằng số logic biểu thị giá trị đúng. |
| `sai_vay`       | `False`          | Hằng số logic biểu thị giá trị sai. |

## 2. Module `chuoi.py` (Xử lý chuỗi)

| Tên tiếng Việt | Tên gốc (Python) | Chức năng |
|-----------------|------------------|-----------|
| `do_dai`        | `len`            | Trả về độ dài của chuỗi. |
| `viet_hoa`      | `upper`          | Chuyển chuỗi thành chữ hoa. |
| `viet_thuong`   | `lower`          | Chuyển chuỗi thành chữ thường. |
| `viet_hoa_chu_dau`| `capitalize`   | Viết hoa chữ cái đầu tiên của chuỗi. |
| `viet_hoa_tung_tu`| `title`        | Viết hoa chữ cái đầu tiên của mỗi từ trong chuỗi. |
| `cat_khoang_trang`| `strip`        | Cắt bỏ khoảng trắng ở đầu và cuối chuỗi. |
| `cat_khoang_trang_trai`| `lstrip`    | Cắt bỏ khoảng trắng ở đầu chuỗi. |
| `cat_khoang_trang_phai`| `rstrip`    | Cắt bỏ khoảng trắng ở cuối chuỗi. |
| `thay_the`      | `replace`        | Thay thế chuỗi con. |
| `tach_chuoi`    | `split`          | Tách chuỗi thành danh sách các chuỗi con. |
| `noi_chuoi`     | `join`           | Nối các phần tử của danh sách thành một chuỗi. |
| `bat_dau_bang`  | `startswith`     | Kiểm tra chuỗi có bắt đầu bằng tiền tố không. |
| `ket_thuc_bang` | `endswith`       | Kiểm tra chuỗi có kết thúc bằng hậu tố không. |
| `chua`          | `in`             | Kiểm tra chuỗi có chứa chuỗi con không. |
| `tim_vi_tri`    | `index`          | Tìm vị trí đầu tiên của chuỗi con. |
| `tim_vi_tri_cuoi`| `rindex`        | Tìm vị trí cuối cùng của chuỗi con. |
| `dem_so_lan`    | `count`          | Đếm số lần xuất hiện của chuỗi con. |
| `la_chu_so`     | `isdigit`        | Kiểm tra chuỗi có phải toàn chữ số không. |
| `la_chu_cai`    | `isalpha`        | Kiểm tra chuỗi có phải toàn chữ cái không. |
| `la_chu_cai_so` | `isalnum`        | Kiểm tra chuỗi có phải toàn chữ cái và số không. |
| `la_khoang_trang`| `isspace`       | Kiểm tra chuỗi có phải toàn khoảng trắng không. |
| `la_chu_hoa`    | `isupper`        | Kiểm tra chuỗi có phải toàn chữ hoa không. |
| `la_chu_thuong` | `islower`        | Kiểm tra chuỗi có phải toàn chữ thường không. |
| `dao_nguoc`     | `[::-1]`         | Đảo ngược chuỗi. |
| `lap_lai`       | `*`              | Lặp lại chuỗi n lần. |
| `chen_vao`      | `slice`          | Chèn chuỗi vào vị trí chỉ định. |
| `xoa_tai_vi_tri`| `slice`          | Xóa ký tự tại vị trí chỉ định. |
| `cat_chuoi`     | `slice`          | Cắt chuỗi từ vị trí bắt đầu đến kết thúc. |
| `chen_khoang_trang`| `ljust`, `rjust`, `center`| Chèn khoảng trắng để đạt độ rộng mong muốn. |
| `ma_hoa_base64` | `base64.b64encode`| Mã hóa chuỗi thành base64. |
| `giai_ma_base64`| `base64.b64decode`| Giải mã chuỗi base64. |
| `bo_dau`        | `unicodedata`    | Bỏ dấu tiếng Việt. |
| `tim_kiem_regex`| `re.findall`     | Tìm kiếm bằng biểu thức chính quy. |
| `thay_the_regex`| `re.sub`         | Thay thế bằng biểu thức chính quy. |
| `tach_chuoi_regex`| `re.split`     | Tách chuỗi bằng biểu thức chính quy. |
| `kiem_tra_email`| `re.match`       | Kiểm tra định dạng email. |
| `kiem_tra_so_dien_thoai`| `re.match`| Kiểm tra định dạng số điện thoại Việt Nam. |
| `tao_slug`      | `re.sub`, `strip`| Tạo slug từ chuỗi (dùng cho URL). |
| `dinh_dang_so`  | `format`         | Định dạng số với dấu phân cách hàng nghìn. |

## 3. Module `file.py` (Xử lý file)

| Tên tiếng Việt | Tên gốc (Python) | Chức năng |
|-----------------|------------------|-----------|
| `doc_file`      | `open().read()`  | Đọc toàn bộ nội dung của một file văn bản. |
| `doc_dong`      | `open().readlines()`| Đọc file thành danh sách các dòng. |
| `ghi_file`      | `open().write()` | Ghi nội dung vào file (ghi đè hoặc thêm vào). |
| `ghi_dong`      | `open().writelines()`| Ghi danh sách dòng vào file. |
| `them_vao_file` | `open().write(mode=\'a\')`| Thêm nội dung vào cuối file. |
| `ton_tai`       | `os.path.exists` | Kiểm tra file/thư mục có tồn tại không. |
| `la_file`       | `os.path.isfile` | Kiểm tra đường dẫn có phải là một file không. |
| `la_thu_muc`    | `os.path.isdir`  | Kiểm tra đường dẫn có phải là một thư mục không. |
| `kich_thuoc_file`| `os.path.getsize`| Lấy kích thước của file (theo bytes). |
| `thoi_gian_sua_doi`| `os.path.getmtime`| Lấy thời gian sửa đổi cuối cùng của file/thư mục. |
| `thoi_gian_tao` | `os.path.getctime`| Lấy thời gian tạo file/thư mục. |
| `xoa_file`      | `os.remove`      | Xóa một file. |
| `sao_chep_file` | `shutil.copy2`   | Sao chép một file từ nguồn đến đích. |
| `di_chuyen_file`| `shutil.move`    | Di chuyển hoặc đổi tên file/thư mục. |
| `tao_thu_muc`   | `os.makedirs`, `os.mkdir`| Tạo thư mục. |
| `xoa_thu_muc`   | `shutil.rmtree`, `os.rmdir`| Xóa thư mục (có thể xóa cả thư mục không rỗng). |
| `liet_ke_file`  | `os.listdir`     | Liệt kê các file và thư mục trong một đường dẫn. |
| `tim_file`      | `os.walk`        | Tìm kiếm file theo tên trong thư mục (có thể đệ quy). |
| `lay_ten_file`  | `os.path.basename`| Lấy tên file từ đường dẫn đầy đủ. |
| `lay_thu_muc_cha`| `os.path.dirname`| Lấy đường dẫn thư mục chứa file. |
| `lay_phan_mo_rong`| `os.path.splitext`| Lấy phần mở rộng của file. |
| `lay_ten_khong_mo_rong`| `os.path.splitext`| Lấy tên file không có phần mở rộng. |
| `duong_dan_tuyet_doi`| `os.path.abspath`| Chuyển đường dẫn tương đối thành tuyệt đối. |
| `noi_duong_dan` | `os.path.join`   | Nối các phần của đường dẫn lại với nhau. |
| `thu_muc_hien_tai`| `os.getcwd`     | Lấy đường dẫn thư mục làm việc hiện tại. |
| `doi_thu_muc`   | `os.chdir`       | Đổi thư mục làm việc hiện tại. |
| `doc_json`      | `json.load`      | Đọc dữ liệu từ file JSON. |
| `ghi_json`      | `json.dump`      | Ghi dữ liệu ra file JSON. |
| `doc_csv`       | `csv.reader`     | Đọc dữ liệu từ file CSV. |
| `ghi_csv`       | `csv.writer`     | Ghi dữ liệu ra file CSV. |
| `nen_file`      | `shutil.make_archive`| Nén file/thư mục thành file zip. |
| `giai_nen_file` | `shutil.unpack_archive`| Giải nén file zip. |
| `dung_luong_thu_muc`| `os.walk`, `os.path.getsize`| Tính tổng dung lượng của một thư mục. |
| `dinh_dang_dung_luong`| Custom       | Định dạng dung lượng file/thư mục sang các đơn vị dễ đọc (KB, MB, GB...). |

## 4. Module `math_vn.py` (Toán học)

| Tên tiếng Việt | Tên gốc (Python) | Chức năng |
|-----------------|------------------|-----------|
| `PI`            | `math.pi`        | Hằng số Pi (π). |
| `E`             | `math.e`         | Hằng số Euler (e). |
| `TAU`           | `math.tau`       | Hằng số Tau (τ). |
| `sin`           | `math.sin`       | Tính sin của một góc (radian). |
| `cos`           | `math.cos`       | Tính cosin của một góc (radian). |
| `tan`           | `math.tan`       | Tính tang của một góc (radian). |
| `asin`          | `math.asin`      | Tính arcsin (kết quả radian). |
| `acos`          | `math.acos`      | Tính arccos (kết quả radian). |
| `atan`          | `math.atan`      | Tính arctan (kết quả radian). |
| `atan2`         | `math.atan2`     | Tính arctan2 (kết quả radian). |
| `log`           | `math.log`       | Tính logarit tự nhiên hoặc logarit với cơ số tùy chọn. |
| `log10`         | `math.log10`     | Tính logarit cơ số 10. |
| `log2`          | `math.log2`      | Tính logarit cơ số 2. |
| `exp`           | `math.exp`       | Tính e mũ x. |
| `pow`           | `math.pow`       | Tính lũy thừa x mũ y. |
| `sqrt`          | `math.sqrt`      | Tính căn bậc hai. |
| `cbrt`          | `x**(1/3)`       | Tính căn bậc ba. |
| `lam_tron`      | `round`          | Làm tròn số đến số nguyên gần nhất. |
| `lam_tron_len`  | `math.ceil`      | Làm tròn số lên số nguyên lớn nhất. |
| `lam_tron_xuong`| `math.floor`     | Làm tròn số xuống số nguyên nhỏ nhất. |
| `cat_phan_thap_phan`| `math.trunc` | Cắt bỏ phần thập phân của số. |
| `gia_tri_tuyet_doi`| `abs`         | Tính giá trị tuyệt đối của số. |
| `dau`           | Custom           | Trả về dấu của số (-1, 0, hoặc 1). |
| `nho_nhat`      | `min`            | Tìm giá trị nhỏ nhất trong một tập hợp số. |
| `lon_nhat`      | `max`            | Tìm giá trị lớn nhất trong một tập hợp số. |
| `la_so_nguyen`  | `isinstance`, `is_integer`| Kiểm tra xem có phải số nguyên không. |
| `la_so_thuc`    | `isinstance`     | Kiểm tra xem có phải số thực không. |
| `la_vo_cuc`     | `math.isinf`     | Kiểm tra xem có phải vô cực không. |
| `la_nan`        | `math.isnan`     | Kiểm tra xem có phải NaN (Not a Number) không. |
| `do_sang_radian`| `math.radians`   | Chuyển đổi độ sang radian. |
| `radian_sang_do`| `math.degrees`   | Chuyển đổi radian sang độ. |
| `giai_thua`     | `math.factorial` | Tính giai thừa của một số nguyên không âm. |
| `to_hop`        | `math.comb`      | Tính tổ hợp C(n, k). |
| `chinh_hop`     | `math.perm`      | Tính chỉnh hợp P(n, k). |
| `trung_binh`    | Custom           | Tính trung bình cộng của một danh sách số. |
| `trung_vi`      | Custom           | Tính trung vị của một danh sách số. |
| `phuong_sai`    | Custom           | Tính phương sai của một danh sách số. |
| `do_lech_chuan` | Custom           | Tính độ lệch chuẩn của một danh sách số. |

## 5. Module `matplotlib_vn.py` (Wrapper cho Matplotlib)

| Tên tiếng Việt | Tên gốc (Matplotlib) | Chức năng |
|-----------------|----------------------|-----------|
| `tao_hinh`      | `plt.figure()`       | Tạo một figure (khung vẽ) mới. |
| `tao_hinh_va_truc`| `plt.subplots()`   | Tạo figure và các trục (axes) con. |
| `ve_duong`      | `plt.plot()`         | Vẽ đường thẳng. |
| `ve_diem`       | `plt.scatter()`      | Vẽ các điểm. |
| `ve_cot`        | `plt.bar()`          | Vẽ biểu đồ cột dọc. |
| `ve_cot_ngang`  | `plt.barh()`         | Vẽ biểu đồ cột ngang. |
| `ve_histogram`  | `plt.hist()`         | Vẽ biểu đồ histogram. |
| `ve_tron`       | `plt.pie()`          | Vẽ biểu đồ tròn. |
| `ve_boxplot`    | `plt.boxplot()`      | Vẽ biểu đồ hộp (boxplot). |
| `ve_violinplot` | `plt.violinplot()`   | Vẽ biểu đồ violin. |
| `dat_tieu_de`   | `plt.title()`        | Đặt tiêu đề cho biểu đồ. |
| `dat_nhan_truc_x`| `plt.xlabel()`      | Đặt nhãn cho trục X. |
| `dat_nhan_truc_y`| `plt.ylabel()`      | Đặt nhãn cho trục Y. |
| `dat_gioi_han_x`| `plt.xlim()`         | Đặt giới hạn cho trục X. |
| `dat_gioi_han_y`| `plt.ylim()`         | Đặt giới hạn cho trục Y. |
| `dat_vi_tri_x`  | `plt.xticks()`       | Đặt vị trí và nhãn cho các điểm trên trục X. |
| `dat_vi_tri_y`  | `plt.yticks()`       | Đặt vị trí và nhãn cho các điểm trên trục Y. |
| `hien_luoi`     | `plt.grid()`         | Hiển thị lưới trên biểu đồ. |
| `hien_chu_thich`| `plt.legend()`       | Hiển thị chú thích (legend) cho các đường/điểm. |
| `dat_mau_nen`   | `plt.gca().set_facecolor()`| Đặt màu nền cho vùng vẽ. |
| `hien_thi`      | `plt.show()`         | Hiển thị biểu đồ. |
| `luu_hinh`      | `plt.savefig()`      | Lưu biểu đồ ra file ảnh. |
| `xoa_hinh`      | `plt.clf()`          | Xóa figure hiện tại. |
| `xoa_tat_ca`    | `plt.close(\'all\')`| Xóa tất cả các figure. |
| `ve_duong_contour`| `plt.contour()`    | Vẽ đường contour. |
| `ve_mat_contour`| `plt.contourf()`     | Vẽ mặt contour (filled contour). |
| `ve_anh`        | `plt.imshow()`       | Vẽ ảnh. |
| `ve_thanh_mau`  | `plt.colorbar()`     | Vẽ thanh màu (colorbar). |
| `ve_duong_loi`  | `plt.plot()`         | Vẽ đường lưới (grid lines). |
| `ve_hinh_chu_nhat`| `patches.Rectangle`| Vẽ hình chữ nhật. |
| `ve_hinh_tron`  | `patches.Circle`     | Vẽ hình tròn. |
| `ve_hinh_elip`  | `patches.Ellipse`    | Vẽ hình elip. |
| `ve_mui_ten`    | `plt.arrow()`        | Vẽ mũi tên. |
| `ve_van_ban`    | `plt.text()`         | Vẽ văn bản trên biểu đồ. |
| `tao_truc_3d`   | `fig.add_subplot(projection=\'3d\')`| Tạo trục 3D. |
| `ve_duong_3d`   | `ax.plot()`          | Vẽ đường 3D. |
| `ve_diem_3d`    | `ax.scatter()`       | Vẽ điểm 3D. |
| `ve_mat_3d`     | `ax.plot_surface()`  | Vẽ mặt 3D. |
| `dat_kich_thuoc_hinh`| `plt.figure(figsize=...)`| Đặt kích thước của figure. |
| `dat_khoang_cach_subplot`| `plt.subplots_adjust()`| Đặt khoảng cách giữa các subplot. |
| `dat_style`     | `plt.style.use()`    | Đặt style cho biểu đồ. |
| `lay_danh_sach_style`| `plt.style.available`| Lấy danh sách các style có sẵn. |
| `dat_font_tieng_viet`| Custom        | Đặt font hỗ trợ tiếng Việt cho biểu đồ. |
| `bieu_do_duong_don_gian`| Custom      | Hàm mẫu tạo biểu đồ đường đơn giản. |
| `bieu_do_cot_don_gian`| Custom        | Hàm mẫu tạo biểu đồ cột đơn giản. |
| `bieu_do_tron_don_gian`| Custom       | Hàm mẫu tạo biểu đồ tròn đơn giản. |

## 6. Module `ngay_gio.py` (Ngày giờ)

| Tên tiếng Việt | Tên gốc (Python) | Chức năng |
|-----------------|------------------|-----------|
| `hom_nay`       | `datetime.date.today()`| Lấy ngày hiện tại. |
| `bay_gio`       | `datetime.datetime.now()`| Lấy thời gian hiện tại (bao gồm ngày và giờ). |
| `tao_ngay`      | `datetime.date()`| Tạo đối tượng ngày. |
| `tao_gio`       | `datetime.time()`| Tạo đối tượng thời gian. |
| `tao_ngay_gio`  | `datetime.datetime()`| Tạo đối tượng ngày giờ. |
| `dinh_dang_ngay`| `strftime`       | Định dạng ngày thành chuỗi theo định dạng. |
| `dinh_dang_gio` | `strftime`       | Định dạng giờ thành chuỗi theo định dạng. |
| `dinh_dang_ngay_gio`| `strftime`   | Định dạng ngày giờ thành chuỗi theo định dạng. |
| `phan_tich_ngay`| `strptime`       | Phân tích chuỗi thành đối tượng ngày. |
| `phan_tich_gio` | `strptime`       | Phân tích chuỗi thành đối tượng giờ. |
| `phan_tich_ngay_gio`| `strptime`   | Phân tích chuỗi thành đối tượng ngày giờ. |
| `lay_nam`       | `year`           | Lấy năm từ đối tượng ngày/ngày giờ. |
| `lay_thang`     | `month`          | Lấy tháng từ đối tượng ngày/ngày giờ. |
| `lay_ngay`      | `day`            | Lấy ngày trong tháng từ đối tượng ngày/ngày giờ. |
| `lay_gio`       | `hour`           | Lấy giờ từ đối tượng thời gian/ngày giờ. |
| `lay_phut`      | `minute`         | Lấy phút từ đối tượng thời gian/ngày giờ. |
| `lay_giay`      | `second`         | Lấy giây từ đối tượng thời gian/ngày giờ. |
| `lay_thu_trong_tuan`| `weekday()`  | Lấy thứ trong tuần (0=Thứ 2, 6=Chủ nhật). |
| `lay_thu_trong_tuan_chu_nhat_dau`| `isoweekday() % 7`| Lấy thứ trong tuần (0=Chủ nhật, 6=Thứ 7). |
| `ten_thu`       | Custom           | Lấy tên thứ trong tuần bằng tiếng Việt. |
| `ten_thang`     | Custom           | Lấy tên tháng bằng tiếng Việt. |
| `cong_ngay`     | `timedelta`      | Cộng số ngày vào một ngày. |
| `cong_tuan`     | `timedelta`      | Cộng số tuần vào một ngày. |
| `cong_thang`    | Custom           | Cộng số tháng vào một ngày. |
| `cong_nam`      | Custom           | Cộng số năm vào một ngày. |
| `tru_ngay`      | `timedelta`      | Tính số ngày giữa hai ngày. |
| `tru_gio`       | `total_seconds()`| Tính số giờ giữa hai thời điểm. |
| `tru_phut`      | `total_seconds()`| Tính số phút giữa hai thời điểm. |
| `tru_giay`      | `total_seconds()`| Tính số giây giữa hai thời điểm. |
| `la_nam_nhuan`  | `calendar.isleap`| Kiểm tra có phải năm nhuận không. |
| `so_ngay_trong_thang`| `calendar.monthrange`| Lấy số ngày trong tháng của một năm cụ thể. |
| `ngay_dau_thang`| Custom           | Lấy ngày đầu tiên của tháng. |
| `ngay_cuoi_thang`| Custom          | Lấy ngày cuối cùng của tháng. |
| `ngay_dau_nam`  | Custom           | Lấy ngày đầu tiên của năm. |
| `ngay_cuoi_nam` | Custom           | Lấy ngày cuối cùng của năm. |
| `timestamp`     | `time.time()`    | Lấy timestamp hiện tại. |
| `timestamp_sang_ngay_gio`| `datetime.datetime.fromtimestamp()`| Chuyển timestamp thành đối tượng ngày giờ. |
| `ngay_gio_sang_timestamp`| `timestamp()`| Chuyển đối tượng ngày giờ thành timestamp. |
| `ngu`           | `time.sleep()`   | Tạm dừng chương trình trong số giây. |
| `do_thoi_gian`  | Custom decorator | Đo thời gian thực thi của một hàm. |
| `tuoi`          | Custom           | Tính tuổi từ ngày sinh. |
| `ngay_le_viet_nam`| Custom         | Lấy danh sách các ngày lễ Việt Nam trong năm. |
| `kiem_tra_ngay_le`| Custom         | Kiểm tra xem một ngày có phải là ngày lễ không. |
| `dinh_dang_tieng_viet`| Custom     | Định dạng ngày giờ theo kiểu tiếng Việt. |

## 7. Module `numpy_vn.py` (Wrapper cho NumPy)

| Tên tiếng Việt | Tên gốc (NumPy) | Chức năng |
|-----------------|-----------------|-----------|
| `tao_mang`      | `np.array`      | Tạo mảng từ dữ liệu. |
| `tao_mang_khong`| `np.zeros`      | Tạo mảng chứa toàn số 0. |
| `tao_mang_mot`  | `np.ones`       | Tạo mảng chứa toàn số 1. |
| `tao_mang_rong` | `np.empty`      | Tạo mảng rỗng (không khởi tạo giá trị). |
| `tao_mang_don_vi`| `np.eye`       | Tạo ma trận đơn vị. |
| `tao_day_so`    | `np.arange`     | Tạo dãy số với bước nhảy xác định. |
| `tao_day_tuyen_tinh`| `np.linspace`| Tạo dãy số cách đều trong một khoảng. |
| `tao_mang_ngau_nhien`| `np.random.uniform`| Tạo mảng số thực ngẫu nhiên. |
| `tao_mang_ngau_nhien_nguyen`| `np.random.randint`| Tạo mảng số nguyên ngẫu nhiên. |
| `kich_thuoc_mang`| `shape`        | Lấy kích thước (hình dạng) của mảng. |
| `so_chieu`      | `ndim`          | Lấy số chiều của mảng. |
| `so_phan_tu`    | `size`          | Lấy tổng số phần tử trong mảng. |
| `kieu_du_lieu`  | `dtype`         | Lấy kiểu dữ liệu của các phần tử trong mảng. |
| `doi_hinh_dang` | `reshape`       | Đổi hình dạng (kích thước) của mảng. |
| `lam_phang`     | `flatten`       | Làm phẳng mảng thành mảng 1 chiều. |
| `chuyen_vi`     | `T`             | Chuyển vị ma trận. |
| `noi_mang`      | `np.concatenate`| Nối các mảng theo một trục. |
| `xep_chong_doc` | `np.vstack`     | Xếp chồng các mảng theo chiều dọc. |
| `xep_chong_ngang`| `np.hstack`    | Xếp chồng các mảng theo chiều ngang. |
| `chia_mang`     | `np.split`      | Chia mảng thành các phần. |
| `cong_mang`     | `np.add`        | Cộng hai mảng (từng phần tử). |
| `tru_mang`      | `np.subtract`   | Trừ hai mảng (từng phần tử). |
| `nhan_mang`     | `np.multiply`   | Nhân hai mảng (từng phần tử). |
| `chia_mang`     | `np.divide`     | Chia hai mảng (từng phần tử). |
| `luy_thua_mang` | `np.power`      | Tính lũy thừa của các phần tử trong mảng. |
| `can_bac_hai`   | `np.sqrt`       | Tính căn bậc hai của các phần tử trong mảng. |
| `gia_tri_tuyet_doi`| `np.abs`     | Tính giá trị tuyệt đối của các phần tử trong mảng. |
| `nhan_ma_tran`  | `np.dot`        | Nhân hai ma trận. |
| `tong`          | `np.sum`        | Tính tổng các phần tử trong mảng. |
| `trung_binh`    | `np.mean`       | Tính giá trị trung bình của các phần tử trong mảng. |
| `trung_vi`      | `np.median`     | Tính giá trị trung vị của các phần tử trong mảng. |
| `do_lech_chuan` | `np.std`        | Tính độ lệch chuẩn của các phần tử trong mảng. |
| `phuong_sai`    | `np.var`        | Tính phương sai của các phần tử trong mảng. |
| `gia_tri_nho_nhat`| `np.min`      | Tìm giá trị nhỏ nhất trong mảng. |
| `gia_tri_lon_nhat`| `np.max`      | Tìm giá trị lớn nhất trong mảng. |
| `vi_tri_nho_nhat`| `np.argmin`    | Tìm vị trí (chỉ số) của giá trị nhỏ nhất. |
| `vi_tri_lon_nhat`| `np.argmax`    | Tìm vị trí (chỉ số) của giá trị lớn nhất. |
| `sap_xep`       | `np.sort`       | Sắp xếp các phần tử trong mảng. |
| `chi_so_sap_xep`| `np.argsort`    | Lấy chỉ số sắp xếp của các phần tử. |
| `tim_kiem_nhi_phan`| `np.searchsorted`| Tìm kiếm nhị phân trong mảng đã sắp xếp. |
| `phan_tu_duy_nhat`| `np.unique`    | Lấy các phần tử duy nhất trong mảng. |
| `dieu_kien`     | `np.where`      | Chọn giá trị dựa trên điều kiện. |
| `tat_ca_dung`   | `np.all`        | Kiểm tra tất cả phần tử đều đúng. |
| `co_phan_tu_dung`| `np.any`       | Kiểm tra có phần tử nào đúng không. |
| `sin`           | `np.sin`        | Tính sin của các phần tử trong mảng. |
| `cos`           | `np.cos`        | Tính cosin của các phần tử trong mảng. |
| `tan`           | `np.tan`        | Tính tang của các phần tử trong mảng. |
| `arcsin`        | `np.arcsin`     | Tính arcsin của các phần tử trong mảng. |
| `arccos`        | `np.arccos`     | Tính arccos của các phần tử trong mảng. |
| `arctan`        | `np.arctan`     | Tính arctan của các phần tử trong mảng. |
| `exp`           | `np.exp`        | Tính e mũ x cho các phần tử trong mảng. |
| `log`           | `np.log`        | Tính logarit tự nhiên cho các phần tử trong mảng. |
| `log10`         | `np.log10`      | Tính logarit cơ số 10 cho các phần tử trong mảng. |
| `log2`          | `np.log2`       | Tính logarit cơ số 2 cho các phần tử trong mảng. |
| `lay_pi`        | `np.pi`         | Lấy hằng số Pi (π). |
| `lay_e`         | `np.e`          | Lấy hằng số Euler (e). |
| `luu_mang`      | `np.save`       | Lưu mảng ra file. |
| `tai_mang`      | `np.load`       | Tải mảng từ file. |
| `luu_van_ban`   | `np.savetxt`    | Lưu mảng ra file văn bản. |
| `tai_van_ban`   | `np.loadtxt`    | Tải mảng từ file văn bản. |
| `in_mang`       | `np.printoptions`| In mảng với độ chính xác chỉ định. |

## 8. Module `thuat_toan.py` (Thuật toán và Cấu trúc dữ liệu)

| Tên tiếng Việt | Tên gốc (Python/Thuật toán) | Chức năng |
|-----------------|-----------------------------|-----------|
| `sap_xep_noi_bot`| `Bubble Sort`             | Thuật toán sắp xếp nổi bọt. |
| `sap_xep_chen`  | `Insertion Sort`          | Thuật toán sắp xếp chèn. |
| `sap_xep_lua_chon`| `Selection Sort`         | Thuật toán sắp xếp lựa chọn. |
| `sap_xep_nhanh` | `Quick Sort`              | Thuật toán sắp xếp nhanh. |
| `sap_xep_tron`  | `Merge Sort`              | Thuật toán sắp xếp trộn. |
| `tron_hai_mang` | `Merge`                   | Hàm phụ trợ để trộn hai mảng đã sắp xếp (cho Merge Sort). |
| `sap_xep_dong`  | `Heap Sort`               | Thuật toán sắp xếp đống. |
| `heapify`       | `Heapify`                 | Hàm phụ trợ cho Heap Sort. |
| `tim_kiem_tuyen_tinh`| `Linear Search`       | Tìm kiếm tuyến tính. |
| `tim_kiem_nhi_phan`| `Binary Search`         | Tìm kiếm nhị phân (yêu cầu mảng đã sắp xếp). |
| `tim_kiem_noi_suy`| `Interpolation Search`  | Tìm kiếm nội suy. |
| `Ngan_xep`      | `Stack`                   | Cấu trúc dữ liệu ngăn xếp (LIFO). |
| `day_vao`       | `push`                    | Đẩy phần tử vào ngăn xếp. |
| `lay_ra`        | `pop`                     | Lấy phần tử ra khỏi ngăn xếp. |
| `xem_dinh`      | `peek`                    | Xem phần tử ở đỉnh ngăn xếp. |
| `rong`          | `is_empty`                | Kiểm tra ngăn xếp có rỗng không. |
| `kich_thuoc`    | `size`                    | Lấy kích thước ngăn xếp. |
| `Hang_doi`      | `Queue`                   | Cấu trúc dữ liệu hàng đợi (FIFO). |
| `them_vao`      | `enqueue`                 | Thêm phần tử vào hàng đợi. |
| `lay_ra`        | `dequeue`                 | Lấy phần tử ra khỏi hàng đợi. |
| `xem_dau`       | `peek`                    | Xem phần tử đầu hàng đợi. |
| `Hang_doi_uu_tien`| `Priority Queue`        | Cấu trúc dữ liệu hàng đợi ưu tiên. |
| `duyet_theo_chieu_rong`| `BFS`              | Duyệt đồ thị theo chiều rộng. |
| `duyet_theo_chieu_sau`| `DFS`                | Duyệt đồ thị theo chiều sâu. |
| `duong_di_ngan_nhat_dijkstra`| `Dijkstra`  | Thuật toán Dijkstra tìm đường đi ngắn nhất. |
| `fibonacci`     | `Fibonacci`               | Tính số Fibonacci thứ n (không đệ quy). |
| `fibonacci_de_quy`| `Fibonacci (recursive)`| Tính số Fibonacci thứ n (đệ quy). |
| `gcd`           | `math.gcd`                | Tìm ước chung lớn nhất (GCD). |
| `lcm`           | Custom                    | Tìm bội chung nhỏ nhất (LCM). |
| `la_so_nguyen_to`| Custom                   | Kiểm tra số nguyên tố. |
| `sang_eratosthenes`| `Sieve of Eratosthenes`| Sàng Eratosthenes tìm tất cả số nguyên tố <= n. |
| `dao_nguoc_danh_sach`| `[::-1]`             | Đảo ngược danh sách. |
| `xao_tron`      | `random.shuffle`          | Xáo trộn danh sách. |
| `lay_mau_ngau_nhien`| `random.sample`       | Lấy k phần tử ngẫu nhiên từ danh sách. |
| `tim_phan_tu_xuat_hien_nhieu_nhat`| Custom | Tìm phần tử xuất hiện nhiều nhất trong danh sách. |
| `loai_bo_trung_lap`| Custom                 | Loại bỏ phần tử trùng lặp trong danh sách. |
| `giao_hai_tap`  | `set.intersection`        | Tìm giao của hai tập hợp. |
| `hop_hai_tap`   | `set.union`               | Tìm hợp của hai tập hợp. |
| `hieu_hai_tap`  | `set.difference`          | Tìm hiệu của hai tập hợp. |



