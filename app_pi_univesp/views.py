

from django.shortcuts import render, redirect, reverse
from .models import Polos, Cursos
from django.views.generic import View
import pandas as pd
import plotly.express as px
import plotly.offline as py
from plotly.offline import plot
import plotly.graph_objs as go


def home(requests):
    return render(requests,'home.html')

def login(request):
    return render(request,'login.html')

class PolosView(View):
    def get(self, request, *args, **kwargs):
        data = Polos.objects.all()
        polos_df = [
            {
                'polos': x.polos,
                'total_vagas': x.total_vagas
            } for x in data
            ]

        df = pd.DataFrame(polos_df)

        data2 = Cursos.objects.all()
        cursos_df = [
            {
                'curso': x.curso,
                'disciplina': x.disciplina,
                'eixo': x.eixo,
            } for x in data2
            ]

        df2 = pd.DataFrame(cursos_df)

        fig1 = px.bar(df, x='polos', y='total_vagas')

        # Customizando o layout
        fig1.update_layout(title='Total de Vagas por Polo',
                  xaxis_title='Polo',
                  yaxis_title='Número Total de Vagas',
                  xaxis = go.layout.XAxis(tickangle = 45))

        fig_plot = plot(fig1, output_type = 'div')





# Gráfico 2
        disc_soma = df2.groupby(['curso', 'eixo']).count()['disciplina'].reset_index()
        print('debug')
        print(df2)
        fig2 = px.scatter(disc_soma, x='curso', y='disciplina', color='eixo', size = 'disciplina',
        labels = {"eixo": "Eixo"}   )

# Customizando o layout
        fig2.update_layout(title='Número de Disciplinas por Curso da Graduação',
                  xaxis_title='Curso',
                  yaxis_title='Nº de Disciplinas')

        fig2_plot = plot(fig2, output_type = 'div')
        ctx = {'fig1': fig_plot, 'fig2': fig2_plot}
        return render(request, 'graphs.html', ctx)
