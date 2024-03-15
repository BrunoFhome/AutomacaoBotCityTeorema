from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA CONTABIL 23.07 - PARTE DE CADASTROS
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - ICTUS 0000024
"""

class Bot(DesktopBot) :
    

    def find_button(self, label) :
        try :
            if not self.find(label,  matching=0.97, waiting_time=10000) :
                raise Exception("Element not found")
        except Exception as error :
            print("Error")
            filepath = self.save_screenshot(r"C:\Users\Usuário\Desktop\printserros\screenshot.png")
            maestro.error(task_id=execution.task_id,
                          exception=error,
                          screenshot=filepath)
            maestro.alert(task_id=execution.task_id,
                          title="Title",
                          message="Erro ao executar o Bot",
                          alert_type=AlertType.ERROR)




    def action(self,execution=None) :
        """
        self.execute(r"C:\Teorema\bin\contabil")
        
        self.wait(6000)
        self.tab()

        self.type_keys_with_interval(100,"teorema")
        self.wait(1000)
        self.tab()
        self.tab()
    
        self.wait(1000)
        self.type_keys_with_interval(100,"1811")
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_empresas_cad_1_men_", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_cad_1_men_")
        self.click()
        
        if not self.find( "cont_empresas_23_empresas", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_23_empresas")
        self.click()
        if not self.find( "cont_localizar_empresas_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_empresas_cadastro")
        self.click()
        if not self.find( "cont_incluir_cadastro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cadastro_empresa")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cadastro_empresa_nao", matching=0.97, waiting_time=10000):
            not_found("cont_cadastro_empresa_nao")
        self.click()
        self.wait(2000)
        self.shift_tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"12312312333")
        self.wait(1000)
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1 
        x = 0
        self.tab()
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_municipio_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_municipio_buscar")
        self.click_relative(56, 27)
        if not self.find( "cont_localizar_municipios", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_municipios")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"85050440")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com")
        self.tab()
        self.type_keys_with_interval(100,"www.google.com") 
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")      
        if not self.find( "cont_funcao_responsavel_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_funcao_responsavel_buscar")
        self.click_relative(50, 26)
        if not self.find( "cont_localizar_municipios", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_municipios")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"www.google.com")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_2_informacoes_de_recursos", matching=0.97, waiting_time=10000):
            not_found("cont_2_informacoes_de_recursos")
        self.click()
        x = 0
        while x < 13:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        
        x = 0 
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        
        x = 0 
        while x < 6:
            self.type_down()
            x += 1
            
        self.tab()
        x = 0 
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"12312312333")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0 
        while x < 6:
            self.type_down()
            x += 1
        x = 0 
        
        while x < 6:
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "Cont_6_RaisDSRGPS", matching=0.97, waiting_time=10000):
            not_found("Cont_6_RaisDSRGPS")
        self.click()
        
        self.wait(1000)
        if not self.find( "Cont_gerar_RAIS", matching=0.97, waiting_time=10000):
            not_found("Cont_gerar_RAIS")
        self.click()
        
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        
        self.tab()
        self.type_down()
        self.type_down()
 
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        x = 0
        while x <12:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_7_mensagens_observacoes", matching=0.97, waiting_time=10000):
            not_found("cont_7_mensagens_observacoes")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_3_informacoes_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_3_informacoes_fiscais")
        self.click()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 12:
            self.type_down()
            x += 1
            
        self.tab()
        
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1
            
            
        self.tab()
        self.space()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.space()
        
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        while x < 20:
            self.type_down()
            x += 1
        x = 0
        while x <6:
            self.space()
            self.wait(1000)
            self.space()
            self.tab()
            x += 1
        self.tab()
        self.type_down()
        self.type_down()
        if not self.find( "cont_4_agrupamentos", matching=0.97, waiting_time=10000):
            not_found("cont_4_agrupamentos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_grupo_de_empresas_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresas_buscar")
        self.click_relative(68, 28)
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_usa_clientes_forn_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_usa_clientes_forn_buscar")
        self.click_relative(69, 27)
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_usa_plano_de_custos_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_usa_plano_de_custos_buscar")
        self.click_relative(71, 25)
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tabela_de_precos", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_precos")
        self.click_relative(66, 27)
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.backspace()
        if not self.find( "cont_usa_contratos_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_contratos_da_empresa")
        self.click_relative(69, 31)
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_planos_de_contas_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_planos_de_contas_da_empresa")
        self.click_relative(68, 30)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_itens_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_itens_da_empresa")
        self.click_relative(67, 26)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_vendedores_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_vendedores_da_empresa")
        self.click_relative(68, 27)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_tabela_de_precos_servico_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_precos_servico_busc")
        self.click_relative(66, 23)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.backspace()
        self.backspace()
        self.backspace()
        self.backspace()
        if not self.find( "cont_contabilista_busc", matching=0.97, waiting_time=10000):
            not_found("cont_contabilista_busc")
        self.click_relative(68, 24)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_ccliente", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_ccliente")
        self.click()
        
        self.wait(1000)

        #
        if not self.find( "cont_usa_historico_da_empre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_historico_da_empre_busc")
        self.click_relative(71, 29)
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_precos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_precos_da_empresa_busc")
        self.click_relative(67, 29)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_situacao_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_situacao_da_empresa_busc")
        self.click_relative(68, 31)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_usa_veiculos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_veiculos_da_empresa_busc")
        self.click_relative(69, 28)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        #MOUSE JA PAROU EM CIMA DO SALVAR
        #if not self.find( "cont_botao_de_salvar_cadastro", matching=0.97, waiting_time=10000):
        #   not_found("cont_botao_de_salvar_cadastro")
        self.wait(1000)
        self.click()
        
        
        if not self.find( "cont_contas_de_cliente_1", matching=0.97, waiting_time=10000):
            not_found("cont_contas_de_cliente_1")
        self.click_relative(123, 26)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        #mouse esta em cima
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        
        
        if not self.find( "cont_contas_de_fornecedores_2", matching=0.97, waiting_time=10000):
            not_found("cont_contas_de_fornecedores_2")
        self.click_relative(125, 26)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_codigo_contabil_clientes", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_clientes")
        self.click_relative(127, 26)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_cont_fornecedor_bsc_12", matching=0.97, waiting_time=10000):
            not_found("cont_cont_fornecedor_bsc_12")
        self.click_relative(126, 30)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_conta_contabil_1", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_1")
        self.click_relative(125, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_conta_contabil_2", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_2")
        self.click_relative(126, 28)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_conta_contabil_3", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_3")
        self.click_relative(127, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_conta_contabil_4", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_4")
        self.click_relative(91, 28)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        
        if not self.find( "cont_conta_contabil_5", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_5")
        self.click_relative(126, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_6", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_6")
        self.click_relative(127, 28)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_7", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_7")
        self.click_relative(125, 27)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_8", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_8")
        self.click_relative(124, 25)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_9", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_9")
        self.click_relative(126, 25)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_10", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_10")
        self.click_relative(126, 26)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_11", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_11")
        self.click_relative(126, 26)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_12", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_12")
        self.click_relative(90, 29)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_13", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_13")
        self.click_relative(93, 28)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_14", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_14")
        self.click_relative(127, 29)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        if not self.find( "cont_5_relacionamentos_cad", matching=0.97, waiting_time=10000):
            not_found("cont_5_relacionamentos_cad")
        self.click()
        if not self.find( "cont_botao_salvar_cad_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_salvar_cad_5")
        self.click()
        if not self.find( "cont_incluir_A_inscricoes_estaduais", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_A_inscricoes_estaduais")
        self.click()
        if not self.find( "cont_botao_buscar_estado_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_buscar_estado_5")
        self.click()
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.enter()
        if not self.find( "cont_x_Cancelar_5_A", matching=0.97, waiting_time=10000):
            not_found("cont_x_Cancelar_5_A")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_lixeira_A_inscricoes", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_A_inscricoes")
        self.click()
        self.enter()
        if not self.find( "cont_B_socios_cad", matching=0.97, waiting_time=10000):
            not_found("cont_B_socios_cad")
        self.click()
        if not self.find( "cont_incluir_A_inscricoes_estaduais", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_A_inscricoes_estaduais")
        self.click()

        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"12312312333")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            self.wait(100)
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"85050440")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"4291472548")
        self.tab()
        self.type_keys_with_interval(100,"teoremateste@gmail.com")
        self.tab()

        x = 0
        while x < 8:
            self.type_down()
            self.wait(100)
            x += 1

        self.tab()
        self.type_keys_with_interval(100,"12")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        

        x = 0
        while x < 25:
            self.type_down()
            self.wait(100)
            x += 1

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.wait(1000)
        if not self.find( "cont_b_funcao", matching=0.97, waiting_time=10000):
            not_found("cont_b_funcao")
        self.click_relative(331, 24)
        self.wait(1000)
        if not self.find( "cont_b_funcao_descricao", matching=0.97, waiting_time=10000):
            not_found("cont_b_funcao_descricao")
        self.click_relative(40, 25)
        self.wait(1000)
        if not self.find( "cont_b_banco", matching=0.97, waiting_time=10000):
            not_found("cont_b_banco")
        self.click_relative(326, 26)
        self.wait(1000)
        if not self.find( "cont_b_banco_descricao", matching=0.97, waiting_time=10000):
            not_found("cont_b_banco_descricao")
        self.click_relative(69, 20)
        self.wait(1000)
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_b_socio", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_b_socio")
        self.click()
        if not self.find( "cont_cancelar_b_socio_cad", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_b_socio_cad")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_lixeira_A_inscricoes", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_A_inscricoes")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_c_documentos_cad", matching=0.97, waiting_time=10000):
            not_found("cont_c_documentos_cad")
        self.click()
        if not self.find( "cont_incluir_A_inscricoes_estaduais", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_A_inscricoes_estaduais")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_livro_c_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_livro_c_documentos")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_arquivos_c_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_arquivos_c_documentos")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_salvar_b_socio", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_b_socio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cancelar_b_socio_cad", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_b_socio_cad")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        if not self.find( "cont_lixeira_A_inscricoes", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_A_inscricoes")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_d_pessoas_autorizadas", matching=0.97, waiting_time=10000):
            not_found("cont_d_pessoas_autorizadas")
        self.click()
        if not self.find( "cont_incluir_A_inscricoes_estaduais", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_A_inscricoes_estaduais")
        self.click()
        if not self.find( "cont_botao_buscar_estado_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_buscar_estado_5")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_contas_autorizadas", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_contas_autorizadas")
        self.click()
        if not self.find( "cont_salvar_b_socio", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_b_socio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cancelar_b_socio_cad", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_b_socio_cad")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_lixeira_A_inscricoes", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_A_inscricoes")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_gnre_botao_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_gnre_botao_cadastro")
        self.click()
        self.wait(1000)
        self.type_down()
        if not self.find( "cont_numero_de_serie_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_numero_de_serie_pasta")
        self.click_relative(437, 28)
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_pastados_schemas", matching=0.97, waiting_time=10000):
            not_found("cont_pastados_schemas")
        self.click_relative(440, 27)
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.tab()
        if not self.find( "contpasta_de_arquivos_gerados", matching=0.97, waiting_time=10000):
            not_found("contpasta_de_arquivos_gerados")
        self.click_relative(437, 27)
        self.wait(1000)
        self.key_esc()
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_up()
        self.type_up()
        self.wait(1000)
        if not self.find( "cont_botao_de_salvar_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_botao_de_salvar_cadastro")
        self.wait(1000)
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        if not self.find( "cont_loc_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_loc_empresa_criada")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_qa12_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_empresa")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_excluir_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_empresa_criada")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_loc_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_loc_empresa_criada")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_empresas_cad_1_men_", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_cad_1_men_")
        self.click()
        #erro aqui com botao
        if not self.find( "cont_grupo_empresas_fin_23", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_empresas_fin_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_loc_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_loc_empresa_criada")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cadastro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cadastro_empresa")
        self.click()
        self.wait(2000)
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_botao_de_salvar_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_botao_de_salvar_cadastro")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_loc_empresa_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_rel_loc_empresa_cadastro")
        self.click_relative(-90, 11)
        ######
        if not self.find( "cont_achar_qa_12_empresa_cad", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa_12_empresa_cad")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_cad_parametro_emp", matching=0.97, waiting_time=10000):
            not_found("cont_editar_cad_parametro_emp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_empresa_criada")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_loc_empresa_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_rel_loc_empresa_cadastro")
        self.click_relative(-90, 11)
        self.wait(1000)
        if not self.find( "cont_retornar_cadastro_empresa_", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadastro_empresa_")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        
        # PARAMETROS FISCAIS ESTA COM PROBLEMA, MOSTRANDO ERRO
        #voltaqui
        
        if not self.find( "cont_parametrosfin_23", matching=0.97, waiting_time=10000):
            not_found("cont_parametrosfin_23")
        self.click()
        if not self.find( "cont_param_empresa_f9_fin", matching=0.97, waiting_time=10000):
            not_found("cont_param_empresa_f9_fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_loc_empresa_criada", matching=0.97, waiting_time=10000):
            not_found("cont_loc_empresa_criada")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cadastro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cadastro_empresa")
        self.click()
        self.wait(4000)
       

        if not self.find( "cont_nao_importar_dados", matching=0.97, waiting_time=10000):
            not_found("cont_nao_importar_dados")
        self.click()
        if not self.find( "cont_buscar_lupa_parametro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_lupa_parametro_empresa")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cor_inicial_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_cor_inicial_parametros")
        self.click_relative(162, 25)
        self.wait(1000)
        self.click()
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 13:
            self.type_down()
            self.type_up()
            self.tab()
            x += 1 
        self.wait(1000)
        x = 0
        while x < 6:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.type_up()
            self.type_up()
            self.type_up()
            self.tab()
            x += 1
        self.type_up()
        self.tab()
        x = 0
        while x < 4:
            self.type_down()
            x += 1 
        x = 0
        while x < 4:
            self.type_up()
            x += 1
        self.tab()
        self.type_down()
        self.type_down()
        self.type_up()
        
        self.wait(3000)
        
        if not self.find( "cont_2_financeiros_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_2_financeiros_parametros")
        self.click()
        x= 0
        while x < 15:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.type_up()
            self.type_up()
            self.type_up()
            self.tab()
            x += 1
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        x = 0
        while x < 2:
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.tab()
            x += 1
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        
        self.wait(3000)
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_up()
        self.type_up()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_down()
        self.type_up()
        if not self.find( "cont_3_gestao_adm_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_3_gestao_adm_parametros")
        self.click()
        x = 0
        while x < 4:
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            self.type_up()
            self.tab()
            x += 1
        x = 0 
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        
        x = 0
        self.tab()
        while x < 7:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        x = 0
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 4:
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        x = 0
        while x < 8:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.type_down()
        self.tab()
        x = 0
        while x < 2:
            self.type_keys_with_interval(100,"25")
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"50")
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        x = 0
        if not self.find( "cont_4_vendas_parametro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_4_vendas_parametro_empresa")
        self.click()
        x = 0
        while x < 4:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        x = 0
        self.type_keys_with_interval(100,"1")
        self.tab()
        while x < 7:
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 26:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        x = 0
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_down()
        self.type_down()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_down()
        self.type_down()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        x = 0
        self.type_keys_with_interval(100,"1")
        self.tab()
        while x < 17:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        x = 0
        if not self.find( "cont_5_compras_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_5_compras_parametros")
        self.click()
        while x < 21:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        
        if not self.find( "cont_6_mensagens_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_6_mensagens_parametros")
        self.click()
        if not self.find( "cont_7_producao_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_7_producao_parametro")
        self.click()
        x = 0
        if not self.find( "cont_1_custo_comecar_7", matching=0.97, waiting_time=10000):
            not_found("cont_1_custo_comecar_7")
        self.click_relative(136, 29)
        self.wait(200)
        self.click()



        while x < 4:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
            
        if not self.find( "cont_gerar_p_usuarios_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_gerar_p_usuarios_buscar")
        self.click()
        if not self.find( "cont_localizar_1_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_parametros")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1")
        x = 0
        self.tab()
        while x < 4:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            self.type_down()
            self.type_up() 
            self.type_up()
            self.tab()
            x += 1
        self.space()
        self.type_up()
        self.space()
        self.type_down()
        self.space()
        self.type_down()
        self.space()
        self.type_down()
        self.space()
        self.type_down()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        x = 0
        while x < 21:
            self.type_keys_with_interval(100,"1")
            self.tab()  
            x += 1
        if not self.find( "cont_8_parametros_nota", matching=0.97, waiting_time=10000):
            not_found("cont_8_parametros_nota")
        self.click()
        self.wait(3000)

        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        # aqui esta dando erro, por enquanto deixar
        
        self.wait(8000)
        
        # aqui aperta para exibir lista de itens a incluir
        #
        self.wait(2000)
        if not self.find( "cont_rel_producao_transf_exibir_itens", matching=0.97, waiting_time=10000):
            not_found("cont_rel_producao_transf_exibir_itens")
        self.click_relative(657, 50)
        self.wait(2000)
        if not self.find( "cont_item_barras_clic", matching=0.97, waiting_time=10000):
            not_found("cont_item_barras_clic")
        self.click()
        self.wait(2000)
        if not self.find( "cont_campos_rel_flecha", matching=0.97, waiting_time=10000):
            not_found("cont_campos_rel_flecha")
        self.click_relative(-27, 20)
        self.wait(2000)
        self.enter()
        if not self.find( "cont_campo_rel_flecha_2", matching=0.97, waiting_time=10000):
            not_found("cont_campo_rel_flecha_2")
        self.click_relative(-28, 45)
        self.wait(2000)
        if not self.find( "cont_campo_rel_flecha_3", matching=0.97, waiting_time=10000):
            not_found("cont_campo_rel_flecha_3")
        self.click_relative(-27, 68)
        self.wait(2000)
        if not self.find( "cont_campo_rel_flecha_4", matching=0.97, waiting_time=10000):
            not_found("cont_campo_rel_flecha_4")
        self.click_relative(-29, 91)
        self.wait(2000)
        if not self.find( "cont_8_exibir_list", matching=0.97, waiting_time=10000):
            not_found("cont_8_exibir_list")
        self.click()
        self.wait(2000)
        if not self.find( "cont_espessura_clic", matching=0.97, waiting_time=10000):
            not_found("cont_espessura_clic")
        self.click()
        self.wait(2000)
        if not self.find( "cont_flecha_item_rel_5", matching=0.97, waiting_time=10000):
            not_found("cont_flecha_item_rel_5")
        self.click_relative(-29, 60)
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 3:
            self.type_down()
            self.type_up()
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_1_nota_fiscal_rel", matching=0.97, waiting_time=10000):
            not_found("cont_1_nota_fiscal_rel")
        self.click_relative(225, 25)
        if not self.find( "cont_nota_fiscal_fatura", matching=0.97, waiting_time=10000):
            not_found("cont_nota_fiscal_fatura")
        self.click()
        self.wait(2000)
        self.tab()
        if not self.find( "cont_add_5_numeracao_notas", matching=0.97, waiting_time=10000):
            not_found("cont_add_5_numeracao_notas")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.tab()
        if not self.find( "cont_finalizar_add_5", matching=0.97, waiting_time=10000):
            not_found("cont_finalizar_add_5")
        self.click()
        self.wait(2000)
        if not self.find( "cont_9_codigos_padroes", matching=0.97, waiting_time=10000):
            not_found("cont_9_codigos_padroes")
        self.click()
        self.wait(2000)
        if not self.find( "cont_1_relacionado_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_relacionado_busc")
        self.click_relative(95, 28)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_selecionar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_1_rel")
        self.click()
        if not self.find( "cont_2_cadastro_mod_busc", matching=0.97, waiting_time=10000):
            not_found("cont_2_cadastro_mod_busc")
        self.click_relative(101, 29)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_selecionar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_1_rel")
        self.click()
        if not self.find( "cont_3_local_estoque_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_local_estoque_busc")
        self.click_relative(88, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_1_transf_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_transf_busc")
        self.click_relative(82, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_2_inventario_busc", matching=0.97, waiting_time=10000):
            not_found("cont_2_inventario_busc")
        self.click_relative(80, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_3_producao_osm_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_producao_osm_busc")
        self.click_relative(88, 28)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_4_item_kit_busc", matching=0.97, waiting_time=10000):
            not_found("cont_4_item_kit_busc")
        self.click_relative(79, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_5_item_mestre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_5_item_mestre_busc")
        self.click_relative(84, 28)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_6_almoxarifado_busc", matching=0.97, waiting_time=10000):
            not_found("cont_6_almoxarifado_busc")
        self.click_relative(80, 24)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_7_desmembra_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_7_desmembra_itens_busc")
        self.click_relative(83, 25)
        
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_devoluca_iten_busc", matching=0.97, waiting_time=10000):
            not_found("cont_devoluca_iten_busc")
        self.click_relative(78, 25)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_3_operacao_saida_1", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_1")
        self.click_relative(83, 44)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_2", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_2")
        self.click_relative(484, 43)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_3")
        self.click_relative(883, 45)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_4", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_4")
        self.click_relative(80, 86)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacoes_saida_5", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacoes_saida_5")
        self.click_relative(486, 85)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_6", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_6")
        self.click_relative(882, 85)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacoes_saida_7", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacoes_saida_7")
        self.click_relative(82, 129)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacaoes_saida_8", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacaoes_saida_8")
        self.click_relative(485, 128)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_b_vendas_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_b_vendas_parametros")
        self.click()
        if not self.find( "cont_1_padroes_venda_1", matching=0.97, waiting_time=10000):
            not_found("cont_1_padroes_venda_1")
        self.click_relative(100, 46)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        ###
        if not self.find( "cont_selec_opc_2_23", matching=0.97, waiting_time=10000):
            not_found("cont_selec_opc_2_23")
        self.click()
        
        if not self.find( "cont_2_vendedor_padrao_2", matching=0.97, waiting_time=10000):
            not_found("cont_2_vendedor_padrao_2")
        self.click_relative(85, 22)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_condicao_pagamento_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_condicao_pagamento_3")
        self.click_relative(83, 29)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_padroes_operacoes_1", matching=0.97, waiting_time=10000):
            not_found("cont_2_padroes_operacoes_1")
        self.click_relative(84, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_operacao_saida_padrao_2", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_saida_padrao_2")
        self.click_relative(82, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_nfe_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_nfe_3")
        self.click_relative(88, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_4_operacao_nfe_4", matching=0.97, waiting_time=10000):
            not_found("cont_4_operacao_nfe_4")
        self.click_relative(84, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        #  este botao esta com erro

         #if not self.find( "cont_5_operacao_saida_padrao", matching=0.97, waiting_time=10000):
         #    not_found("cont_5_operacao_saida_padrao")
         #self.click_relative(82, 26)
        self.wait(2000)
         #if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
         #    not_found("cont_localizar_1_rel")
         #self.click()
        self.wait(2000)
         #if not self.find( "cont_selec_opc_23_final", matching=0.97, waiting_time=10000):
         #    not_found("cont_selec_opc_23_final")
         #self.click()
        self.wait(2000)
        if not self.find( "cont_1_condi_pagamento_ad", matching=0.97, waiting_time=10000):
            not_found("cont_1_condi_pagamento_ad")
        self.click_relative(80, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_vendedor_clientes_disp", matching=0.97, waiting_time=10000):
            not_found("cont_2_vendedor_clientes_disp")
        self.click_relative(82, 29)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_plano_preco_min", matching=0.97, waiting_time=10000):
            not_found("cont_3_plano_preco_min")
        self.click_relative(78, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_4_plano_preco_max", matching=0.97, waiting_time=10000):
            not_found("cont_4_plano_preco_max")
        self.click_relative(80, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_1_cliente_4", matching=0.97, waiting_time=10000):
            not_found("cont_1_cliente_4")
        self.click_relative(82, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)

        ###
        ###
        if not self.find( "cont_selecionar_1_cliente", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_1_cliente")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_2_operacao_saida", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_saida")
        self.click_relative(84, 32)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_cfop_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_cfop_busc")
        self.click_relative(83, 28)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_4_cfop_sub", matching=0.97, waiting_time=10000):
            not_found("cont_4_cfop_sub")
        self.click_relative(79, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_5_cfop_iss", matching=0.97, waiting_time=10000):
            not_found("cont_5_cfop_iss")
        self.click_relative(83, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_6_operacao_saida_iss", matching=0.97, waiting_time=10000):
            not_found("cont_6_operacao_saida_iss")
        self.click_relative(82, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(2000)
        if not self.find( "cont_c_financeiro_param", matching=0.97, waiting_time=10000):
            not_found("cont_c_financeiro_param")
        self.click()
        if not self.find( "cont_1_classific_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_classific_busc")
        self.click_relative(82, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_moedapadrao", matching=0.97, waiting_time=10000):
            not_found("cont_2_moedapadrao")
        self.click_relative(83, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_tipo_pagamento_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_tipo_pagamento_busc")
        self.click_relative(82, 22)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_4_tipo_pagamento_troc", matching=0.97, waiting_time=10000):
            not_found("cont_4_tipo_pagamento_troc")
        self.click_relative(78, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_5_tipo_pag_entra", matching=0.97, waiting_time=10000):
            not_found("cont_5_tipo_pag_entra")
        self.click_relative(81, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_6_tipo_pag_saida", matching=0.97, waiting_time=10000):
            not_found("cont_6_tipo_pag_saida")
        self.click_relative(80, 28)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_7_tipo_pag_baixa", matching=0.97, waiting_time=10000):
            not_found("cont_7_tipo_pag_baixa")
        self.click_relative(81, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_1_conta_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_conta_busc")
        self.click_relative(84, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_tipo_pag_bus", matching=0.97, waiting_time=10000):
            not_found("cont_2_tipo_pag_bus")
        self.click_relative(80, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_busc")
        self.click_relative(83, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_E_descricao_macros", matching=0.97, waiting_time=10000):
            not_found("cont_E_descricao_macros")
        self.click()
        x = 0 
        while x <16:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_10_commerce", matching=0.97, waiting_time=10000):
            not_found("cont_10_commerce")
        self.click()
        self.wait(1000)
        self.type_up()
        if not self.find( "cont_1_vend_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_1_vend_padrao")
        self.click_relative(80, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_2_operacao_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_padrao")
        self.click_relative(80, 30)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_3_cond_de_pag", matching=0.97, waiting_time=10000):
            not_found("cont_3_cond_de_pag")
        self.click_relative(80, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_4_plano_preco", matching=0.97, waiting_time=10000):
            not_found("cont_4_plano_preco")
        self.click_relative(81, 23)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        
        # AQUI AACABA O PARAMETROS COM ERRO
        if not self.find( "cont_parametrosfin_23", matching=0.97, waiting_time=10000):
            not_found("cont_parametrosfin_23")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_parametros_transpo_23_f", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_transpo_23_f")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_nao_param", matching=0.97, waiting_time=10000):
            not_found("cont_botao_nao_param")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_busc_param_lup", matching=0.97, waiting_time=10000):
            not_found("cont_botao_busc_param_lup")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.tab()
        x = 0 
        while x < 20:
            self.type_down()
            self.type_up()
            self.tab()
            x += 1
        self.wait(3000)
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()
        self.wait(1000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_regionalizacao_23_fin_2", matching=0.97, waiting_time=10000):
            not_found("cont_regionalizacao_23_fin_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_paises_regionali_23", matching=0.97, waiting_time=10000):
            not_found("cont_paises_regionali_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_paises", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_paises")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(3000)
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(3000)
        #####
        #####
        self.click()
        
        if not self.find( "cont_cadastros_fin_23_menu", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_fin_23_menu")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_regionalizacao_23_fin_2", matching=0.97, waiting_time=10000):
            not_found("cont_regionalizacao_23_fin_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_regioes_regionali_23", matching=0.97, waiting_time=10000):
            not_found("cont_regioes_regionali_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        ####
        ####
        if not self.find( "cont_busc_pais_parame", matching=0.97, waiting_time=10000):
            not_found("cont_busc_pais_parame")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        if not self.find( "cont_selecionar_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_pais_param")
        self.click()
        
        if not self.find( "cont_param_regiao_1_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_param_regiao_1_entrada")
        self.click_relative(-8, 8)
        if not self.find( "cont_5_saida_param_regioes", matching=0.97, waiting_time=10000):
            not_found("cont_5_saida_param_regioes")
        self.click_relative(-10, 7)
        self.wait(3000)
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(3000)
        self.click()
        
        ##################################################
        ##### CADASTRO -> REGIONALIZACAO -> ESTADOS ######
        ##################################################

        self.wait(3000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_regionalizacao_23_fin_2", matching=0.97, waiting_time=10000):
            not_found("cont_regionalizacao_23_fin_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_estados_regionali_23", matching=0.97, waiting_time=10000):
            not_found("cont_estados_regionali_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        self.tab()
        self.type_down()
        ####
        ####
        if not self.find( "cont_estados_busc_bot", matching=0.97, waiting_time=10000):
            not_found("cont_estados_busc_bot")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.tab()
        self.tab()
        self.type_down()
        self.wait(3000)
        #mouse esta parando em cima de salvar
        #if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(3000)
        self.click()
        
        ###########################################################################
        ##### CADASTROS -> PARAMETROS FISCAIS -> REGIONALIZACAO -> MUNICIPIOS #####
        ###########################################################################
        self.wait(2000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_regionalizacao_23_fin_2", matching=0.97, waiting_time=10000):
            not_found("cont_regionalizacao_23_fin_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_municipios_regionali_23", matching=0.97, waiting_time=10000):
            not_found("cont_municipios_regionali_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        
        ####
        ####
        if not self.find( "cont_estados_busc_bot", matching=0.97, waiting_time=10000):
            not_found("cont_estados_busc_bot")
        self.click()
        self.wait(2000)
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        x = 0
        while x< 7:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1 
        self.wait(2000)
        self.click()
        self.wait(2000)
        #mouse ja esta em cima de salvar
        #if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_botaoo")
        self.click()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_grupo_fiscal_produtos_23_f", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_produtos_23_f")
        self.click()
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localiz_opc_23_1", matching=0.97, waiting_time=10000):
            not_found("cont_localiz_opc_23_1")
        self.click()
        self.wait(2000)
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()
        
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigos_fiscais_cfop_1_23_f", matching=0.97, waiting_time=10000):
            not_found("cont_codigos_fiscais_cfop_1_23_f")
        self.click()
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"1233")
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_botao_busc_cinz", matching=0.97, waiting_time=10000):
            not_found("cont_botao_busc_cinz")
        self.click()
        self.wait(2000)
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        ###
        ###
        if not self.find( "cont_selecionar_item_22", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_item_22")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1233")
        self.tab()
        self.type_keys_with_interval(100,"1233")
        self.tab()
        x = 0
        while x < 5:
            self.space()
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"1233")
        x = 0
        while x < 3:
            self.space()
            self.tab()
            x += 1
        self.tab()
        self.wait(2000)
        self.type_right()
        
        self.tab()
        self.type_right()
        self.type_right()
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigos_fisca_cfop_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_codigos_fisca_cfop_imp_23")
        self.click()
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cfop_origem_busc", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_origem_busc")
        self.click_relative(133, 2)
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        ###
        ###
        if not self.find( "cont_selecionar_item_22", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_item_22")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cfop_destino_busc", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_destino_busc")
        self.click_relative(131, 1)
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        ###
        ###
        if not self.find( "cont_selecionar_item_22", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_item_22")
        self.click()
        self.wait(2000)
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"1.101")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_1101", matching=0.97, waiting_time=10000):
            not_found("cont_achar_1101")
        self.click()
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigos_de_operacao_fin_23", matching=0.97, waiting_time=10000):
            not_found("cont_codigos_de_operacao_fin_23")
        self.click()
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_locali_param_emp", matching=0.97, waiting_time=10000):
            not_found("cont_locali_param_emp")
        self.click()
        ###
        ###
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        x = 0
        while x < 4:
            self.tab()
            x += 1
        x = 0
        while x < 12:
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        x = 0
        while x < 21:
            self.type_down()
            self.type_down()
            self.type_down()
            self.tab()
            x += 1
        self.tab()
        self.space()
        self.tab()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 21:
            self.space()
            self.space()
            self.tab()
            x += 1
        if not self.find( "cont_dados_adicionais_cod", matching=0.97, waiting_time=10000):
            not_found("cont_dados_adicionais_cod")
        self.click()
        if not self.find( "cont_cfop_padrao_de_movimento", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_padrao_de_movimento")
        self.click_relative(68, 25)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_busc")
        self.click_relative(69, 26)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()

        if not self.find( "cont_tabela_precos_servicos_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_servicos_busc")
        self.click_relative(60, 26)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_movimentacao_para_trans_rel", matching=0.97, waiting_time=10000):
            not_found("cont_movimentacao_para_trans_rel")
        self.click_relative(186, 27)
        self.wait(1000)
        self.click()
        if not self.find( "cont_campos_inserir_clien", matching=0.97, waiting_time=10000):
            not_found("cont_campos_inserir_clien")
        self.click_relative(45, 11)
        self.wait(1000)
        if not self.find( "cont_campos_de_clientes_e", matching=0.97, waiting_time=10000):
            not_found("cont_campos_de_clientes_e")
        self.click()
        self.wait(1000)
        if not self.find( "cont_empresa_codigo_achar", matching=0.97, waiting_time=10000):
            not_found("cont_empresa_codigo_achar")
        self.click()
        self.wait(1000)
        if not self.find( "cont_inserir_campo_disponivel_emp", matching=0.97, waiting_time=10000):
            not_found("cont_inserir_campo_disponivel_emp")
        self.click()
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_decretos_e_observacoes_fin_23", matching=0.97, waiting_time=10000):
            not_found("cont_decretos_e_observacoes_fin_23")
        self.click()
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
            not_found("cont_editar_qa_12_pais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_pais_param")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        if not self.find( "cont_cadastros_opc_sem_lin_23", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_opc_sem_lin_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_parametros_fiscais_fin_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_fiscais_fin_23_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_situacoes_fin_par_23", matching=0.97, waiting_time=10000):
            not_found("cont_situacoes_fin_par_23")
        self.click()
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        if not self.find( "cont_operacao_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_selec_busc")
        self.click_relative(53, 28)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        self.wait(2000)
        #
        #
        #
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_regiao_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_regiao_selec_busc")
        self.click_relative(48, 28)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_grupo_fiscal_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_selec_busc")
        self.click_relative(51, 26)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        #
        x = 0
        while x < 4:
            self.tab()
            x += 1 
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 3:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 2:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 3:
            self.type_down()
            x += 1
        self.tab()
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"0")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.space()
            self.space()
            self.tab()
            x += 1
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        if not self.find( "cont_pis_cofins_iss_", matching=0.97, waiting_time=10000):
            not_found("cont_pis_cofins_iss_")
        self.click()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 8:
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        if not self.find( "cont_decretos_e_obs_bt", matching=0.97, waiting_time=10000):
            not_found("cont_decretos_e_obs_bt")
        self.click()
        self.wait(2000)
        if not self.find( "cont_decreto_1_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_decreto_1_busc_")
        self.click_relative(44, 27)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_decreto_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_decreto_2_busc_")
        self.click_relative(46, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_obs_1_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_1_busc_")
        self.click_relative(43, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_obs_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_2_busc_")
        self.click_relative(43, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cfop_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_busc_")
        self.click_relative(60, 25)
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        
        
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'qa12!')
        if not self.find( "cont_gnre_buscar_cad", matching=0.97, waiting_time=10000):
            not_found("cont_gnre_buscar_cad")
        self.click()
        if not self.find( "cont_add_botao_gnre_v", matching=0.97, waiting_time=10000):
            not_found("cont_add_botao_gnre_v")
        self.click()
        if not self.find( "cont_cancelar_receita_1", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_receita_1")
        self.click()
        if not self.find( "cont_dare_sp_busc", matching=0.97, waiting_time=10000):
            not_found("cont_dare_sp_busc")
        self.click()
        if not self.find( "cont_add_botao_gnre_v", matching=0.97, waiting_time=10000):
            not_found("cont_add_botao_gnre_v")
        self.click()
        self.wait(2000)
        self.enter()
        #CANCELAR NO LUGAR DE SALVAR
        if not self.find( "cont_cancelar_bot_itens_23", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_bot_itens_23")
        self.click()
        self.wait(2000)
        self.enter()
        #if not self.find( "cont_salvar_regiao_cad_3", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_regiao_cad_3")
        #self.click()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        #if not self.find( "cont_achar_123_situacoes", matching=0.97, waiting_time=10000):
        #    not_found("cont_achar_123_situacoes")
        #self.click()
        
        self.wait(2000)
        #if not self.find( "cont_editar_qa_12_pais", matching=0.97, waiting_time=10000):
        #    not_found("cont_editar_qa_12_pais")
        #self.click()
        #self.wait(2000)
        #if not self.find( "cont_excluir_pais_param", matching=0.97, waiting_time=10000):
        #    not_found("cont_excluir_pais_param")
        #self.click()
        #self.wait(2000)
        #self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        
        ####################################################################
        ######### CADASTRO DE CLIENTE, FORNECEDOR E TRANSPORTADOR ##########
        ####################################################################
        
        
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_1fin", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_1fin")
        self.click()
        self.wait(1000)
        
        self.wait(2000)
        if not self.find( "cont_menu_clientes_fornece", matching=0.97, waiting_time=10000):
            not_found("cont_menu_clientes_fornece")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_param_empr", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_param_empr")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"85050440")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_acha_num_munic", matching=0.97, waiting_time=10000):
            not_found("cont_acha_num_munic")
        self.click_relative(-57, 67)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1 
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1 
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1 
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 3:
            self.type_down()
            x+= 1
        self.tab()
        x = 0
        while x < 2:
            self.type_down()
            x+= 1
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x+= 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@") # COMPLEMENTO
        self.tab()
        self.type_keys_with_interval(100,"85050440") # CEP
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        #MUNICIPIO
        self.wait(2000)
        if not self.find( "cont_endereco_cob_alter_mun_rel", matching=0.97, waiting_time=10000):
            not_found("cont_endereco_cob_alter_mun_rel")
        self.click_relative(55, 87)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com") #Email
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com") 
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com") 
        self.tab()
        self.type_keys_with_interval(100,"www.google.com") 
        self.tab()
        self.type_keys_with_interval(100,"qa12!@") 
        self.tab()
        self.type_keys_with_interval(100,"123123123") 
        self.tab()
        x = 0
        while x < 17:
            self.space()
            self.space()
            self.tab()
            x += 1 
        
        if not self.find( "cont_botao_salva_23_fin_3", matching=0.97, waiting_time=10000):
            not_found("cont_botao_salva_23_fin_3")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)

        self.wait(3000)
        if not self.find( "cont_2_agrupamento_clientes", matching=0.97, waiting_time=10000):
            not_found("cont_2_agrupamento_clientes")
        self.click()
        
        self.wait(3000)
        if not self.find( "cont_local_de_cobranca_11", matching=0.97, waiting_time=10000):
            not_found("cont_local_de_cobranca_11")
        self.click_relative(68, 26)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        
        self.wait(2000)
        if not self.find( "cont_ramo_de_atividade_12", matching=0.97, waiting_time=10000):
            not_found("cont_ramo_de_atividade_12")
        self.click_relative(68, 29)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_comissao_13", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_13")
        self.click_relative(70, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_vendedor_compr_14", matching=0.97, waiting_time=10000):
            not_found("cont_vendedor_compr_14")
        self.click_relative(65, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_plano_financeiro_15", matching=0.97, waiting_time=10000):
            not_found("cont_plano_financeiro_15")
        self.click_relative(84, 26)
        self.wait(2000)
        self.type_keys_with_interval(100,"0010010")
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        
        self.wait(2000)
        self.enter()
        self.wait

        if not self.find( "cont_centro_de_custo_16", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custo_16")
        self.click_relative(84, 27)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.enter()
        
        self.wait(2000)
        if not self.find( "cont_classificacao_17", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_17")
        self.click_relative(67, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_conta_corrente_18", matching=0.97, waiting_time=10000):
            not_found("cont_conta_corrente_18")
        self.click_relative(70, 29)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cod_con_cliente_19", matching=0.97, waiting_time=10000):
            not_found("cont_cod_con_cliente_19")
        self.click_relative(64, 25)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_fornecedor_fix", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_fornecedor_fix")
        self.click_relative(69, 26)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_segmento_busc_rel_21", matching=0.97, waiting_time=10000):
            not_found("cont_segmento_busc_rel_21")
        self.click_relative(67, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_linha_rel_busc_22", matching=0.97, waiting_time=10000):
            not_found("cont_linha_rel_busc_22")
        self.click_relative(71, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_bsc_23", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_bsc_23")
        self.click_relative(67, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)

        if not self.find( "cont_tabela_de_preco_servico_24", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_preco_servico_24")
        self.click_relative(71, 26)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_operacao_pdv_busc_25", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_pdv_busc_25")
        self.click_relative(69, 29)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_transportador_busc_26", matching=0.97, waiting_time=10000):
            not_found("cont_transportador_busc_26")
        self.click_relative(83, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_condicao_pag_2_27", matching=0.97, waiting_time=10000):
            not_found("cont_condicao_pag_2_27")
        self.click_relative(71, 27)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_operacao_nfs_e_ordem_28", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_nfs_e_ordem_28")
        self.click_relative(72, 32)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)

        # CADASTROS CLIENTES -> INCLUIR -> 2 AGRUPAMENTO -> CONTABILIZAÇÃO MACROS
        #
        #
        
        self.wait(3000)
        if not self.find( "cont_contabilizacao_macros", matching=0.97, waiting_time=10000):
            not_found("cont_contabilizacao_macros")
        self.click()
        if not self.find( "cont_codigo_contabil_clientes_23_re", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_clientes_23_re")
        self.click_relative(62, 24)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_fornecedor", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_fornecedor")
        self.click_relative(66, 22)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(3000)
        if not self.find( "cont_botao_salva_23_fin_3", matching=0.97, waiting_time=10000):
            not_found("cont_botao_salva_23_fin_3")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_2_agrupamento_clientes", matching=0.97, waiting_time=10000):
            not_found("cont_2_agrupamento_clientes")
        self.click()
        self.wait(2000)

        if not self.find( "cont_codigo_contabeis_multi_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabeis_multi_empresa")
        self.click()

        if not self.find( "cont_codigo_contabil_client_22", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_client_22")
        self.click_relative(63, 29)
        self.wait(4000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_forne_23")
        self.click_relative(65, 27)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_confirmar_opc_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_confirmar_opc_5")
        self.click()
        
        # CADASTROS -> INCLUIR -> 3_PESSOA_FISICA
        self.wait(3000)
        if not self.find( "cont_3_pessoa_fisica_btn", matching=0.97, waiting_time=10000):
            not_found("cont_3_pessoa_fisica_btn")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        
        # 4 ROTAS DADOS ADICIONAIS
        #
        #
        self.wait(3000)
        if not self.find( "cont_4_rotas_dados_adicionais", matching=0.97, waiting_time=10000):
            not_found("cont_4_rotas_dados_adicionais")
        self.click()
        if not self.find( "cont_rota_de_entrega_23", matching=0.97, waiting_time=10000):
            not_found("cont_rota_de_entrega_23")
        self.click_relative(62, 22)
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 7:
            self.space()
            self.space()
            self.space()
            self.tab()
            x += 1
        x = 0
        while x < 7:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"12312312333")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        x = 0
        while x < 12:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        
        # CADASTROS -> 5 OBS REF LIMITE CREDITO
        #
        #
        self.wait(3000)
        if not self.find( "cont_5_obs_ref_limite_cred", matching=0.97, waiting_time=10000):
            not_found("cont_5_obs_ref_limite_cred")
        self.click()
        self.wait(2000)
        if not self.find( "cont_situacao_limite_credito_2", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_limite_credito_2")
        self.click_relative(13, 42)
        self.wait(1000)

        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 5:
            self.space()
            self.space()
            self.tab()
            x += 1
        x = 0
        while x < 3:
            self.type_down()
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_botao_5_observacoes", matching=0.97, waiting_time=10000):
            not_found("cont_botao_5_observacoes")
        self.click()
        if not self.find( "cont_observacoes_relativo_des", matching=0.97, waiting_time=10000):
            not_found("cont_observacoes_relativo_des")
        self.click_relative(10, 31)
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_btn_referencias_5", matching=0.97, waiting_time=10000):
            not_found("cont_btn_referencias_5")
        self.click()
        self.wait(1000)
        if not self.find( "cont_referencias_pessoais_23", matching=0.97, waiting_time=10000):
            not_found("cont_referencias_pessoais_23")
        self.click_relative(44, 30)

        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_5_bens_contatos_avalistas", matching=0.97, waiting_time=10000):
            not_found("cont_5_bens_contatos_avalistas")
        self.click()
        if not self.find( "cont_bens_rel_descr", matching=0.97, waiting_time=10000):
            not_found("cont_bens_rel_descr")
        self.click_relative(11, 25)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_6_relacionamentos_5_obs", matching=0.97, waiting_time=10000):
            not_found("cont_6_relacionamentos_5_obs")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        # 6RELACIONAMENTOS -> REPRESENTANTES
        #
        #
        self.wait(3000)
        if not self.find( "cont_representantes_6relacionamento", matching=0.97, waiting_time=10000):
            not_found("cont_representantes_6relacionamento")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        if not self.find( "cont_busc_municipio_represent", matching=0.97, waiting_time=10000):
            not_found("cont_busc_municipio_represent")
        self.click()
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"85050440")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123123")# fax
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com")# email
        self.tab()
        self.type_keys_with_interval(100,"www.google.com")
        self.tab()
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_local_entrega_6_repre", matching=0.97, waiting_time=10000):
            not_found("cont_local_entrega_6_repre")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        self.tab()
        self.wait(1000)
        self.enter()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"11517192935") #cpf 
        self.tab()
        self.type_keys_with_interval(100,"123123123") 
        self.tab()
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        
        # BUSCAR MUNICIPIO EM LOCAL DE ENTREGA
        #
        self.wait(3000)
        if not self.find( "cont_buscar_mun_6_rep_2", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_mun_6_rep_2")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"85050440")
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@") #complemento
        self.tab()
        self.type_keys_with_interval(100,"qa12!@") #bairro
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        #6 relacionamento -> Pessoas(contato)
        self.wait(3000) 
        if not self.find( "cont_pessoas_contatos_6", matching=0.97, waiting_time=10000):
            not_found("cont_pessoas_contatos_6")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"11517192935")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"85050440") #CEP
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        
        #BUSCAR MUNICIPIO EM PESSOAS(CONTATO)
        self.wait(3000)
        if not self.find( "cont_buscar_mun_6_rep_2", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_mun_6_rep_2")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123") #hobby
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        self.type_keys_with_interval(100,"123123")
        self.tab()
        self.type_keys_with_interval(100,"qa12@teorema.com") #email
        if not self.find( "cont_receber_email_de_opc", matching=0.97, waiting_time=10000):
            not_found("cont_receber_email_de_opc")
        self.click()
        self.type_down()
        x = 0
        while x <9:
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.wait(1000)
        self.enter()
        self.type_keys_with_interval(100,"qa12!@") #observacoes
        self.tab()
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        # 6_REPRESENTANTE -> AVALIAÇOES 
        self.wait(3000)
        
        if not self.find( "cont_avaliacoes_6_repre", matching=0.97, waiting_time=10000):
            not_found("cont_avaliacoes_6_repre")
        self.click()
        
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        
        self.wait(3000)
        if not self.find( "cont_botao_busc_avaliacao_6", matching=0.97, waiting_time=10000):
            not_found("cont_botao_busc_avaliacao_6")
        self.click()
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        ### NAO EXISTE AVALIAÇÃO DISPONIVEL PARA SELECIONAR NESTA BASE, APENAS CANCELAR
        ##
        ##
        if not self.find( "cont_cancelar_avaliacoes_btn", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_avaliacoes_btn")
        self.click()
        if not self.find( "cont_vendedores_auxiliares_6", matching=0.97, waiting_time=10000):
            not_found("cont_vendedores_auxiliares_6")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_codigo_rel_consulta_vend", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_rel_consulta_vend")
        self.click_relative(-28, 24)
        
        
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        self.wait(3000)
        ### 6 RELACIONAMENTOS -> DOCUMENTOS 
        if not self.find( "cont_6rela_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_6rela_documentos")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_arquivo_rel_botao_doc", matching=0.97, waiting_time=10000):
            not_found("cont_arquivo_rel_botao_doc")
        self.click_relative(16, 33)
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        if not self.find( "cont_btn_confirmar_doc_avali", matching=0.97, waiting_time=10000):
            not_found("cont_btn_confirmar_doc_avali")
        self.click()
        if not self.find( "cont_retornar_rel_documentos_6", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_rel_documentos_6")
        self.click_relative(26, -48)
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        # 6 RELACIONAMENTOS -> CONTRATOS
        #
        #

        self.wait(3000)
        if not self.find( "cont_contratos_6_relacionamentos", matching=0.97, waiting_time=10000):
            not_found("cont_contratos_6_relacionamentos")
        self.click()
        self.wait(2000)
        #self.enter() ATIVAR ISSO QUANDO FOR CORRER O BOT PRIMEIRA VEZ, POIS PERGUNTA SE QR INCLUIR CONTRATO
        self.wait(1000)
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        if not self.find( "cont_tipo_contrato_6rel_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_contrato_6rel_bsc")
        self.click_relative(61, 23)
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_comissao_contratos_bsc_rel", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_contratos_bsc_rel")
        self.click_relative(58, 26)
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        #6 RELACIONAMENTO => CLIENTES VINCULADOS
        
        self.wait(3000)
        if not self.find( "cont_clientes_vinculados_6relac", matching=0.97, waiting_time=10000):
            not_found("cont_clientes_vinculados_6relac")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_buscar_mun_6_rep_2", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_mun_6_rep_2")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        #CATEGORIA CAMPANHA ESTA COM PROBLEMA AO INCLUIR NA MINHA MAQUINA
        #if not self.find( "cont_categoria_campanha_6_rel", matching=0.97, waiting_time=10000):
        #    not_found("cont_categoria_campanha_6_rel")
        #self.click()
        #if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_incluir_spc")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_rateio_centro_custo_6_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rateio_centro_custo_6_rel")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_bsc_centro_custo_btn_rel", matching=0.97, waiting_time=10000):
            not_found("cont_bsc_centro_custo_btn_rel")
        self.click_relative(173, 9)
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.enter()


        #BOTAO DE RATEINO ESTA COM ERRO DE FECHAR AUTOMATICAMENTE AO SELECIONAR
        #if not self.find( "cont_rel_do_rateio_busc", matching=0.97, waiting_time=10000):
        #    not_found("cont_rel_do_rateio_busc")
        #self.click_relative(-23, 6)

        # CANCELAR INCLUSAO POIS NAO POSSUI OS ITENS NECESSARIOS NA BASE

        if not self.find( "cont_cancelar_avaliacoes_btn", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_avaliacoes_btn")
        self.click()
        
        # 6 RELACIONAMENTO -> EQUIPAMENTOS
        #
        #
        self.wait(3000)
        if not self.find( "cont_equipamento_6relacio", matching=0.97, waiting_time=10000):
            not_found("cont_equipamento_6relacio")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"2000") # ano
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        # 6 RELACIONAMENTOS -> REDES SOCIAIS
        #
        #
        if not self.find( "cont_redes_sociais_6_relac", matching=0.97, waiting_time=10000):
            not_found("cont_redes_sociais_6_relac")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"www.google.com")
        self.tab()
        self.wait(1000)
        self.type_down()
        self.type_down()
        self.wait(1000)
        self.enter()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        
        # 6 RELACIONAMENTO -> 0 HISTORICO 
        #
        #
        self.wait(3000)
        if not self.find( "cont_clientes_cad_0_historico", matching=0.97, waiting_time=10000):
            not_found("cont_clientes_cad_0_historico")
        self.click()
        self.wait(2000)
        if not self.find( "cont_periodo_de_movimento_rel_5", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_de_movimento_rel_5")
        self.click_relative(220, 27)
        if not self.find( "cont_data_carregar_ano_historic", matching=0.97, waiting_time=10000):
            not_found("cont_data_carregar_ano_historic")
        self.click()
        if not self.find( "cont_atual_data_historico", matching=0.97, waiting_time=10000):
            not_found("cont_atual_data_historico")
        self.click()
        if not self.find( "cont_consultar_movto_financeiro_1", matching=0.97, waiting_time=10000):
            not_found("cont_consultar_movto_financeiro_1")
        self.click()
        if not self.find( "cont_ref_comerciais_31", matching=0.97, waiting_time=10000):
            not_found("cont_ref_comerciais_31")
        self.click()
        if not self.find( "cont_ref_bancarias_32", matching=0.97, waiting_time=10000):
            not_found("cont_ref_bancarias_32")
        self.click()
        if not self.find( "cont_ref_pessoais_33", matching=0.97, waiting_time=10000):
            not_found("cont_ref_pessoais_33")
        self.click()
        if not self.find( "cont_obs_das_referencias_34", matching=0.97, waiting_time=10000):
            not_found("cont_obs_das_referencias_34")
        self.click()
        if not self.find( "cont_spc_35", matching=0.97, waiting_time=10000):
            not_found("cont_spc_35")
        self.click()
        if not self.find( "cont_remessa_serasa_36", matching=0.97, waiting_time=10000):
            not_found("cont_remessa_serasa_36")
        self.click()
        if not self.find( "cont_contatos_37", matching=0.97, waiting_time=10000):
            not_found("cont_contatos_37")
        self.click()
        if not self.find( "cont_clientes_vinculados_38", matching=0.97, waiting_time=10000):
            not_found("cont_clientes_vinculados_38")
        self.click()
        if not self.find( "cont_tipos_de_contratos_39", matching=0.97, waiting_time=10000):
            not_found("cont_tipos_de_contratos_39")
        self.click()
        if not self.find( "cont_b_agrupamento_0hist", matching=0.97, waiting_time=10000):
            not_found("cont_b_agrupamento_0hist")
        self.click()
        if not self.find( "cont_2_movto_financeiro_0hist", matching=0.97, waiting_time=10000):
            not_found("cont_2_movto_financeiro_0hist")
        self.click()
        if not self.find( "cont_mostrar_adiamentos_0hist", matching=0.97, waiting_time=10000):
            not_found("cont_mostrar_adiamentos_0hist")
        self.click()
        if not self.find( "cont_mostrar_ocorrencias_0hist", matching=0.97, waiting_time=10000):
            not_found("cont_mostrar_ocorrencias_0hist")
        self.click()
        if not self.find( "cont_informado_btn_0_hist", matching=0.97, waiting_time=10000):
            not_found("cont_informado_btn_0_hist")
        self.click()
        self.wait(2000)
        self.key_esc()
        if not self.find( "cont_abertas_0_histor", matching=0.97, waiting_time=10000):
            not_found("cont_abertas_0_histor")
        self.click()
        if not self.find( "cont_baixadas_0_histori", matching=0.97, waiting_time=10000):
            not_found("cont_baixadas_0_histori")
        self.click()
        if not self.find( "cont_todas_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_todas_hist_0")
        self.click()
        if not self.find( "cont_efetivos_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_efetivos_hist_0")
        self.click()
        if not self.find( "cont_nao_efetivo_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_nao_efetivo_hist_0")
        self.click()
        if not self.find( "cont_invoice_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_invoice_hist_0")
        self.click()
        if not self.find( "cont_todas_hist_0_situac", matching=0.97, waiting_time=10000):
            not_found("cont_todas_hist_0_situac")
        self.click()
        if not self.find( "cont_b_cheques_2_mov_hist", matching=0.97, waiting_time=10000):
            not_found("cont_b_cheques_2_mov_hist")
        self.click()
        if not self.find( "cont_c_conta_corrente_hist", matching=0.97, waiting_time=10000):
            not_found("cont_c_conta_corrente_hist")
        self.click()
        self.wait(1000)
        if not self.find( "cont_conta_rel_busc_corrente", matching=0.97, waiting_time=10000):
            not_found("cont_conta_rel_busc_corrente")
        self.click_relative(67, 22)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        if not self.find( "cont_consultar_0_hist_conta", matching=0.97, waiting_time=10000):
            not_found("cont_consultar_0_hist_conta")
        self.click()
        if not self.find( "cont_d_estatistica_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_d_estatistica_hist_0")
        self.click()
        if not self.find( "cont_contas_a_receber_checkbox", matching=0.97, waiting_time=10000):
            not_found("cont_contas_a_receber_checkbox")
        self.double_click()
        if not self.find( "cont_contas_a_pagar_checkbox", matching=0.97, waiting_time=10000):
            not_found("cont_contas_a_pagar_checkbox")
        self.double_click()
        if not self.find( "cont_3_movmto_es_dev_hist", matching=0.97, waiting_time=10000):
            not_found("cont_3_movmto_es_dev_hist")
        self.click()
        if not self.find( "cont_exibir_itens_servicos_hist", matching=0.97, waiting_time=10000):
            not_found("cont_exibir_itens_servicos_hist")
        self.click_relative(5, 21)
        if not self.find( "cont_exibir_itens_e_serv_hist", matching=0.97, waiting_time=10000):
            not_found("cont_exibir_itens_e_serv_hist")
        self.click_relative(71, 22)
        if not self.find( "cont_tipo_movimentacao_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_movimentacao_hist0")
        self.click_relative(6, 22)
        if not self.find( "cont_tipo_de_mov_entradas_hist", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_de_mov_entradas_hist")
        self.click_relative(225, 22)
        if not self.find( "cont_tipo_movimen_saida_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_movimen_saida_hist0")
        self.click_relative(449, 22)
        if not self.find( "cont_tipo_da_movim_dev_hist", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_da_movim_dev_hist")
        self.click_relative(667, 21)
        if not self.find( "cont_visualiza_somente_mov_nao_hist", matching=0.97, waiting_time=10000):
            not_found("cont_visualiza_somente_mov_nao_hist")
        self.click_relative(113, 22)
        if not self.find( "cont_visualizar_movimento_todos_hist", matching=0.97, waiting_time=10000):
            not_found("cont_visualizar_movimento_todos_hist")
        self.click_relative(219, 24)
        if not self.find( "cont_5_vendas_orctos_pedidos_hist", matching=0.97, waiting_time=10000):
            not_found("cont_5_vendas_orctos_pedidos_hist")
        self.click()
        if not self.find( "cont_condicionais_5_vendas_hist", matching=0.97, waiting_time=10000):
            not_found("cont_condicionais_5_vendas_hist")
        self.click()
        if not self.find( "cont_5_vendas_orcamentos_hist", matching=0.97, waiting_time=10000):
            not_found("cont_5_vendas_orcamentos_hist")
        self.click()
        if not self.find( "cont_transferencias_hist_5_vendas", matching=0.97, waiting_time=10000):
            not_found("cont_transferencias_hist_5_vendas")
        self.click()
        if not self.find( "cont_devolucoes_5_vendas_hist", matching=0.97, waiting_time=10000):
            not_found("cont_devolucoes_5_vendas_hist")
        self.click()
        if not self.find( "cont_5_vendas_pedidos_hist", matching=0.97, waiting_time=10000):
            not_found("cont_5_vendas_pedidos_hist")
        self.click()
        if not self.find( "cont_situacao_abertos_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_abertos_hist_0")
        self.click_relative(8, 22)
        if not self.find( "cont_situacao_aq_liberacao_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_aq_liberacao_hist0")
        self.click_relative(9, 33)
        if not self.find( "cont_situacao_nao_liberados_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_nao_liberados_hist0")
        self.click_relative(122, 23)
        if not self.find( "cont_situacao_liberados_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_liberados_hist0")
        self.click_relative(122, 34)
        if not self.find( "cont_situacao_cancelados_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_cancelados_hist0")
        self.click_relative(237, 22)
        if not self.find( "cont_situacao_fechados_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_fechados_hist0")
        self.click_relative(237, 34)
        if not self.find( "cont_situacao_todos_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_todos_hist0")
        self.click_relative(349, 21)
        if not self.find( "cont_situacao_emproducao_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_emproducao_hist0")
        self.click_relative(351, 34)
        if not self.find( "cont_situacao_producao_fin_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_situacao_producao_fin_hist0")
        self.click_relative(464, 22)

        if not self.find( "cont_6_os_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_6_os_hist_0")
        self.click()
        self.wait(1000)
        if not self.find( "cont_7_prospeccao_crm_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_7_prospeccao_crm_hist_0")
        self.click()
        if not self.find( "cont_8_ultimos_contatos_tele_hist", matching=0.97, waiting_time=10000):
            not_found("cont_8_ultimos_contatos_tele_hist")
        self.click()
        if not self.find( "cont_data_historico_0_rel", matching=0.97, waiting_time=10000):
            not_found("cont_data_historico_0_rel")
        self.click_relative(32, 8)
        if not self.find( "cont_carregar_ano_data_hist_0", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_data_hist_0")
        self.click()
        if not self.find( "cont_ano_atual_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_ano_atual_hist0")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retornar_historico_de_cliente", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_historico_de_cliente")
        self.click()
        self.wait(2000)
        #if not self.find( "cont_salvar_opc_23_fin_4", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_fin_4")
        #self.click()
        self.wait(2000)
        self.click()
        self.wait(2000)
        self.wait(2000)
        
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        self.wait(2000)
        
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()
        if not self.find( "cont_editar_cliente_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_editar_cliente_forne_23")
        self.click()
        self.wait(3000)
        if not self.find( "cont_excluir_cad_clientes_forn", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_cad_clientes_forn")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()
        self.wait(2000)
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        
        
        ########################################################################
        ########### CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO #############
        ########################################################################

        self.wait(3000)
        
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_plano_de_contas_f4_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_f4_men")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"4")
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_centro_inicial_plano_rel_busc", matching=0.97, waiting_time=10000):
            not_found("cont_centro_inicial_plano_rel_busc")
        self.double_click_relative(143, 6)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)
        self.backspace()
        #aqui nao tem nada, entao voltar com esc
        self.key_esc()
        self.wait(1000)
        if not self.find( "cont_centro_final_rel_busc_plano", matching=0.97, waiting_time=10000):
            not_found("cont_centro_final_rel_busc_plano")
        self.click_relative(144, 8)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        #AQUI ESTA VAZIO, APENAS DAR ESC PRA VOLTAR
        #if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
        #    not_found("cont_selecionar_situacoes_op_23")
        #self.click()
        self.wait(3000)
        self.key_esc()
        self.wait(1000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_grupo_de_empresa_rel_plano", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_rel_plano")
        self.click_relative(43, 32)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        #mouse parando em cima, salvar apenas clicando
        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #   not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        #mouse em cima do bottão de retornar para o menu, apenas clicar
        self.wait(1000)
        self.click()



        # CADASTROS -> PLANO DE CONTAS - > MANUTENÇÃO DE CONTAS 
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        self.wait(2000)
        if not self.find( "cont_manutencao_do_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_manutencao_do_plano_contas")
        self.click()
        self.wait(1000)
        if not self.find( "cont_contas_do_grupo_busc_rel", matching=0.97, waiting_time=10000):
            not_found("cont_contas_do_grupo_busc_rel")
        self.click_relative(155, 24)
        self.wait(1000)
        if not self.find( "cont_localiza_grupos_no_plano_23", matching=0.97, waiting_time=10000):
            not_found("cont_localiza_grupos_no_plano_23")
        self.click()
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.space()
        self.space()
        self.tab()  
        self.type_right()
        self.type_right()
        self.type_right()
        self.wait(2000)
        if not self.find( "cont_acertar_reduzido_23_checkbox", matching=0.97, waiting_time=10000):
            not_found("cont_acertar_reduzido_23_checkbox")
        self.click()
        self.wait(2000)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_acertar_reduzido_btn_check", matching=0.97, waiting_time=10000):
            not_found("cont_acertar_reduzido_btn_check")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_alterar_manutencao_plano_cont", matching=0.97, waiting_time=10000):
            not_found("cont_alterar_manutencao_plano_cont")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_down()
        self.tab()
        self.type_down()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.wait(2000)
        #mouse parou em cima, apenas clicar
        #if not self.find( "cont_gravar_opc_25_btn", matching=0.97, waiting_time=10000):
        #    not_found("cont_gravar_opc_25_btn")
        self.click()
        self.wait(2000)
        if not self.find( "cont_reduz_duplic_manutencao_contas", matching=0.97, waiting_time=10000):
            not_found("cont_reduz_duplic_manutencao_contas")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_alt_grupos_manutencao_contas", matching=0.97, waiting_time=10000):
            not_found("cont_alt_grupos_manutencao_contas")
        self.click()
        if not self.find( "cont_flecha_alterar_grupo_contas", matching=0.97, waiting_time=10000):
            not_found("cont_flecha_alterar_grupo_contas")
        self.click()
        self.wait(2000)
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"110102")
        self.tab()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.tab()
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()

        # CADASTROS -> PLANO DE CONTAS -> PLANO DE CUSTOS

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        if not self.find( "cont_plano_de_custos_op23", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_custos_op23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_criar_cod_plano_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_criar_cod_plano_custos_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        # mouse parou em cima de retornar, apenas clicar para voltar ao menu
        self.click()


        #CADASTROS -> PLANO DE CONTAS ->  PLANO FINANCEIRO

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        self.wait(1000)
        if not self.find( "cont_plano_financeiro_custos", matching=0.97, waiting_time=10000):
            not_found("cont_plano_financeiro_custos")
        self.click()

        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        if not self.find( "cont_criar_cod_plano_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_criar_cod_plano_custos_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        # mouse parou em cima de retornar, apenas clicar para voltar ao menu
        self.click()



        # CADASTROS -> PLANO DE CONTAS ACERTO DE COD REDUZIDO

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        self.wait(1000)


        # este tela é igual ao manutenção de contas, então nao vou mexer por enquanto
        if not self.find( "cont_cad_plano_cus_plan_conta", matching=0.97, waiting_time=10000):
            not_found("cont_cad_plano_cus_plan_conta")
        self.click()
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_cond_pagto_moedas", matching=0.97, waiting_time=10000):
            not_found("cont_cond_pagto_moedas")
        self.click()
        if not self.find( "cont_moedas_cond_pag", matching=0.97, waiting_time=10000):
            not_found("cont_moedas_cond_pag")
        self.click()
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        x = 0
        while x < 9:
            self.type_down()
            x += 1 
        self.wait(2000)
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cotacoes_diarias", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cotacoes_diarias")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        self.wait(1000)
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_cliente_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_editar_cliente_forne_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_lixeira_cotacao_diaria", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_cotacao_diaria")
        self.click()
        self.wait(1000)
        self.enter()    
        if not self.find( "cont_excluir_cad_clientes_forn", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_cad_clientes_forn")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        self.click()
        self.wait(1000)
        
        self.wait(2000)
        # CADASTROS -> HISTORICOS 
        #
        #
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_historicos_menu_23", matching=0.97, waiting_time=10000):
            not_found("cont_historicos_menu_23")
        self.click()
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_cliente_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_editar_cliente_forne_23")
        self.click()
        self.wait(1000)
        # mouse vai parar em cima de excluir, apenas apertar novamente
        self.wait(1000)
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        #if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
        #    not_found("cont_locali_plano_contas_23")
        #self.click()
        #if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
        ##    not_found("cont_retornar_cad_client_forn_2")
        #self.click()
        #self.wait(2000)
        
        self.wait(3000)
        """
        ###################################
        #CADASTROS -> DEMONSTRATIVOS -> DRE
        ###################################
        self.wait(3000)

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_demonstrativos_menu_23", matching=0.97, waiting_time=10000):
            not_found("cont_demonstrativos_menu_23")
        self.click()
        if not self.find( "cont_dre_demonstrativo", matching=0.97, waiting_time=10000):
            not_found("cont_dre_demonstrativo")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        if not self.find( "cont_incluir_cotacoes_diarias", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cotacoes_diarias")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            self.type_up()
            x += 1
        self.tab()
        self.wait(1000)
        if not self.find( "cont_buscar_dre_demonstrativo_btn", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_dre_demonstrativo_btn")
        self.click()
        self.wait(1000)
        if not self.find( "cont_dre_localizar_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_dre_localizar_plano_contas")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_confirmar_inclusao_dre", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_inclusao_dre")
        self.click()
        self.wait(2000)
        if not self.find( "cont_lixeira_cotacao_diaria", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_cotacao_diaria")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        # DRE -> INCLUSAO RAPIDA
        #
        if not self.find( "cont_inclusao_rapida_dre", matching=0.97, waiting_time=10000):
            not_found("cont_inclusao_rapida_dre")
        self.click()
        if not self.find( "cont_nivel_rel_dre", matching=0.97, waiting_time=10000):
            not_found("cont_nivel_rel_dre")
        self.click_relative(62, 0)
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab() 
        self.type_down()
        self.wait(1000)
        
        ########################################################
        ########### DRE -> ESPACAMENTO DA ORDEM ################
        ########################################################

        self.wait(2000)
        if not self.find( "cont_espacamento_da_ordens_dre", matching=0.97, waiting_time=10000):
            not_found("cont_espacamento_da_ordens_dre")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_dre_relatorio_demonstrativos", matching=0.97, waiting_time=10000):
            not_found("cont_dre_relatorio_demonstrativos")
        self.click()
        
        if not self.find( "cont_livro_oficial_relatorio_dre", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_relatorio_dre")
        self.click_relative(50, 33)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_grupo_de_empresa_dre_rel", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_dre_rel")
        self.click_relative(52, 32)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        if not self.find( "cont_moedas_rel_busc_dre", matching=0.97, waiting_time=10000):
            not_found("cont_moedas_rel_busc_dre")
        self.click_relative(50, 26)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_botn_excluir_opc_7", matching=0.97, waiting_time=10000):
           not_found("cont_cad_botn_excluir_opc_7")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        
        ################################################################
        ############# CADASTROS -> DEMONSTRATIVOS -> DLPA ##############
        ################################################################
        self.wait(2000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        if not self.find( "cont_demonstrativos_menu_23", matching=0.97, waiting_time=10000):
            not_found("cont_demonstrativos_menu_23")
        self.click()
        if not self.find( "cont_dlpa_demonstrativos_menu", matching=0.97, waiting_time=10000):
            not_found("cont_dlpa_demonstrativos_menu")
        self.click()
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_plano_de_custos_23", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_plano_de_custos_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cotacoes_diarias", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cotacoes_diarias")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            self.type_up()
            x += 1
        self.tab()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123123123")
        self.wait(2000)
        if not self.find( "cont_confirmar_inclusao_dre", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_inclusao_dre")
        self.click()
        if not self.find( "cont_lixeira_cotacao_diaria", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_cotacao_diaria")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_inclusao_rapida_dre", matching=0.97, waiting_time=10000):
            not_found("cont_inclusao_rapida_dre")
        self.click()
        if not self.find( "cont_nivel_rel_dre", matching=0.97, waiting_time=10000):
            not_found("cont_nivel_rel_dre")
        self.click_relative(62, 0)
        self.tab() 
        self.type_keys_with_interval(100,"1")
        self.tab() 
        self.type_keys_with_interval(100,"123")
        self.tab() 
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.tab()
        self.enter()
        if not self.find( "cont_espacamento_da_ordens_dre", matching=0.97, waiting_time=10000):
            not_found("cont_espacamento_da_ordens_dre")
        self.click()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_dre_relatorio_demonstrativos", matching=0.97, waiting_time=10000):
            not_found("cont_dre_relatorio_demonstrativos")
        self.click()
        if not self.find( "cont_data_rel_relatorio_dlpa", matching=0.97, waiting_time=10000):
            not_found("cont_data_rel_relatorio_dlpa")
        self.click_relative(30, 6)
        if not self.find( "cont_data_carregar_ano_historic", matching=0.97, waiting_time=10000):
            not_found("cont_data_carregar_ano_historic")
        self.click()
        if not self.find( "cont_atual_data_historico", matching=0.97, waiting_time=10000):
            not_found("cont_atual_data_historico")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.tab()
        if not self.find( "cont_livro_oficial_rel_dpla", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_rel_dpla")
        self.click_relative(45, 32)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_grupo_de_empresas_rel_dlpa", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresas_rel_dlpa")
        self.click_relative(53, 29)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        if not self.find( "cont_cad_botn_excluir_opc_7", matching=0.97, waiting_time=10000):
           not_found("cont_cad_botn_excluir_opc_7")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()

        ##############################################
        ####### MENU -> CADASTROS -> IMPOSTOS ########
        ##############################################

        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_impostos_23", matching=0.97, waiting_time=10000):
            not_found("cont_menu_impostos_23")
        self.click()
        if not self.find( "cont_incluir_plano_de_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_plano_de_contas_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_btn_buscar_impostos_cad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_buscar_impostos_cad")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"0081260")
        self.wait(1000)
        if not self.find( "cont_localizar_clientes_forn_hist0", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_clientes_forn_hist0")
        self.click()

        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"12")
        self.tab()
        self.tab()
        self.type_down()
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        self.enter()
        self.space()
        self.tab()
        self.tab()
        self.type_down()
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        self.enter()
        self.tab()
        self.type_down()
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_cfop_relati_impost", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_relati_impost")
        self.click_relative(114, 8)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        if not self.find( "cont_2_importacao_cfop_imp", matching=0.97, waiting_time=10000):
            not_found("cont_2_importacao_cfop_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cfop_inicial_imp_rel", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_inicial_imp_rel")
        self.click_relative(65, 20)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_cfop_final_rel_busc", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_final_rel_busc")
        self.click_relative(66, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_right()
        self.type_right()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_qa12_opcao_imposto_clicar", matching=0.97, waiting_time=10000):
            not_found("cont_qa12_opcao_imposto_clicar")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(2000)
        #mouse para em cima de botao EXCLUIR
        #APENAS CLICAR PARA EXCLUIR
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.click() #MOUSE PAROU EM CIMA DE RETORNAR PARA MENU, CLICAR NOVAMENTE PARA RETORNAR
        
        #######################################
        #######################################
        # CADASTROS -> IMPOSTO PRESUMIDO ######
        #######################################
        #######################################
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_cad_imposto_presumido", matching=0.97, waiting_time=10000):
            not_found("cont_menu_cad_imposto_presumido")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 20:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_botao_contabilizacao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_botao_contabilizacao_imp")
        self.click()
        if not self.find( "cont_busc_imp_contabilizacao_23", matching=0.97, waiting_time=10000):
            not_found("cont_busc_imp_contabilizacao_23")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        if not self.find( "cont_confirma_opcao_contabilizacao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_opcao_contabilizacao_imp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_lixeira_20_imp", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_20_imp")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)

        if not self.find( "cont_incidencias_do_simples_nacional_menu", matching=0.97, waiting_time=10000):
            not_found("cont_incidencias_do_simples_nacional_menu")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()

        if not self.find( "cont_opc_20_busc_botao", matching=0.97, waiting_time=10000):
            not_found("cont_opc_20_busc_botao")
        self.click()


        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        self.wait(1000)
        x = 0
        while x < 8:
            self.space()
            self.space()
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        ########################################
        # CADASTROS -> TABELAS - TABELAS DARF_GR 
        ########################################

        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tabelas_menu_opcao", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_menu_opcao")
        self.click()
        if not self.find( "cont_tabelas_darf_gr", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_darf_gr")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()

        x = 0
        while x < 9:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(2000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tabelas_menu_opcao", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_menu_opcao")
        self.click()
        if not self.find( "cont_tabelas_darf_gr", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_darf_gr")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_botn_excluir_opc_7", matching=0.97, waiting_time=10000):
           not_found("cont_cad_botn_excluir_opc_7")
        self.click()
        self.wait(2000)
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        
        self.wait(3000)

        ###############################################
        #CADASTROS -> TABELA -> TABELA SIMPLES NACIONAL
        ###############################################


        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tabelas_menu_opcao", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_menu_opcao")
        self.click()
        if not self.find( "cont_tabela_simples_nacional_men", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_simples_nacional_men")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(3000)
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opc_3_conta_busc_btn", matching=0.97, waiting_time=10000):
            not_found("cont_opc_3_conta_busc_btn")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 4: 
            self.type_down()
            self.type_down()
            self.enter()
            self.tab()
            x += 1
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(2000)
        self.enter()
        
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_itens_de_estoque_opc_menu", matching=0.97, waiting_time=10000):
            not_found("cont_itens_de_estoque_opc_menu")
        self.click()
        if not self.find( "cont_agrupamento_itens_menu", matching=0.97, waiting_time=10000):
            not_found("cont_agrupamento_itens_menu")
        self.click()
        if not self.find( "cont_btn_unidades_menu_agrupamentos", matching=0.97, waiting_time=10000):
            not_found("cont_btn_unidades_menu_agrupamentos")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        #mouse vai parar em cima, apenas clicar novamente para voltar ao menu
        self.click()
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_itens_de_estoque_opc_menu", matching=0.97, waiting_time=10000):
            not_found("cont_itens_de_estoque_opc_menu")
        self.click()
        if not self.find( "cont_agrupamento_itens_menu", matching=0.97, waiting_time=10000):
            not_found("cont_agrupamento_itens_menu")
        self.click()
        if not self.find( "cont_agrupamento_itens_ncm", matching=0.97, waiting_time=10000):
            not_found("cont_agrupamento_itens_ncm")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        self.shift_tab()
        self.type_keys_with_interval(100,"qa12")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_btn_busc_ncm_23", matching=0.97, waiting_time=10000):
            not_found("cont_btn_busc_ncm_23")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        x = 0
        while x < 10:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        #######################################
        #######################################
        #CADASTROS -> ITENS DE ESTOQUE -> ITENS
        #######################################
        #######################################


        self.wait(3000)

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_itens_de_estoque_opc_menu", matching=0.97, waiting_time=10000):
            not_found("cont_itens_de_estoque_opc_menu")
        self.click()

        if not self.find( "cont_menu_itens_23_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_itens_23_2")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_itens_btn_ncm_busc", matching=0.97, waiting_time=10000):
            not_found("cont_itens_btn_ncm_busc")
        self.click_relative(138, 4)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"12")
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_itens_unidade_btn_busc", matching=0.97, waiting_time=10000):
            not_found("cont_itens_unidade_btn_busc")
        self.click_relative(93, 8)
        self.wait(2000)
        self.type_keys_with_interval(100,"c")
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.tab()
        if not self.find( "cont_grupo_fiscal_itens_btn_busc", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_itens_btn_busc")
        self.click_relative(116, 7)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_down()
        self.type_down()
        if not self.find( "cont_conta_contabil_busc_item_rel", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_busc_item_rel")
        self.click_relative(139, 6)
        self.wait(2000)
        self.type_keys_with_interval(100,"001")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        self.click() # botao ja esta em cima de salvar, apenas clicar
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_fornecedor_busc_rel_itens", matching=0.97, waiting_time=10000):
            not_found("cont_fornecedor_busc_rel_itens")
        self.click_relative(59, 21)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_unidade_rel_bsc_btn_2_itens", matching=0.97, waiting_time=10000):
            not_found("cont_unidade_rel_bsc_btn_2_itens")
        self.click_relative(56, 58)
        self.wait(2000)
        self.type_keys_with_interval(100,"c")
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_cancelar_referencias_itens", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_referencias_itens")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_cancelar_bot_itens_23", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_bot_itens_23")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_itens_de_estoque_opc_menu", matching=0.97, waiting_time=10000):
            not_found("cont_itens_de_estoque_opc_menu")
        self.click()
        self.wait(2000)
        if not self.find( "cont_itens_menu_tipo_do_item", matching=0.97, waiting_time=10000):
            not_found("cont_itens_menu_tipo_do_item")
        self.click()
        self.wait(2000)

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        x = 0
        while x < 12:
            self.type_down()
            x += 1
        self.tab()
        self.type_down()
        self.tab()
        self.type_down()
        self.wait(2000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"99")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        #################################
        ########## CADASTROS -> BENS
        #################################
        
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_bens_23", matching=0.97, waiting_time=10000):
            not_found("cont_menu_bens_23")
        self.click()
        self.wait(3000)

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()

        if not self.find( "cont_inserir_ale_codigo_bens", matching=0.97, waiting_time=10000):
            not_found("cont_inserir_ale_codigo_bens")
        self.click()
        self.type_keys_with_interval(100,"qa12!@")
        x = 0
        while x < 4:
            self.tab()
            x += 1
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        if not self.find( "cont_conta_contabil_rel_btn_atv", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_rel_btn_atv")
        self.click_relative(421, 7)
        self.wait(1000)
        self.type_down()
        self.enter()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 3:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 4: #Utilização do bem
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 6: #Numero de parcelas
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 8:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_2_controle_de_credito_bens", matching=0.97, waiting_time=10000):
            not_found("cont_2_controle_de_credito_bens")
        self.click()
        self.wait(1000)
        self.click()
        self.tab()
        x = 0
        while x < 21:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_3_contabilizacao_fornecedor_bens", matching=0.97, waiting_time=10000):
            not_found("cont_3_contabilizacao_fornecedor_bens")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.type_down()
        self.type_down()
        self.enter()
        if not self.find( "cont_bens_btn_loc_fornecedor", matching=0.97, waiting_time=10000):
            not_found("cont_bens_btn_loc_fornecedor")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(3000)
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_bens_contabilizacao_baixa", matching=0.97, waiting_time=10000):
            not_found("cont_bens_contabilizacao_baixa")
        self.click()
        self.wait(1000)
        self.click()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.type_down()
        self.type_down()
        self.enter()
        if not self.find( "cont_bens_5_localizacao", matching=0.97, waiting_time=10000):
            not_found("cont_bens_5_localizacao")
        self.click()
        self.wait(1000)
        self.click()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_bens_6_observacoes", matching=0.97, waiting_time=10000):
            not_found("cont_bens_6_observacoes")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        # aqui da um erro que o codigo nao é valido pois possui ponto
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        #################################
        #################################
        ##### CADASTROS -> SERVIÇOS #####
        #################################
        #################################
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_servicos_23", matching=0.97, waiting_time=10000):
            not_found("cont_menu_servicos_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        
        if not self.find( "cont_servicos_unidade_btn_busc", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_unidade_btn_busc")
        self.click_relative(52, 28)
        self.type_keys_with_interval(100,"c")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()

        if not self.find( "cont_servicos_agrupamento_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_agrupamento_rel_btn")
        self.click_relative(58, 96)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        if not self.find( "cont_plano_de_contas_rel_btn_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_rel_btn_servicos") #plano de contas
        self.click_relative(62, 141)
        self.wait(1000)
        self.type_keys_with_interval(100,"001")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_grupo_fiscal_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_grupo_fiscal_rel_btn")
        self.click_relative(54, 27)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_servicos_subgrupo_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_subgrupo_rel_btn")
        self.click_relative(55, 30)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_ncm_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_ncm_rel_btn")
        self.click_relative(107, 29) # NCM 
        self.wait(1000)
        self.type_keys_with_interval(100,"1")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_familia_bsc_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_familia_bsc_rel_btn")
        self.click_relative(56, 26)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_marca_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_marca_rel_btn")
        self.click_relative(55, 30)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_centro_custo_servicos_rel", matching=0.97, waiting_time=10000):
            not_found("cont_centro_custo_servicos_rel")
        self.click_relative(86, 31)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        
        if not self.find( "cont_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_serv_cardex_botao_data", matching=0.97, waiting_time=10000):
            not_found("cont_serv_cardex_botao_data")
        self.click_relative(30, 7)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_servicos_cardex_precos", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_cardex_precos")
        self.click()
        self.wait(1000)
        # NAO PRECISA SALVAR AQUI 
        # CADASTROS DE SERVIÇOS -> PREÇOS 

        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_precos_servicos_incluir_btn", matching=0.97, waiting_time=10000):
            not_found("cont_precos_servicos_incluir_btn")
        self.click()
        self.wait(1000)
        self.backspace()
        if not self.find( "cont_servicos_precos_btn_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_precos_btn_buscar")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.backspace()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        if not self.find( "cont_gravar_servicos_preco", matching=0.97, waiting_time=10000):
            not_found("cont_gravar_servicos_preco")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_servicos_principal_volt", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_principal_volt")
        self.click()
        self.wait(1000)
        self.click()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        # Cadastros -> ECF
        #
        #
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_efc", matching=0.97, waiting_time=10000):
            not_found("cont_menu_efc")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"3")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        x = 0
        while x <11:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"3")
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        # CADASTROS -> LIVROS OFICIAIS 
        #
        #
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_menu_livros_oficiais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_livros_oficiais_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_livros_oficiais_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_salvar_opcao_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opcao_livros_oficiais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_livros_oficiais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_menu_livros_oficiais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_livros_oficiais")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_livros_oficiais")
        self.click()
        self.wait(1000)

        # CADASTROS -> PROCESSOS ADMINISTRATIVOS 
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_processos_administrativos_menu", matching=0.97, waiting_time=10000):
            not_found("cont_processos_administrativos_menu")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_cod_fisc_busc_impos_23", matching=0.97, waiting_time=10000):
            not_found("cont_cod_fisc_busc_impos_23")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ######################################################
        ## CADASTROS -> DOCUMENTAÇOES -> TIPOS DE DOCUMENTO ##
        ######################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_documentacoes", matching=0.97, waiting_time=10000):
            not_found("cont_menu_documentacoes")
        self.click()
        self.wait(1000)
        if not self.find( "cont_documentos_tipos_de_doc", matching=0.97, waiting_time=10000):
            not_found("cont_documentos_tipos_de_doc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        # CADASTROS -> DOCUMENTAÇOES -> DOCUMENTOS 
        #
        #
        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_documentacoes", matching=0.97, waiting_time=10000):
            not_found("cont_menu_documentacoes")
        self.click()
        self.wait(1000)
        if not self.find( "cont_documentos_menu_doc", matching=0.97, waiting_time=10000):
            not_found("cont_documentos_menu_doc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_tipo_documento_documentos_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_documento_documentos_bsc")
        self.click_relative(119, 4)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_cliente_fornec_bsc_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_fornec_bsc_documentos")
        self.click_relative(172, 4)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_arquivo_documentos_tipo", matching=0.97, waiting_time=10000):
            not_found("cont_arquivo_documentos_tipo")
        self.click()
        self.wait(1000)
        self.key_esc()

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        # CADASTROS -> DOCUMENTEÇOS -> DOCUMENTOS REFERENCIADOS 

        self.wait(3000)
        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_documentacoes", matching=0.97, waiting_time=10000):
            not_found("cont_menu_documentacoes")
        self.click()
        self.wait(1000)
        if not self.find( "cont_documentos_referenciados_menu", matching=0.97, waiting_time=10000):
            not_found("cont_documentos_referenciados_menu")
        self.click()


        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        x = 0
        while x < 16: 
            self.type_down()
            x += 1
        if not self.find( "cont_observacao_lancamento_fiscal_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_observacao_lancamento_fiscal_bsc")
        self.click_relative(152, 26)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_cad_muni_opc_selec_07", matching=0.97, waiting_time=10000):
           not_found("cont_cad_muni_opc_selec_07")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 4:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ##########################################################################################
        ##########################################################################################
        ################################# FIM DE CADASTROS #######################################
        ##########################################################################################
        ##########################################################################################



def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()




























