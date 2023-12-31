# SCS Converter

O SCS Converter é um aplicativo web desenvolvido com o Streamlit que permite realizar conversões em arquivos CSV. Com este aplicativo, você pode fazer upload de um arquivo CSV, selecionar uma opção de conversão e fazer o download do arquivo convertido.

## Funcionalidades

O aplicativo SCS Converter oferece as seguintes funcionalidades:

- Upload de arquivo CSV: Permite que o usuário faça upload de um arquivo CSV a ser convertido.

- Opções de conversão: O usuário pode selecionar uma opção de conversão para alterar o arquivo CSV de acordo com a sua necessidade.

- A coluna 'Type' tem seus valores convertidos de 'P' para 'RP' quando a coluna 'Name' é igual a L", P, Q, R, R', R", T, V, Y, F''' ou O, e caso o pneu seja bordo avolgente, as colunas com 'Name' igual a 'S' também tem seu valor em 'Type' convertida para 'RP' senão mantém da sem alteração.
  
- Um conjunto de dados são concatenados ao final dos arquivos CSV.

- Download do arquivo convertido: Após a conversão, o usuário pode fazer o download do arquivo CSV convertido.

## Como executar o aplicativo

Para executar o aplicativo SCS Converter localmente, siga as instruções abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Recomenda-se usar a versão 3.7 ou superior.

2. Clone o repositório do aplicativo do GitHub:

```
git clone https://github.com/seu-usuario/scs-converter.git
```

3. Acesse o diretório do projeto:

```
cd scs-converter
```

4. Execute o aplicativo:

```
streamlit run app.py
```

5. O aplicativo será aberto em seu navegador padrão. Agora você pode usar o SCS Converter para fazer upload de arquivos CSV e realizar conversões.

## Tecnologias utilizadas

- Python
- Streamlit

## Contribuição

Se você quiser contribuir para o desenvolvimento do SCS Converter, sinta-se à vontade para enviar um pull request no repositório do GitHub. Ficaremos felizes em analisar e incorporar suas contribuições.

---

Esperamos que você encontre o SCS Converter útil e eficiente para suas necessidades de conversão de arquivos CSV. Aproveite o aplicativo e faça suas conversões de forma rápida e fácil!
