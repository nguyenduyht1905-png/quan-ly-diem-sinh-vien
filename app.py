import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SỐ VÀ THỐNG KÊ SINH VIÊN")
st.write("Ứng dụng quản lý điểm, xếp loại và trực quan hóa dữ liệu sinh viên.")

data = {
    'Họ và tên': [
        'Lê Dương Bảo Lâm', 'Kiều Minh Tuấn', 'Phan Lê Minh Tinh', 'Ngô Kiến Huy', 
        'Trần Minh Hiếu', 'Ninh Dương Lan Ngọc', 'Huỳnh Trấn Thành', 'Liên Bình Phát', 
        'Phạm Duy Thuận', 'Trần Phan Quốc Bảo'
    ],
    'Điểm chuyên cần': [8.0, 9.0, 7.0, 9.5, 7.5, 7.0, 9.0, 7.0, 7.5, 9.5],
    'Điểm giữa kỳ': [7.5, 8.0, 7.5, 9.0, 7.0, 7.0, 8.5, 7.0, 7.5, 9.0],
    'Điểm cuối kỳ': [8.0, 8.5, 7.5, 9.0, 7.5, 7.0, 8.5, 7.0, 7.5, 9.5]
}

df = pd.DataFrame(data)

df['Điểm tổng kết'] = (
    0.20 * df['Điểm chuyên cần'] + 
    0.30 * df['Điểm giữa kỳ'] + 
    0.50 * df['Điểm cuối kỳ']
).round(2)

def xep_loai(dtk):
    if dtk >= 8.5:
        return 'Giỏi'
    elif dtk >= 7.0:
        return 'Khá'
    elif dtk >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại học sinh'] = df['Điểm tổng kết'].apply(xep_loai)

st.subheader("Bảng điểm chi tiết và Xếp loại của sinh viên")
st.dataframe(df)

dtb_lop = df['Điểm tổng kết'].mean()
sv_max = df.loc[df['Điểm tổng kết'].idxmax()]
sv_min = df.loc[df['Điểm tổng kết'].idxmin()]
so_sv_dat = (df['Điểm tổng kết'] >= 5.0).sum()

st.subheader("Thông tin thống kê chung")
st.markdown(f"- **Điểm tổng kết trung bình của lớp:** {dtb_lop:.2f}")
st.markdown(f"- **Sinh viên có điểm cao nhất:** {sv_max['Họ và tên']} ({sv_max['Điểm tổng kết']} điểm)")
st.markdown(f"- **Sinh viên có điểm thấp nhất:** {sv_min['Họ và tên']} ({sv_min['Điểm tổng kết']} điểm)")
st.markdown(f"- **Số sinh viên đạt ($\ge 5.0$):** {so_sv_dat}")

st.subheader("Biểu đồ cột thể hiện điểm tổng kết của sinh viên")
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df['Họ và tên'], df['Điểm tổng kết'], color='orange', edgecolor='black')

ax.set_title('BIỂU ĐỒ THỂ HIỆN ĐIỂM TỔNG KẾT CỦA SINH VIÊN', fontsize=14, fontweight='bold')
ax.set_xlabel('Họ và tên sinh viên', fontsize=12)
ax.set_ylabel('Điểm tổng kết', fontsize=12)
ax.set_ylim(0, 10.5)

for i, v in enumerate(df['Điểm tổng kết']):
    ax.text(i, v + 0.15, f"{v:.2f}", ha='center', fontsize=10, fontweight='bold')

plt.xticks(rotation=30, ha='right', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

st.pyplot(fig)
