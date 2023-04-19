from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_protected_pdf(title, message, password):
    # Cria um novo arquivo PDF
    pdf = canvas.Canvas(title + '.pdf', pagesize=letter)

    # Define a senha de abertura do arquivo
    pdf.setEncrypt(password)

    # Adiciona a mensagem na página
    pdf.drawString(100, 700, message)

    # Fecha o arquivo PDF
    pdf.save()

    print('PDF criado com sucesso!')


# Exemplo de uso
#create_protected_pdf('Meu PDF Protegido', 'Este é o meu primeiro PDF criado com Python e ReportLab.', 'minha_senha')
