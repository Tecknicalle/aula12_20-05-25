import pandas as pd

categoria_escolares = ['Lit br','Lit est' 'Cênc', 'Mat', 'Hist']
qnt_livros = [12, 9, 18, 14, 20]

livros = pd.Series(qnt_livros, qnt_livros)  # index=

qnt_emp_escolares = [4, 2, 7, 5, 6]

print("\nQuantidade de livros")

print(qnt_livros)


print("\nQuantidade de livros emprestados: ")
# print(qnt_livros)# ['Literatura Brasileira', 'Ciências', 'Matemática', 'Hst']
print(qnt_emp_escolares)

# nao_contido["Filosofia"] = None



