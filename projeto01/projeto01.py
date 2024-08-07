from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(horas_previstas) * int(valor_hora)

pdv = FPDF()

pdv.add_page()
pdv.set_font("Arial")

pdv.image("template.png", x=0, y=0)

pdv.text(115, 145, projeto)
pdv.text(115, 160, horas_previstas)
pdv.text(115, 175, valor_hora)
pdv.text(115, 190, prazo)
pdv.text(115, 205, str(valor_total))

pdv.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")