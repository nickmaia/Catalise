# Catálise

Aplicação web para simulação cinética e cálculo de reatores catalíticos, desenvolvida durante a graduação em Engenharia Química (UFTM). Une o que antes eram dois repositórios separados (`Catalise_backend` e `Catalise_frontend`) em um único monorepo.

## ⚠️ Importante: arquitetura real

O `backend/` é uma **aplicação Django completa e autocontida** — tem seus próprios 37 templates HTML com formulários (CSRF incluído) e renderiza os resultados server-side. **A pasta `frontend/` nunca foi conectada ao backend**: é um template estático (Bootstrap) solto, sem nenhuma chamada de API (`fetch`/`axios`) para o backend. Para efeitos práticos, **é o `backend/` sozinho que é a calculadora funcional**.

## Objetivo

Apoiar o cálculo de cinética de reações catalíticas e dimensionamento de reatores (CSTR, PFR, batelada, semibatelada), com formulários web para inserção de parâmetros e visualização dos resultados numéricos.

## Estrutura

```
Catalise/
├── backend/     # app Django completa (é o produto real)
│   └── meu_projeto/
│       ├── manage.py
│       └── minha_app/       # views, cálculos (scipy) e templates HTML
├── frontend/    # template estático Bootstrap, NÃO integrado ao backend
└── render.yaml  # deploy no Render (web service)
```

### Rodando localmente

```bash
cd backend
pip install -r requirements.txt
cd meu_projeto
export DJANGO_SECRET_KEY="qualquer-valor-para-dev"   # obrigatório se DEBUG=False
export DEBUG=True
python manage.py migrate
python manage.py runserver
```

### Deploy (Render)

O `render.yaml` na raiz já configura o serviço (`rootDir: backend`, instala dependências, roda migrations e `collectstatic`, sobe com gunicorn). Variáveis de ambiente necessárias — configuradas automaticamente pelo `render.yaml`, exceto quando indicado:

| Variável | Obrigatória | Observação |
|---|---|---|
| `DJANGO_SECRET_KEY` | ✅ | Gerada automaticamente pelo Render (`generateValue: true`) |
| `DEBUG` | Não (default `False`) | Nunca deixar `True` em produção |
| `ALLOWED_HOSTS` | ✅ em produção | Domínio(s) separados por vírgula |
| `DATABASE_URL` | Não | Se ausente, usa SQLite local (ok para demo; para produção séria, adicionar um banco Postgres no Render e conectar via `DATABASE_URL`) |

**Passo a passo no Render:** New → Blueprint → conectar este repositório → o `render.yaml` é detectado automaticamente.

## Stack

- **Backend:** Django, cálculo numérico via SciPy (`scipy.integrate`)
- **Deploy:** Gunicorn + Whitenoise (arquivos estáticos), Render

## Histórico

Projeto citado no Currículo Lattes como "Catálise – Aplicação Web para Simulação Cinética e Cálculo de Reatores" (2023). Consolidado a partir de dois repositórios separados em julho/2026; nessa consolidação também foram corrigidos: `requirements.txt` que estava salvo em UTF-16 (quebrava `pip install`), uma `SECRET_KEY` do Django hardcoded no código-fonte, `whitenoise` não configurado, e dependências (`numpy`/`scipy`) desatualizadas sem wheel para Python atual.
