import pandas as pd

produtos = {
    'produto': ['lapis', 'caneta', 'borracha', 'caderno', 'mochila'],
    'preço': [1.50, 2.00, 0.50, 10.00, 30.00]
}
df = pd.DataFrame(produtos)
print('dataframe: ')
print(df)

media_precos = df['preço'].mean()

print('Média de preço: ', media_precos)
