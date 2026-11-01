# 📊 Desafio SYNAPTA - Gustavo Rodrigues

Este repositório contém o projeto desenvolvido como requisito avaliativo para ingresso no SYNAPTA (Laboratório de Dados e Inteligência Artificial) do Centro Universitário Maurício de Nassau (UNINASSAU), realizado sob a supervisão e orientação da professora Vitória Freire.

# 📌 Dataset escolhido: Preços de imóveis em São Paulo

Nesse dataset contém uma análise detalhada sobre preços de aluguel em São Paulo. Mostra os seguintes dados em relação aos imóveis:<br>
<br>
* Endereço: Contém o nome da rua; <br>
* Bairro: O bairro onde é localizado.<br>
* Tamanho: Tamanho do imóvel em metros quadrados.<br>
* Quartos: O total de número de quartos.<br>
* Garagem: Número de vagas de estacionamento disponíveis.<br>
* Aluguel: O valor do aluguel mensal do imóvel.<br>
* Tipo: O tipo de propriedade (apartamento, casa, etc.)<br>
* Total: O custo total do imóvel, incluindo aluguel, impostos e outras taxas.<br>
<br>
Nesse dataset contém 11658 imóveis, contendo em cada imóvel as informações descritas acima.
<br>

# 🛠️ Ferramentas utilizadas

* _Python & VS Code_ - O arquivo do dataset original continha erros de codificação de caracteres (acentos e cedilhas corrompidos devido à falta de UTF-8) e colunas desalinhadas por vírgulas nos endereços. Através do Python e VS Code, os dados foram realinhados e padronizados no formato UTF-8.<br>
* _Excel_ - Após realinhar e padronizar toda a tabela, consegui detectar algumas incoerências utilizando filtros de formatação condicional nas colunas. Foi utilizado a formatação igual a 0, para identificar valores nulos e formatação menor ou igual a 8, para identificar imóveis com menos de 8 metros quadrados.
