# Know Your Fan - FURIA Challenge 2 🦊🎮

Projeto desenvolvido como parte do processo seletivo para a vaga de Assistente em Engenharia de Software na FURIA.  
O objetivo é criar uma aplicação interativa que colete e organize dados sobre fãs de e-sports, integrando validação de documentos e informações de redes sociais.

---

## 📌 Funcionalidades

- 📋 Coleta de dados básicos (nome, CPF, endereço, data de nascimento).
- 🎮 Registro de interesses, eventos e compras relacionadas ao último ano.
- 🌐 Campos opcionais para inserção de perfis em redes sociais (Instagram, Twitter, Facebook e outros links).
- 📸 Upload de documento (RG/CNH) com detecção facial usando OpenCV.
- 💾 Salvamento local dos dados em arquivos `.json`.

---

## 🚀 Como rodar o projeto

1. Clone este repositório
   ```bash
   git clone https://github.com/seu-usuario/know-your-fan.git
   cd know-your-fan

2. Crie um ambiente virtual (opcional, mas recomendado)
   ```bash 
   python -m venv venv

Ative o ambiente:
- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate

3. Instale as dependências
   ```bash
   pip install -r requirements.txt

4. Execute o app
   ```bash
   streamlit run app.py

---

## 📂 Estrutura do Projeto

know-your-fan/
├── dados/
├── uploads/
├── utils/
│   └── salvar_dados.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt

---

## 📸 Demonstração
O vídeo `furia-tech-challenge2-diego.mp4` mostra o aplicativo em ação.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit (Interface web)
- OpenCV (Detecção facial)
- Pillow (Manipulação de imagens)

---

## 📄 Licença

Este projeto é de uso exclusivo para fins de avaliação técnica no processo seletivo da FURIA.
Não é permitido o uso ou reprodução fora desse contexto sem autorização prévia.

---

## ⚠️ Observações Técnicas

- O projeto não armazena dados em nuvem, apenas localmente.
- A validação facial utiliza OpenCV HaarCascade e ocorre localmente.
- Integração com IA avançada (ex: DeepFace) pode ser adicionada futuramente.
- Bibliotecas como face_recognition exigem compiladores extras, por isso foram evitadas por simplicidade e portabilidade.

---

🚀 Let's go FURIA! 🦊🔥



