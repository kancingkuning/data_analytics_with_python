import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import datetime

#fungsi markdown - menampilkan output dari argument markdown
st.markdown(
    """
# Plis Bisa
udah capek banget"""
)

#fungsi write untuk nulis
st.write(pd.DataFrame({
    'c1': [1,2,3,4],
    'c2': [2,3,4,5]
}))

#fungsi title - menampilkan teks format judul 
st.title('boleh diadu')

#fungsi header untuk ya format header
st.header('Pengembangan diriku')


#fungsi subheader untuk ya format subheader
st.subheader('ya gini gini aja')

#fungsi caption, untuk output teks ukuran kecil 
st.caption('hak cipta ada')

#fungsi code sebagai dibawah ini
code = """def hello():
print("bisa sih harusnya")"""
st.code(code, language='python')

#fungsi text
st.text('halo teman2')

#fungsi latex
st.latex(r"""
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)""")

#fungsi dataframe
df = pd.DataFrame({
    'aku': [5,6,7,8],
'kamu': [2,3,4,5]
})
st.dataframe(data=df, width=500, height=150)

#fungsi table() -- opsi lain dataframe func
st.table(data=df)

#fungsi metric
st.metric(label='Temperature', value="28 ℃", delta="1.2 ℃")

#fungsi json()
st.json({
    'kol': [1,'c',3],
    'kol2': [3,5,7]
})

x = np.random.normal(15,5,250)

fig, ax= plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

#text input function, untuk mendapatkan single-line text
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama: ', name)

#multi-line text, text area
text = st.text_area('Pesan dan Kesan')
st.write('Feedback: ', text)

#number input, masukan berupa angka
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), 'tahun')

#date input, masukin tanggal
date = st.date_input(label='Tgl lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tgl lahir: ', date)

#fungsi upload file
uploaded_file = st.file_uploader('masukin csvmu')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

#fungsi camera input

pic = st.camera_input('silakan masukan poto')
if pic:
    st.image(pic)

#button widget = button, checkbox, radio button
    
if st.button('halo'):
    st.write('hai')

agree = st.checkbox('setuju')

if agree:
    st.write('selamat datang')

genre = st.radio(
    label='genre film yg lo suka apa',
    options=('cinta', 'drama', 'scifi'),
    horizontal=False
)

#fungsi select box, opsi alternatif radio button
musik = st.selectbox(
    label='apa musik yg lo suka',
    options=('indie', 'shoegaze', 'jazz')
)

#fungsi multi, bs pilih banyak 
bacaan = st.multiselect(
    label='apa bacaan yg lo suka',
    options=('filsapat', 'kiri', 'kanan')
)

#slider untuk rentang
nilai = st.slider(
    label='pilih jarak yg km mau', 
    min_value=0, max_value=100, value=(0,100)
)
st.write('jarak yg km mau:', nilai)

#LAYOUTING

#sidebar
st.title('judul-judulan')

with st.sidebar:
    st.text('ini sidebar')

    values= st.slider(
        label='pilih range nilai',
        min_value=0, max_value=100, value=(0,100)
    )
    st.write('Values:', values)


#columns

col1,col2,col3 = st.columns([1, 2, 1])

with col1:
    st.header("Kucing")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Anjeng")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Burng")
    st.image("https://static.streamlit.io/examples/owl.jpg")


#tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

#container
with st.container():
    st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
 
st.write("Outside the container")

#expander
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) 
 
with st.expander("See explanation"):
    st.write(
        """contoh gambar bar chart ya guys ini kayak gitu deh
        """
    )