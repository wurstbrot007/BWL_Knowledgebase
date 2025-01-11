import streamlit as st
import PyPDF2
import openai
import os

# OpenAI API Key
os.environ["OPENAI_API_KEY"] = "sk-XXXXXX"  # Ersetze das mit deinem OpenAI-Schlüssel

# App Titel
st.title("Dokumentenbasierte Frage-Antwort-App")

# Schritt 1: Dokument hochladen
st.header("1. Lade ein PDF-Dokument hoch")
uploaded_file = st.file_uploader("Ziehe hier ein PDF hinein oder wähle eine Datei aus", type="pdf")

# Dokumentinhalt extrahieren
if uploaded_file:
    st.success(f"Die Datei {uploaded_file.name} wurde erfolgreich hochgeladen!")
    
    # PDF-Inhalt extrahieren
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    document_text = ""
    for page in pdf_reader.pages:
        document_text += page.extract_text()

    st.info("Das Dokument wurde erfolgreich verarbeitet. Jetzt kannst du Fragen dazu stellen!")

    # Schritt 2: Frage eingeben
    st.header("2. Frage eingeben")
    question = st.text_input("Was möchtest du über das Dokument wissen?")
    
    if question:
        # OpenAI API Anfrage
        prompt = f"Beantworte die folgende Frage basierend auf diesem Text:\n\n{document_text}\n\nFrage: {question}\nAntwort:"
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=200
            )
            st.header("Antwort der KI")
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"Ein Fehler ist aufgetreten: {e}")
