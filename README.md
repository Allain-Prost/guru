# guru
Automação da Aplicação GURU99 para disciplina de testes web. Foi utilizado o framework Selenium com Python.

Link da aplicação: https://demo.guru99.com/v4/

Tecnologias necessárias: 
  - Python
  - Selenium
  - Pytest

Observações: 
  - Para cada Teste feito foi realiazado a criação dos casos de testes;
  - O script/caso de teste 2 (test_delete_customer) está com um bug. No momento em que o gerente tenta deletar um cliente(customer) o sistema diz que não existe aquele customerID. Mas caso o gerente tente editar os dados cadastrais de um cliente(customer) através do mesmo customerID é possível. Vale salientar que caso você queira reproduzir esse cenário é necessário que tente editar primeiro, para depois tentar deletar, já que a deleção é feita mesmo o sistema dizendo que o customerID não existe.
  - O script/caso de teste 3 (test_edit_customer) está com um bug. No momento que é feito a edição dos dados do cliente(customer) o sistema retornar uma mensagem dizendo que os dados do cliente não foi editado. Mas caso o usuário tente editar novamente os dados do cliente(customer) é possível verificar que os dados passados na edição anterior foram editados com sucesso. Ou seja, o sistema edita os dados mas informa uma mensagem incorreta.

# O GURU99 até o dia 16/07/2023 apresenta várias telas com retorno 500
  - Várias funcionalidades do sistema estão retornar um erro 500. Todas as páginas do sistema podem ser carregadas, mas ao executar as funçãos que cada página desempenha podemos receber um erro 500.

# Anúncios durante a automação 
 - A automação pode ser quebrada por conta de anúncios que o GURU99 possui. Durante a execução dos testes automatizados houve várias interrupções por anúncios, o que acaba impossíbilitando ao selenium encontrar os elementos hmtl.
