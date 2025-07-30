"""
Định nghĩa các token cho ViPython-VN
"""

from enum import Enum, auto

class TokenType(Enum):
    # Literals
    SO = auto()           # số (number)
    THUC = auto()         # thực (float)
    VAN_BAN = auto()      # văn bản (string)
    LOGIC = auto()        # logic (boolean)
    
    # Identifiers
    TEN_BIEN = auto()     # tên biến (identifier)
    
    # Keywords
    NEU = auto()          # nếu (if)
    KHAC = auto()         # khác (else)
    NEU_KHAC = auto()     # nếu khác (elif)
    TRONG_KHI = auto()    # trong khi (while)
    VOI = auto()          # với (for)
    HAM = auto()          # hàm (def)
    TRA_VE = auto()       # trả về (return)
    DUNG = auto()         # dừng (break)
    TIEP_TUC = auto()     # tiếp tục (continue)
    LOP = auto()          # lớp (class)
    THUOC_TINH = auto()   # thuộc tính (self)
    NHAP = auto()         # nhập (import)
    TU = auto()           # từ (from)
    THU = auto()          # thử (try)
    BAT = auto()          # bắt (except)
    CUOI_CUNG = auto()    # cuối cùng (finally)
    DUNG_LAI = auto()     # dừng lại (pass)
    TRONG = auto()        # trong (in)
    LA = auto()           # là (is)
    KHONG = auto()        # không (not)
    VA = auto()           # và (and)
    HOAC = auto()         # hoặc (or)
    DUNG_VAY = auto()     # đúng vậy (True)
    SAI_VAY = auto()      # sai vậy (False)
    KHONG_CO = auto()     # không có (None)
    
    # Operators
    CONG = auto()         # + (plus)
    TRU = auto()          # - (minus)
    NHAN = auto()         # * (multiply)
    CHIA = auto()         # / (divide)
    CHIA_NGUYEN = auto()  # // (floor divide)
    CHIA_DU = auto()      # % (modulo)
    LUY_THUA = auto()     # ** (power)
    
    # Comparison
    BANG = auto()         # == (equal)
    KHONG_BANG = auto()   # != (not equal)
    NHO_HON = auto()      # < (less than)
    LON_HON = auto()      # > (greater than)
    NHO_HON_BANG = auto() # <= (less than or equal)
    LON_HON_BANG = auto() # >= (greater than or equal)
    
    # Assignment
    GAN = auto()          # = (assign)
    CONG_BANG = auto()    # += (plus assign)
    TRU_BANG = auto()     # -= (minus assign)
    NHAN_BANG = auto()    # *= (multiply assign)
    CHIA_BANG = auto()    # /= (divide assign)
    
    # Delimiters
    NGOAC_TRON_MO = auto()    # (
    NGOAC_TRON_DONG = auto()  # )
    NGOAC_VUONG_MO = auto()   # [
    NGOAC_VUONG_DONG = auto() # ]
    NGOAC_NHON_MO = auto()    # {
    NGOAC_NHON_DONG = auto()  # }
    PHAY = auto()             # ,
    HAI_CHAM = auto()         # :
    CHAM_PHAY = auto()        # ;
    CHAM = auto()             # .
    
    # Special
    XUONG_DONG = auto()   # newline
    THUT_LE = auto()      # indent
    BO_THUT_LE = auto()   # dedent
    KET_THUC = auto()     # EOF
    
    # Comments
    BINH_LUAN = auto()    # # comment

# Từ khóa ViPython
KEYWORDS = {
    'neu': TokenType.NEU,
    'khac': TokenType.KHAC,
    'neu_khac': TokenType.NEU_KHAC,
    'trong_khi': TokenType.TRONG_KHI,
    'voi': TokenType.VOI,
    'ham': TokenType.HAM,
    'tra_ve': TokenType.TRA_VE,
    'dung': TokenType.DUNG,
    'tiep_tuc': TokenType.TIEP_TUC,
    'lop': TokenType.LOP,
    'thuoc_tinh': TokenType.THUOC_TINH,
    'nhap': TokenType.NHAP,
    'tu': TokenType.TU,
    'thu': TokenType.THU,
    'bat': TokenType.BAT,
    'cuoi_cung': TokenType.CUOI_CUNG,
    'dung_lai': TokenType.DUNG_LAI,
    'trong': TokenType.TRONG,
    'la': TokenType.LA,
    'khong': TokenType.KHONG,
    'va': TokenType.VA,
    'hoac': TokenType.HOAC,
    'dung_vay': TokenType.DUNG_VAY,
    'sai_vay': TokenType.SAI_VAY,
    'khong_co': TokenType.KHONG_CO,
}

class Token:
    def __init__(self, type_: TokenType, value: str, line: int, column: int):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"

