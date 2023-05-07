import streamlit as st

from streamlit_option_menu import option_menu

# navigasi sidebar:
with st.sidebar :
    selected = option_menu ('Menghitung Luas Dan Volume Bangun',
    ['Luas Bangun Datar Persegi Panjang',
    'Luas Bangun Datar Segitiga', 
    'Luas Bangun Datar Persegi',
    'Luas Bangun Datar Jajar Genjang',
    'Luas Bangun Datar Layang-layang',
    'Luas Bangun Datar Trapesium',
    'Luas Bangun Datar Lingkaran'],
    default_index=0)

st.caption('*POLITEKNIK AKA BOGOR*')
st.markdown('Dibuat oleh **1E (PMIP): kelompok 10.**')
st.caption(':smile:_:blue["Matematika mengajarkan bahwa tidak ada masalah di dunia ini tanpa solusi."]_ :sunglasses:')

# halaman luas bangun datar persegi panjang
if (selected == 'Luas Bangun Datar Persegi Panjang') :
    st.title('Luas Bangun Datar Persegi Panjang')
    
    panjang = st.number_input ("Masukan Nilai Panjang (cm)", 0)
    lebar = st.number_input ("Masukan Nilai Lebar (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = panjang * lebar
        st.success (f"Luas Persegi Panjang Adalah = {luas} cm^2")

# halaman hitung luas segitiga
if (selected == 'Luas Bangun Datar Segitiga') :
    st.title('Luas Bangun Datar Segitiga')

    alas = st.number_input ("Masukan Nilai Alas (cm)", 0, 1000)
    tinggi = st.number_input ("Masukan Nilai Tinggi (cm)", 0, 1000)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 0,5 * alas * tinggi
        st.success (f"Luas Segitiga Adalah = {luas} cm^2")

# halaman hitung luas persegi 
if (selected == 'Luas Bangun Datar Persegi') :
    st.title('Luas Bangun Datar Persegi')

    sisx = st.number_input ("Masukan Nilai Sisi (cm) ", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = sisx * sisx
        st.success (f"Luas Persegi Adalah {luas} cm^2")

# halaman hitung luas jajar genjang
if (selected == 'Luas Bangun Datar Jajar Genjang') :
    st.title('Luas Bangun Datar Jajar Genjang')

    alas = st.number_input ("Masukan Nilai Alas (cm)", 0)
    tinggi = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = alas * tinggi
        st.success (f"Luas Jajar Genjang Adalah = {luas} cm^2")

# halaman hitung luas layangan 
if (selected == 'Luas Bangun Datar Layang-layang') :
    st.title('Luas Bangun Datar Layang-layang')

    x = st.number_input ("Masukan Nilai d1 (cm)", 0)
    y = st.number_input ("Masukan Nilai d2 (cm)", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 0,5 * x * y
        st.success (f"Luas Layang- layang Adalah = {luas} cm^2")

# halaman hitung luas Trapesium 
if (selected == 'Luas Bangun Datar Trapesium') :
    st.title('Luas Bangun Datar Trapesium')

    a = st.number_input ("Masukan Nilai Sisi Sejajar Atas (cm)", 0)
    b = st.number_input ("Masukan Nilai Sisi Sejajar Bawah (cm)", 0)
    t = st.number_input ("Masukan Nilai t (cm)", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = ((a + b) / 2) * t
        st.success (f"Luas Trapesium Adalah = {luas} cm^2")

# halaman hitung luas Lingkaran
if (selected == 'Luas Bangun Datar Lingkaran'):
    st.title('Luas Bangun Datar Lingkaran')

    r = st.number_input ("Masukan Nilai r (cm)", 0)
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = 3.14 * r * r
        st.success (f"Luas Lingkaran Adalah = {luas} cm^2")
