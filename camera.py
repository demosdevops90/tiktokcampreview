import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TikTok Camera Preview", layout="centered")

# --- INTERFAZ DE USUARIO ---
st.title("TikTok Preview Style")

# --- CÓDIGO HTML/JS PARA LA CÁMARA ---
# Este código crea el visor y el punto rojo parpadeante arriba
camera_html = """
<div id="container" style="position: relative; width: 100%; max-width: 400px; height: 600px; background: black; border-radius: 20px; overflow: hidden; margin: auto;">
    <div id="rec-dot" style="position: absolute; top: 20px; left: 20px; width: 15px; height: 15px; background: red; border-radius: 50%; z-index: 10; animation: blink 1s infinite;"></div>
    <span style="position: absolute; top: 17px; left: 45px; color: white; font-family: sans-serif; font-weight: bold; z-index: 10;">REC</span>

    <video id="video" autoplay playsinline muted style="width: 100%; height: 100%; object-fit: cover;"></video>
</div>

<style>
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
</style>

<script>
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" }, audio: false })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Error accediendo a la cámara: ", err);
        });
</script>
"""

# Renderizar el componente en Streamlit
components.html(camera_html, height=650)

st.write("Si no ves la cámara, asegúrate de dar permisos en el candado de la barra de direcciones.")
