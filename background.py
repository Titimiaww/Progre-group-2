import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Transformasi Gambar Group 2", layout="wide")

# Menambahkan gambar latar belakang universitas dengan CSS
st.markdown(
    """
    <style>
    body {
        background-image: url("Logo-HD-2.jpg");  /* Ganti dengan URL gambar latar belakang universitas */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.8); /* Membuat latar belakang sidebar sedikit transparan */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar untuk navigasi
menu = ["Home", "Upload & Transform"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

# Judul Utama
st.title("Selamat datang di Website Transformasi Gambar Group 2")

# Konten Berdasarkan Menu yang Dipilih
if choice == "Home":
    st.write("Pilih menu di sebelah kiri untuk memulai!")
    
    st.subheader("Foto Members:")
    st.write("Nama anggota Group 2:")
    
    # Menampilkan foto anggota dengan nama mereka
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Kucing sweg.jpeg", caption="Aep Saepudin")  # Ganti dengan foto asli
    with col2:
        st.image("kucing cool.jpeg", caption="Aliffa Fiqria Wanda")  # Ganti dengan foto asli
    with col3:
        st.image("dog 🐶.jpeg", caption="Siti Khomsiah")  # Ganti dengan foto asli

elif choice == "Upload & Transform":
    st.subheader("Upload Gambar dan Transformasi")
    st.write("Di sini Anda dapat meng-upload gambar dan melakukan transformasi.")
    
    # Membuat uploader untuk gambar
    uploaded_file = st.file_uploader("Pilih gambar untuk di-upload", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Gambar yang di-upload.", use_column_width=True)
        st.write("Gambar berhasil di-upload. Proses transformasi akan dilakukan di sini.")
