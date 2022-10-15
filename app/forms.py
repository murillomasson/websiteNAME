from django import forms
import pycep_correios

TURNO =(
    ('m', 'Manhã'),
    ('t', 'Tarde'),
    ('n', 'Noite'),
    ('m', 'Madrugada'),
)

PARENTESCO =(
    ('p', "Mãe ou Pai"),
    ('f', "Filho(a)"),
    ('c', "Cônjuge"),
    ('o', "Outro"),
)

class FormFiliacao(forms.Form):
    nome = forms.CharField(label="Nome Completo")
    email_principal = forms.EmailField(required=False, max_length=20, label="E-mail Principal")
    email_hcpa = forms.EmailField(label="E-mail HCPA")
    tel_res = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"(00) 0000-0000"}), required=False, label="Telefone residencial")
    tel_cel = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"(00) 00000-0000"}), label="Telefone celular")
    rg = forms.IntegerField(label="RG")
    orgao_exp = forms.CharField(max_length=10, label="Órg. Exp.")
    cpf = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"000.000.000-00"}), label="CPF")
    nasc = forms.DateField(widget=forms.TextInput(attrs={'data-mask':"00/00/0000"}), label="Data de nascimento")
    cep = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"00000-000"}), label="CEP")
    endereco = forms.CharField(label="Endereço") # receive address from CEP
    numero = forms.CharField(max_length=5, label="Nº.")
    bairro = forms.CharField(label="Bairro") # receive from CEP
    complemento = forms.CharField(required=False, max_length=15, label="Compl.")

    cartao = forms.IntegerField(label="Cartão-ponto HCPA")
    matricula_hcpa = forms.IntegerField(max_value=10, label="Matrícula HCPA")
    admissao = forms.DateField(required=False, widget=forms.TextInput(attrs={'data-mask':"00-00-0000"}), label="Data de Admissão")
    setor = forms.CharField(max_length=20, label="Setor de trabalho")
    ramal = forms.IntegerField(max_value=8, label="Ramal do setor", required=False)
    turno = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=TURNO)
    cargo = forms.CharField(max_length=20, help_text="Cargo")
    salario_nominal = forms.FloatField(widget=forms.TextInput(attrs={'data-mask': "00.000,00"}),
                                       label="Salário Nominal",
                                       help_text="Insira 7 dígitos,"
                                                 "por exemplo: 09.999,99")


    nome_1 = forms.CharField(required=False, max_length=25, label="Nome")
    nasc_1 = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'data-mask':"00/00/0000"}), label="Data de Nascimento")
    tel_1 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'data-mask':"(00) 00000-0000"}), label="Telefone") #
    parentesco_1 = forms.ChoiceField(required=False, choices=PARENTESCO, label="Parentesco")
    qual = forms.CharField(required=False, label="se for outro, qual?")

    nome_2 = forms.CharField(required=False, max_length=25, label="Nome")
    nasc_2 = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'data-mask': "00/00/0000"}),
                                 label="Data de Nascimento")
    tel_2 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}),
                               label="Telefone")  #
    parentesco_2 = forms.ChoiceField(required=False, choices=PARENTESCO, label="Parentesco")
    qual_2 = forms.CharField(required=False, label="se for outro, qual?")

    nome_3 = forms.CharField(required=False, max_length=25, label="Nome")
    nasc_3 = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'data-mask': "00/00/0000"}),
                                 label="Data de Nascimento")
    tel_3 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}),
                               label="Telefone")  #
    parentesco_3 = forms.ChoiceField(required=False, choices=PARENTESCO, label="Parentesco")
    qual_3 = forms.CharField(required=False, label="se for outro, qual?")

    nome_4 = forms.CharField(required=False, max_length=25, label="Nome")
    nasc_4 = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'data-mask': "00/00/0000"}),
                                 label="Data de Nascimento")
    tel_4 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}),
                               label="Telefone")  #
    parentesco_4 = forms.ChoiceField(required=False, choices=PARENTESCO, label="Parentesco")
    qual_4 = forms.CharField(required=False, label="se for outro, qual?")

    nome_5 = forms.CharField(required=False, max_length=25, label="Nome")
    nasc_5 = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'data-mask': "00/00/0000"}),
                                 label="Data de Nascimento")
    tel_5 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}),
                               label="Telefone")  #
    parentesco_5 = forms.ChoiceField(required=False, choices=PARENTESCO, label="Parentesco")
    qual_5 = forms.CharField(required=False, label="se for outro, qual?")


class Duvidas:
    nome = forms.CharField(max_length=25, help_text="Nome")
    email = forms.EmailField(help_text="Email")
    tel = forms.IntegerField(widget=forms.TextInput(attrs={'data-mask':"00-00-0000"}))
    mensagem = forms.CharField(max_length=150, help_text="Tire sua dúvida")
