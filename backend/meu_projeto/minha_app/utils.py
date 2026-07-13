from math import exp
from numpy import log as ln
from scipy import integrate


def calculate_batch_time_direct_one_reagent(e, x, K):
    def determining(x):
        return (1 + e * x) / ((1 - x) * K)

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 2)


def calculate_batch_time_direct_one_reagent_no_var_mols(x, K):
    def determining(x):
        return 1 / ((1 - x) * K)

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 2)


def calculate_batch_time_direct_two_reagent(e, x, K, Cao, nb, Cbo):
    def determining(x):
        return (Cao * (1 + e * x) ** (1 + nb)) / (
            (K * Cao ** (1 + nb)) * (1 - x) * ((Cbo / Cao) - (nb * x)) ** nb
        )

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 2)


def calculate_batch_time_direct_two_reagent_no_var_mols(x, K, Cao, nb, Cbo):
    def determining(x):
        return Cao / ((K * Cao ** (1 + nb)) * (1 - x) * ((Cbo / Cao) - (nb * x)) ** nb)

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 2)


def calculate_mixture_reactor_volume_direct_one_reagent_no_var_mols(Fjo, x, K, Cao):
    volume = (Fjo * x) / (K * Cao * (1 - x))

    return round(volume, 2)


def calculate_mixture_reactor_volume_direct_one_reagent(Fjo, e, x, K, Cao):
    volume = (Fjo * x * (1 + e * x)) / (K * Cao * (1 - x))

    return round(volume, 2)


def calculate_mixture_reactor_volume_direct_two_reagent_no_var_mols(
    Fjo, x, K, Cao, nb, Cbo
):
    volume = (Fjo * x) / (
        K * (Cao ** (1 + nb)) * (1 - x) * ((Cbo / Cao) - (nb * x)) ** nb
    )

    return round(volume, 2)


def calculate_mixture_reactor_volume_direct_two_reagent(Fjo, e, x, K, Cao, nb, Cbo):
    volume = (Fjo * x * ((1 + e * x) ** (1 + nb))) / (
        K * (Cao ** (1 + nb)) * (1 - x) * ((Cbo / Cao) - (nb * x)) ** nb
    )

    return round(volume, 2)


def calculate_tubular_reactor_volume_direct_one_reagent(Fjo, e, x, K, Cao):
    def determining(x):
        return (1 + e * x) / (1 - x)

    volume, _ = integrate.quad(determining, 0, x)

    num = (Fjo / (Cao * K)) * volume
    return round(num, 2)


def calculate_tubular_reactor_volume_direct_one_reagent_no_var_mols(Fjo, x, K, Cao):
    def determining(x):
        return 1 / (1 - x)

    volume, _ = integrate.quad(determining, 0, x)

    num = (Fjo / (Cao * K)) * volume
    return round(num, 2)


def calculate_tubular_reactor_volume_direct_two_reagent(Fjo, e, x, K, Cao, nb, Cbo):
    def determining(x):
        return ((1 + e * x) ** (1 + nb)) / ((1 - x) * ((Cbo / Cao) - (nb * x)) ** nb)

    volume, _ = integrate.quad(determining, 0, x)

    num = (Fjo / (Cao ** (1 + nb) * K)) * volume
    return round(num, 2)


def calculate_tubular_reactor_volume_direct_two_reagent_no_var_mols(
    Fjo, x, K, Cao, nb, Cbo
):
    def determining(x):
        return 1 / ((1 - x) * ((Cbo / Cao) - (nb * x)) ** nb)

    volume, _ = integrate.quad(determining, 0, x)

    num = (Fjo / (Cao ** (1 + nb) * K)) * volume
    return round(num, 2)


def calculate_semi_batch_concentration(K, cbo, cao, cai, vo, qo, t):
    tau = vo / qo
    K1 = cbo * K
    fao = cao * qo

    ca = (cao / (K1 * (tau + t))) + (
        (tau / (tau + t)) * exp(-t * K1) * (cai - (cao / (K1 * tau)))
    )

    x = ((fao * t) - (ca * (vo + qo * t))) / (cbo * vo)

    cc = (cbo * vo * x) / (vo + (qo * t))

    return (round(ca, 4), round(x * 100, 2), round(cc, 4))


def calculate_startup_time(k, cao, cai, vo, qo):
    tau = vo / qo
    ca = 0.99 * cao / (tau * k + 1)
    t = -(ln((ca - cao / (tau * k + 1)) / (cai - cao / (tau * k + 1)))) / (
        (tau * k + 1) / tau
    )

    return round(t, 4)


def calculate_startup_concentration(k, cao, cai, vo, qo, t):
    tau = vo / qo
    ca = (cao / (tau * k + 1)) + (cai - (cao / (tau * k + 1))) * exp(
        ((tau * k + 1) * -t) / (tau)
    )

    return round(ca, 4)


def calculate_pressure_fall_typeone_massadecatalisador(fto, ac, w, rho, dp, eb, po, mi):
    gc = 417000000  # lbm ft / h^2 lbf
    G = fto / ac  # lbm/ft2 h

    bo = (G * (1 - eb) / (rho * gc * dp * eb**3)) * (
        ((150 * (1 - eb) * mi) / dp) + 1.75 * G
    )

    b = bo * (1 / 14.7) * (1 / 144)

    alfa = b / (ac * rho * (1 - eb) * po)
    p = (1 - alfa * w) * po
    deltap = po - p
    return round(deltap, 4)


