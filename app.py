
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import re
from datetime import datetime

from utils.salvar_dados import salvar_dados_usuario

st.title("Know Your Fan - Cadastro Interativo")
aba1, aba2= st.tabs(["Cadastro do Fã", "Upload de Documento"])

with aba1:
    st.header("1. Cadastro do Fã")

    with st.form("form_fan"):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF", placeholder="000.000.000-00")
        data_nascimento = st.text_input("Data de Nascimento", placeholder="DD/MM/AAAA")
        endereco = st.text_input("Endereço")
        interesses = st.text_area("Quais jogos, times ou eventos de esports você mais gosta?")
        eventos = st.text_area("Quais eventos você participou no último ano?")
        compras = st.text_area("Compras relacionadas à esports (ex: ingressos, camisetas, etc)?")

        st.markdown("---")
        st.subheader("🔗 Redes Sociais (Opcional)")
        instagram = st.text_input("Usuário do Instagram (sem @)", placeholder="ex: furia")
        twitter = st.text_input("Usuário do Twitter (sem @)", placeholder="ex: furia")
        facebook = st.text_input("Usuário do Facebook", placeholder="ex: furiaesports")
        outros_links = st.text_input("Outro link relevante (LinkedIn, Site pessoal, etc)", placeholder="https://...")

        submitted = st.form_submit_button("Salvar dados")
                
    if submitted:
        if not nome or not cpf or not endereco:
            st.error("❌ Preencha todos os campos obrigatórios: nome, CPF e endereço.")
        elif not re.match(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf):
            st.error("❌ CPF inválido! Use o formato 000.000.000-00.")
        elif not data_nascimento:
            st.error("❌ Data de nascimento é obrigatória.")
        else:
            try:
                data_nascimento_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date().isoformat()
                path = salvar_dados_usuario(
                    nome, cpf, endereco, interesses, eventos, compras,
                    data_nascimento_formatada, instagram, twitter, facebook, outros_links
                )
                st.success(f"✅ Dados salvos com sucesso em `{path}`!")
            except ValueError:
                st.error("❌ Data de nascimento inválida. Use o formato DD/MM/AAAA.")

with aba2:
    st.header("2. Upload de Documento (RG ou CNH)")

    doc_file = st.file_uploader("Envie uma imagem do seu documento", type=["jpg", "jpeg", "png"])

    if doc_file:
        img = Image.open(doc_file).convert("RGB")
        img_np = np.array(img)

        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            st.success(f"✅ Rosto detectado com sucesso! ({len(faces)} rosto(s))")
            st.image(img, caption="Documento com rosto detectado", use_container_width=True)

            if not os.path.exists("uploads"):
                os.makedirs("uploads")
            with open(os.path.join("uploads", doc_file.name), "wb") as f:
                f.write(doc_file.getbuffer())
        else:
            st.error("❌ Nenhum rosto detectado. Tente enviar uma imagem melhor.")

