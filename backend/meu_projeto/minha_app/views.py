from django.shortcuts import render
from .utils import (
    calculate_batch_time_direct_one_reagent,
    calculate_batch_time_direct_one_reagent_no_var_mols,
    calculate_batch_time_direct_two_reagent,
    calculate_batch_time_direct_two_reagent_no_var_mols,
    calculate_mixture_reactor_volume_direct_one_reagent,
    calculate_mixture_reactor_volume_direct_one_reagent_no_var_mols,
    calculate_mixture_reactor_volume_direct_two_reagent,
    calculate_mixture_reactor_volume_direct_two_reagent_no_var_mols,
    calculate_tubular_reactor_volume_direct_one_reagent,
    calculate_tubular_reactor_volume_direct_one_reagent_no_var_mols,
    calculate_tubular_reactor_volume_direct_two_reagent,
    calculate_tubular_reactor_volume_direct_two_reagent_no_var_mols,
    calculate_semi_batch_concentration,
    calculate_startup_time,
    calculate_startup_concentration,
    calculate_pressure_fall_typeone_massadecatalisador,
    calculate_pressure_fall_typetwo_massadecatalisador,
    calculate_pressure_fall_typeone_comprimento,
    calculate_pressure_fall_typetwo_comprimento,
    calculate_pressure_fall_reatortubular,
    calculate_temp_batch,
    calculate_time_mixture_ordem_um,
    calculate_time_mixture_ordem_dois,
    calculate_time_mixture_ordem_um_doisreagentes,
    calculate_time_tubular_ordem_um,
    calculate_time_tubular_ordem_dois,
    calculate_time_tubular_ordem_um_doisreagentes,
    calculate_time_tubular_ordem_um_reversivel,
    calculate_time_mixture_ordem_um_reversivel,
)


def timebateladadirectonereagentView(request):
    if request.method == "POST":
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        K_kinetic = float(request.POST["K_kinetic"])
        tempo = calculate_batch_time_direct_one_reagent(epsilon, conversion, K_kinetic)
        return render(
            request,
            "minha_app/time_result.html",
            {"tempo": tempo},
        )
    else:
        return render(request, "minha_app/time_one_reagent_index.html")


def timebateladadirectonereagentnovarmolsView(request):
    if request.method == "POST":
        conversion = float(request.POST["conversion"])
        K_kinetic = float(request.POST["K_kinetic"])
        tempo = calculate_batch_time_direct_one_reagent_no_var_mols(
            conversion, K_kinetic
        )
        return render(
            request,
            "minha_app/time_result.html",
            {"tempo": tempo},
        )
    else:
        return render(request, "minha_app/time_one_reagent_nomols_index.html")


