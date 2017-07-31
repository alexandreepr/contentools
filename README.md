## Project Descprition

Este web crawler foi desenvolvido usando uma estrutura chamada Scrapy, específica para rastreamento web e extração de dados estruturados.


This web crawler was developed using a framework called Scrapy, specific for web crawling and structured data extraction.
Basicamente, ele define os domínios que serão rastreados, as requisições iniciais e como tratar o resultado dessas requisições.
Após isso, várias formas de saída de dados podem ser geradas, incluindo um arquivo .CSV.


## Steps to run the project
	
	1. Open the project directory in the terminal
	2. Type the command below to output the crawler results in a csv file
	
```
scrapy crawl agency -o agencies.csv
```

if you don't have scrappy installed, run the following command in the terminal:

```
pip install scrapy
```

Or follow the structions from Scrapy [documentation](https://docs.scrapy.org/en/latest/) if you need further details on how to install it.
