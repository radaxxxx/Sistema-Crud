# Sistema de Gerenciamento de Alunos

Sistema CRUD completo em Python para gerenciamento de alunos, funcionando no terminal.

## 📋 Funcionalidades

- **Cadastrar**: Adiciona novos alunos com nome, matrícula e nota
- **Listar**: Exibe todos os alunos ordenados por nota
- **Atualizar**: Modifica dados de alunos existentes
- **Remover**: Remove alunos do sistema
- **Relatório**: Gera estatísticas (total, aprovados, reprovados, média geral)

## 🚀 Como usar

Execute o arquivo Python:

```bash
python sistema_alunos.py
```

Siga o menu interativo para realizar as operações desejadas.

## 📝 Estrutura

- **Armazenamento**: Lista de dicionários
- **Validações**: Nome não vazio, matrícula única, nota entre 0-10
- **Situação automática**: Aprovado (≥7.0), Recuperação (≥5.0), Reprovado (<5.0)

## 💡 Recursos Avançados

- `sorted()` com `lambda` para ordenar alunos por nota
- List comprehension para filtrar alunos por situação
- `enumerate()` para numeração na listagem

👥 Autores
-Ryan Porto Antunes, João Manoel de Sousa Morais






