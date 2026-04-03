!pip install reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from google.colab import files

def criar_relatorio(lang="pt"):
    if lang == "pt":
        filename = "Tese_Geopolitica_Brasil_2026_PT.pdf"
        title = "DOCUMENTO TÉCNICO: O ACORDO ALCÂNTARA E A TRI-POLARIDADE GLOBAL (2026)"
        author = "Autor: Especialista Multidisciplinar (Direito, Engenharias, Saúde e Gestão)"
        sections = [
            ("SUMÁRIO EXECUTIVO", "Análise da transição do Brasil para motor industrial do Hemisfério Sul sob a égide do eixo Washington-Brasília (Doutrina Trump/Vance)."),
            ("1. O TABULEIRO TRIPOLAR", "Consolidação de três esferas de influência: EUA (Américas/Europa/Oriente Médio), China (Ásia/Semicondutores) e Rússia (Neo-URSS)."),
            ("2. BRASIL: A TAIWAN DAS AMÉRICAS", "Integração vertical da Petrobras no refino de Terras Raras e produção de semicondutores para garantir a autossuficiência do bloco americano."),
            ("3. HUB AEROESPACIAL ALCÂNTARA-SPACEX", "Uso estratégico da posição geográfica brasileira para domínio lunar e marcial, gerando soberania técnica e astronautas nacionais."),
            ("4. DEFESA QUÂNTICA E CIBERSEGURANÇA", "Aplicação de IA e criptografia quântica para anular a espionagem chinesa, movida pela ambição e meritocracia da nova classe média."),
            ("5. DEMOGRAFIA E SOCIEDADE", "Ressurgimento da classe média com alta taxa de natalidade, sustentada por um modelo de saúde privado próspero e educação de elite por mérito."),
            ("CONCLUSÃO", "O fim da 'Terceira Via' e a ascensão de um Brasil Americanizado: soberania por competência, estabilidade pelo petróleo barato (V8) e hegemonia do dólar.")
        ]
    else:
        filename = "Geopolitical_Thesis_Brazil_2026_EN.pdf"
        title = "TECHNICAL PAPER: THE ALCÂNTARA ACCORD AND GLOBAL TRI-POLARITY (2026)"
        author = "Author: Multidisciplinary Specialist (Law, Engineering, Health, and Management)"
        sections = [
            ("EXECUTIVE SUMMARY", "Analysis of Brazil's transition to the industrial engine of the Southern Hemisphere under the Washington-Brasília axis (Trump/Vance Doctrine)."),
            ("1. THE TRI-POLAR CHESSBOARD", "Consolidation of three spheres of influence: USA (Americas/Europe/Middle East), China (Asia/Semiconductors), and Russia (Neo-USSR)."),
            ("2. BRAZIL: THE TAIWAN OF THE AMERICAS", "Vertical integration of Petrobras into Rare Earths refining and semiconductor production to ensure the American bloc's self-sufficiency."),
            ("3. ALCÂNTARA-SPACEX AEROSPACE HUB", "Strategic use of Brazilian geographic positioning for Lunar and Martian dominance, generating technical sovereignty and national astronauts."),
            ("4. QUANTUM DEFENSE AND CYBERSECURITY", "Application of AI and quantum cryptography to neutralize Chinese espionage, driven by the ambition and meritocracy of the new middle class."),
            ("5. DEMOGRAPHICS AND SOCIETY", "Resurgence of the middle class with high birth rates, supported by a prosperous private health model and elite merit-based education."),
            ("CONCLUSION", "The end of the 'Third Way' and the rise of an Americanized Brazil: sovereignty through competence, stability through cheap oil (V8), and dollar hegemony.")
        ]

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Estilo Justificado
    style_justify = ParagraphStyle(name='Justify', parent=styles['Normal'], alignment=TA_JUSTIFY, fontSize=11, leading=14)
    style_title = ParagraphStyle(name='CenterTitle', parent=styles['Title'], alignment=TA_CENTER, fontSize=16, spaceAfter=20)

    story = []
    story.append(Paragraph(title, style_title))
    story.append(Paragraph(author, styles['Italic']))
    story.append(Spacer(1, 20))

    for sec_title, sec_text in sections:
        story.append(Paragraph(f"<b>{sec_title}</b>", styles['Heading2']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(sec_text, style_justify))
        story.append(Spacer(1, 12))

    doc.build(story)
    files.download(filename)

# Gerar ambos
criar_relatorio(lang="pt")
criar_relatorio(lang="en")
