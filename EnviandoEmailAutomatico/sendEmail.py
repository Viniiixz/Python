import win32com.client as win

# enviar um email com o relatório
outlook = win.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'carlos.vinicius.dev@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Envio teste.</p>

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Carlos Vinícius</p>
'''

mail.Send()

print('Email Enviado')
