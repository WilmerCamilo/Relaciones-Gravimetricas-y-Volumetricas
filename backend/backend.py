from dash import html
import dash_bootstrap_components as dbc

imagen = html.Img(src='backend/diagrama.jpg')

fases = dbc.Container(
    [
        imagen
    ]
)


# # AVANCE CODIGO PYTHON

# # Solicitamos los datos de entrada al usuario
# masa_humedo = float(input("Ingrese la masa del suelo húmedo (en gramos): "))
# masa_seco = float(input("Ingrese la masa del suelo seco (en gramos): "))
# volumen = float(input("Ingrese el volumen total del suelo (en centímetros cúbicos): "))

# # Calculamos las relaciones gravimétricas y volumétricas
# humedad = ((masa_humedo - masa_seco) / masa_seco) * 100
# densidad_aparente = masa_humedo / volumen
# densidad_real = masa_seco / volumen
# porosidad = ((densidad_aparente - densidad_real) / densidad_aparente) * 100

# # Imprimimos los resultados
# print("La humedad del suelo es: {:.2f}%".format(humedad))
# print("La densidad aparente del suelo es: {:.2f} g/cm³".format(densidad_aparente))
# print("La densidad real del suelo es: {:.2f} g/cm³".format(densidad_real))
# print("La porosidad del suelo es: {:.2f}%".format(porosidad))

# # Importar las librerias necesarias

# import sympy as sp

# # Definir las variables

# Ww, Ws, Vv, Vs, Vt, Vw, peso_unitario_agua = sp.symbols('Ww Ws Vv Vs Vt Vw gamma_w')
# w, e, n, Wt, peso_unitario_humedo, peso_unitario_particulas_solidas, peso_unitario_seco, Gs, Sr = sp.symbols('w e n Wt gamma_t gamma_s gamma_d Gs Sr')

# # definir las ecuaciones a resolver por medio de un proceso iterativo.

# eq1 = w - (Ww/Ws)*100
# eq2 = e - Vv/Vs
# eq3 = e - n/(1-n)
# eq4 = n - Vv/Vt
# eq5 = n - e/(1+e)
# eq6 = Wt - Ww - Ws
# eq7 = peso_unitario_humedo - Wt/Vt
# eq8 = peso_unitario_particulas_solidas - Ws/Vs
# eq9 = peso_unitario_seco - Ws/Vt
# eq10 = Gs - peso_unitario_particulas_solidas/peso_unitario_agua
# eq11 = Gs - Ws/(Vs*peso_unitario_agua)
# eq12 = Sr - (Vw/Vv)*100

# # Definir las variables o datos conocidos por el usuario con sus respectivos valores

# variables_conocidas = [Ww, Ws, Vv, Vs, Vt, Vw, peso_unitario_agua]
# valores_variables = [100, 200, 0.7, 0.9, 1, 0.1, 9.81]

# # Definir las variables desconocidas y los valores semilla (iniciales) para realizar el cálculo iterativo mas adelante

# variables_desconocidas = [w, e, n, Wt, peso_unitario_humedo, peso_unitario_particulas_solidas, peso_unitario_seco, Gs, Sr]
# valores_semilla = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# # Proceso iterativo

# max_iteraciones = 1000
# tolerancia = 1e-6
# for i in range(max_iteraciones):
#   valores_semilla_prev = valores_semilla.copy()
#   # Resolver las variables desconocidas
#   for j in range(len(variables_desconocidas)):
#     eq = locals()[f'eq{j+1}']
#     var = variables_desconocidas[j]
#     val = valores_semilla[j]
#     sol = sp.solve(eq.subs(zip(variables_conocidas, valores_variables)).subs(zip(variables_desconocidas, valores_semilla)), var, val)
#     valores_semilla[j] = sol

#   # Comprobar con los valores de las variables conocidas
#   for j in range(len(variables_conocidas)):
#     var = variables_conocidas[j]
#     val = valores_variables[j]
#     sol = sp.solve(eq12.subs(zip(variables_conocidas, valores_variables)).subs(zip(variables_desconocidas, valores_semilla)), var)
#     if len(sol) > 0:
#       valores_variables[j] = sol[0]

#   # Comprobar la convergencia de las respuestas (Comprobar que la solución es correcta)

#   if all(abs(old_val - new_val) < tolerancia for old_val, new_val in zip(valores_semilla, valores_semilla_prev) for old_val, new_val in zip(*[iter(old_val)]*2) for new_val in zip(*[iter(new_val)]*2)):
#     break

# for i in range(len(variables_desconocidas)):
#   print(f"{variables_desconocidas[i]} = {valores_semilla[i]}")
