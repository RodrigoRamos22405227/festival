# festival

No urls.py organizei a navegação do site para que tudo ficasse ligado. Comecei por definir o app_name como 'festival' para conseguir usar as URLs com nomes nos templates.
Depois, criei as rotas principais: uma para a página inicial, outra para a lista de dias e outra para os palcos. Para as páginas que precisam de mostrar informação específica (como o detalhe de um dia ou de um concerto), usei o parâmetro <int:id>. Fiz isto para que o Django consiga apanhar o ID diretamente da barra de endereço e passá-lo para a função na views.py. Assim, a mesma página adapta-se ao conteúdo que o utilizador clicar.