def timebateladadirecttworeagentView(request):
    if request.method == "POST":
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        K_kinetic = float(request.POST["K_kinetic"])
        initial_concentration = float(request.POST["initial_concentration"])
        coef = float(request.POST["coef"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        tempo = calculate_batch_time_direct_two_reagent(
            epsilon,
            conversion,
            K_kinetic,
            initial_concentration,
            coef,
            initial_concentration_b,
        )
        return render(
            request,
            "minha_app/time_result.html",
            {"tempo": tempo},
        )
    else:
        return render(request, "minha_app/time_two_reagent_index.html")


def timebateladadirecttworeagentnovarmolsView(request):
    if request.method == "POST":
        conversion = float(request.POST["conversion"])
        K_kinetic = float(request.POST["K_kinetic"])
        initial_concentration = float(request.POST["initial_concentration"])
        coef = float(request.POST["coef"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        tempo = calculate_batch_time_direct_two_reagent_no_var_mols(
            conversion, K_kinetic, initial_concentration, coef, initial_concentration_b
        )
        return render(
            request,
            "minha_app/time_result.html",
            {"tempo": tempo},
        )
    else:
        return render(request, "minha_app/time_two_reagent_nomols_index.html")


def calculatecstrvolumedirectonereagentView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        volume = calculate_mixture_reactor_volume_direct_one_reagent(
            flow, epsilon, conversion, K_kinetic, initial_concentration
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/volume_one_reagent_index.html")


def calculatecstrvolumedirectonereagentnovarmolsView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        volume = calculate_mixture_reactor_volume_direct_one_reagent_no_var_mols(
            flow, conversion, K_kinetic, initial_concentration
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/volume_one_reagent_nomols_index.html")


def calculatecstrvolumedirecttworeagentView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        coef = float(request.POST["coef"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        volume = calculate_mixture_reactor_volume_direct_two_reagent(
            flow,
            epsilon,
            conversion,
            K_kinetic,
            initial_concentration,
            coef,
            initial_concentration_b,
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/volume_two_reagent_index.html")


def calculatecstrvolumedirecttworeagentnovarmolsView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        coef = float(request.POST["coef"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        volume = calculate_mixture_reactor_volume_direct_two_reagent_no_var_mols(
            flow,
            conversion,
            K_kinetic,
            initial_concentration,
            coef,
            initial_concentration_b,
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/volume_two_reagent_nomols_index.html")


def calculatepfrvolumedirectonereagentView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        volume = calculate_tubular_reactor_volume_direct_one_reagent(
            flow, epsilon, conversion, K_kinetic, initial_concentration
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/pfr_volume_one_reagent_index.html")


def calculatepfrvolumedirectonereagentnovarmolsView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        K_kinetic = float(request.POST["K_kinetic"])
        volume = calculate_tubular_reactor_volume_direct_one_reagent_no_var_mols(
            flow,
            conversion,
            K_kinetic,
            initial_concentration,
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/pfr_volume_one_reagent_nomols_index.html")


def calculatepfrvolumedirecttworeagentView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        epsilon = float(request.POST["epsilon"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        K_kinetic = float(request.POST["K_kinetic"])
        coef = float(request.POST["coef"])
        volume = calculate_tubular_reactor_volume_direct_two_reagent(
            flow,
            epsilon,
            conversion,
            K_kinetic,
            initial_concentration,
            coef,
            initial_concentration_b,
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/pfr_volume_two_reagent_index.html")


def calculatepfrvolumedirecttworeagentnovarmolsView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        conversion = float(request.POST["conversion"])
        initial_concentration = float(request.POST["initial_concentration"])
        initial_concentration_b = float(request.POST["initial_concentration_b"])
        K_kinetic = float(request.POST["K_kinetic"])
        coef = float(request.POST["coef"])
        volume = calculate_tubular_reactor_volume_direct_two_reagent_no_var_mols(
            flow,
            conversion,
            K_kinetic,
            initial_concentration,
            coef,
            initial_concentration_b,
        )
        return render(
            request,
            "minha_app/volume_result.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/pfr_volume_two_reagent_nomols_index.html")


def calculate_semibatelada_concentrationView(request):
    if request.method == "POST":
        K_kinetic = float(request.POST["K_kinetic"])
        b_conversion = float(request.POST["b_conversion"])
        a_conversion = float(request.POST["a_conversion"])
        ai_conversion = float(request.POST["ai_conversion"])
        volume = float(request.POST["volume"])
        vazao = float(request.POST["vazao"])
        tempo = float(request.POST["tempo"])

        (
            concentrationA,
            conversion,
            concentrationC,
        ) = calculate_semi_batch_concentration(
            K_kinetic, b_conversion, a_conversion, ai_conversion, volume, vazao, tempo
        )
        return render(
            request,
            "minha_app/result.html",
            {
                "concentrationA": concentrationA,
                "conversion": conversion,
                "concentrationC": concentrationC,
            },
        )
    else:
        return render(request, "minha_app/calculate_semibatelada_concentration.html")


def calculate_startup_timeView(request):
    if request.method == "POST":
        K_kinetic = float(request.POST["K_kinetic"])
        a_conversion = float(request.POST["a_conversion"])
        ai_conversion = float(request.POST["ai_conversion"])
        volume = float(request.POST["volume"])
        vazao = float(request.POST["vazao"])

        time = calculate_startup_time(
            K_kinetic, a_conversion, ai_conversion, volume, vazao
        )
        return render(
            request,
            "minha_app/resultstartuptime.html",
            {"time": time},
        )
    else:
        return render(request, "minha_app/calculate_startup_time.html")


def calculate_startup_concentrationView(request):
    if request.method == "POST":
        K_kinetic = float(request.POST["K_kinetic"])
        a_conversion = float(request.POST["a_conversion"])
        ai_conversion = float(request.POST["ai_conversion"])
        volume = float(request.POST["volume"])
        vazao = float(request.POST["vazao"])
        tempo = float(request.POST["tempo"])

        concentration = calculate_startup_concentration(
            K_kinetic, a_conversion, ai_conversion, volume, vazao, tempo
        )
        return render(
            request,
            "minha_app/resultstartupconcentration.html",
            {"concentration": concentration},
        )
    else:
        return render(request, "minha_app/calculate_startup_concentration.html")


def calculate_quedapressao_typeone_massadecatalisadorView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        ac = float(request.POST["ac"])
        massa = float(request.POST["massa"])
        densidade = float(request.POST["densidade"])
        diametro = float(request.POST["diametro"])
        porosidade = float(request.POST["porosidade"])
        pressao = float(request.POST["pressao"])
        mi = float(request.POST["mi"])

        deltap = calculate_pressure_fall_typeone_massadecatalisador(
            flow, ac, massa, densidade, diametro, porosidade, pressao, mi
        )
        return render(
            request,
            "minha_app/resultquedapressao.html",
            {"deltap": deltap},
        )
    else:
        return render(request, "minha_app/quedapressao_typeone_massadecatalisador.html")


def calculate_quedapressao_typetwo_massadecatalisadorView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        ac = float(request.POST["ac"])
        massa = float(request.POST["massa"])
        densidade = float(request.POST["densidade"])
        diametro = float(request.POST["diametro"])
        porosidade = float(request.POST["porosidade"])
        pressao = float(request.POST["pressao"])
        mi = float(request.POST["mi"])

        deltap = calculate_pressure_fall_typetwo_massadecatalisador(
            flow, ac, massa, densidade, diametro, porosidade, pressao, mi
        )
        return render(
            request,
            "minha_app/resultquedapressao.html",
            {"deltap": deltap},
        )
    else:
        return render(request, "minha_app/quedapressao_typetwo_massadecatalisador.html")


def calculate_quedapressao_typeone_comprimentoView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        ac = float(request.POST["ac"])
        massa = float(request.POST["massa"])
        densidade = float(request.POST["densidade"])
        diametro = float(request.POST["diametro"])
        porosidade = float(request.POST["porosidade"])
        pressao = float(request.POST["pressao"])
        mi = float(request.POST["mi"])

        deltap = calculate_pressure_fall_typeone_comprimento(
            flow, ac, massa, densidade, diametro, porosidade, pressao, mi
        )
        return render(
            request,
            "minha_app/resultquedapressao.html",
            {"deltap": deltap},
        )
    else:
        return render(request, "minha_app/quedapressao_typeone_comprimento.html")


def calculate_quedapressao_typetwo_comprimentoView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        ac = float(request.POST["ac"])
        massa = float(request.POST["massa"])
        densidade = float(request.POST["densidade"])
        diametro = float(request.POST["diametro"])
        porosidade = float(request.POST["porosidade"])
        pressao = float(request.POST["pressao"])
        mi = float(request.POST["mi"])

        deltap = calculate_pressure_fall_typetwo_comprimento(
            flow, ac, massa, densidade, diametro, porosidade, pressao, mi
        )
        return render(
            request,
            "minha_app/resultquedapressao.html",
            {"deltap": deltap},
        )
    else:
        return render(request, "minha_app/quedapressao_typetwo_comprimento.html")


def calculate_quedapressao_reatortubularView(request):
    if request.method == "POST":
        flow = float(request.POST["flow"])
        ac = float(request.POST["ac"])
        massa = float(request.POST["massa"])
        densidade = float(request.POST["densidade"])
        diametro = float(request.POST["diametro"])
        porosidade = float(request.POST["porosidade"])
        pressao = float(request.POST["pressao"])
        mi = float(request.POST["mi"])
        constante = float(request.POST["constante"])
        volume = float(request.POST["volume"])

        conversion = calculate_pressure_fall_reatortubular(
            flow,
            ac,
            massa,
            densidade,
            diametro,
            porosidade,
            pressao,
            mi,
            constante,
            volume,
        )
        return render(
            request,
            "minha_app/resultcalculate_quedapressao_reatortubular.html",
            {"conversion": conversion},
        )
    else:
        return render(request, "minha_app/calculate_quedapressao_reatortubular.html")


def calculate_temp_bateladaView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])
        concentration = float(request.POST["concentration"])

        (tempo, temperatura) = calculate_temp_batch(
            temp1,
            K_kinetic,
            cpi,
            to,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
            concentration,
        )
        return render(
            request,
            "minha_app/result_temp_batelada.html",
            {
                "tempo": tempo,
                "temperatura": temperatura,
            },
        )
    else:
        return render(request, "minha_app/calculate_temp_batelada.html")


def calculate_temp_cstr_ordem_doisView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])
        concentration = float(request.POST["concentration"])

        volume = calculate_time_mixture_ordem_dois(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
            concentration,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/calculate_temp_cstr_ordem_dois.html")


def calculate_temp_cstr_ordem_um_doisreagentesView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])
        concentration = float(request.POST["concentration"])
        concentration_b = float(request.POST["concentration_b"])

        volume = calculate_time_mixture_ordem_um_doisreagentes(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
            concentration,
            concentration_b,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {"volume": volume},
        )
    else:
        return render(
            request, "minha_app/calculate_temp_cstr_ordem_um_doisreagentes.html"
        )


def calculate_temp_cstr_ordem_umView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])

        volume = calculate_time_mixture_ordem_um(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {"volume": volume},
        )
    else:
        return render(request, "minha_app/calculate_temp_cstr_ordem_um.html")


def calculate_temp_pfr_ordem_doisView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])
        concentration = float(request.POST["concentration"])

        volume = calculate_time_tubular_ordem_dois(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
            concentration,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {
                "volume": volume,
            },
        )
    else:
        return render(request, "minha_app/calculate_temp_pfr_ordem_dois.html")


def calculate_temp_pfr_ordem_um_doisreagentesView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])
        concentration = float(request.POST["concentration"])
        concentration_b = float(request.POST["concentration_b"])

        volume = calculate_time_tubular_ordem_um_doisreagentes(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
            concentration,
            concentration_b,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {
                "volume": volume,
            },
        )
    else:
        return render(
            request, "minha_app/calculate_temp_pfr_ordem_um_doisreagentes.html"
        )


def calculate_temp_pfr_ordem_um_reversivelView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        K_eq = float(request.POST["K_eq"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])

        volume = calculate_time_tubular_ordem_um_reversivel(
            temp1,
            K_kinetic,
            K_eq,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {
                "volume": volume,
            },
        )
    else:
        return render(request, "minha_app/calculate_temp_pfr_ordem_um_reversivel.html")


def calculate_temp_pfr_ordem_umView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])

        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])

        volume = calculate_time_tubular_ordem_um(
            temp1,
            K_kinetic,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {
                "volume": volume,
            },
        )
    else:
        return render(request, "minha_app/calculate_temp_pfr_ordem_um.html")


def calculate_temp_cstr_ordem_um_reversivelView(request):
    if request.method == "POST":
        temp1 = float(request.POST["temp1"])
        K_kinetic = float(request.POST["K_kinetic"])
        K_eq = float(request.POST["K_eq"])
        cpi = float(request.POST["cpi"])
        to = float(request.POST["to"])
        tr = float(request.POST["tr"])
        delta_hr = float(request.POST["delta_hr"])
        delta_cp = float(request.POST["delta_cp"])
        conversion = float(request.POST["conversion"])
        vazao = float(request.POST["vazao"])
        energia = float(request.POST["energia"])

        volume = calculate_time_mixture_ordem_um_reversivel(
            temp1,
            K_kinetic,
            K_eq,
            cpi,
            to,
            tr,
            delta_hr,
            delta_cp,
            conversion,
            vazao,
            energia,
        )
        return render(
            request,
            "minha_app/result_temp_volume.html",
            {
                "volume": volume,
            },
        )
    else:
        return render(request, "minha_app/calculate_temp_cstr_ordem_um_reversivel.html")
