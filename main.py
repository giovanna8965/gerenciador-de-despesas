import tkinter as tk
from expense import Expense
from expense_manager import ExpenseManager

# Função para adicionar uma despesa
def add_expense():
    name = entry_name.get()
    amount = float(entry_amount.get())
    category = entry_category.get()
    expense = Expense(name, amount, category)
    manager.add_expense(expense)
    update_summary()

# Função para atualizar o resumo das despesas na interface 
def update_summary():
    text_summary.config(state=tk.NORMAL)
    text_summary.delete("1.0", tk.END)
    for expense in manager.expenses:
        text_summary.insert(tk.END, f"{expense.name}: ${expense.amount} ({expense.category})\n")
    text_summary.insert(tk.END, f"\nTotal de Despesas: ${manager.total_expenses()}\n")
    text_summary.config(state=tk.DISABLED)

manager = ExpenseManager()

# Configuração da interface 
root = tk.Tk()
root.title("Gerenciador de Despesas")

label_name = tk.Label(root, text="Nome:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_amount = tk.Label(root, text="Valor:")
label_amount.grid(row=1, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1, padx=5, pady=5)

label_category = tk.Label(root, text="Categoria:")
label_category.grid(row=2, column=0, padx=5, pady=5)
entry_category = tk.Entry(root)
entry_category.grid(row=2, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Adicionar Despesa", command=add_expense)
button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_summary = tk.Label(root, text="Resumo de Despesas:")
label_summary.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
text_summary = tk.Text(root, height=10, width=50)
text_summary.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
text_summary.config(state=tk.DISABLED)

root.mainloop()
