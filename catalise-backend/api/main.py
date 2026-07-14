from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import calculos

app = FastAPI(title="Catálise API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Modelos de entrada ──────────────────────────────────────────────

class BateladaOneReagentInput(BaseModel):
    epsilon: float
    conversion: float
    K_kinetic: float


class BateladaOneReagentNoVarMolsInput(BaseModel):
    conversion: float
    K_kinetic: float


class BateladaTwoReagentInput(BaseModel):
    epsilon: float
    conversion: float
    K_kinetic: float
    initial_concentration: float
    coef: float
    initial_concentration_b: float


class BateladaTwoReagentNoVarMolsInput(BaseModel):
    conversion: float
    K_kinetic: float
    initial_concentration: float
    coef: float
    initial_concentration_b: float


class VolumeOneReagentInput(BaseModel):
    flow: float
    epsilon: float
    conversion: float
    initial_concentration: float
    K_kinetic: float


class VolumeOneReagentNoVarMolsInput(BaseModel):
    flow: float
    conversion: float
    initial_concentration: float
    K_kinetic: float


class VolumeTwoReagentInput(BaseModel):
    flow: float
    epsilon: float
    conversion: float
    initial_concentration: float
    K_kinetic: float
    coef: float
    initial_concentration_b: float


class VolumeTwoReagentNoVarMolsInput(BaseModel):
    flow: float
    conversion: float
    initial_concentration: float
    K_kinetic: float
    coef: float
    initial_concentration_b: float


class SemiBateladaConcentrationInput(BaseModel):
    K_kinetic: float
    b_conversion: float
    a_conversion: float
    ai_conversion: float
    volume: float
    vazao: float
    tempo: float


class StartupTimeInput(BaseModel):
    K_kinetic: float
    a_conversion: float
    ai_conversion: float
    volume: float
    vazao: float


class StartupConcentrationInput(BaseModel):
    K_kinetic: float
    a_conversion: float
    ai_conversion: float
    volume: float
    vazao: float
    tempo: float


class QuedaPressaoInput(BaseModel):
    flow: float
    ac: float
    massa: float
    densidade: float
    diametro: float
    porosidade: float
    pressao: float
    mi: float


class QuedaPressaoReatorTubularInput(BaseModel):
    flow: float
    ac: float
    massa: float
    densidade: float
    diametro: float
    porosidade: float
    pressao: float
    mi: float
    constante: float
    volume: float


class TempBateladaInput(BaseModel):
    temp1: float
    K_kinetic: float
    cpi: float
    to: float
    delta_hr: float
    delta_cp: float
    conversion: float
    vazao: float
    energia: float
    concentration: float


class TempOrdemUmInput(BaseModel):
    temp1: float
    K_kinetic: float
    cpi: float
    to: float
    tr: float
    delta_hr: float
    delta_cp: float
    conversion: float
    vazao: float
    energia: float


class TempOrdemDoisInput(BaseModel):
    temp1: float
    K_kinetic: float
    cpi: float
    to: float
    tr: float
    delta_hr: float
    delta_cp: float
    conversion: float
    vazao: float
    energia: float
    concentration: float


class TempOrdemUmDoisReagentesInput(BaseModel):
    temp1: float
    K_kinetic: float
    cpi: float
    to: float
    tr: float
    delta_hr: float
    delta_cp: float
    conversion: float
    vazao: float
    energia: float
    concentration: float
    concentration_b: float


class TempOrdemUmReversivelInput(BaseModel):
    temp1: float
    K_kinetic: float
    K_eq: float
    cpi: float
    to: float
    tr: float
    delta_hr: float
    delta_cp: float
    conversion: float
    vazao: float
    energia: float


# ── Modelos de saída ─────────────────────────────────────────────────

class TempoOutput(BaseModel):
    tempo: float


class VolumeOutput(BaseModel):
    volume: float


class DeltaPOutput(BaseModel):
    deltap: float


class ConversionOutput(BaseModel):
    conversion: float


class TimeOutput(BaseModel):
    time: float


class ConcentrationOutput(BaseModel):
    concentration: float


class SemiBateladaOutput(BaseModel):
    concentrationA: float
    conversion: float
    concentrationC: float


class TempBateladaOutput(BaseModel):
    tempo: float
    temperatura: float


# ── Rotas: batelada ──────────────────────────────────────────────────

@app.post("/batelada/onemols", response_model=TempoOutput)
def batelada_one_reagent(data: BateladaOneReagentInput):
    tempo = calculos.calculate_batch_time_direct_one_reagent(
        data.epsilon, data.conversion, data.K_kinetic
    )
    return TempoOutput(tempo=tempo)


@app.post("/batelada/one", response_model=TempoOutput)
def batelada_one_reagent_no_var_mols(data: BateladaOneReagentNoVarMolsInput):
    tempo = calculos.calculate_batch_time_direct_one_reagent_no_var_mols(
        data.conversion, data.K_kinetic
    )
    return TempoOutput(tempo=tempo)


@app.post("/batelada/twomols", response_model=TempoOutput)
def batelada_two_reagent(data: BateladaTwoReagentInput):
    tempo = calculos.calculate_batch_time_direct_two_reagent(
        data.epsilon,
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return TempoOutput(tempo=tempo)


@app.post("/batelada/two", response_model=TempoOutput)
def batelada_two_reagent_no_var_mols(data: BateladaTwoReagentNoVarMolsInput):
    tempo = calculos.calculate_batch_time_direct_two_reagent_no_var_mols(
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return TempoOutput(tempo=tempo)


# ── Rotas: CSTR (mistura) ────────────────────────────────────────────

@app.post("/cstr/onemols", response_model=VolumeOutput)
def cstr_one_reagent(data: VolumeOneReagentInput):
    volume = calculos.calculate_mixture_reactor_volume_direct_one_reagent(
        data.flow, data.epsilon, data.conversion, data.K_kinetic, data.initial_concentration
    )
    return VolumeOutput(volume=volume)


@app.post("/cstr/one", response_model=VolumeOutput)
def cstr_one_reagent_no_var_mols(data: VolumeOneReagentNoVarMolsInput):
    volume = calculos.calculate_mixture_reactor_volume_direct_one_reagent_no_var_mols(
        data.flow, data.conversion, data.K_kinetic, data.initial_concentration
    )
    return VolumeOutput(volume=volume)


@app.post("/cstr/twomols", response_model=VolumeOutput)
def cstr_two_reagent(data: VolumeTwoReagentInput):
    volume = calculos.calculate_mixture_reactor_volume_direct_two_reagent(
        data.flow,
        data.epsilon,
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return VolumeOutput(volume=volume)


@app.post("/cstr/two", response_model=VolumeOutput)
def cstr_two_reagent_no_var_mols(data: VolumeTwoReagentNoVarMolsInput):
    volume = calculos.calculate_mixture_reactor_volume_direct_two_reagent_no_var_mols(
        data.flow,
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return VolumeOutput(volume=volume)


# ── Rotas: PFR (tubular) ─────────────────────────────────────────────

@app.post("/pfr/onemols", response_model=VolumeOutput)
def pfr_one_reagent(data: VolumeOneReagentInput):
    volume = calculos.calculate_tubular_reactor_volume_direct_one_reagent(
        data.flow, data.epsilon, data.conversion, data.K_kinetic, data.initial_concentration
    )
    return VolumeOutput(volume=volume)


@app.post("/pfr/one", response_model=VolumeOutput)
def pfr_one_reagent_no_var_mols(data: VolumeOneReagentNoVarMolsInput):
    volume = calculos.calculate_tubular_reactor_volume_direct_one_reagent_no_var_mols(
        data.flow, data.conversion, data.K_kinetic, data.initial_concentration
    )
    return VolumeOutput(volume=volume)


@app.post("/pfr/twomols", response_model=VolumeOutput)
def pfr_two_reagent(data: VolumeTwoReagentInput):
    volume = calculos.calculate_tubular_reactor_volume_direct_two_reagent(
        data.flow,
        data.epsilon,
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return VolumeOutput(volume=volume)


@app.post("/pfr/two", response_model=VolumeOutput)
def pfr_two_reagent_no_var_mols(data: VolumeTwoReagentNoVarMolsInput):
    volume = calculos.calculate_tubular_reactor_volume_direct_two_reagent_no_var_mols(
        data.flow,
        data.conversion,
        data.K_kinetic,
        data.initial_concentration,
        data.coef,
        data.initial_concentration_b,
    )
    return VolumeOutput(volume=volume)


# ── Rotas: semibatelada ───────────────────────────────────────────────

@app.post("/semibatelada/concentration", response_model=SemiBateladaOutput)
def semibatelada_concentration(data: SemiBateladaConcentrationInput):
    concentrationA, conversion, concentrationC = calculos.calculate_semi_batch_concentration(
        data.K_kinetic,
        data.b_conversion,
        data.a_conversion,
        data.ai_conversion,
        data.volume,
        data.vazao,
        data.tempo,
    )
    return SemiBateladaOutput(
        concentrationA=concentrationA, conversion=conversion, concentrationC=concentrationC
    )


@app.post("/semibatelada/startuptime", response_model=TimeOutput)
def semibatelada_startup_time(data: StartupTimeInput):
    time = calculos.calculate_startup_time(
        data.K_kinetic, data.a_conversion, data.ai_conversion, data.volume, data.vazao
    )
    return TimeOutput(time=time)


@app.post("/semibatelada/startupconcentration", response_model=ConcentrationOutput)
def semibatelada_startup_concentration(data: StartupConcentrationInput):
    concentration = calculos.calculate_startup_concentration(
        data.K_kinetic,
        data.a_conversion,
        data.ai_conversion,
        data.volume,
        data.vazao,
        data.tempo,
    )
    return ConcentrationOutput(concentration=concentration)


@app.post("/semibatelada/quedapressaotypeone", response_model=DeltaPOutput)
def quedapressao_typeone_massa(data: QuedaPressaoInput):
    deltap = calculos.calculate_pressure_fall_typeone_massadecatalisador(
        data.flow, data.ac, data.massa, data.densidade, data.diametro,
        data.porosidade, data.pressao, data.mi,
    )
    return DeltaPOutput(deltap=deltap)


@app.post("/semibatelada/quedapressaotypetwo", response_model=DeltaPOutput)
def quedapressao_typetwo_massa(data: QuedaPressaoInput):
    deltap = calculos.calculate_pressure_fall_typetwo_massadecatalisador(
        data.flow, data.ac, data.massa, data.densidade, data.diametro,
        data.porosidade, data.pressao, data.mi,
    )
    return DeltaPOutput(deltap=deltap)


@app.post("/semibatelada/quedapressaotypeonecomprimento", response_model=DeltaPOutput)
def quedapressao_typeone_comprimento(data: QuedaPressaoInput):
    deltap = calculos.calculate_pressure_fall_typeone_comprimento(
        data.flow, data.ac, data.massa, data.densidade, data.diametro,
        data.porosidade, data.pressao, data.mi,
    )
    return DeltaPOutput(deltap=deltap)


@app.post("/semibatelada/quedapressaotypetwocomprimento", response_model=DeltaPOutput)
def quedapressao_typetwo_comprimento(data: QuedaPressaoInput):
    deltap = calculos.calculate_pressure_fall_typetwo_comprimento(
        data.flow, data.ac, data.massa, data.densidade, data.diametro,
        data.porosidade, data.pressao, data.mi,
    )
    return DeltaPOutput(deltap=deltap)


@app.post("/semibatelada/quedapressaoreatortubular", response_model=ConversionOutput)
def quedapressao_reatortubular(data: QuedaPressaoReatorTubularInput):
    conversion = calculos.calculate_pressure_fall_reatortubular(
        data.flow, data.ac, data.massa, data.densidade, data.diametro,
        data.porosidade, data.pressao, data.mi, data.constante, data.volume,
    )
    return ConversionOutput(conversion=conversion)


@app.post("/semibatelada/calculatetempbatelada", response_model=TempBateladaOutput)
def temp_batelada(data: TempBateladaInput):
    tempo, temperatura = calculos.calculate_temp_batch(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia, data.concentration,
    )
    return TempBateladaOutput(tempo=tempo, temperatura=temperatura)


@app.post("/semibatelada/calculatetempcstrordemum", response_model=VolumeOutput)
def temp_cstr_ordem_um(data: TempOrdemUmInput):
    volume = calculos.calculate_time_mixture_ordem_um(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetempcstrordemdois", response_model=VolumeOutput)
def temp_cstr_ordem_dois(data: TempOrdemDoisInput):
    volume = calculos.calculate_time_mixture_ordem_dois(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia, data.concentration,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetempcstrordemumdoisreagentes", response_model=VolumeOutput)
def temp_cstr_ordem_um_doisreagentes(data: TempOrdemUmDoisReagentesInput):
    volume = calculos.calculate_time_mixture_ordem_um_doisreagentes(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia,
        data.concentration, data.concentration_b,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetempcstrordemumreversivel", response_model=VolumeOutput)
def temp_cstr_ordem_um_reversivel(data: TempOrdemUmReversivelInput):
    volume = calculos.calculate_time_mixture_ordem_um_reversivel(
        data.temp1, data.K_kinetic, data.K_eq, data.cpi, data.to, data.tr,
        data.delta_hr, data.delta_cp, data.conversion, data.vazao, data.energia,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetemppfrordemum", response_model=VolumeOutput)
def temp_pfr_ordem_um(data: TempOrdemUmInput):
    volume = calculos.calculate_time_tubular_ordem_um(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetemppfrordemdois", response_model=VolumeOutput)
def temp_pfr_ordem_dois(data: TempOrdemDoisInput):
    volume = calculos.calculate_time_tubular_ordem_dois(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia, data.concentration,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetemppfrordemumdoisreagentes", response_model=VolumeOutput)
def temp_pfr_ordem_um_doisreagentes(data: TempOrdemUmDoisReagentesInput):
    volume = calculos.calculate_time_tubular_ordem_um_doisreagentes(
        data.temp1, data.K_kinetic, data.cpi, data.to, data.tr, data.delta_hr,
        data.delta_cp, data.conversion, data.vazao, data.energia,
        data.concentration, data.concentration_b,
    )
    return VolumeOutput(volume=volume)


@app.post("/semibatelada/calculatetemppfrordemumreversivel", response_model=VolumeOutput)
def temp_pfr_ordem_um_reversivel(data: TempOrdemUmReversivelInput):
    volume = calculos.calculate_time_tubular_ordem_um_reversivel(
        data.temp1, data.K_kinetic, data.K_eq, data.cpi, data.to, data.tr,
        data.delta_hr, data.delta_cp, data.conversion, data.vazao, data.energia,
    )
    return VolumeOutput(volume=volume)


@app.get("/")
def health():
    return {"status": "ok", "service": "Catalise API"}
