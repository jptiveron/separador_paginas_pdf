import os
import PyPDF2

def separa_pdf(caminho_arquivo_entrada, diretorio_saida):
    # Cria o diretório de saída se não existir
    os.makedirs(diretorio_saida, exist_ok=True)

    # Com o arquivo de entrada aberto no modo leitura
    with open(caminho_arquivo_entrada, 'rb') as arquivo_pdf:
        pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
        paginas_total = len(pdf_reader.pages)

        for pagina_numero, pagina in enumerate(pdf_reader.pages, start=1):
            caminho_arquivo_saida = os.path.join(diretorio_saida, f'{pagina_numero}.pdf')
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pagina)

            with open(caminho_arquivo_saida, 'wb') as arquivo_saida:
                pdf_writer.write(arquivo_saida)
                print(f'Pagina {pagina_numero}/{paginas_total} salva em {caminho_arquivo_saida}')


if __name__ == '__main__':
    arquivo_entrada = 'certificados.pdf'
    diretorio_saida = 'certificados_separados'
    separa_pdf(arquivo_entrada, diretorio_saida)

