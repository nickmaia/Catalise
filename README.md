# Catálise

Aplicação web para simulação cinética e cálculo de reatores catalíticos, desenvolvida durante a graduação em Engenharia Química (UFTM). Une o que antes eram dois repositórios separados (`Catalise_backend` e `Catalise_frontend`) em um único monorepo.

## Objetivo

Apoiar o cálculo de cinética de reações catalíticas e dimensionamento de reatores, oferecendo uma interface web para inserção de parâmetros e visualização dos resultados numéricos.

## Estrutura

```
Catalise/
├── backend/    # API em Django + Django REST Framework
└── frontend/   # Interface web em HTML/CSS/JS
```

### Backend

- **Stack:** Django 4.1, Django REST Framework, PostgreSQL (via `dj-database-url`/`psycopg2`)
- **Cálculo numérico:** NumPy, SciPy, SymPy, mpmath
- **Deploy:** Gunicorn + Whitenoise (Render/Heroku, via `Procfile`)

```bash
cd backend
pip install -r requirements.txt
cd meu_projeto
python manage.py migrate
python manage.py runserver
```

### Frontend

- HTML/CSS/JS estático, com páginas para cálculos (`calculos.html`), preços, contato e treinamentos.
- Consome a API do backend.

```bash
cd frontend
# servir os arquivos estáticos, ex.: python -m http.server
```

## Histórico

Projeto citado no Currículo Lattes como "Catálise – Aplicação Web para Simulação Cinética e Cálculo de Reatores" (2023).
