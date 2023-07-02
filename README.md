# guru
Automação da Aplicação GURU99 para disciplina de testes web. Foi utilizado o framework Selenium com Python.

Link da aplicação: https://demo.guru99.com/v4/

Tecnologias necessárias: 
  - Python
  - Selenium
  - Pytest

Observações: 
  - Para cada Teste feito foi realiazado a criação dos casos de testes;
  - O script/caso de teste 2 (test_delete_customer) está com uma bug. No momento em que o gerente tenta deletar um cliente(customer) o sistema diz que não existe aquele customerID. Mas caso o gerente tente editar os dados cadastrais de um cliente(customer) através do mesmo customerID é possível. Vale salientar que caso você queira reproduzir esse cenário é necessário que tente editar primeiro, para depois tentar deletar, já que a deleção é feita mesmo o sistema dizendo que o customerID não existe.
