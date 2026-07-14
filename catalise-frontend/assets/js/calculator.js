/* Catálise — integração real com a API (catalise-api.vercel.app)
 * Substitui os links antigos que apontavam para http://127.0.0.1:8000
 * Cada entrada de CALCULATIONS corresponde 1:1 a uma rota do backend FastAPI. */

const API_BASE = "https://catalise-api.vercel.app";

const F = {
  epsilon: "Epsilon (ε)",
  conversion: "Conversão (X)",
  K_kinetic: "Constante cinética (K)",
  initial_concentration: "Concentração inicial de A (Cao)",
  initial_concentration_b: "Concentração inicial de B (Cbo)",
  coef: "Coeficiente estequiométrico de B (nb)",
  flow: "Vazão molar de alimentação (Fjo)",
  b_conversion: "Concentração inicial de B (Cbo)",
  a_conversion: "Concentração inicial de A (Cao)",
  ai_conversion: "Concentração inicial no tanque (Cai)",
  volume: "Volume (Vo)",
  vazao: "Vazão volumétrica (Qo)",
  tempo: "Tempo (t)",
  ac: "Área da seção transversal (Ac)",
  massa: "Massa de catalisador (W)",
  densidade: "Densidade do fluido (ρ)",
  diametro: "Diâmetro da partícula (Dp)",
  porosidade: "Porosidade do leito (εb)",
  pressao: "Pressão inicial (Po)",
  mi: "Viscosidade (μ)",
  constante: "Constante cinética (k)",
  temp1: "Temperatura de referência (T1)",
  cpi: "Capacidade calorífica do inerte (Cpi)",
  to: "Temperatura de entrada (To)",
  tr: "Temperatura de referência da reação (Tr)",
  delta_hr: "Calor de reação (ΔHr)",
  delta_cp: "Variação de Cp (ΔCp)",
  energia: "Energia de ativação (Ea)",
  concentration: "Concentração inicial de A (Cao)",
  concentration_b: "Concentração inicial de B (Cbo)",
  K_eq: "Constante de equilíbrio (Ke1)",
};

function field(name) {
  return { name, label: F[name] || name };
}

