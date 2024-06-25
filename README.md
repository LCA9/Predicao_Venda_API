
### IPNET.ipynb
Arquivo que contem todo o processo de treinamento do modelo. Na primeira parte foi feita o carregamento e  analises inicias, quantidade de linhas do arquivo, features, tipos dos dados, analise preliminar dos outliers, valores nulos e duplicados. Posteriormente foram retirados os outliers que que ficaram inferiores ao limite inferior. No tópico seguinte, foram feitas analises com as features, mostrando suas realações e tendências. Posteriormente, os dados foram Padronizados. Utilizou-se na etapa seguinte o cross validation para treina e testa o modelo. Na penultipa etapa foram comparados os modelos. E por ultimo foi salvo o modelo com a melhor performance.

### back_end.py
Constrói a API com FastAPI e utiliza o modelo XGBoost. Assim que a Api recebe os inputs em são padronizados por meio de uma função, pois foi assim que o modelo foi treinado.

O modelo obteve a seguintes métricas
MAE: 1.615 , MSE: 66;743 , MAPE: 0.829 e R²: 0.109

### front_end.py
Front-end da aplicação, utilizando Streamlit. Possui layout com 3 campos, fatures que o modelo foi treinado.


### Configurações iniciais e Comando para funcinamento da aplicação
Utilize o comando pip install -r requirements.txt no terminal, para instalar as bibliotecas itlizadas. Posteriormente de run no documento back_end.py para inicializa-lô. Por ultimo utilize o comando streamlit run front_end para iniciar o streamlit.


posteriormente copie e cole no url do browser:http://localhost:8501/



