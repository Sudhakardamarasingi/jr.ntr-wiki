import streamlit as st

st.set_page_config(page_title="Jr. NTR - Fan Page", layout="wide")

# Sidebar
st.sidebar.title("🎥 Jr. NTR Wiki")
page = st.sidebar.radio("Go to", ["Home", "Biography", "Career", "Filmography", "Awards","Anticipated movies","Message"])

# Header 
st.image("https://i.pinimg.com/736x/cd/52/1b/cd521bef226fe1ea4ba2a12edd742a97.jpg",
         caption="N. T. Rama Rao Jr",
         width=250)

# Home
if page == "Home":
    st.title("Jr. NTR - The Young Tiger 🐯")
    st.write("""
    **Nandamuri Taraka Rama Rao Jr.**, popularly known as **Jr. NTR**, is one of the biggest stars in Telugu cinema.
    Known for his powerful acting, dance skills, and versatility, Jr. NTR is a legacy carrier of the legendary N. T. Rama Rao.

    He is not just an actor, but also a singer, television personality, and philanthropist.
    """)

# Biography
elif page == "Biography":
    st.header("📖 Biography")
    st.write("""
    **Full Name:** Nandamuri Taraka Rama Rao Jr.  
    **Born:** May 20, 1983 — Hyderabad, India  
    **Father:** Nandamuri Harikrishna  
    **Grandfather:** N. T. Rama Rao (former CM of Andhra Pradesh and film legend)

    Jr. NTR began acting as a child artist and made his lead debut in 2001 with *Ninnu Choodalani*. 
    His breakout came with *Student No.1* (2001) and *Simhadri* (2003).
    """)

# Career
elif page == "Career":
    st.header("💼 Career Highlights")
    st.markdown("""
    - Debut as lead actor: *Ninnu Choodalani* (2001)
    - Blockbusters: *Aadi*, *Simhadri*, *Yamadonga*, *Temper*, *Janatha Garage*, *Aravinda Sametha*, *RRR*
    - Versatile roles in action, drama, and mythological films
    - Hosted TV show *Bigg Boss Telugu Season 1*
    - International recognition for *RRR* (2022), especially in the West
    """)

# Filmography
elif page == "Filmography":
    st.header("🎥 Notable Filmography")

    movies = {
        "2001": ["Student No.1"],
        "2003": ["Simhadri"],
        "2007": ["Yamadonga"],
        "2010": ["Brindavanam"],
        "2015": ["Temper"],
        "2016": ["Janatha Garage"],
        "2018": ["Aravinda Sametha Veera Raghava"],
        "2022": ["RRR"]
    }

    for year, films in movies.items():
        st.subheader(f"📅 {year}")
        for film in films:
            st.markdown(f"- {film}")

# Awards
elif page == "Awards":
    st.header("🏆 Awards & Recognition")
    st.write("""
    - 2 × **Filmfare Awards South**
    - 4 × **Nandi Awards**
    - **SIIMA**, **CineMAA**, and **IIFA Utsavam** awards
    - **RRR (2022)** won global praise; nominated at **Golden Globes**, won **Best Song at Oscars** (*Naatu Naatu*)

    Jr. NTR is celebrated for both mass and critical appeal.
    """)

#Anticipated movies
elif page == "Anticipated movies":
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.image("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSVZ1yNwu2MLyl3dqE82OX-dRIAE1gxt6Op5EbdWhTXJCz7aaq7",
         caption="WAR2",
         use_container_width=True)
    with col2:     
        st.image("https://scontent.fblr18-1.fna.fbcdn.net/v/t39.30808-6/488088454_1226089598873434_4650105298467268981_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=833d8c&_nc_ohc=A_kvTtxKjzcQ7kNvwGrah5w&_nc_oc=AdnHe4X5YHsIReruBhz3xFIzTQ-kQLuUOkFc-UL_k-qdWoVAr861x5Y2U_IPehaBCiI&_nc_zt=23&_nc_ht=scontent.fblr18-1.fna&_nc_gid=o_taZAFoGHP3hTLm_mzUHQ&oh=00_AfOwNwLoaqo18cf5iXXdcecvIeBcNE4oGKkcg-tpZwSHnQ&oe=6860FF80",
         caption="Dragon",
         use_container_width=True)
    with col3:     
        st.image("https://cdn.gulte.com/wp-content/uploads/2025/03/Devara-part-2-.jpg",
         caption="Devara-2",
         use_container_width=True)  
    with col4:     
        st.image("god_of_war.jpg",
         caption="GOD OF WAR",
         use_container_width=True)        
#Message
elif page == "Message":
    st.audio("Drive Home Safe - message in public interest by Junior NTR.mp3", format="audio/mpeg", loop=True)

   
# Footer
st.markdown("---")
st.caption("Made with ❤️ not only by Streamlit")
