# 🔁 GitHub Org Pipeline Trigger (SE-Tools)

Ferramenta para disparar pipelines (GitHub Actions) em **todos os repositórios de uma organização**, de forma controlada e manual.

---

## 📂 Localização do Script

O script responsável pela execução está em:

```text
Tools/trigger-all-repos/trigger-all-repos.py
```

---

## 🎯 Objetivo

Disparar pipelines (ex: Veracode, CI, testes) em massa, garantindo:

* Execução manual e controlada
* Compatibilidade com qualquer workflow baseado em `push`
* Simplicidade operacional
* Independência de ferramentas locais

---

## ⚙️ Como funciona

O workflow:

1. Lista todos os repositórios da organização via API do GitHub
2. Clona cada repositório (shallow clone)
3. Atualiza o arquivo `.github/trigger.txt` com timestamp
4. Realiza commit e push
5. O `push` dispara os pipelines

---

## ▶️ Como executar

1. Acesse o repositório **SE-Tools**
2. Vá na aba **Actions**
3. Selecione **Trigger All Repos**
4. Clique em **Run workflow**

---

## 🔐 Configuração

### Secret necessário

```text
GH_TOKEN
```

### Permissões do token

* `repo` (acesso aos repositórios da organização)

---

## 🌐 Organização dinâmica

A organização é identificada automaticamente:

```yaml
${{ github.repository_owner }}
```

---

## 📁 Estrutura do projeto

```text
SE-Tools/
├── .github/
│   └── workflows/
│       └── trigger-all-repos.yml
├── Tools/
│   └── trigger-all-repos/
│       └── trigger-all-repos.py
└── README.md
```

---

## 🧪 Comportamento

Para cada repositório:

Arquivo atualizado:

```text
.github/trigger.txt
```

Conteúdo adicionado:

```text
trigger: 2026-01-01 12:00:00
```

Commit gerado:

```text
chore: trigger pipeline (timestamp)
```

---

## ⚠️ Limitações

* Requer permissão de escrita
* Pode falhar com branch protegida
* Gera commits em todos os repositórios
* Execução sequencial (mais lenta em orgs grandes)

---

## 🧠 Considerações

* Ideal para ambientes de teste
* Funciona com qualquer pipeline (incluindo Veracode)
* Simples e previsível

---

## 🔐 GitHub Token

1. Gere um token em: https://github.com/settings/tokens
2. Configure no repositório:
   Settings → Secrets and variables → Actions

```text
GH_TOKEN=<seu_token>
```

---

## 📄 Licença

MIT License