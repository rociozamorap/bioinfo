import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

streamlit run bioinfo.py


# Título de la app
st.title("Selector de Gráficos")

# Opciones de gráficos
options = ["Seno", "Coseno", "Tangente", "Logaritmo"]
selection = st.radio("Selecciona un gráfico:", options)

# Función para generar gráficos
def generate_graph(option):
    fig, ax = plt.subplots()  # Crea un lienzo de Matplotlib
    x = np.linspace(0, 10, 100)  # Valores para el eje x

    # Gráfico según la opción seleccionada
    if option == "Seno":
        ax.plot(x, np.sin(x), label="Seno", color="blue")
    elif option == "Coseno":
        ax.plot(x, np.cos(x), label="Coseno", color="green")
    elif option == "Tangente":
        ax.plot(x, np.tan(x), label="Tangente", color="red")
    elif option == "Logaritmo":
        ax.plot(x, np.log(x + 1), label="Logaritmo", color="purple")
    
    ax.legend()
    ax.set_title(f"Gráfico de {option}")
    ax.grid(True)
    return fig

# Mostrar el gráfico seleccionado
try:
    fig = generate_graph(selection)
    st.pyplot(fig)
except Exception as e:
    st.error(f"¡Error al generar el gráfico: {e}!")
