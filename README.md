
# Sistema Bancário em Python

## Caso Proposto

Um grande banco contratou nossa equipe para desenvolver a primeira versão de seu novo sistema bancário. O objetivo é modernizar suas operações utilizando a linguagem Python.

Nesta versão inicial (v1), o sistema deve permitir depósitos, saques e emissão de extrato bancário.

---

## Funcionalidades Implementadas

### Operação de Depósito

* Permite depositar valores positivos na conta bancária.
* Os valores depositados são armazenados em uma variável.
* Cada depósito é registrado e exibido no extrato.
* Não há necessidade de número de conta ou agência (sistema com apenas 1 usuário).

### Operação de Saque

* O usuário pode realizar até 3 saques diários.
* O limite máximo por saque é de R$ 500,00.
* Caso o saldo seja insuficiente, o sistema informa que não é possível sacar.
* Todos os saques são armazenados e exibidos no extrato.

### Operação de Extrato

* Exibe todas as transações (depósitos e saques).
* Ao final, mostra o saldo atual da conta.
* Os valores são formatados no padrão: R$ xxx.xx.

---

## Regras de Negócio

| Regra           | Descrição                     |
| --------------- | ----------------------------- |
| Depósito        | Apenas valores positivos      |
| Saque           | Máximo de 3 saques por dia    |
| Limite de Saque | R$ 500,00 por operação        |
| Extrato         | Exibe histórico e saldo atual |


