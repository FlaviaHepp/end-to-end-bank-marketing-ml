# ==============================================================================
# FASE 3: EXPERIMENTACIÓN Y VALIDACIÓN DE HIPÓTESIS (A/B TESTING)
# ==============================================================================
# Contexto: En el archivo "01_eda_and_insights.py" identificamos que las 
# llamadas de larga duración (>375s) tienen una tasa de éxito del 78%. 
# 
# Este script simula la validación de un nuevo guion de ventas diseñado para 
# aumentar el engagement, comparándolo con el método tradicional mediante 
# estadística Frecuentista y Bayesiana.
# ==============================================================================

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import beta
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import TTestIndPower

f = pd.read_csv("bank.csv")

# ------------------------------------------------------------------------------
# 1. DISEÑO DEL EXPERIMENTO (POWER ANALYSIS)
# Antes de lanzar la prueba, calculamos cuántos clientes necesitamos contactar
# para que los resultados sean estadísticamente confiables.
# ------------------------------------------------------------------------------

effect_size = 0.12  # Queremos detectar al menos un 12% de mejora relativa
alpha = 0.05        # Umbral de error falso positivo (5%)
power = 0.80        # Probabilidad de detectar el efecto si realmente existe

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, power=power, alpha=alpha)

print("--- FASE 1: DISEÑO DEL EXPERIMENTO ---")
print(f"Tamaño de muestra requerido por grupo: {int(sample_size)}")
print("-" * 40)

# ------------------------------------------------------------------------------
# 2. PRUEBA A/B FRECUENTISTA (Z-TEST)
# Simulamos los resultados tras 15 días de campaña con el nuevo guion.
# ------------------------------------------------------------------------------

# Datos simulados basados en el volumen del dataset original
n_control, conv_control = 1200, 144  # Grupo A: Guion Viejo (12% conversión)
n_test, conv_test = 1200, 186       # Grupo B: Guion Nuevo (15.5% conversión)

# Ejecución del test de proporciones
z_stat, p_value = proportions_ztest([conv_test, conv_control], [n_test, n_control], alternative='larger')

print("\n--- FASE 2: RESULTADOS FRECUENTISTAS (Z-TEST) ---")
print(f"Tasa Conversión Control: {conv_control/n_control:.2%}")
print(f"Tasa Conversión Test (Nuevo Guion): {conv_test/n_test:.2%}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("RESULTADO: Significancia estadística alcanzada. El nuevo guion mejora la conversión.")
else:
    print("RESULTADO: No hay evidencia suficiente para asegurar que el cambio sea efectivo.")
print("-" * 40)

# ------------------------------------------------------------------------------
# 3. INFERENCIA BAYESIANA (PROBABILIDAD DE ÉXITO)
# Para el negocio, el P-Value es difícil de interpretar. Usamos Bayes para dar 
# una respuesta clara: "¿Qué tan probable es que el nuevo guion sea mejor?"
# ------------------------------------------------------------------------------

def perform_bayesian_test(successes_a, total_a, successes_b, total_b, sims=100000):
    # Definimos la distribución 'prior' (Beta 1,1 es una distribución uniforme)
    # Posteriores: Beta(éxitos + 1, fracasos + 1)
    samples_a = beta.rvs(successes_a + 1, total_a - successes_a + 1, size=sims)
    samples_b = beta.rvs(successes_b + 1, total_b - successes_b + 1, size=sims)
    
    # Probabilidad de que B sea mejor que A
    prob_b_better_than_a = np.mean(samples_b > samples_a)
    
    # Cálculo del Lift esperado (Mejora porcentual estimada)
    lift = (np.mean(samples_b) - np.mean(samples_a)) / np.mean(samples_a)
    
    return prob_b_better_than_a, lift

prob_sup, expected_lift = perform_bayesian_test(conv_control, n_control, conv_test, n_test)

print("\n--- FASE 3: ANÁLISIS BAYESIANO PARA STAKEHOLDERS ---")
print(f"Probabilidad de que el Nuevo Guion sea mejor que el viejo: {prob_sup:.2%}")
print(f"Mejora esperada (Lift) en las ventas: {expected_lift:.2%}")

# Conclusión ejecutiva
if prob_sup > 0.95:
    print("\nRECOMENDACIÓN FINAL: Desplegar el nuevo guion en todas las sucursales.")
    print("La probabilidad de éxito supera el umbral de confianza del 95%.")
else:
    print("\nRECOMENDACIÓN FINAL: Mantener el guion actual y recolectar más datos.")
print("=" * 60)