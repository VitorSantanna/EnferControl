#coding: utf-8
#Author: Joao Vitor Sant Anna
##################
####GDM Family####
##################

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
import DaoEnferControl as s


s.criar_tabela()


class TelaPrincipal(Screen):
    pass


class TelaCadastro(Screen):
    color = 200, 200, 200, 1
    txtnome = ObjectProperty(None)
    txttitulo = ObjectProperty(None)
    spnturma = ObjectProperty(None)
    spnlocal = ObjectProperty(None)
    data_inicio = ObjectProperty(None)
    data_fim = ObjectProperty(None)
    spnsetor = ObjectProperty(None)
    spnhoras = ObjectProperty(None)

    def enviar(self):
        nome = self.txtnome.text
        titulo = self.txttitulo.text
        turma = self.spnturma.text
        local = self.txtlocal.text
        data_inicio = self.txtinicio.text
        data_fim= self.txtinicio.text
        setor = self.spnsetor.text
        horas = self.spnhoras.text
        atividades = self.txtatividade.text
        lista = [nome, titulo, turma, local, data_inicio, data_fim, setor, horas, atividades]
        r = s.registrar_dados(*lista)
        popup = Popup(title="Registro de Dados",
                      content=Label(text="""             Olá """
                                         +nome+"\n"+r, font_size='13sp', markup=1),
                      size_hint=(.36, .18), pos_hint={"center_x": .5, "center_y": .5}, auto_dismiss='False')
        popup.open()


class TelaSelecao(Screen):
    s.contar_linhas()


class TelaAtualizacao(Screen):
    color = 200, 200, 200, 1
    txtnome = ObjectProperty(None)
    txttitulo = ObjectProperty(None)
    spnturma = ObjectProperty(None)
    lbllocal = ObjectProperty(None)
    data_inicio = ObjectProperty(None)
    data_fim = ObjectProperty(None)
    spnsetor = ObjectProperty(None)
    spnhoras = ObjectProperty(None)

    def enviar(self):
        ident = "1"
        nome = self.txtnome.text
        titulo = self.txttitulo.text
        turma = self.spnturma.text
        local = self.txtlocal.text
        data_inicio = self.txtinicio.text
        data_fim= self.txtinicio.text
        setor = self.spnsetor.text
        horas = self.spnhoras.text
        atividades = self.txtatividade.text
        lista = [nome, titulo, turma, local, data_inicio, data_fim, setor, horas, atividades, ident]
        a = s.atualizar_dados(*lista)
        popup = Popup(title="Atualização de Dados",
                      content=Label(text="""             Olá """
                                         +nome+"\n"+a, font_size='13sp', markup=1),
                      size_hint=(.36, .18), pos_hint={"center_x": .5, "center_y": .5}, auto_dismiss='False')
        popup.open()


class TelaConsulta(Screen):
    color = 200, 200, 200, 1
    txtnome = ObjectProperty(None)
    txttitulo = ObjectProperty(None)
    spnturma = ObjectProperty(None)
    lbllocal = ObjectProperty(None)
    data_inicio = ObjectProperty(None)
    data_fim = ObjectProperty(None)
    spnsetor = ObjectProperty(None)
    spnhoras = ObjectProperty(None)

    def on_pre_enter(self, *args):
        r = s.consultar_dados(1)
        saida =['', '', '', '', '', '', '', '', '', '']
        for y in range(10):
            saida[y] = r[y]
        popup = Popup(title="",
                      content=Label(text="""Consulta realizada com sucesso!\n"""
                                         + saida[1] + "\n", font_size='13sp', markup=1),
                      size_hint=(.36, .18), pos_hint={"center_x": .5, "center_y": .5}, auto_dismiss='False')
        popup.open()
        self.ids.lblNome.text = saida[1]
        self.ids.lblTitulo.text = saida[2]
        self.ids.lblTurma.text = saida[3]
        self.ids.lblLocal.text = saida[4]
        self.ids.lblInicio.text = saida[5]
        self.ids.lblTermino.text = saida[6]
        self.ids.lblSetor.text = saida[7]
        self.ids.lblHorario.text = str(saida[8])
        self.ids.lblRelatorio.text = saida[9]

    def click(self):
        i = s.imprimir_relatorio


class EnferControlApp(App):

    def build(self):
        Builder.load_string(open("enfercontrol.kv", encoding="utf-8").read(), rulesonly=True)
        root = ScreenManager()
        self.icon = 'icon.jpg'
        self.title = "EnferControl"
        root.add_widget(TelaPrincipal(name='EnferControl'))
        root.add_widget(TelaCadastro(name='Tela de Cadastro'))
        root.add_widget(TelaSelecao(name='Tela de Selecao'))
        root.add_widget(TelaAtualizacao(name='Tela de Atualizaçao'))
        root.add_widget(TelaConsulta(name='Tela de Consulta'))
        return root


enf = EnferControlApp()


if __name__ == '__main__':
    enf.run()



