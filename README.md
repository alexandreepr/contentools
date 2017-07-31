## Project Description

This web crawler was developed using a framework called Scrapy, specific for web crawling and structured data extraction.
Basically, it defines the domains that will be covered, the initial requisitions and how to handle the result of these requisitions.
After this, various forms of data output can be generated, including a .CSV file.


## Steps to run the project
	
	1. Open the project directory in the terminal
	2. Type the command below to output the crawler results in a csv file
	
```
scrapy crawl agency -o agencies.csv
```

if you don't have scrapy installed, run the following command in the terminal:

```
pip install scrapy
```

Or follow the structions from Scrapy [documentation](https://docs.scrapy.org/en/latest/) if you need further details on how to install it.

## Descrição do Projeto

Este web crawler foi desenvolvido usando uma estrutura chamada Scrapy, específica para rastreamento web e extração de dados estruturados.
Basicamente, ele define os domínios que serão rastreados, as requisições iniciais e como tratar o resultado dessas requisições.
Após isso, várias formas de saída de dados podem ser geradas, incluindo um arquivo .CSV.

## Passos para rodar o projeto
	
	1. Abra o diretório do projeto no terminal
	2. Escreva o comando abaixo para o crawler gerar um arquivo csv com o resultado
	
```
scrapy crawl agency -o agencies.csv
```

se você não tiver o scrapy instaldo, execute o seguinte comando no terminal:

```
pip install scrapy
```

Ou siga as instruções Scrapy [documentation](https://docs.scrapy.org/en/latest/) se você precisar de mais detalhes na instalação.

