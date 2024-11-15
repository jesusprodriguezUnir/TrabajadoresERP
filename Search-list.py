import streamlit as st
import pandas as pd

# Tu JSON
data = [
    {
        "DisplayName": "Mikel izal",
        "Id": 100000834,
        "EstadoTrabajador": "Activo",
        "Nombre": "MIKEL",
        "Apellido1": "IZAL",
        "Email": "MIKELIZALz@unir.net",
        "FechaNacimiento": "1968-06-05T00:00:00Z"
    },
    {
        "DisplayName": "MIKEL ERENCHUN",
        "Id": 100000836,
        "EstadoTrabajador": "Activo",
        "Nombre": "MIKEL",
        "Apellido1": "ERENCHUN",
        "Email": "mikel.eren@unir.net"
    },
    {
        "DisplayName": "María Paz Sanz Díaz",
        "Id": 100000838,
        "EstadoTrabajador": "Activo",
        "Nombre": "María Paz",
        "Apellido1": "Sanz",
        "Email": "maripaz.sanz@unir.net",
        "FechaNacimiento": "1976-02-23T00:00:00Z"
    },
    {
        "DisplayName": "MONICA PEREZ INIESTA",
        "Id": 100000840,
        "EstadoTrabajador": "Activo",
        "Nombre": "MONICA",
        "Apellido1": "PEREZ",
        "Email": "monica.perez@unir.net"
    },
    {
        "DisplayName": "MARCOS SANCHEZ GARCIA",
        "Id": 100000841,
        "EstadoTrabajador": "Activo",
        "Nombre": "MARCOS",
        "Apellido1": "SANCHEZ",
        "Email": "marcos.sanchez@unir.net"
    },
    {
        "DisplayName": "Alicia Keys",
        "Id": 100000842,
        "EstadoTrabajador": "Activo",
        "Nombre": "100000842",
        "Apellido1": "100000842",
        "Email": "100000842@unir.net"
    },
    {
        "DisplayName": "100000843",
        "Id": 100000843,
        "EstadoTrabajador": "Activo",
        "Nombre": "SUSANA",
        "Apellido1": "RODRIGUEZ",
        "Email": "100000843@unir.net",
        "FechaNacimiento": "1972-10-21T00:00:00Z"
    },
    {
        "DisplayName": "100000844",
        "Id": 100000844,
        "EstadoTrabajador": "Activo",
        "Nombre": "100000844",
        "Apellido1": "RICO",
        "Email": "100000844@cepal.es"
    },
    {
        "DisplayName": "100000845",
        "Id": 100000845,
        "EstadoTrabajador": "Activo",
        "Nombre": "100000845",
        "Apellido1": "100000845",
        "Email": "100000845@unir.net"
    },
    {
        "DisplayName": "100000846a",
        "Id": 100000846,
        "EstadoTrabajador": "Activo",
        "Nombre": "100000846",
        "Apellido1": "100000846",
        "Email": "100000846@unir.net"
    }
]

# Lista de universidades
universidades = ["Universidad de Madrid", "Universidad de Barcelona", "Universidad de Valencia", "Universidad de Sevilla"]

# Convertir JSON a DataFrame
df = pd.DataFrame(data)

# Título de la aplicación
st.title("Selección de Trabajadores")

# Mostrar la tabla con multiselección
selected_indices = st.multiselect("Selecciona los trabajadores", df.index, format_func=lambda x: df.loc[x, "DisplayName"])

# Mostrar la tabla completa
st.write("Todos los trabajadores:")
st.dataframe(df)

# Mostrar los registros seleccionados
if selected_indices:
    selected_rows = df.loc[selected_indices]
    st.write("Trabajadores seleccionados:")
    st.dataframe(selected_rows)
else:
    st.write("No se han seleccionado trabajadores.")

# Botón para asignar universidades
if st.button("Asignar Universidades"):
    if selected_indices:
        st.write("Asignar universidades a los trabajadores seleccionados:")
        for index in selected_indices:
            trabajador = df.loc[index]
            universidades_seleccionadas = st.multiselect(f"Selecciona universidades para {trabajador['DisplayName']}", universidades, key=index)
            st.write(f"{trabajador['DisplayName']} asignado a {', '.join(universidades_seleccionadas)}")
    else:
        st.write("No se han seleccionado trabajadores para asignar universidades.")
