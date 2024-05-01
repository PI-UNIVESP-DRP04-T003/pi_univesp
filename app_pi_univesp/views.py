

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
                'polo': x.polo,
                'disciplina': x.disciplina,
                'eixo': x.eixo
            } for x in data2
            ]

        df2 = pd.DataFrame(cursos_df)

        fig1 = px.bar(df, x='polos', y='total_vagas')

        # Customizando o layout
        fig1.update_layout(title='Total de Vagas por Polo',
                  xaxis_title='Polo',
                  yaxis_title='Número Total de Vagas')

        fig_plot = plot(fig1, output_type = 'div')



# Gráfico 2
        disc_soma = df2.groupby(['polo', 'eixo']).count()['disciplina'].reset_index()
        print('debug')
        print(df2)
        fig2 = px.scatter(disc_soma, x='polo', y='disciplina', color='eixo')

# Customizando o layout
        fig2.update_layout(title='Número de Disciplinas por Polo',
                  xaxis_title='Polo',
                  yaxis_title='Disciplina')

        fig2_plot = plot(fig2, output_type = 'div')
        ctx = {'fig1': fig_plot, 'fig2': fig2_plot}
        return render(request, 'graphs.html', ctx)