def calculate_pressure_fall_typetwo_massadecatalisador(fto, ac, w, rho, dp, eb, po, mi):
    gc = 417000000  # lbm ft / h^2 lbf
    G = fto / ac  # lbm/ft2 h

    bo = (G * (1 - eb) / (rho * gc * dp * eb**3)) * (
        ((150 * (1 - eb) * mi) / dp) + 1.75 * G
    )

    b = bo * (1 / 14.7) * (1 / 144)

    alfa = (2 * bo) / (ac * rho * (1 - eb) * po)
    p = ((1 - alfa * w) ** (0.5)) * po
    deltap = po - p
    return round(deltap, 4)


def calculate_pressure_fall_typeone_comprimento(fto, ac, L, rho, dp, eb, po, mi):
    gc = 417000000  # lbm ft / h^2 lbf
    G = fto / ac  # lbm/ft2 h

    bo = (G * (1 - eb) / (rho * gc * dp * eb**3)) * (
        ((150 * (1 - eb) * mi) / dp) + 1.75 * G
    )
    b = bo * (1 / 14.7) * (1 / 144)

    p = (1 - ((b * L) / po)) * po

    deltap = po - p
    return round(deltap, 4)


def calculate_pressure_fall_typetwo_comprimento(fto, ac, L, rho, dp, eb, po, mi):
    gc = 417000000  # lbm ft / h^2 lbf
    G = fto / ac  # lbm/ft2 h

    bo = ((G * (1 - eb)) / (rho * gc * dp * eb**3)) * (
        ((150 * (1 - eb) * mi) / dp) + 1.75 * G
    )
    b = bo * (1 / 14.7) * (1 / 144)

    p = (1 - ((2 * b * L) / po)) ** (1 / 2) * po

    deltap = po - p
    return round(deltap, 4)


def calculate_pressure_fall_reatortubular(fto, ac, w, rho, dp, eb, po, mi, k, vo):
    gc = 417000000  # lbm ft / h^2 lbf
    G = fto / ac  # lbm/ft2 h

    bo = (G * (1 - eb) / (rho * gc * dp * eb**3)) * (
        ((150 * (1 - eb) * mi) / dp) + 1.75 * G
    )

    b = bo * (1 / 14.7) * (1 / 144)

    alfa = b / (ac * rho * (1 - eb) * po)

    x = 1 - exp(-((k / vo) * w * (1 - (alfa * (w / 2)))))
    xf = x * 100
    return round(xf, 2)


def calculate_time_mixture_ordem_um(t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    volume = (qo / k2) * (x / (1 - x))

    return round(volume, 4)


def calculate_time_mixture_ordem_dois(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao
):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    volume = (qo / (k2 * cao)) * (x / (1 - x) ** 2)

    return round(volume, 4)


def calculate_time_mixture_ordem_um_doisreagentes(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao, cbo
):
    teta_b = cbo / cao
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * ((1 / t1) - (1 / t2)))

    volume = (qo * x) / (k2 * cao * (1 - x) * (teta_b - x))

    return round(volume, 4)


def calculate_time_mixture_ordem_um_reversivel(
    t1, k1, ke1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea
):
    R = 1.987  # cal
    R1 = 8.31  # J/mol K

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    ke2 = (
        ke1
        * (t2 / t1) ** (delta_cp / R1)
        * exp(((delta_hr - tr * delta_cp) / R1) * (1 / t1 - 1 / t2))
    )

    volume = qo / (k2 * (to / t2) * ((1 - x) - (x / ke2)))

    return round(volume, 4)


def calculate_time_tubular_ordem_um(t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    def determining(x):
        return (qo / k2) * (x / (1 - x))

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 4)


def calculate_time_tubular_ordem_dois(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao
):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    def determining(x):
        return (qo / (k2 * cao)) * (x / ((1 - x) ** 2))

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 4)


def calculate_time_tubular_ordem_um_doisreagentes(
    t1, k1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea, cao, cbo
):
    R = 1.987  # cal

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    teta_b = cbo / cao

    def determining(x):
        return qo / (k2 * cao * (1 - x) * (teta_b - x))

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 4)


def calculate_time_tubular_ordem_um_reversivel(
    t1, k1, ke1, cpi, to, tr, delta_hr, delta_cp, x, qo, ea
):
    R = 1.987  # cal
    R1 = 8.31  # J/mol K

    t2 = (x * delta_hr - cpi * to - x * delta_cp * tr) / ((-x * delta_cp - cpi))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    ke2 = (
        ke1
        * (t2 / t1) ** (delta_cp / R1)
        * exp(((delta_hr - tr * delta_cp) / R1) * (1 / t1 - 1 / t2))
    )

    def determining(x):
        return qo / (k2 * (to / t2) * ((1 - x) - (x / ke2)))

    volume, _ = integrate.quad(determining, 0, x)

    return round(volume, 4)


def calculate_temp_batch(t1, k1, cpi, to, delta_hr, delta_cp, x, qo, ea, cao):
    R = 1.987  # cal

    t2 = to - ((delta_hr * x) / (cpi + delta_cp * x))

    k2 = k1 * exp((ea / R) * (1 / t1 - 1 / t2))

    def determining(x):
        return 1 / (k2 * (1 - x))

    tempo, _ = integrate.quad(determining, 0, x)

    return (round(tempo, 4), round(t2, 4))
