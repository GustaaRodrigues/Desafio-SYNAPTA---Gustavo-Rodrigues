# 🐍 Python
Com o Python, o arquivo desse dataset foi organizado e reformulado, devido a várias discrepâncias de formatação. Todos os dados estavam juntos em uma coluna só no Excel, com as informações apenas separadas por vírgulas e algumas palavras embaralhadas, devido a não conter a codificação de caracteres UTF-8, deixando diversas palavras com símbolos estranhos. Essa é o arquivo cru e sem formatações:<br>
<br>
<img width="649" height="304" alt="image" src="https://github.com/user-attachments/assets/4e4db659-cd86-4e19-af64-d52ba4986601" />

Após a formatação utilizando o código incluso na pasta de arquivos nomeado como `organizacaoUTF8.py`, ficou tudo da seguinte forma:<br>
<br>
<img width="411" height="300" alt="image" src="https://github.com/user-attachments/assets/d341faa3-eed7-4684-ab36-2baed5839516" />

Após essa organização, podemos seguir a análise dos dados com mais exatidão e organização.<br>
<br>
# 📊 Excel
No Excel podemos identificar dados incoerentes com a formatação condicional, além de poder calcular valores por colunas.<br>
## Para baixar o arquivo clique aqui -> [data_organizado.xlsx](https://github.com/user-attachments/files/34244786/data_organizado.xlsx)
### 🚽 Imóveis sem banheiro
Foram identificados 37 imóveis sem banheiro com o comando =CONT.SE(D:D; 0), que identifica se na coluna que indica a quantidade de banheiros no imóvel se tem algum valor igual à 0. Dado que é incoerente, pois até pequenas kitnets de 10m², possuem banheiro integrado.<br>
<br>
Um exemplo dessa situação está situada na linha 1004, imóvel do tipo apartamento de 28m², que não possue um banheiro.<br>

<img width="584" height="240" alt="image" src="https://github.com/user-attachments/assets/a990b40a-8b88-4a8e-81a1-9a79d5377746" />

### 🏠 Imóveis com 9 ou menos m²
Foram identificados 7 imóveis com 9 ou menos m² com o comando =CONT.SE(C:C; "<=9"), que identifica na coluna que indica o tamanho do imóvel se tem algum valor menor ou igual a 9. De acordo com o documentário feito pelo site [Exame](https://exame.com/mercado-imobiliario/menor-apartamento-pais-10-metros-quadrados-preco-200-mil/), diz que o menor imóvel registrado em São Paulo possui 10m².<br>
<br>
Um exemplo dessa situação está situada na linha 964, imóvel do tipo Studio e Kitnet que possui apenas 1m², 1 banheiro e 1 vaga para garagem.<br>

<img width="575" height="222" alt="image" src="https://github.com/user-attachments/assets/faaee2a7-21d1-47f1-8686-d5fbc53353a2" />

# 🔢 Calculo de média e mediana dos valores de aluguel
A partir de comandos no Excel, criei novas colunas mostrando a média e a mediana dos valores de aluguel.<br>
### 🧮 Calculo da média
O calculo da média é definido coletando todos os valores da coluna e dividindo pela quantidades de linhas disponíveis, nesse caso seria 37.894.748 dividido por 11.658, que da 3250 reais. <br>
<br>
Esse calculo foi feito a partir do comando =MÉDIA(G:G), ele é mostrado na coluna L arquivo.<br>

<img width="512" height="296" alt="image" src="https://github.com/user-attachments/assets/b8604f2f-10f1-48d7-86fb-ffd0bc1d37ba" />


### 🧮 Calculo da mediana
O calculo da mediana é definido coletando todos os valores e separando do menor para o maior, o valor mediano é o valor que está no centro dessa separação. <br>
<br>
Nesse caso, o valor mediano é 2415 reais e foi encontrado a partir do comando =MED(G:G), ele é mostrado na coluna M do arquivo.<br>

<img width="547" height="321" alt="image" src="https://github.com/user-attachments/assets/f4e9ec79-2ffa-4116-a26f-42081a781c66" />

# 📊 Bairros com maiores e menores preços médios
Por meio do Power BI, fiz um gráfico de barras empilhadas, mostrando o valor os bairros com o valor médio mais caro até o mais barato em ordem decrescente, utilizando filtros para calcular valor médio.<br>

### Bairros com valor médio mais caro:
<img width="595" height="334" alt="image" src="https://github.com/user-attachments/assets/ea79d471-0d4f-42df-802f-6ca9693ce8e3" />

### Bairros com valor médio mais barato:
<img width="587" height="329" alt="image" src="https://github.com/user-attachments/assets/021066bf-bad4-4fb3-8b53-6941f6a7afc1" />













