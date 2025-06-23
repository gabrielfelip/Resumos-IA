import streamlit as st
from pdf_utils import extrair_texto_pdf
from summarizer import gerar_resumo
from youtube_utils import extrair_transcricao_youtube

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
        font-size: 2.5rem !important;
    }
    textarea, button, input {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="Gerador de Resumos com IA", layout="centered")

if "historico" not in st.session_state:
    st.session_state.historico = []

# Título principal
st.title("🧠 Gerador de Resumos Inteligente")
st.caption("Envie um PDF ou cole um link do YouTube para gerar um resumo com inteligência artificial local.")

st.divider()

# Tabs: Principal e Histórico
aba_principal, aba_historico = st.tabs(["📄 PDF e YouTube", "🕘 Histórico"])

# ----------------- 📄 Aba Principal -----------------
with aba_principal:
    # Upload de PDF
    st.subheader("📄 Upload de PDF")
    arquivo_pdf = st.file_uploader("Selecione um PDF", type=["pdf"])

    if arquivo_pdf is not None:
        texto_extraido = extrair_texto_pdf(arquivo_pdf)

        st.markdown("#### 📃 Texto extraído:")
        st.text_area("Conteúdo extraído", texto_extraido, height=300)

        if st.button("📝 Gerar Resumo do PDF"):
            with st.spinner("Gerando resumo com IA..."):
                resumo = gerar_resumo(texto_extraido)

            st.success("✅ Resumo gerado com sucesso!")
            st.markdown("#### 📌 Resumo do PDF:")
            st.write(resumo)

            st.download_button(
                label="📥 Baixar Resumo (.txt)",
                data=resumo,
                file_name="resumo.txt",
                mime="text/plain"
            )

            st.session_state.historico.append({
                "tipo": "PDF",
                "conteudo": texto_extraido,
                "resumo": resumo
            })

    st.divider()

    # Link do YouTube
    st.subheader("📹 Resumo de Vídeo do YouTube")
    url_video = st.text_input("📎 Cole o link do vídeo")

    if url_video and st.button("🎬 Gerar Resumo do Vídeo"):
        with st.spinner("Transcrevendo vídeo..."):
            texto_video = extrair_transcricao_youtube(url_video)

        if texto_video.startswith("Erro"):
            st.error(texto_video)
        else:
            st.success("✅ Transcrição capturada!")
            st.markdown("#### 📝 Trecho da Transcrição:")
            st.text_area("Transcrição parcial", texto_video[:1000], height=200)

            with st.spinner("Gerando resumo com IA..."):
                resumo_video = gerar_resumo(texto_video)

            st.markdown("#### 📌 Resumo do Vídeo:")
            st.write(resumo_video)

            st.download_button(
                label="📥 Baixar Resumo do Vídeo (.txt)",
                data=resumo_video,
                file_name="resumo_video.txt",
                mime="text/plain"
            )

            st.session_state.historico.append({
                "tipo": "YouTube",
                "conteudo": texto_video,
                "resumo": resumo_video
            })

# ----------------- 🕘 Aba Histórico -----------------
with aba_historico:
    st.subheader("🕘 Histórico de Resumos")

    if st.session_state.historico:
        for i, item in enumerate(reversed(st.session_state.historico), 1):
            with st.expander(f"{i}. Tipo: {item['tipo']}"):
                st.text_area("📄 Conteúdo Original", item['conteudo'][:1000], height=150, key=f"c_{i}")
                st.text_area("📌 Resumo", item['resumo'], height=150, key=f"r_{i}")
    else:
        st.info("Nenhum resumo gerado ainda nesta sessão.")
