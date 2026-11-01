# 🐍 Python
Com o Python, o arquivo desse dataset foi organizado e reformulado, devido a várias discrepâncias de formatação. Todos os dados estavam juntos em uma coluna só no Excel, com as informações apenas separadas por vírgulas e algumas palavras embaralhadas, devido a não conter a codificação de caracteres UTF-8, deixando diversas palavras com símbolos estranhos. Essa é o arquivo cru e sem formatações:<br>
<br>
<img width="649" height="304" alt="image" src="https://github.com/user-attachments/assets/4e4db659-cd86-4e19-af64-d52ba4986601" />

Após a formatação utilizando o código incluso na pasta de arquivos nomeado como `organizacaoUTF8.py`, ficou tudo da seguinte forma:<br>
<br>
<img width="411" height="300" alt="image" src="https://github.com/user-attachments/assets/d341faa3-eed7-4684-ab36-2baed5839516" />

Após essa organização, podemos seguir a análise dos dados com mais exatidão e organização.<br>
<br>
# Excel
No Excel podemos identificar dados incoerentes com a formatação condicional, podendo assim marcar dados incorretos com a cor vermelha.<br>
### Imóveis sem banheiro
Foram identificados 37 imóveis sem banheiro com o comando =CONT.SE(D:D; 0), que identifica se na coluna que indica a quantidade de banheiros no imóvel se tem algum valor igual à 0. Dado que é incoerente, pois até pequenas kitnets de 10m², possuem banheiro integrado.<br>
<br>
Um exemplo dessa situação está situada na linha 1004, imóvel do tipo apartamento de 28m², que não possue um banheiro.<br>

<img width="584" height="240" alt="image" src="https://github.com/user-attachments/assets/a990b40a-8b88-4a8e-81a1-9a79d5377746" />

### Imóveis com 9 ou menos m²
Foram identificados 7 imóveis com 9 ou menos m² com o comando =CONT.SE(C:C; "<=9"), que identifica na coluna que indica o tamanho do imóvel se tem algum valor menor ou igual a 9. De acordo com o documentário feito pelo site [Exame](https://exame.com/mercado-imobiliario/menor-apartamento-pais-10-metros-quadrados-preco-200-mil/), diz que o menor imóvel registrado em São Paulo possui 10m².<br>
<br>
Um exemplo dessa situação está situada na linha 964, imóvel do tipo Studio e Kitnet que possui apenas 1m², 1 banheiro e 1 vaga para garagem.<br>

<img width="575" height="222" alt="image" src="https://github.com/user-attachments/assets/faaee2a7-21d1-47f1-8686-d5fbc53353a2" />




