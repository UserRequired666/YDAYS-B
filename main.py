from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Matths Curicullum')

import streamlit as st

st.title('Mais QUI est Matthieu Denieul Le Diraison ?')
# Display an image from a local file
current_path = Path().parent if "file" in locals() else Path.cwd()
st.image(Image.open(current_path / "asset" / "image_moi_1.jpg"))

#cursus scolaire info
st.title('Mon Cursus Scolaire')
st.write('2022/2023 -B1 Informatique chez Ynov')
st.write('2023/2024 -B2 Informatique chez Ynov')
st.write('2021-2022: L1 Licence Management Uni Montpellier')
st.write('2019-2020 : 1ère année Rennes School of Business: International Bachelor Program in Management ')
st.write('2016-2019: Lycée Français de Barcelone (Baccalaureate ES)')
st.write('2018:  Bismarck High School: North Dakota USA including Marketing, Psychology, History, Theater')
st.write('2016-2017: “Brevet d*Initiation Aéronautique” (BIA)')
st.write('2013-2015: Collège Brizeux Lorient : Brevet des Collèges Mention TB')
st.write('2011-2012: Killarney Heights Public School : Sydney : Australie')

#langues parlées
st.title('Langues')

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.header('Maîtrise complet')
    st.write('English: C2')
    st.write('French: C2')
with col2:
    st.header('Maîtrise partiel')
    st.write('Spanish: C1')

#compétences techniques
st.header('Capacités informatiques')
st.write('photoshop Beau Art Lorient 2015-2016')
st.write('Adobe illustrator Beau Art Lorient 2015-2016')


st.title('COMMENT ME JOINDRE')
st.header('mes infos:')
col1,col2 = st.columns(2, gap="medium")
with col1:
        st.header('telephone:')
        st.write('+33651727692')
with col2:
        st.header('email')
        st.write('matthieu.denieullediraison@ynov.com')
        
        
st.warning('vous arrivez à la fin de ce CV')