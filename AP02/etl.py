
 #%%  
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

        df_sp = self.transformed['SOPRADORA']
        for indice,linha in df_pc.iterrows():
            numero = linha['numero']
            vazao_sopro=linha['vazao_sopro']
            pressao_sopro = linha['pressao_sopro']
            sp = SOPRADORA(numero = numero, vazao_sopro = vazao_sopro, pressao_sopro = pressao_sopro)
            session.add(sp)
        session.commit()

        df_fs = self.transformed['FRESADORA']
        for indice,linha in df_pc.iterrows():
            numero = linha['numero']
            velocidade_rotacao = linha['velocidade_rotacao']
            profundidade_corte = linha['profundidade_corte']
            fs = FRESADORA(numero = numero, velocidade_rotacao = velocidade_rotacao, profundidade_corte = profundidade_corte)
            session.add(fs)
        session.commit()

        df_tc = self.transformed['TORNO_CNC']
        for indice,linha in df_pc.iterrows():
            numero = linha['numero']
            velocidade_rotacao = linha['velocidade_rotacao']
            tolerancia = linha['tolerancia']
            tc = TORNO_CNC(numero = numero, velocidade_rotacao = velocidade_rotacao, tolerancia = tolerancia)
            session.add(tc)
        session.commit()

        df_i3d = self.transformed['IMPRESSORA_3D']
        for indice,linha in df_pc.iterrows():
            numero = linha['numero']
            espessura_camada = linha['espessura_camada']
            tipo_material = linha['tipo_material']
            i3d = IMPRESSORA_3D(numero = numero, espessura_camada = espessura_camada, tipo_material = tipo_material)
            session.add(i3d)
        session.commit()