const CALCULATIONS = {
  "batelada/onemols": {
    title: "Batelada — Tempo (1 reagente, com variação de mols)",
    fields: [field("epsilon"), field("conversion"), field("K_kinetic")],
    results: [{ key: "tempo", label: "Tempo" }],
  },
  "batelada/one": {
    title: "Batelada — Tempo (1 reagente, sem variação de mols)",
    fields: [field("conversion"), field("K_kinetic")],
    results: [{ key: "tempo", label: "Tempo" }],
  },
  "batelada/twomols": {
    title: "Batelada — Tempo (2 reagentes, com variação de mols)",
    fields: [
      field("epsilon"), field("conversion"), field("K_kinetic"),
      field("initial_concentration"), field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "tempo", label: "Tempo" }],
  },
  "batelada/two": {
    title: "Batelada — Tempo (2 reagentes, sem variação de mols)",
    fields: [
      field("conversion"), field("K_kinetic"), field("initial_concentration"),
      field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "tempo", label: "Tempo" }],
  },
  "cstr/onemols": {
    title: "CSTR — Volume (1 reagente, com variação de mols)",
    fields: [field("flow"), field("epsilon"), field("conversion"), field("initial_concentration"), field("K_kinetic")],
    results: [{ key: "volume", label: "Volume" }],
  },
  "cstr/one": {
    title: "CSTR — Volume (1 reagente, sem variação de mols)",
    fields: [field("flow"), field("conversion"), field("initial_concentration"), field("K_kinetic")],
    results: [{ key: "volume", label: "Volume" }],
  },
  "cstr/twomols": {
    title: "CSTR — Volume (2 reagentes, com variação de mols)",
    fields: [
      field("flow"), field("epsilon"), field("conversion"), field("initial_concentration"),
      field("K_kinetic"), field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "cstr/two": {
    title: "CSTR — Volume (2 reagentes, sem variação de mols)",
    fields: [
      field("flow"), field("conversion"), field("initial_concentration"),
      field("K_kinetic"), field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "pfr/onemols": {
    title: "PFR — Volume (1 reagente, com variação de mols)",
    fields: [field("flow"), field("epsilon"), field("conversion"), field("initial_concentration"), field("K_kinetic")],
    results: [{ key: "volume", label: "Volume" }],
  },
  "pfr/one": {
    title: "PFR — Volume (1 reagente, sem variação de mols)",
    fields: [field("flow"), field("conversion"), field("initial_concentration"), field("K_kinetic")],
    results: [{ key: "volume", label: "Volume" }],
  },
  "pfr/twomols": {
    title: "PFR — Volume (2 reagentes, com variação de mols)",
    fields: [
      field("flow"), field("epsilon"), field("conversion"), field("initial_concentration"),
      field("K_kinetic"), field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "pfr/two": {
    title: "PFR — Volume (2 reagentes, sem variação de mols)",
    fields: [
      field("flow"), field("conversion"), field("initial_concentration"),
      field("K_kinetic"), field("coef"), field("initial_concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/concentration": {
    title: "Semibatelada — Concentração",
    fields: [
      field("K_kinetic"), field("b_conversion"), field("a_conversion"),
      field("ai_conversion"), field("volume"), field("vazao"), field("tempo"),
    ],
    results: [
      { key: "concentrationA", label: "Concentração de A" },
      { key: "conversion", label: "Conversão (%)" },
      { key: "concentrationC", label: "Concentração de C" },
    ],
  },
  "semibatelada/startuptime": {
    title: "Semibatelada — Tempo de partida (start-up)",
    fields: [field("K_kinetic"), field("a_conversion"), field("ai_conversion"), field("volume"), field("vazao")],
    results: [{ key: "time", label: "Tempo" }],
  },
  "semibatelada/startupconcentration": {
    title: "Semibatelada — Concentração de partida (start-up)",
    fields: [
      field("K_kinetic"), field("a_conversion"), field("ai_conversion"),
      field("volume"), field("vazao"), field("tempo"),
    ],
    results: [{ key: "concentration", label: "Concentração" }],
  },
  "semibatelada/quedapressaotypeone": {
    title: "Queda de Pressão — Tipo 1 (massa de catalisador)",
    fields: [field("flow"), field("ac"), field("massa"), field("densidade"), field("diametro"), field("porosidade"), field("pressao"), field("mi")],
    results: [{ key: "deltap", label: "ΔP" }],
  },
  "semibatelada/quedapressaotypetwo": {
    title: "Queda de Pressão — Tipo 2 (massa de catalisador)",
    fields: [field("flow"), field("ac"), field("massa"), field("densidade"), field("diametro"), field("porosidade"), field("pressao"), field("mi")],
    results: [{ key: "deltap", label: "ΔP" }],
  },
  "semibatelada/quedapressaotypeonecomprimento": {
    title: "Queda de Pressão — Tipo 1 (comprimento)",
    fields: [field("flow"), field("ac"), field("massa"), field("densidade"), field("diametro"), field("porosidade"), field("pressao"), field("mi")],
    results: [{ key: "deltap", label: "ΔP" }],
  },
  "semibatelada/quedapressaotypetwocomprimento": {
    title: "Queda de Pressão — Tipo 2 (comprimento)",
    fields: [field("flow"), field("ac"), field("massa"), field("densidade"), field("diametro"), field("porosidade"), field("pressao"), field("mi")],
    results: [{ key: "deltap", label: "ΔP" }],
  },
  "semibatelada/quedapressaoreatortubular": {
    title: "Queda de Pressão — Reator Tubular",
    fields: [
      field("flow"), field("ac"), field("massa"), field("densidade"), field("diametro"),
      field("porosidade"), field("pressao"), field("mi"), field("constante"), field("volume"),
    ],
    results: [{ key: "conversion", label: "Conversão (%)" }],
  },
  "semibatelada/calculatetempbatelada": {
    title: "Batelada com Efeito de Temperatura",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("delta_hr"),
      field("delta_cp"), field("conversion"), field("vazao"), field("energia"), field("concentration"),
    ],
    results: [{ key: "tempo", label: "Tempo" }, { key: "temperatura", label: "Temperatura" }],
  },
  "semibatelada/calculatetempcstrordemum": {
    title: "CSTR com Efeito de Temperatura — Ordem 1",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"),
      field("delta_hr"), field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetempcstrordemdois": {
    title: "CSTR com Efeito de Temperatura — Ordem 2",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"), field("delta_hr"),
      field("delta_cp"), field("conversion"), field("vazao"), field("energia"), field("concentration"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetempcstrordemumdoisreagentes": {
    title: "CSTR com Efeito de Temperatura — Ordem 1, 2 reagentes",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"), field("delta_hr"),
      field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
      field("concentration"), field("concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetempcstrordemumreversivel": {
    title: "CSTR com Efeito de Temperatura — Ordem 1, Reversível",
    fields: [
      field("temp1"), field("K_kinetic"), field("K_eq"), field("cpi"), field("to"), field("tr"),
      field("delta_hr"), field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetemppfrordemum": {
    title: "PFR com Efeito de Temperatura — Ordem 1",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"),
      field("delta_hr"), field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetemppfrordemdois": {
    title: "PFR com Efeito de Temperatura — Ordem 2",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"), field("delta_hr"),
      field("delta_cp"), field("conversion"), field("vazao"), field("energia"), field("concentration"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetemppfrordemumdoisreagentes": {
    title: "PFR com Efeito de Temperatura — Ordem 1, 2 reagentes",
    fields: [
      field("temp1"), field("K_kinetic"), field("cpi"), field("to"), field("tr"), field("delta_hr"),
      field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
      field("concentration"), field("concentration_b"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
  "semibatelada/calculatetemppfrordemumreversivel": {
    title: "PFR com Efeito de Temperatura — Ordem 1, Reversível",
    fields: [
      field("temp1"), field("K_kinetic"), field("K_eq"), field("cpi"), field("to"), field("tr"),
      field("delta_hr"), field("delta_cp"), field("conversion"), field("vazao"), field("energia"),
    ],
    results: [{ key: "volume", label: "Volume" }],
  },
};

function buildModal() {
  const modalHtml = `
  <div class="modal fade" id="catalise-modal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="catalise-modal-title">Cálculo</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form id="catalise-modal-form"></form>
          <div id="catalise-modal-result" class="mt-3"></div>
          <div id="catalise-modal-error" class="alert alert-danger mt-3 d-none"></div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
          <button type="button" class="btn btn-primary" id="catalise-modal-submit">Calcular</button>
        </div>
      </div>
    </div>
  </div>`;
  document.body.insertAdjacentHTML("beforeend", modalHtml);
}

function openCalculator(routeKey) {
  const config = CALCULATIONS[routeKey];
  if (!config) return;

  document.getElementById("catalise-modal-title").textContent = config.title;

  const form = document.getElementById("catalise-modal-form");
  form.innerHTML = config.fields
    .map(
      (f) => `
      <div class="mb-2">
        <label class="form-label">${f.label}</label>
        <input type="number" step="any" class="form-control" name="${f.name}" required>
      </div>`
    )
    .join("");

  document.getElementById("catalise-modal-result").innerHTML = "";
  const errorBox = document.getElementById("catalise-modal-error");
  errorBox.classList.add("d-none");
  errorBox.textContent = "";

  const submitBtn = document.getElementById("catalise-modal-submit");
  submitBtn.onclick = () => runCalculation(routeKey, config);

  const modalEl = document.getElementById("catalise-modal");
  const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
  modal.show();
}

async function runCalculation(routeKey, config) {
  const form = document.getElementById("catalise-modal-form");
  const resultBox = document.getElementById("catalise-modal-result");
  const errorBox = document.getElementById("catalise-modal-error");

  errorBox.classList.add("d-none");
  resultBox.innerHTML = "";

  if (!form.reportValidity()) return;

  const payload = {};
  new FormData(form).forEach((value, key) => {
    payload[key] = parseFloat(value);
  });

  try {
    const response = await fetch(`${API_BASE}/${routeKey}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errData = await response.json().catch(() => ({}));
      throw new Error(errData.detail ? JSON.stringify(errData.detail) : `Erro ${response.status}`);
    }

    const data = await response.json();
    resultBox.innerHTML = "";
    const wrapper = document.createElement("div");
    wrapper.className = "alert alert-success mb-0";
    const heading = document.createElement("strong");
    heading.textContent = "Resultado:";
    const list = document.createElement("ul");
    list.className = "mb-0";
    config.results.forEach((r) => {
      const li = document.createElement("li");
      const strong = document.createElement("strong");
      strong.textContent = String(data[r.key]);
      li.append(`${r.label}: `, strong);
      list.appendChild(li);
    });
    wrapper.append(heading, list);
    resultBox.appendChild(wrapper);
  } catch (err) {
    errorBox.textContent = "Erro ao calcular: " + err.message;
    errorBox.classList.remove("d-none");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  buildModal();

  document.querySelectorAll('a[href^="http://127.0.0.1:8000/"]').forEach((link) => {
    const routeKey = link.getAttribute("href").replace("http://127.0.0.1:8000/", "").trim();
    if (!CALCULATIONS[routeKey]) return;
    link.setAttribute("href", "#");
    link.addEventListener("click", (e) => {
      e.preventDefault();
      openCalculator(routeKey);
    });
  });
});
