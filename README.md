# 🛠️ SE-Tools

Repositório com uma coleção de scripts e utilitários voltados para o dia a dia de um **Sales Engineer (SE)**, com foco em automação, produtividade e suporte a atividades técnicas.

---

## 🎯 Objetivo

Centralizar ferramentas que ajudem em tarefas recorrentes como:

* Automação de processos
* Integração com pipelines e ferramentas de segurança
* Execução de tarefas em massa (multi-repo, multi-ambiente)
* Apoio a demonstrações e troubleshooting

---

## 📦 Conteúdo

Este repositório é organizado por ferramentas, cada uma isolada em sua própria pasta:

```text
SE-Tools/
├── Tools/
│   └── trigger-all-repos/
│       └── trigger-all-repos.py
├── .github/
│   └── workflows/
│       └── trigger-all-repos.yml
└── README.md
```

---

## 🔁 Trigger All Repos

Ferramenta para disparar pipelines (GitHub Actions) em todos os repositórios de uma organização.

### O que faz

* Lista os repositórios da organização
* Atualiza `.github/trigger.txt` com timestamp
* Realiza commit e push
* Dispara pipelines baseados em `push`

### Quando usar

* Rodar scans de segurança (ex: Veracode) em massa
* Validar pipelines após mudanças globais
* Executar testes em múltiplos repositórios

---

## ▶️ Execução

1. Acesse a aba **Actions**
2. Selecione o workflow **Trigger All Repos**
3. Clique em **Run workflow**

---

## 🔐 Configuração

É necessário configurar o seguinte secret:

```text
GH_TOKEN
```

### Permissões necessárias

* `repo`

---

## 🧠 Princípios do repositório

* Simplicidade > complexidade
* Scripts diretos e pragmáticos
* Foco em execução real (não acadêmico)
* Reutilização em cenários corporativos

---

## ⚠️ Observações

* Algumas ferramentas podem gerar alterações em massa (ex: commits automatizados)
* Use com cautela em ambientes produtivos
* Ideal para ambientes controlados ou de teste

---

## 📄 Licença

MIT License