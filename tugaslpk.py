import streamlit as st

from streamlit_option_menu import option_menu

# navigasi sidebar:
with st.sidebar :
    selected = option_menu ('Menghitung Luas Dan Volume Bangun',
    ['Informasi Singkat',
    'Luas Bangun Datar Persegi Panjang',
    'Luas Bangun Datar Segitiga', 
    'Luas Bangun Datar Persegi',
    'Luas Bangun Datar Jajar Genjang',
    'Luas Bangun Datar Layang-layang',
    'Luas Bangun Datar Trapesium',
    'Luas Bangun Datar Lingkaran',
    'Luas dan Volume Kubus',
    'Luas dan Volume Balok',
    'Luas dan Volume Limas',
    'Luas dan Volume Kerucut',
    'Luas dan Volume Prisma Segitiga',
    'Luas dan Volume Tabung',
    'Luas dan Volume Bola',],
    default_index=0)

st.caption('*POLITEKNIK AKA BOGOR*')
st.markdown('Dibuat oleh **1E (PMIP): kelompok 10.**')
st.caption(':male-teacher:_:blue["Matematika mengajarkan bahwa tidak ada masalah di dunia ini tanpa solusi."]_')

# halaman informasi singkat
if (selected == 'Informasi Singkat') :
    st.title('Bangun Datar dan Bangun Ruang')
    st.write('Bangun datar merupakan sebuah bangun geometri dua yang memiliki permukaan datar serta memiliki dua dimensi, yakni panjang dan lebar. Permukaan bagun datar biasanya dibatasi oleh garis lurus ataupun lengkung.Bangun datar mempunyai berbagai bentuk, seperti segitiga, persegi, persegi panjang, lingkaran, trapesium, dan jajargenjang. Bangun ruang adalah sebuah bangun geometri yang berisikan volume dan isi, selain itu juga bangun ruang juga memiliki tiga komponen penyusun lain berupa dimensi tiga yang mempunyai sifat-sifat tertentu, yakni dengan adanya sisi (bidang), rusuk, dan titik sudut. Adapun macam-macam bangun ruang, yaitu kubus, balok, prisma, limas, tabung, kerucut, dan bola')

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

    alas = st.number_input ("Masukan Nilai Alas (cm)")
    tinggi = st.number_input ("Masukan Nilai Tinggi (cm)")
    hitung = st.button ("Hitung Luas")

    if hitung :
        luas = (alas * tinggi)/2
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
        luas = (x * y)/2
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
        luas = 3.14 *(r * r)
        st.success (f"Luas Lingkaran Adalah = {luas} cm^2")
        
# halaman hitung luas dan volume kubus
if (selected == 'Luas dan Volume Kubus') :
    st.title('Luas Kubus')
    
    r = st.number_input ("Masukan Nilai Panjang Rusuk (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 6*r*r
        st.success (f"Luas Kubus Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Kubus') :
    st.title('Volume kubus')
    
    r = st.number_input ("Masukan Nilai Panjang rusuk (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = r*r*r
        st.success (f"Volume Kubus Adalah = {Volume} cm^3")

# halaman hitung luas dan volume Balok
if (selected == 'Luas dan Volume Balok') :
    st.title('Luas Balok')
    
    p = st.number_input ("Masukan Nilai Panjang (cm)", 0)
    l = st.number_input ("Masukan Nilai Lebar (cm)", 0)
    t = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 2*((p*l)+(p*t)+(l*t))
        st.success (f"Luas Balok Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Balok') :
    st.title('Volume Balok')
    
    p = st.number_input ("Masukan Nilai panjang (cm)", 0)
    l = st.number_input ("Masukan Nilai lebar (cm)", 0)
    t = st.number_input ("Masukan Nilai tinggi (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = p*l*t
        st.success (f"Volume Balok Adalah = {Volume} cm^3")

# halaman hitung luas dan volume Limas
if (selected == 'Luas dan Volume Limas') :
    st.title('Luas Limas')
    
    la = st.number_input ("Masukan Nilai Luas Alas (cm)", 0)
    ls = st.number_input ("Masukan Nilai Luas Sisi Tegak (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = la+ls
        st.success (f"Luas Limas Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Limas') :
    st.title('Volume Limas')
    
    la = st.number_input ("Masukan Nilai Luas alas (cm)", 0)
    t = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = 0.3*la*t
        st.success (f"Volume Limas Adalah = {Volume} cm^3")

# halaman hitung luas dan volume Kerucut
if (selected == 'Luas dan Volume Kerucut') :
    st.title('Luas Kerucut')
    
    r = st.number_input ("Masukan Nilai jari-jari (cm)", 0)
    s = st.number_input ("Masukan Nilai garis miring (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 3.14*r*(r+s)
        st.success (f"Luas Limas Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Kerucut') :
    st.title('Volume Kerucut')
    
    r = st.number_input ("Masukan Nilai Jari-jari (cm)", 0)
    t = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = 0.3*3.14*r*r*t
        st.success (f"Volume Kerucut Adalah = {Volume} cm^3")
        
# halaman hitung luas dan volume Prisma Segitiga
if (selected == 'Luas dan Volume Prisma Segitiga') :
    st.title('Luas Prisma Segitiga')
    
    la = st.number_input ("Masukan Nilai Luas alas (cm)", 0)
    ka = st.number_input ("Masukan Nilai Keliling alas (cm)", 0)
    t = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = (2*la)+(ka*t)
        st.success (f"Luas Prisma Segitiga Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Prisma Segitiga') :
    st.title('Volume Prisma Segitiga')
    
    la = st.number_input ("Masukan Nilai Luas Alas (cm)", 0)
    t = st.number_input ("Masukan Nilai tinggi (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = la*t
        st.success (f"Volume Prisma Segitiga Adalah = {Volume} cm^3")

# halaman hitung luas dan volume Tabung
if (selected == 'Luas dan Volume Tabung') :
    st.title('Luas Tabung')
    
    r = st.number_input ("Masukan Nilai Jari-Jari (cm)", 0)
    t = st.number_input ("Masukan Nilai Tinggi (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 2*3.14*r*(t+r)
        st.success (f"Luas Tabung Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Tabung') :
    st.title('Volume Tabung')
    
    r = st.number_input ("Masukan Nilai Jari-jari (cm)", 0)
    t = st.number_input ("Masukan Nilai tinggi (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = 3.14*r*r*t
        st.success (f"Volume Tabung Adalah = {Volume} cm^3")
        
# halaman hitung luas dan volume Bola
if (selected == 'Luas dan Volume Bola') :
    st.title('Luas Bola')
    
    r = st.number_input ("Masukan Nilai Jari-Jari (cm)", 0)
    hitung = st.button ("Hitung Luas")
    
    if hitung :
        luas = 4*3.14*r*r
        st.success (f"Luas Bola Adalah = {luas} cm^2")
        
if (selected == 'Luas dan Volume Bola') :
    st.title('Volume Bola')
    
    r = st.number_input ("Masukan Nilai Jari-jari (cm)", 0)
    hitung = st.button ("Hitung Volume")
    
    if hitung :
        Volume = 1.3*3.14*r*r*r
        st.success (f"Volume Bola Adalah = {Volume} cm^3")
