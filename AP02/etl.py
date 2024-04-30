import json
from abstract_etl import AbstractETL
from classes import *
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

 #%%  
class ETL(AbstractETL):
    def __init__(self, source: str, target: str):
        super().__init__(source, target)

    def extract(self):           
        with open(self.source, 'r') as arquivo:
            dados_arquivo = json.load(arquivo)
        self.extracted = dados_arquivo

    def transform(self):
        dicionario = {}
        for elemento in self.extracted:
            chave= elemento['tipo']
            lista_atributos = elemento['atributos']
            df = pd.DataFrame(lista_atributos)
            dicionario[chave]=df
        self.transformed = dicionario

    def load(self):
        engine = create_engine(self.target)
        Session = sessionmaker(bind=engine)
        session = Session()
    
        df_up = self.transformed['UNIDADE_PRODUCAO']
        for indice,linha in df_up.iterrows():
            numero = linha['numero']
            pchn=linha['peca_hora_nominal']
            up = UNIDADE_PRODUCAO(numero=numero,peca_hora_nominal=pchn)
            session.add(up)
        session.commit()

        df_rg = self.transformed['REGISTRO FALHA']
        for indice,linha in df_rg.iterrows():
            id = linha['id']
            severidade=linha['severidade']
            inicio = linha['inicio']
            fim=linha['fim']
            numero_unidade_producao = linha['numero_unidade_producao']
            rg = REGISTRO_FALHA(id=id,severidade = severidade, inicio = inicio, fim = fim, numero_unidade_producao = numero_unidade_producao)
            session.add(rg)
        session.commit()

        df_pc = self.transformed['PECA']
        for indice,linha in df_pc.iterrows():
            numero = linha['numero']
            status=linha['status']
            inicio_fabricacao = linha['inicio_fabricacao']
            fim_fabricacao=linha['fim_fabricacao']
            numero_unidade_producao = linha['numero_unidade_producao']
            pc = PECA(numero = numero, status = status, inicio_fabricacao=inicio_fabricacao, fim_fabricacao = fim_fabricacao, numero_unidade_producao = numero_unidade_producao)
            session.add(pc)
        session.commit()
