import streamlit as st
import pandas as pd

df= pd.DataFrame()

df[['horario_linha','numero_onibus']] = None

def criar_lista_horarios(inicio,fimm,intervalos):
    horarios=[]
    hora_atual= inicio
    for horario_limite in intervalos:
        while hora_atual <= horario_limite:
            horarios.append(hora_atual)
            hora_atual += datetime.timedelta(minutes=intervalo)
    return horarios 

st.markdown('# Controle de Frota de Ônibus')

extensao_ida_volta = st.sidebar.number_input('Digite a extensão de ida e volta da Linha')

velocidade_comercial = st.sidebar.number_input('Digite o valor da velocidade comercial')

numero_passageiros_pico = st.sidebar.number_input('Digite o volume de passageiros PICO')

numero_passageiros_normal = st.sidebar.number_input('Digite o volume de passageiros NORMAL')

capacidade_dos_onibus_pico = st.sidebar.number_input('Digite a capacidade do ônibus PICO',1)

capacidade_dos_onibus_normal = st.sidebar.number_input('Digite a capacidade do ônibus NORMAL',1)

from datetime import time
import datetime as dt

horario_da_linha = st.sidebar.slider(
    "Selecione o intervalo do horário da linha:", value=(time(7, 00), time(8, 00))
)

horario_pico = st.sidebar.slider(
    "Selecione o intervalo do horário de PICO:", value=(time(7, 00), time(8, 00))
)


## REALIZANDO OS CÁLCULOS

# Coeficiente de Pico e Normal

qp = (numero_passageiros_pico/capacidade_dos_onibus_pico)

qn = numero_passageiros_normal/capacidade_dos_onibus_normal

# Calculando Headway de Pico e Normal

if qp !=0 and qn != 0:
    hp = 60/qp
    hn = 60/qn

# Calculando Tempo de ciclo e Pico

    tc = extensao_ida_volta/velocidade_comercial
    tp = horario_pico[1].hour - horario_pico[0].hour

# Verificando a condição da cálculo da Frota de Pico e Normal
    if tc <= tp:
      fp = tc/hp
      fn = tc/hn
    else:
      fp = (tp/hp) + (tc-tp)/hn
      fn = tc/hn

# Desenvolvendo a tabela
    if fp and fn:
      intervalos = [(dt.time(horario_pico[0].hour,0),hp),(dt.time(horario_pico[0].hour,0),hn)]
    
      lista = criar_lista_horarios(horario_da_linha[0],horario_da_linha[1],intervalos)

    #  st.write((dt.time(horario_pico[0].hour,0),hp))
      hora_atual = (dt.time(horario_da_linha[0].hour,0)
      for horario_limite, intervalo in intervalos:
        while hora_atual.time  <= horario_limite:
          st.write(hora_atual)
