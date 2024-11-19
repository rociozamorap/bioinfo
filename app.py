import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título de la app
st.title("Selector de Gráficos")

# Opciones de gráficos
options = ["Gráfico 1", "Gráfico 2", "Gráfico 3", "Gráfico 4"]
selection = st.radio("Selecciona un gráfico:", options)

# Función para generar gráficos
def generate_graph(option):
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    
    if option == "Gráfico 1":
        ax.plot(x, np.sin(x), label="Seno", color="blue")
    elif option == "Gráfico 2":
        ax.plot(x, np.cos(x), label="Coseno", color="green")
    elif option == "Gráfico 3":
        ax.plot(x, np.tan(x), label="Tangente", color="red")
    elif option == "Gráfico 4":
        ax.plot(x, np.log(x+1), label="Logaritmo", color="purple")
    
    ax.legend()
    ax.set_title(option)
    ax.grid(True)
    return fig

# Mostrar el gráfico seleccionado
fig = generate_graph(selection)
st.pyplot(fig)
