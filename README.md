### Introdução
Projeto de software do sistema de uma livraria, para conclusão da disciplina Engenharia de Software II, pela Universidade Federal do Piaui - UFPI (CSHNB).
#### Escopo do produto:
Uma determinada livraria precisa de um sistema para realizar a venda de livros de modo que haja a interação do cliente com o vendedor e do cliente com o sistema.
Fazendo com que o cliente sinta mais comodidade e segurança na hora de realizar suas compras de forma“independente”.
#### Limites do produto:
1. O LivrariaSI irá gerenciar informações de pagamento (cliente) e estoque de livros.
2. O sistema irá realizar buscas por parte do cliente e funcionário, onde o cliente irá solicitar uma compra do produto buscado e o funcionário será o responsável por validar essa compra (mediante pagamento e disponibilidade no estoque).
3. No que se refere ao Funcionário é necessário um registro para o gerenciamento dos dados de estoque e venda onde contém seus dados pessoais (nome, e-mail, senha, ID). O sistema também poderá cancelar uma venda caso não tenha disponibilidade de estoque ou ausência de pagamento.
4. Na parte de Cliente, não haverá qualquer tipo de cadastro. Haverá a possibilidade de somente buscar por um livro, solicitar uma compra ou cancelar essa compra.


	Todo o projeto está sendo desenvolvido na linguagem de programação python em sua versão 3.7, e para criação de interface gráfica do projeto foi utilizado a biblioteca Tkinter, tendo como fonte a própria documentação da linguagem, para o banco de dados está sendo utilizado o módulo Shelve.

### Processos e Técnicas
Foi utilizado para o presente desenvolvimento do projeto o modelo incremental no qual o mesmo foi avaliado em um ciclo de desenvolvimento dirigido por testes de caixa preta para compor cada incremento do projeto e dessa forma sua versão funcional.

### Tarefas alocadas
Código  | Pontos| Situação|
------------- | -------------|-------
 Criação login de Funcionários | 7 pts| OK
Criação Do Crud De Livros  | 4 pts | OK
Construção Da Validação De Compras  | 3 pts | OK
Construção Do Campo De Busca De Livros | 3 pts | OK
Gerar Compra  | 2 pts | OK
Testes Finais  | 1 pts | OK
