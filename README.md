# Catálise

Aplicação web para simulação cinética e cálculo de reatores catalíticos, desenvolvida durante a graduação em Engenharia Química (UFTM).

## No ar (Vercel)

| Serviço | URL |
|---|---|
| **Frontend** — calculadora interativa | https://catalise.vercel.app/calculos.html |
| **Backend** — API FastAPI | https://catalise-api.vercel.app |
| Docs interativos (Swagger) | https://catalise-api.vercel.app/docs |

O frontend chama a API em produção via `fetch()` (ver `catalise-frontend/assets/js/calculator.js`) e mostra o resultado num modal — antes disso os links eram estáticos apontando para `http://127.0.0.1:8000` (servidor Django local antigo), nunca funcionaram fora da máquina de desenvolvimento original.

```bash
curl -X POST https://catalise-api.vercel.app/cstr/onemols \
  -H "Content-Type: application/json" \
  -d '{"flow":10,"conversion":0.5,"epsilon":0.1,"initial_concentration":2,"K_kinetic":0.05}'
# {"volume":105.0}
```

## Estrutura

```
Catalise/
├── catalise-backend/   # API FastAPI (29 endpoints de cálculo de reatores)
│   ├── api/
│   │   ├── main.py       # rotas + modelos Pydantic
│   │   └── calculos.py   # lógica matemática (scipy/numpy), sem dependência de framework
│   └── requirements.txt
└── catalise-frontend/  # site estático (Bootstrap) + calculadora interativa
    └── assets/js/calculator.js   # integração real com a API via fetch()
```

## Rodando localmente

```bash
# backend
cd catalise-backend
pip install -r requirements.txt
uvicorn api.main:app --reload

# frontend (aponta para produção por padrão — ver API_BASE em calculator.js)
cd catalise-frontend
python3 -m http.server 5500
```

## Deploy

Cada pasta é um projeto Vercel independente (zero-config: Vercel detecta `api/` com Python automaticamente pro backend; `catalise-frontend/` é servido como site estático).

```bash
cd catalise-backend && vercel deploy --prod
cd catalise-frontend && vercel deploy --prod
```

## Endpoints da API

29 rotas cobrindo: tempo de batelada (1 e 2 reagentes), volume de CSTR e PFR, concentração em partida de semibatelada, queda de pressão em leito catalítico (Ergun), e volume/tempo com efeito de temperatura (ordem 1, ordem 2, reversível, 2 reagentes). Lista completa em `/docs`.

## Histórico

Projeto citado no Currículo Lattes como "Catálise – Aplicação Web para Simulação Cinética e Cálculo de Reatores" (2023). Consolidado a partir de dois repositórios separados (`Catalise_backend` e `Catalise_frontend`) em julho/2026. O backend foi originalmente escrito em Django (server-rendered, 37 templates HTML) — migrado para FastAPI (mesma lógica de cálculo, testada e validada contra os resultados do Django antes da migração) e publicado no Vercel. O frontend, que nunca teve integração real com nenhum backend, ganhou uma calculadora funcional de verdade (`calculator.js`) na mesma leva de mudanças.
