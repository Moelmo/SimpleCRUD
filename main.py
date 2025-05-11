import streamlit as st 

st.title("Simple CRUD")

if "namalist" not in st.session_state:
    st.session_state.namalist = []

def tambah():
    if new not in st.session_state.namalist:
        st.session_state.namalist.append(new)
        st.success("Nama berhasil di tambahkan", icon="✅")
    else:
        st.warning("Nama sudah terdaftar", icon="⚠️")

def hapus():
    if remove in st.session_state.namalist:
        item_number = st.session_state.namalist.index(remove)
        st.success(f"Nama {remove} berhasil di hapus")
        del st.session_state.namalist[item_number]
    else:
        st.warning(f"Tidak ada nama {remove} di dalam list", icon="⚠️")

def edit():

    if old_name in st.session_state.namalist:
        item_number = st.session_state.namalist.index(old_name)
        st.session_state.namalist[item_number] = new_name
        st.success(f"Nama {old_name} Berhasil di ubah ke {new_name}", icon="✅")
    else:
        st.warning(f"Nama {old_name} tidak ada di dalam list", icon="⚠️")

new = st.text_input("Masukkan nama yang ingin di tambahkan")
if st.button("Tambah", icon="➕"):
    if new:
        tambah()
    else:
        st.error("Masukkan nama terlebih dahulu", icon="❌")

remove = st.text_input("Masukkan nama yang ingin di hapus")
if st.button("Hapus", icon="🗑️"):
    if remove:
        hapus()
    else:
        st.error("Masukkan nama terlebih dahulu", icon="❌")

old_name = st.text_input("Masukkan nama yang ingin anda ganti")
new_name = st.text_input("Ganti nama dengan yang baru")
if st.button("Ganti", icon="♻️"):
    if old_name:
        edit()
    else:
        st.error("Masukkan nama yang ingin kamu ubah", icon="⚠️")

st.subheader("Daftar Nama")
if st.session_state.namalist:
    st.write(f"Jumlah nama dalam data : {len(st.session_state.namalist)}")
    data = [{"No": i, "Nama":nama} for i, nama in enumerate(st.session_state.namalist, start=1)]
    st.dataframe(data)
else:
    st.write("Tidak ada nama di dalam list")



# COPYRIGHT

st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 25px; color: #555;">
        <p>Follow us on:</p>
        <a href="https://github.com" target="https://github.com/Moelmo" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" width="35" height="35" alt="GitHub" />
        </a>
        <a href="https://discord.com" target="https://discord.users/" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111370.png" width="35" height="35" alt="Discord" />
        </a>
        <a href="https://www.tiktok.com" target="https://tiktok.com/@moelmo57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/4782/4782345.png" width="35" height="35" alt="TikTok" />
        </a>
        <a href="https://www.instagram.com" target="https://instagram.com/moelmo.57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111463.png" width="35" height="35" alt="Instagram" />
        </a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 25px; color: #888;'>© Moelmo 2025</p>", unsafe_allow_html=True)