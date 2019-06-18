<p align="center">
<img src="https://scontent.fpcs1-1.fna.fbcdn.net/v/t1.0-9/64892376_332220464342171_7808059873349861376_n.jpg?_nc_cat=106&_nc_oc=AQkii1-lirgl1lqFdFFGBSN4reaLo88_-7HmHRMjfpeKUdW_0xGmyNo7XnC4iGaKRIQ&_nc_ht=scontent.fpcs1-1.fna&oh=3ce2e073fcd0055e187e41a4e4b5620e&oe=5DC184C3" alt="LivrariaSI" />
</p>

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


### Diagramas
[![Caso e Uso](https://scontent.fpcs1-1.fna.fbcdn.net/v/t1.0-9/65015628_332224777675073_8953840329107177472_n.jpg?_nc_cat=101&_nc_oc=AQkX7Inz2jhqOybxbgn_R6cpIp5fzIO0D4u-VkxZkGYfLHmWvkXbamHl2SF78VgMs24&_nc_ht=scontent.fpcs1-1.fna&oh=fd2b40215ebf9e439dbfaebc49aea84f&oe=5DC2685C "Caso e Uso")](https://scontent.fpcs1-1.fna.fbcdn.net/v/t1.0-9/65015628_332224777675073_8953840329107177472_n.jpg?_nc_cat=101&_nc_oc=AQkX7Inz2jhqOybxbgn_R6cpIp5fzIO0D4u-VkxZkGYfLHmWvkXbamHl2SF78VgMs24&_nc_ht=scontent.fpcs1-1.fna&oh=fd2b40215ebf9e439dbfaebc49aea84f&oe=5DC2685C "Caso e Uso")



.

.




[![Classes](https://scontent.fpcs1-1.fna.fbcdn.net/v/t1.0-9/64418289_332224791008405_1624337248159793152_n.jpg?_nc_cat=105&_nc_oc=AQkuGO3VJ1-nRURHW-DDZPV6LrerxkOFUbNj9IjQcqt-nrz2bm189rIlues6LIOqvD0&_nc_ht=scontent.fpcs1-1.fna&oh=6ebc0a4352f9aa24002e4ca23db78165&oe=5D89D5F5 "Classes")](https://scontent.fpcs1-1.fna.fbcdn.net/v/t1.0-9/64418289_332224791008405_1624337248159793152_n.jpg?_nc_cat=105&_nc_oc=AQkuGO3VJ1-nRURHW-DDZPV6LrerxkOFUbNj9IjQcqt-nrz2bm189rIlues6LIOqvD0&_nc_ht=scontent.fpcs1-1.fna&oh=6ebc0a4352f9aa24002e4ca23db78165&oe=5D89D5F5 "Classes")

### Tarefas alocadas
Código  | Pontos| Situação|
------------- | -------------|-------
 Criação login de Funcionários | 7 pts| OK
Criação Do Crud De Livros  | 4 pts | OK
Construção Da Validação De Compras  | 3 pts | OK
Construção Do Campo De Busca De Livros | 3 pts | OK
Gerar Compra  | 2 pts | OK
Testes Finais  | 1 pts | OK
