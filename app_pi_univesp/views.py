

from django.shortcuts import render, redirect, reverse
from .models import Polos
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

        fig1 = px.bar(df, x='polos', y='total_vagas')

        fig_plot = plot(fig1, output_type = 'div')

        ctx = {'fig1': fig_plot}
        return render(request, 'home.html', ctx)
