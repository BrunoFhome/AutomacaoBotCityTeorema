from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

""" 
CÓDIGO FEITO PARA SISTEMA CONTABIL 24.07
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
        
        #######################################################
        ############# COMEÇO CONTABIL - COMPLETO ##############
        #######################################################
        
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
        
        ############################################################################################
        ########################### CADASTROS -> EMPRESAS  -> EMPRESAS #############################
        ############################################################################################
        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        self.type_keys_with_interval(100,"QA12!@")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_planos_de_contas_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_planos_de_contas_da_empresa")
        self.click_relative(68, 30)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_itens_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_itens_da_empresa")
        self.click_relative(67, 26)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_vendedores_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_vendedores_da_empresa")
        self.click_relative(68, 27)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_tabela_de_precos_servico_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_precos_servico_busc")
        self.click_relative(66, 23)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.backspace()
        self.backspace()
        self.backspace()
        self.backspace()
        
        self.wait(2000)
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
        
        self.wait(3000)
        #
        if not self.find( "cont_usa_historico_da_empre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_historico_da_empre_busc")
        self.click_relative(71, 29)
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_precos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_precos_da_empresa_busc")
        self.click_relative(67, 29)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_situacao_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_situacao_da_empresa_busc")
        self.click_relative(68, 31)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_usa_veiculos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_veiculos_da_empresa_busc")
        self.click_relative(69, 28)
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        
        #MOUSE JA PAROU EM CIMA DO SALVAR
        if not self.find( "cont_botao_de_salvar_cadastro", matching=0.97, waiting_time=10000):
           not_found("cont_botao_de_salvar_cadastro")
        self.wait(3000)
        self.click()
        
        
        self.wait(3000)
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
        self.wait(2000)
        if not self.find( "cont_cad_conta_contabil_96", matching=0.97, waiting_time=10000):
            not_found("cont_cad_conta_contabil_96")
        self.click_relative(120, 24)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_cad_conta_contabil_95", matching=0.97, waiting_time=10000):
            not_found("cont_cad_conta_contabil_95")
        self.click_relative(122, 25)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not self.find( "cont_localizar1", matching=0.97, waiting_time=10000):
            not_found("cont_localizar1")
        self.click()
        if not self.find( "cont_selecionar_outro_2", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_outro_2")
        self.click()
        self.wait(2000)
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
        self.wait(2000)
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
        self.wait(2000)
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
        self.wait(2000)
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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

        if not self.find( "btn_retornar_excluir_teste_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_retornar_excluir_teste_apagar")
        self.click()
        
        #################################################################################
        ######################### EXCLUIR O CADASTRO DA EMPRESA #########################
        #################################################################################

        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()

        self.wait(2000)
        if not self.find( "cont_empresas_cad_1_men_", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_cad_1_men_")
        self.click()
        
        if not self.find( "cont_empresas_23_empresas", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_23_empresas")
        self.click()
        self.wait(1000)
        if not self.find( "btn_localizar_teste_apagar_qa12", matching=0.97, waiting_time=10000):
            not_found("btn_localizar_teste_apagar_qa12")
        self.click()
            
        self.wait(1000)
        if not self.find( "btn_clicar_teste_qa_12_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_clicar_teste_qa_12_apagar")
        self.click()
        self.wait(1000)
        if not self.find( "editar_teste_24_apagar_qa12", matching=0.97, waiting_time=10000):
            not_found("editar_teste_24_apagar_qa12")
        self.click()
        self.wait(1000)
        if not self.find( "excluir_btn_teste_apagar_qa12", matching=0.97, waiting_time=10000):
            not_found("excluir_btn_teste_apagar_qa12")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "btn_retornar_excluir_teste_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_retornar_excluir_teste_apagar")
        self.click()
        self.wait(1000)
        if not self.find( "btn_localizar_teste_apagar_qa12", matching=0.97, waiting_time=10000):
            not_found("btn_localizar_teste_apagar_qa12")
        self.click()
        self.wait(1000)
        if not self.find( "btn_retornar_excluir_teste_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_retornar_excluir_teste_apagar")
        self.click()

        self.wait(2000)

        
        ############################################################################
        ################# CADASTROS -> EMPRESAS -> GRUPO DE EMPRESAS ###############
        ############################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        
        ###########################################################################
        ########## CADASTROS -> PARAMETROS -> PARAMETROS DA EMPRESA - F9 ##########
        ###########################################################################
        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        self.wait(1000)
        
        
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

        if not self.find( "cont_achar_teste_parametros_24_07", matching=0.97, waiting_time=10000):
            not_found("cont_achar_teste_parametros_24_07")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_producao_btn_relativo_custo_1", matching=0.97, waiting_time=10000):
            not_found("cont_producao_btn_relativo_custo_1")
        self.click_relative(165, 39)
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        self.wait(30000)
        
        #aqui aperta para exibir lista de itens a incluir
        
        self.wait(3000)
        if not self.find( "cont_cad_linha_1_rel_teste", matching=0.97, waiting_time=10000):
            not_found("cont_cad_linha_1_rel_teste")
        self.click_relative(65, 8)
        
        self.wait(4000)
        if not self.find( "cont_10_e_comerce_exibir_itens", matching=0.97, waiting_time=10000):
            not_found("cont_10_e_comerce_exibir_itens")
        self.click_relative(-151, 72)
        
        self.wait(4000)
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
        
        self.wait(1000)


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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_1_transf_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_transf_busc")
        self.click_relative(82, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_2_inventario_busc", matching=0.97, waiting_time=10000):
            not_found("cont_2_inventario_busc")
        self.click_relative(80, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_3_producao_osm_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_producao_osm_busc")
        self.click_relative(88, 28)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_4_item_kit_busc", matching=0.97, waiting_time=10000):
            not_found("cont_4_item_kit_busc")
        self.click_relative(79, 26)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_5_item_mestre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_5_item_mestre_busc")
        self.click_relative(84, 28)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_6_almoxarifado_busc", matching=0.97, waiting_time=10000):
            not_found("cont_6_almoxarifado_busc")
        self.click_relative(80, 24)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_7_desmembra_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_7_desmembra_itens_busc")
        self.click_relative(83, 25)
        
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_devoluca_iten_busc", matching=0.97, waiting_time=10000):
            not_found("cont_devoluca_iten_busc")
        self.click_relative(78, 25)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_3_operacao_saida_1", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_1")
        self.click_relative(83, 44)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        
        self.wait(3000)
        if not self.find( "cont_3_operacao_saida_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_3")
        self.click_relative(883, 45)
        self.wait(2000)
        if not self.find( "cont_localizar_1_rel", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_1_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        self.backspace()
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
        self.click()
        self.wait(3000)
        self.enter()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()


        #################################################################################
        #################### EXCLUINDO PARAMETRO DA EMPRESA DE TESTES ###################
        #################################################################################

        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        self.wait(1000)
        
        
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

        if not self.find( "cont_btn_parametros_empresa_exclusao_teste", matching=0.97, waiting_time=10000):
            not_found("cont_btn_parametros_empresa_exclusao_teste")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_editar_parametros_empresa_excluir", matching=0.97, waiting_time=10000):
            not_found("cont_btn_editar_parametros_empresa_excluir")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_excluir_24_07_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_24_07_parametros_fiscais")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_sim_exclusao_parametros_teste", matching=0.97, waiting_time=10000):
            not_found("cont_btn_sim_exclusao_parametros_teste")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.click()
        self.wait(2000)
                         
        
        #################################################################################
        ############### CADASTROS -> PARAMETROS -> PARAMETROS TRANSPORTES ###############
        #################################################################################
        
        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_parametros_menu_transp_21", matching=0.97, waiting_time=10000):
            not_found("cont_parametros_menu_transp_21")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> REGIONALIZAÇÃO -> PAISES ###############
        ############################################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        self.click()

        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> REGIONALIZAÇÃO -> REGIOES ##############
        ############################################################################################

        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> REGIONALIZAÇÃO -> ESTADOS ##############
        ############################################################################################

        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.tab()
        self.tab()
        self.type_down()
        self.wait(3000)
        #mouse esta parando em cima de salvar
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
        self.wait(3000)
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(3000)
        self.click()
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> REGIONALIZAÇÃO -> REGIOES ##############
        ############################################################################################

        self.wait(2000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_salvar_botaoo", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botaoo")
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
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> GRUPO FISCAL DE PRODUTOS  ##############
        ############################################################################################



        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        ############################################################################################
        ################ CADASTROS -> PARAMETROS FISCAIS  -> CODIGOS FISCAIS (CFOP) ################
        ############################################################################################



        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        ############################################################################################
        ######## CADASTROS -> PARAMETROS FISCAIS  -> CODIGOS FISCAIS (CFOP) IMPORTAÇÃO NFE #########
        ############################################################################################

        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        self.wait(3000)
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
        self.wait(3000)
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
        
        
        ############################################################################################
        ################## CADASTROS -> PARAMETROS FISCAIS  -> CODIGOS DE OPERAÇÃO #################
        ############################################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_busc")
        self.click_relative(69, 26)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        self.backspace()

        if not self.find( "cont_tabela_precos_servicos_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_servicos_busc")
        self.click_relative(60, 26)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        ############################################################################################
        ################ CADASTROS -> PARAMETROS FISCAIS  -> DECRETOS E OBSERVAÇOES ################
        ############################################################################################


        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        ############################################################################################
        ####################### CADASTROS -> PARAMETROS FISCAIS  -> SITUAÇÕES ######################
        ############################################################################################
        self.wait(2000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_regiao_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_regiao_selec_busc")
        self.click_relative(48, 28)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        if not self.find( "cont_grupo_fiscal_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_selec_busc")
        self.click_relative(51, 26)
        
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_decreto_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_decreto_2_busc_")
        self.click_relative(46, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_obs_1_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_1_busc_")
        self.click_relative(43, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_obs_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_2_busc_")
        self.click_relative(43, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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
        #if not self.find( "cont_cancelar_bot_itens_23", matching=0.97, waiting_time=10000):
        #    not_found("cont_cancelar_bot_itens_23")
        #self.click()
        #self.wait(2000)
        #self.enter()
        if not self.find( "cont_salvar_regiao_cad_3", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_regiao_cad_3")
        self.click()
        if not self.find( "cont_retornar_parametro", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_parametro")
        self.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        
        if not self.find( "cont_localizar_pais", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_pais")
        self.click()
        if not self.find( "cont_achar_123_situacoes", matching=0.97, waiting_time=10000):
            not_found("cont_achar_123_situacoes")
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
        
        ############################################################################################
        ############### CADASTROS -> CLIENTES, FORNECEDORES E TRANSPORTADORES - F3 #################
        ############################################################################################
        
        
        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
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
        
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        
        self.wait(2000)
        if not self.find( "cont_ramo_de_atividade_12", matching=0.97, waiting_time=10000):
            not_found("cont_ramo_de_atividade_12")
        self.click_relative(68, 29)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_comissao_13", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_13")
        self.click_relative(70, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_vendedor_compr_14", matching=0.97, waiting_time=10000):
            not_found("cont_vendedor_compr_14")
        self.click_relative(65, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        #if not self.find( "cont_plano_financeiro_15", matching=0.97, waiting_time=10000):
        #    not_found("cont_plano_financeiro_15")
        #self.click_relative(84, 26)
        #self.wait(2000)
        #self.type_keys_with_interval(100,"0010010")
        #if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
        #    not_found("cont_loc_cod_fiscais_5")
        #self.click()
        #
        #if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
        #    not_found("cont_24_botao_selecionar_contabil")
        #self.click()
        
        #self.wait(2000)
        #self.backspace()
        
        self.wait(1000)

        if not self.find( "cont_centro_de_custo_16", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custo_16")
        self.click_relative(84, 27)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        self.backspace()
        
        
        self.wait(2000)
        if not self.find( "cont_classificacao_17", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_17")
        self.click_relative(67, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_conta_corrente_18", matching=0.97, waiting_time=10000):
            not_found("cont_conta_corrente_18")
        self.click_relative(70, 29)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_segmento_busc_rel_21", matching=0.97, waiting_time=10000):
            not_found("cont_segmento_busc_rel_21")
        self.click_relative(67, 30)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_linha_rel_busc_22", matching=0.97, waiting_time=10000):
            not_found("cont_linha_rel_busc_22")
        self.click_relative(71, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_bsc_23", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_bsc_23")
        self.click_relative(67, 28)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        if not self.find( "cont_transportador_busc_26", matching=0.97, waiting_time=10000):
            not_found("cont_transportador_busc_26")
        self.click_relative(83, 25)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_clientes_cond_pagamento_rel_2407", matching=0.97, waiting_time=10000):
            not_found("cont_btn_clientes_cond_pagamento_rel_2407")
        self.click_relative(67, 25)
        self.wait(3000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_operacao_nfs_e_ordem_28", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_nfs_e_ordem_28")
        self.click_relative(72, 32)
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        

        #########################################################################################
        ##### CADASTROS -> CLIENTES... -> INCLUIR -> 2 AGRUPAMENTO -> CONTABILIZAÇÃO MACROS #####
        #########################################################################################

        self.wait(3000)
        if not self.find( "cont_contabilizacao_macros", matching=0.97, waiting_time=10000):
             not_found("cont_contabilizacao_macros")
        self.click()
        if not self.find( "cont_cad_contabilizacao_macros_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_cad_contabilizacao_macros_contabil")
        self.click_relative(421, 46)
        self.wait(2000)
        self.type_down()
        self.wait(1000)
        self.enter()
        # self.wait(2000)
        # if not self.find( "cont_codigo_contabil_fornecedor", matching=0.97, waiting_time=10000):
        #     not_found("cont_codigo_contabil_fornecedor")
        # self.click_relative(66, 22)
        # self.wait(2000)
        # self.type_keys_with_interval(100,"1")
        # self.wait(1000)
        # if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
        #     not_found("cont_loc_cod_fiscais_5")
        # self.click()
        # if not self.find( "cont_cad_btn_selec_opc_19_03", matching=0.97, waiting_time=10000):
        #     not_found("cont_cad_btn_selec_opc_19_03")
        # self.click()
        # self.wait(3000)
        # if not self.find( "cont_botao_salva_23_fin_3", matching=0.97, waiting_time=10000):
        #     not_found("cont_botao_salva_23_fin_3")
        # self.click()
        # self.wait(3000)
        # self.enter()
        # self.wait(2000)
        # if not self.find( "cont_2_agrupamento_clientes", matching=0.97, waiting_time=10000):
        #     not_found("cont_2_agrupamento_clientes")
        # self.click()
        # self.wait(2000)
        
        if not self.find( "cont_codigo_contabeis_multi_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabeis_multi_empresa")
        self.click()

        if not self.find( "cont_codigo_contabil_client_22", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_client_22")
        self.click_relative(63, 29)
        self.wait(4000)
        self.type_down()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_2_agrupamento_clientes", matching=0.97, waiting_time=10000):
             not_found("cont_2_agrupamento_clientes")
        self.click()
        self.wait(1000)

        if not self.find( "cont_codigo_contabeis_multi_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabeis_multi_empresa")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_client_22", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_client_22")
        self.click_relative(63, 29)

        self.type_keys_with_interval(100,"00001")
        self.wait(2000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_forne_23")
        self.click_relative(65, 27)
        self.wait(2000)
        self.type_keys_with_interval(100,"00001")
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_confirmar_opc_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_confirmar_opc_5")
        self.click()

        ##########################################################
        ######## CADASTROS -> INCLUIR -> 3_PESSOA_FISICA #########
        ##########################################################

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
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
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
        self.type_keys_with_interval(100,"123") # Data Nascimento
        self.tab()
        self.type_keys_with_interval(100,"11517192935") #CPF
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
        self.type_keys_with_interval(100,"123123123") # Telefone
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
        
        ###########################################################
        ################ 4 ROTAS DADOS ADICIONAIS #################
        ###########################################################
        
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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

        #####################################################
        ####### CADASTROS -> 5 OBS REF LIMITE CREDITO #######
        #####################################################
        
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
        
        ##########################################
        ########## 6 RELACIONAMENTOS #############
        ##########################################

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
        
        ###########################################
        ### 6 RELACIONAMENTOS -> REPRESENTANTES ###
        ###########################################
        
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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

        ###############################################
        #### 6 RELACIONAMENTOS -> LOCAL DE ENTREGA ####
        ###############################################

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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        ###############################################
        #### 6 RELACIONAMENTOS -> PESSOAS CONTATOS ####
        ###############################################

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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        self.type_keys_with_interval(100,"42991472544")
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
        
        ###############################################
        ######## 6 RELACIONAMENTOS -> AVALIAÇÕES ######
        ###############################################

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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)

        ### NAO EXISTE AVALIAÇÃO DISPONIVEL PARA SELECIONAR NESTA BASE, APENAS CANCELAR
        

        
        if not self.find( "cont_cancelar_avaliacoes_btn", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_avaliacoes_btn")
        self.click()

        ###########################################################
        ######## 6 RELACIONAMENTOS -> VENDEDORES AUXILIARES #######
        ###########################################################


        if not self.find( "cont_vendedores_auxiliares_6", matching=0.97, waiting_time=10000):
            not_found("cont_vendedores_auxiliares_6")
        self.click()
        if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_incluir_spc")
        self.click()
        
        self.wait(3000)
        if not self.find( "cont_selecionar_nome_nuhar", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_nome_nuhar")
        self.click_relative(26, 25)
        
        
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_exclusao_dad_spc", matching=0.97, waiting_time=10000):
            not_found("cont_exclusao_dad_spc")
        self.click()
        self.wait(1000)
        self.enter()
        
        self.wait(3000)

        ###########################################################
        ############# 6 RELACIONAMENTOS -> DOCUMENTOS #############
        ###########################################################

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
        
        ###########################################################
        ############# 6 RELACIONAMENTOS -> CONTRATOS ##############
        ###########################################################

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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_comissao_contratos_bsc_rel", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_contratos_bsc_rel")
        self.click_relative(58, 26)
        self.wait(1000)
        if not self.find( "cont_loc_cod_fiscais_5", matching=0.97, waiting_time=10000):
            not_found("cont_loc_cod_fiscais_5")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        ####################################################################
        ############# 6 RELACIONAMENTOS -> CLIENTES VINCULADOS #############
        ####################################################################
        
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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

        ###################################################################
        ############# 6 RELACIONAMENTOS -> CATEGORIA CAMPANHA #############
        ###################################################################
        
        # CATEGORIA CAMPANHA ESTÁ COM PROBLEMA AO INCLUIR

        #if not self.find( "cont_categoria_campanha_6_rel", matching=0.97, waiting_time=10000):
        #    not_found("cont_categoria_campanha_6_rel")
        #self.click()
        #if not self.find( "cont_btn_incluir_spc", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_incluir_spc")
        #self.click()



        #######################################################################
        ############# 6 RELACIONAMENTOS -> RATEIO CENTRO DE CUSTO #############
        #######################################################################

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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        #############################################################
        ############# 6 RELACIONAMENTOS -> EQUIPAMENTOS #############
        #############################################################

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

        ##############################################################
        ############# 6 RELACIONAMENTOS -> REDES SOCIAIS #############
        ##############################################################

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
        

        #############################################################
        #####################  0 HISTORICOS #########################
        #############################################################

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
        if not self.find( "cont_abertas_0_histor", matching=0.97, waiting_time=10000):
            not_found("cont_abertas_0_histor")
        self.click()
        if not self.find( "cont_baixadas_0_histori", matching=0.97, waiting_time=10000):
            not_found("cont_baixadas_0_histori")
        self.click()
        self.wait(1000)
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        
        ################################################################################################
        ########### CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO -> PLANO DE CONTAS - F4 #############
        ################################################################################################

        self.wait(3000)
        
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(3000)

       
        self.wait(1000)
        if not self.find( "cont_centro_final_rel_busc_plano", matching=0.97, waiting_time=10000):
            not_found("cont_centro_final_rel_busc_plano")
        self.click_relative(144, 8)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
    
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_grupo_de_empresa_rel_plano", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_rel_plano")
        self.click_relative(43, 32)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        #mouse parando em cima, salvar apenas clicando
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
           not_found("cont_salvar_opc_23_plano_c")
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


        
        #########################################################################################################
        ########### CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO -> MANUTENÇÃO DO PLANO DE CONTAS #############
        #########################################################################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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
        
        ################################################################################################
        ############### CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO -> PLANO DE CUSTOS ##############
        ################################################################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        
        ################################################################################################
        ############# CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO -> PLANO FINANCEIRO ###############
        ################################################################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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

        
        ###########################################################################################################
        # CADASTRO -> PLANO DE CONTAS, CUSTOS E FINCEIRO -> PLANO DE CONTAS - ACERTO DE CÓD. REDUZIDOS DUPLICADOS #
        ###########################################################################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
        self.click()
        if not self.find( "cont_plano_de_contas_custos_men", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_custos_men")
        self.click()
        self.wait(1000)

        # este tela é igual ao manutenção de contas, nao  mexer por enquanto
        if not self.find( "cont_cad_plano_cus_plan_conta", matching=0.97, waiting_time=10000):
            not_found("cont_cad_plano_cus_plan_conta")
        self.click()



        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        
        ####################################################################
        ###################### CADASTROS -> HISTORICOS #####################
        ####################################################################
        self.wait(8000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        #    not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        
        self.wait(3000)
        
        ###################################
        #CADASTROS -> DEMONSTRATIVOS -> DRE
        ###################################
        self.wait(3000)

        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_grupo_de_empresa_dre_rel", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_dre_rel")
        self.click_relative(52, 32)
        if not self.find( "cont_locali_plano_contas_23", matching=0.97, waiting_time=10000):
            not_found("cont_locali_plano_contas_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        
        self.wait(1000)
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_24_opcao_nova", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_24_opcao_nova")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        if not self.find( "cont_excluir_24_opcao_nova", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_24_opcao_nova")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retornar_cad_client_forn_2", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cad_client_forn_2")
        self.click()
        
        ##################################################################################################
        ################################# MENU -> CADASTROS -> IMPOSTOS ##################################
        ##################################################################################################

        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_impostos_24_opc_menu", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impostos_24_opc_menu")
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

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_cfop_final_rel_busc", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_final_rel_busc")
        self.click_relative(66, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        
        ################################################################################################
        ############################## CADASTROS -> IMPOSTO PRESUMIDO ##################################
        ################################################################################################
        
        
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tabelas_menu_opcao", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_menu_opcao")
        self.click()
        if not self.find( "cont_tabelas_darf_gr", matching=0.97, waiting_time=10000):
            not_found("cont_tabelas_darf_gr")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_24_opcao_nova", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_24_opcao_nova")
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


        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        
        #####################################################################################################################
        ########################################CADASTROS -> ITENS DE ESTOQUE -> ITENS #######################################
        #####################################################################################################################

        self.wait(3000)

        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000) # botao ja esta em cima de salvar, apenas clicar
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_fornecedor_busc_rel_itens", matching=0.97, waiting_time=10000):
            not_found("cont_fornecedor_busc_rel_itens")
        self.click_relative(59, 21)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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

        
        ###################################################################################################
        ###################################### CADASTROS -> SERVIÇOS ######################################
        ###################################################################################################
        
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()

        if not self.find( "cont_servicos_agrupamento_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_agrupamento_rel_btn")
        self.click_relative(58, 96)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_grupo_fiscal_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_grupo_fiscal_rel_btn")
        self.click_relative(54, 27)
        self.wait(2000)
        self.type_keys_with_interval(100,"006")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.wait(2000)
        if not self.find( "cont_btn_sub_grupo_opc_2407_relativo", matching=0.97, waiting_time=10000):
            not_found("cont_btn_sub_grupo_opc_2407_relativo")
        self.click_relative(53, 24)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_familia_2407_relativo", matching=0.97, waiting_time=10000):
            not_found("cont_btn_familia_2407_relativo")
        self.click_relative(54, 24)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_servicos_marca_rel_btn", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_marca_rel_btn")
        self.click_relative(55, 30)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        self.wait(3000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        
        if not self.find( "cont_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_cardex")
        self.click()
        self.wait(1000)
        
        self.wait(3000)
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
        
        self.wait(3000)
        if not self.find( "cont_btn_lupa_precos_24_07", matching=0.97, waiting_time=10000):
            not_found("cont_btn_lupa_precos_24_07")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        
        ###############################################################################################
        ################################# CADASTROS -> LIVROS OFICIAIS  ###############################
        ###############################################################################################
        
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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

        ########################################################################################
        ######################## CADASTROS -> PROCESSOS ADMINISTRATIVOS ########################
        ########################################################################################

        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        ##################################################################################
        ################ CADASTROS -> DOCUMENTAÇOES -> TIPOS DE DOCUMENTO ################
        ##################################################################################
        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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

        ################################################################################################
        ############################# CADASTROS -> DOCUMENTAÇOES -> DOCUMENTOS #########################
        ################################################################################################
        

        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
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

        ##################################################################################################
        ###################### CADASTROS -> DOCUMENTEÇOS -> DOCUMENTOS REFERENCIADOS #####################
        ##################################################################################################

        self.wait(3000)
        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
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
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
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
        
        ##########################################################################################
        ##########################################################################################
        ################################ COMEÇO DE MOVIMENTOS ####################################
        ##########################################################################################
        ##########################################################################################
        
        self.wait(3000)
        
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        if not self.find( "cont_movimento_fiscal_f6_rel", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_fiscal_f6_rel")
        self.click_relative(50, -16)
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_data_movimento_opc_3_rel", matching=0.97, waiting_time=10000):
            not_found("cont_data_movimento_opc_3_rel")
        self.click_relative(30, 7)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        if not self.find( "cont_cliente_fornecedor_movimentos_rel", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_fornecedor_movimentos_rel")
        self.click()
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_notas_fiscais_normal_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_notas_fiscais_normal_movimentos")
        self.click()
        self.type_down()
        self.type_down()
        self.type_down()
        if not self.find( "cont_movimentos_periodo_rel_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_periodo_rel_emissao")
        self.click_relative(21, 24)
        self.wait(1000)
        self.type_right()
        self.type_right()
        
        # Incluir -> Movimentação fiscal
        self.wait(2000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.tab()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.wait(1000)           
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        if not self.find( "cont_achar_operacao_bsc_movi_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_achar_operacao_bsc_movi_fisc")
        self.click_relative(60, 21)
        if not self.find( "cont_mov_fisc_localiza_operacao", matching=0.97, waiting_time=10000):
            not_found("cont_mov_fisc_localiza_operacao")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.wait(3000)
        if not self.find( "cont_mov_fiscal_cliente_forn_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_mov_fiscal_cliente_forn_bsc")
        self.click_relative(202, 21)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(8000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_mov_fiscal_cfop_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_mov_fiscal_cfop_bsc")
        self.click_relative(62, 23)
        if not self.find( "cont_localizar_cod_fisc_f10_mov", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_cod_fisc_f10_mov")
        self.click()
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_centro_de_custos_bsc_mov_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custos_bsc_mov_fisc")
        self.click_relative(91, 23)
        if not self.find( "cont_mov_fisc_locali_centro_custo_f10", matching=0.97, waiting_time=10000):
            not_found("cont_mov_fisc_locali_centro_custo_f10")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.tab()
        self.tab()
        x = 0
        while x < 3:
            self.space()
            self.space()
            self.tab()
            x += 1
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1

        if not self.find( "cont_desdobramentos_rel_tipo_imposto_24", matching=0.97, waiting_time=10000):
            not_found("cont_desdobramentos_rel_tipo_imposto_24")
        self.click_relative(35, 46)
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        self.tab()
        if not self.find( "cont_operacao_desdobramento_24", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_desdobramento_24")
        self.click_relative(117, 22)
        self.wait(1000)
        self.type_down()
        self.enter()

        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        #if not self.find( "cont_lixeira_opc_23_sma", matching=0.97, waiting_time=10000):
        #    not_found("cont_lixeira_opc_23_sma")
        #self.click()
        #self.wait(1000)
        #self.enter()
        if not self.find( "cont_contabilizacao_mov_fisc_btn", matching=0.97, waiting_time=10000):
            not_found("cont_contabilizacao_mov_fisc_btn")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.tab()
        self.wait(1000)
        #if not self.find( "cont_lixeira_opc_23_sma", matching=0.97, waiting_time=10000):
        #    not_found("cont_lixeira_opc_23_sma")
        #self.click()
        #self.wait(1000)
        #self.enter()
        if not self.find( "cont_movimento_itens_servico_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_itens_servico_fiscal")
        self.click()
        # possivel erro de clicar em botao incluir no topo
        #

        if not self.find( "cont_botao_incluir_movimentos_ciap", matching=0.97, waiting_time=10000):
            not_found("cont_botao_incluir_movimentos_ciap")
        self.click()
        self.wait(1000)
        if not self.find( "cont_bens_btn_loc_fornecedor", matching=0.97, waiting_time=10000):
            not_found("cont_bens_btn_loc_fornecedor")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"116830")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(4000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_cfop_imposto_movimento_3", matching=0.97, waiting_time=10000):
            not_found("cont_btn_cfop_imposto_movimento_3")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.tab()
        self.wait(1000)
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
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
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()

        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
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
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
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
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_documentos_referenciados_mov_fisc_23", matching=0.97, waiting_time=10000):
            not_found("cont_documentos_referenciados_mov_fisc_23")
        self.click()
        if not self.find( "cont_incluir_movimentos_itens_fisc23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_movimentos_itens_fisc23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_emissao_doc_referenciado_fnd", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_doc_referenciado_fnd")
        self.click()
        self.wait(1000)
        self.type_down()
        self.type_up()
        self.type_up()
        self.wait(2000)
        if not self.find( "cont_botao_data_documentos_rel", matching=0.97, waiting_time=10000):
            not_found("cont_botao_data_documentos_rel")
        self.click_relative(29, 8)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_down()
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.type_down()
        self.type_down()
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"123")
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
        if not self.find( "cont_documento_referenciado_23_rel_2", matching=0.97, waiting_time=10000):
            not_found("cont_documento_referenciado_23_rel_2")
        self.click_relative(24, 45)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_dmed_beneficiarios_mov", matching=0.97, waiting_time=10000):
            not_found("cont_dmed_beneficiarios_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        self.wait(1000)
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        if not self.find( "cont_rel_mov_beneficiario_dependente", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_beneficiario_dependente")
        self.click_relative(197, 6)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_rel_mov_empresa_reembolso", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_empresa_reembolso")
        self.click_relative(175, 4)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_valor_rel_mov_23", matching=0.97, waiting_time=10000):
            not_found("cont_achar_valor_rel_mov_23")
        self.click_relative(50, 6)
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_cancelar_referencias_itens", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_referencias_itens")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        #self.enter()
        #self.wait(1000)
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.wait(2000)
        self.tab()
        self.wait(1000)
        self.backspace()
        self.tab()
        self.wait(2000)
        #MOUSE ESTA PARANDO EM CIMA DE LOCALIZAR
        #if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
        #    not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_24_opcao", matching=0.97, waiting_time=10000):
            not_found("cont_editar_24_opcao")
        self.click()
        if not self.find( "cont_btn_excluir_opcao_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_opcao_24")
        self.click()
        self.wait(1000)
        self.enter()
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
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        
        
        #####################################################################################
        ############################ MOVIMENTOS -> CONTABIL F7 ##############################
        #####################################################################################
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        if not self.find( "cont_contabil_f7_movimentos_23", matching=0.97, waiting_time=10000):
            not_found("cont_contabil_f7_movimentos_23")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_data_achar_rel_cont_f7", matching=0.97, waiting_time=10000):
            not_found("cont_data_achar_rel_cont_f7")
        self.click_relative(29, 8)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        # na primeira vez ele da a opcao de criar o lote, depois que ja criado nao tem mais esta opcao
        #self.enter()
        #self.wait(1000)
        #self.type_keys_with_interval(100,"qa12!@")
        #self.tab()
        #self.type_keys_with_interval(100,"123")
        #self.tab()
        #self.type_keys_with_interval(100,"123")
        #self.tab()
        #self.type_keys_with_interval(100,"123")
        #self.wait(1000)
        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        #self.click()
        #self.wait(1000)
        #if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
        #    not_found("cont_retorn_opc_23_imposto")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_conta_debito_bsc_rel_1", matching=0.97, waiting_time=10000):
            not_found("cont_conta_debito_bsc_rel_1")
        self.click_relative(154, 4)
        self.wait(1000)
        self.type_keys_with_interval(100,"1.1.02.01.0001")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        #
        #

        if not self.find( "cont_debito_rel_centro_custo_1", matching=0.97, waiting_time=10000):
            not_found("cont_debito_rel_centro_custo_1")
        self.click_relative(161, 39)
        # aqui nao tem nenhum item para selecionar, apenas voltar com esc
        self.wait(2000)
        self.key_esc()
        self.wait(1000)
        if not self.find( "cont_historico_rel_btn_1_deb", matching=0.97, waiting_time=10000):
            not_found("cont_historico_rel_btn_1_deb")
        self.click_relative(163, 67)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_conta_credito_f7_rel_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_conta_credito_f7_rel_bsc")
        self.click_relative(153, 4)
        self.wait(1000)
        self.type_keys_with_interval(100,"1.1.02.01.0001")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_credito_centro_de_custo_rel_2", matching=0.97, waiting_time=10000):
            not_found("cont_credito_centro_de_custo_rel_2")
        self.click_relative(164, 39)
        # aqui nao tem nenhum item para selecionar, apenas voltar com esc
        self.wait(2000)
        self.key_esc()
        self.wait(2000)
        if not self.find( "cont_credito_mov_contabil_f7_hist", matching=0.97, waiting_time=10000):
            not_found("cont_credito_mov_contabil_f7_hist")
        self.click_relative(160, 64)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        self.tab()
        self.wait(1000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_salvar_mov_btn_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_mov_btn_opc_8")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        self.click()
        
        #####################################################################################################
        ################################ MOVIMENTOS -> LOTES  ###############################################
        #####################################################################################################

        self.wait(1000)

        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_lotes_menu_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_lotes_menu_movimentos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"112")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.tab()
        self.type_keys_with_interval(100,"12032023")
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_2_26_02", matching=0.97, waiting_time=10000):
            not_found("cont_editar_2_26_02")
        self.click()
        self.wait(1000)
        if not self.find( "cont_bot_excluir_opc_3_mov_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_bot_excluir_opc_3_mov_lotes")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        self.click()
        
        # MOVIMENTOS -> GERAÇÃO CONTABIL
        #
        # 
        self.wait(3000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_mov_geracao_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_menu_mov_geracao_contabil")
        self.click()
        if not self.find( "cont_encontrar_data_mov_ger_cont", matching=0.97, waiting_time=10000):
            not_found("cont_encontrar_data_mov_ger_cont")
        self.click_relative(33, 7)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        self.tab()
        x = 0
        while x < 8:
            self.type_down()
            x += 1
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_right()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_contabilizacao_mov_ger_cont", matching=0.97, waiting_time=10000):
            not_found("cont_contabilizacao_mov_ger_cont")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        #########################################################################################################
        ########################### MOVIMENTOS -> INVENTARIO ####################################################
        #########################################################################################################
        

        
        self.wait(3000)
        
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()

        self.wait(1000)
        if not self.find( "cont_inventario_menu_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_inventario_menu_movimentos")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_up()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        x = 0
        while x < 5:
            self.type_up()
            x += 1
        self.tab()
        self.wait(1000)
        self.type_down()
        self.type_up()
        self.wait(1000)
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        x = 0
        while x < 3:
            self.type_up()
            x += 1
        self.tab()
        self.wait(1000)
        if not self.find( "cont_mov_codigo_cliente_forn_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_mov_codigo_cliente_forn_bsc")
        self.click_relative(72, 27)
        self.wait(1000)
        self.type_keys_with_interval(100,"0082955")

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimentos_operacao_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_operacao_entrada")
        self.click_relative(69, 26)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_operacao_saida_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_saida_movimentos")
        self.click_relative(71, 30)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_local_de_estoque_movimentos_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_local_de_estoque_movimentos_bsc")
        self.click_relative(68, 24)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_2_movt_dos_itens_mov_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_2_movt_dos_itens_mov_inventario")
        self.click()
        self.wait(2000)
        if not self.find( "cont_5_itens_botao_incluir_opc_3", matching=0.97, waiting_time=10000):
            not_found("cont_5_itens_botao_incluir_opc_3")
        self.click()
        self.wait(2000)
        if not self.find( "cont_rel_f2_itens_bsc_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_rel_f2_itens_bsc_inventario")
        self.click_relative(9, 36)
        self.wait(1000)
        self.type_keys_with_interval(100,"107026")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_confirmar_inventario_itens", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_inventario_itens")
        self.click()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_6_itens_bloco_k_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_6_itens_bloco_k_inventario")
        self.click()
        if not self.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        self.click()

        self.wait(1000)
        if not self.find( "cont_rel_f2_itens_bsc_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_rel_f2_itens_bsc_inventario")
        self.click_relative(9, 36)
        self.wait(1000)
        self.type_keys_with_interval(100,"107026")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_cliente_fornecedor_rel_f2_item", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_fornecedor_rel_f2_item")
        self.click_relative(66, 25)
        self.wait(2000)
        self.type_keys_with_interval(100,"0082955")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_confirmar_inventario_itens", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_inventario_itens")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_mov_inventario_7_contagem", matching=0.97, waiting_time=10000):
            not_found("cont_mov_inventario_7_contagem")
        self.click()
        if not self.find( "cont_mov_inventario_a_lancamento", matching=0.97, waiting_time=10000):
            not_found("cont_mov_inventario_a_lancamento")
        self.click_relative(95, 46)
        self.type_keys_with_interval(100,"107026")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.wait(1000)
        if not self.find( "cont_data_acumulativa_7_contagem", matching=0.97, waiting_time=10000):
            not_found("cont_data_acumulativa_7_contagem")
        self.click()
        self.wait(1000)
        self.type_down()
        self.space()
        self.type_down()
        self.space()
        if not self.find( "cont_8_geracao_do_espelho_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_8_geracao_do_espelho_inventario")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_data_8_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_botao_data_8_geracao_rel")
        self.click_relative(30, 10)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        #deixa data vazia
        self.tab()
        x = 0
        while x < 3:
            self.space()
            self.space()
            self.tab()
            x += 1
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.tab()
        self.type_right()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_inventario_gerar_movimento_mov", matching=0.97, waiting_time=10000):
            not_found("cont_inventario_gerar_movimento_mov")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(15000)
        self.enter()
        self.wait(7000)
        if not self.find( "cont_3_registros_inventario_mov", matching=0.97, waiting_time=10000):
            not_found("cont_3_registros_inventario_mov")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_down()
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1

        self.tab()
        self.space()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        x = 0
        while x < 5:
            self.type_right()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_right()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_right()
            x += 1
        self.tab()
        x = 0
        while x < 5:
            self.type_right()
            x += 1
        self.tab()
        if not self.find( "cont_4_coletor_de_dados_inventorio_mov", matching=0.97, waiting_time=10000):
            not_found("cont_4_coletor_de_dados_inventorio_mov")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        self.wait(3000)
        
        if not self.find( "cont_mov_btn_data_rel_achar_qa_12", matching=0.97, waiting_time=10000):
            not_found("cont_mov_btn_data_rel_achar_qa_12")
        self.click_relative(27, 7)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)



        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_achar_qa12_btn_mov_inventario", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_btn_mov_inventario")
        self.click()
        self.wait(2000)
        if not self.find( "cont_editar_botao_24", matching=0.97, waiting_time=10000):
            not_found("cont_editar_botao_24")
        self.click()
        
        self.wait(3000)
        if not self.find( "cont_btn_excluir_24_opc", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_24_opc")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.type_keys_with_interval(100,"1811")
        self.wait(1000)
        self.enter()
        self.wait(2000)
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
        self.wait(2000)
        
        ##############################################################################################
        ############################# MOVIMENTOS -> REDUÇÕES Z #######################################
        ##############################################################################################
        
        self.wait(3000)
        
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_mov_reducoes_z", matching=0.97, waiting_time=10000):
            not_found("cont_menu_mov_reducoes_z")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_achar_data_mov_reducoes_z", matching=0.97, waiting_time=10000):
            not_found("cont_achar_data_mov_reducoes_z")
        self.click_relative(31, 9)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
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
        self.space()
        self.tab()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"12:30")
        self.tab()
        self.space()
        self.tab()
        self.type_right()
        if not self.find( "cont_mov_reducoesz_empresa_rel", matching=0.97, waiting_time=10000):
            not_found("cont_mov_reducoesz_empresa_rel")
        self.click_relative(51, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.tab()
        #32 no total
        #6 antes do 492
        x = 0
        while x < 6: 
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.type_keys_with_interval(100,"492")
        self.tab()
        x = 0
        while x < 25: 
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0
        while x < 8:
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0
        while x < 2:
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.space()
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_mov_reducoes_z_3_itens", matching=0.97, waiting_time=10000):
            not_found("cont_mov_reducoes_z_3_itens")
        self.click()
        self.wait(100)
        self.click()
        self.wait(100)
        self.click()
        # 3 cliques para confirmar, pois ao apertar apenas uma vez nem sempre vai 
        self.wait(2000)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()

        # mensagem aparece "Esta movimentação é apenas para Modulo Contabil"
        # Aqui vai o codigo ao aparecer item
        # explicação = Não é mais usado este metodo Reduções Z, apenas ignorar
        #
        self.wait(1000)
        self.enter()

        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        #self.click()
        #self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(2000)
        # mouse esta parando em cima de exclusao

        if not self.find( "cont_excluir_botao_reducoesz_2", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_botao_reducoesz_2")
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


        # MOVIMENTOS -> INTEGRAÇOES -> 
        #
        #
        #

        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_integracoes_menu_movimentos_23", matching=0.97, waiting_time=10000):
            not_found("cont_integracoes_menu_movimentos_23")
        self.click()
        self.wait(2000)
        x = 0
        while x < 6:
            self.type_right()
            x += 1
        
        if not self.find( "cont_relativo_data_movimentos_integracao_1", matching=0.97, waiting_time=10000):
            not_found("cont_relativo_data_movimentos_integracao_1")
        self.click_relative(221, -47) # data 1
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)
        if not self.find( "cont_rel_data_movimento_integracao_2", matching=0.97, waiting_time=10000):
            not_found("cont_rel_data_movimento_integracao_2")
        self.click_relative(460, -45) # data 2 
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_contabilizacao_integracao_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_contabilizacao_integracao_movimentos")
        self.click()
        self.wait(20000)
        self.enter()
        
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        #######################################################################################################
        ##################################    MOVIMENTOS -> INF. EXTRAS ->   ##################################
        #######################################################################################################
        #
        #
        self.wait(3000)

        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_inf_extras_gia_movimentos_menu", matching=0.97, waiting_time=10000):
            not_found("cont_inf_extras_gia_movimentos_menu")
        self.click()
        self.wait(2000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 12:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"2024")
        x= 0 
        while x < 9:
            self.type_down()
            x += 1
        self.tab()
        self.tab()
        x = 0 
        while x < 5:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_codigo_ajuste_inf_extras", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_ajuste_inf_extras")
        self.click_relative(152, 6)
        self.wait(500)
        self.type_down()
        self.enter()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 20:
            self.type_down()
            x+= 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(500)
        if not self.find( "cont_confirma_inf_extras_mov_2", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_inf_extras_mov_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_mov_info_adicionais_inf_extras", matching=0.97, waiting_time=10000):
            not_found("cont_mov_info_adicionais_inf_extras")
        self.click()
        self.wait(500)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.wait(500)
        if not self.find( "cont_confirma_inf_extras_mov_2", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_inf_extras_mov_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_obrigacoes_recolher_mov_inf_extras", matching=0.97, waiting_time=10000):
            not_found("cont_obrigacoes_recolher_mov_inf_extras")
        self.click()
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(500)
        if not self.find( "cont_confirma_inf_extras_mov_2", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_inf_extras_mov_2")
        self.click()
        self.wait(2000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_edit_opc_2_ver_26", matching=0.97, waiting_time=10000):
            not_found("cont_botao_edit_opc_2_ver_26")
        self.click()
        if not self.find( "cont_excluir_movimentos_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_movimentos_apuracao_imp")
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
        
        
        ##################################################################################################
        ################################### MOVIMENTOS -> FECHAMENTOS CONTABEIS  #########################
        ##################################################################################################
        
        self.wait(3000)

        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_mov_fechamentos_contabeis", matching=0.97, waiting_time=10000):
            not_found("cont_menu_mov_fechamentos_contabeis")
        self.click()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_mov_conta_resultado_fechamento", matching=0.97, waiting_time=10000):
            not_found("cont_mov_conta_resultado_fechamento")
        self.click_relative(220, 4)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()

        if not self.find( "cont_conta_lucro_mov_f12", matching=0.97, waiting_time=10000):
            not_found("cont_conta_lucro_mov_f12")
        self.click_relative(195, 7)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_up()
            x += 1
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()

        if not self.find( "cont_conta_prejuizo_f12_mov", matching=0.97, waiting_time=10000):
            not_found("cont_conta_prejuizo_f12_mov")
        self.click_relative(208, 6)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_grupo_de_empresa_rel_mov", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_rel_mov")
        self.click_relative(142, 6)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
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
        if not self.find( "cont_botao_edit_opc_2_ver_26", matching=0.97, waiting_time=10000):
            not_found("cont_botao_edit_opc_2_ver_26")
        self.click()
        # mouse para em cima, entao apenas clicar
        #if not self.find( "cont_excluir_movimentos_apuracao_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_excluir_movimentos_apuracao_imp")
        #self.click()
        self.wait(1000)
        self.click()
        self.wait(800)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        
        # MOVIMENTOS -> REGISTROS MENSAIS EFD -> REGISTRO 2050
        #
        #
        #

        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_registros_mensais_efd_menu", matching=0.97, waiting_time=10000):
            not_found("cont_registros_mensais_efd_menu")
        self.click()
        if not self.find( "cont_registros_2050_mensais", matching=0.97, waiting_time=10000):
            not_found("cont_registros_2050_mensais")
        self.click()

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"012024")
        self.tab()
        self.tab()
        x = 0
        while x < 13:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_cancelar_bot_itens_23", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_bot_itens_23")
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
        if not self.find( "cont_botao_edit_opc_2_ver_26", matching=0.97, waiting_time=10000):
            not_found("cont_botao_edit_opc_2_ver_26")
        self.click()
        #mouse em cima 
        #if not self.find( "cont_excluir_movimentos_apuracao_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_excluir_movimentos_apuracao_imp")
        #self.click()
        self.wait(1000)
        self.wait(800)
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
        
        # MOVIMENTOS -> REGISTROS MENSAIS EFD -> REGISTRO 2060
        #
        #
        #
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_registros_mensais_efd_menu", matching=0.97, waiting_time=10000):
            not_found("cont_registros_mensais_efd_menu")
        self.click()
        self.wait(500)
        if not self.find( "cont_registro_2060_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_registro_2060_mov_contabil")
        self.click()
        self.wait(1000)
        self.backspace()

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"012024")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        self.click()
        
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_confirma_botao_claro_verde", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_botao_claro_verde")
        self.click()
        self.wait(1000)

        if not self.find( "cont_2060_ajustes_contribuicao_apu_mov", matching=0.97, waiting_time=10000):
            not_found("cont_2060_ajustes_contribuicao_apu_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        self.click()
        x = 0
        while x < 4:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_tipo_ajuste_movimento_reducao", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_ajuste_movimento_reducao")
        self.click()
        self.wait(700)
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_confirma_botao_claro_verde", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_botao_claro_verde")
        self.click()
        self.wait(1000)


        if not self.find( "cont_supensao_processos_2060_mov", matching=0.97, waiting_time=10000):
            not_found("cont_supensao_processos_2060_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        self.click()
        self.wait(1000)
        if not self.find( "cont_buscar_processos_2060_mov", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_processos_2060_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(1000)
        
        
        self.wait(300)
        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        # CANCELAR A INCLUSAO, POIS SEM INFORMAR O PROCESSO VAI DAR UM ERRO
        if not self.find( "cont_movimento_2060_efc_concluir", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_2060_efc_concluir")
        self.click()
        self.wait(2000)
        if not self.find( "cont_excluir_opcao_2060_mov", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_opcao_2060_mov")
        self.click()
        self.wait(300)
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
        
        ##############################################################################################
        ############################### MOVIMENTOS -> Movimento CIAP #################################
        ##############################################################################################
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_ciap_menu", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_ciap_menu")
        self.click()
        if not self.find( "cont_achar_ciap_escolher_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_achar_ciap_escolher_imposto")
        self.click_relative(49, 22)
        self.wait(300)
        self.type_down()
        self.enter()
        self.wait(1000)

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        # BOTAO CIAP NAO MUDA TIPO DE PROCESSO
        self.tab()
        x = 0 
        while x < 7:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_incluir_movimentos_ciap", matching=0.97, waiting_time=10000):
            not_found("cont_botao_incluir_movimentos_ciap")
        self.click()
        if not self.find( "cont_botao_ciap_bens_buscar_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_botao_ciap_bens_buscar_movimentos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.backspace()
        self.tab()
        self.tab()
        self.type_down()
        self.enter()
        # CODIGO ACIMA É PARA PREENCHER O CAMPO MANUALMENTE JA QUE A LUPA ESTA COM PROBLEMAS
        # aqui vou apagar o 000002 pois nao estou conseguindo incluir pela lupa
        # Erro documentado 12/01
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 10:
            self.type_down()
            x += 1

        self.tab()
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        # cancelar pois sem o BEM não é possivel incluir, e não estou conseguindo fazer o Bem aparecer
        # CONSEGUI CADASTRAR O BEM, NAO PRECISA CANCELAR 12/01
        if not self.find( "cont_cancelar_referencias_itens", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_referencias_itens")
        self.click()
        #if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_confirma_incluir_cod_fisc_imp")
        #self.click()
        
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_edit_opc_2_ver_26", matching=0.97, waiting_time=10000):
            not_found("cont_botao_edit_opc_2_ver_26")
        self.click()
        if not self.find( "cont_excluir_ciap_movimentos", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_ciap_movimentos")
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
        
        ###########################################################################################
        ###################### MOVIMENTOS -> Movimento Fiscal - Inutilizadas ######################
        ###########################################################################################
        
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_fiscal_inutilizadas_menu", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_fiscal_inutilizadas_menu")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"01012024")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_data_mov_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_botao_data_mov_fiscal")
        self.click_relative(29, 11)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(500)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        if not self.find( "cont_excluir_opcao_2060_mov", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_opcao_2060_mov")
        self.click()
        self.wait(500)
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
        self.wait(1000)
        
        ###########################################################################################
        ################### MOVIMENTOS -> Movimento Documentos (Fiscal) ###########################
        ###########################################################################################

        ### ESTA PARTE NAO ESTA COMPLETA ###
        ### RETORNAR DEPOIS ###
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_documentos_fiscal_menu", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_documentos_fiscal_menu")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        x = 0
        while x < 15:
            self.type_up()
            x += 1
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        x = 0
        while x < 15:
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        if not self.find( "cont_codigo_de_operacao_dados_doc", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_de_operacao_dados_doc")
        self.click_relative(57, 23)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        
        self.wait(2000)

        if not self.find( "cont_cfop_dados_de_doc_mov", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_dados_de_doc_mov")
        self.click_relative(61, 26)
        self.wait(1000)
        self.backspace()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(500)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        if not self.find( "cont_cond_de_pagamento_mov_rel", matching=0.97, waiting_time=10000):
            not_found("cont_cond_de_pagamento_mov_rel")
        self.click_relative(51, 24)
        self.wait(500)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(500)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(2000)
      
        if not self.find( "cont_cliente_rel_mov_movi_de_itens", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_rel_mov_movi_de_itens")
        self.click_relative(200, 44)
        self.wait(2000)
        self.type_keys_with_interval(100,"0089720")
        
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_vendedor_mov_movi_itens", matching=0.97, waiting_time=10000):
            not_found("cont_rel_vendedor_mov_movi_itens")
        self.click_relative(58, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rota_mov_rel_busc_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_rota_mov_rel_busc_documentos")
        self.click_relative(56, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        x = 0
        while x < 10: 
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 5: 
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_centro_de_custo_mov_rel_doc", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custo_mov_rel_doc")
        self.click_relative(87, 28)
        self.wait(2000)
        #if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
        #    not_found("cont_opcao_loc_imp_23")
        #self.click()
        #self.wait(2000)
        #if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
        #    not_found("cont_botao_selec_tela_maior_2")
        #self.click()
        #self.wait(1000)
        
        # OS BOTOES DE LOCALIZAR E SELECIONAR NAO ESTAO FUNCIONANDO POIS NAO TEM DADO NENHUM AQUI, APENAS RETORNAR

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        # tab para a tela descer
        self.tab()
        self.tab()
        self.tab()

        if not self.find( "cont_transportador_movimento_documentos_busc", matching=0.97, waiting_time=10000):
            not_found("cont_transportador_movimento_documentos_busc")
        self.click_relative(61, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        self.tab()
        self.tab()
        # tipo de frete
        x = 0
        while x < 5:
            self.type_down()
            x += 1
        self.tab()
        if not self.find( "cont_municipio_coleta_sped_rel_mov", matching=0.97, waiting_time=10000):
            not_found("cont_municipio_coleta_sped_rel_mov")
        self.click_relative(51, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_municipio_entrega_sped_rel_mov", matching=0.97, waiting_time=10000):
            not_found("cont_municipio_entrega_sped_rel_mov")
        self.click_relative(58, 27)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        if not self.find( "cont_classificacao_rel_busc_mov_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_rel_busc_mov_documentos")
        self.click_relative(54, 28)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"qa12!@2")
        self.tab()
        x = 0
        while x < 16:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        if not self.find( "cont_5_retencoes_mov_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_5_retencoes_mov_documentos")
        self.click()
        x = 0
        while x < 12:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        if not self.find( "cont_6_impostos_mov_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_6_impostos_mov_documentos")
        self.click()
        x = 0
        while x < 14:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        #########################################################################################
        ################################# movimento de itens 2 ##################################
        #########################################################################################
        
        self.wait(3000)
        if not self.find( "cont_2_movto_dos_itens_documentos_mov", matching=0.97, waiting_time=10000):
            not_found("cont_2_movto_dos_itens_documentos_mov")
        self.click()
        self.wait(500)
        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        if not self.find( "cont_mov_f2_itens_rel_busc", matching=0.97, waiting_time=10000):
            not_found("cont_mov_f2_itens_rel_busc")
        self.click_relative(8, 38)
        self.wait(2000)
        self.type_keys_with_interval(100,"114380")
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.tab()
        if not self.find( "cont_relativo_centro_de_custos_item_23", matching=0.97, waiting_time=10000):
            not_found("cont_relativo_centro_de_custos_item_23")
        self.click_relative(88, 30)
        self.wait(500)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_mov_relat_classificacao_item", matching=0.97, waiting_time=10000):
            not_found("cont_mov_relat_classificacao_item")
        self.click_relative(54, 27)
        self.wait(500)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_confirmar_mov_item_v", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_mov_item_v")
        self.click()
        self.wait(2000)
        self.enter() # aparecendo mensagem de erro
        self.wait(2000)
        
        # antes aparecia uma janela, que nao esta aparecendo mais, por enquanto pular, a tela aparece 
        # apenas para itens especificos
        
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        #if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            #not_found("cont_retorn_opc_23_imposto")
        #MOUSE JA ESTA EM CIMA DE RETORNAR, APENAS CLICAR NOVAMENTE
        

        self.click()
        self.wait(2000)

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()

        self.wait(1000)
        self.enter()


        self.wait(2000)
        if not self.find( "cont_3_opcao_servicos_mov_item", matching=0.97, waiting_time=10000):
            not_found("cont_3_opcao_servicos_mov_item")
        self.click()

        if not self.find( "cont_servico_rel_busc_3_serv_mov", matching=0.97, waiting_time=10000):
            not_found("cont_servico_rel_busc_3_serv_mov")
        self.click_relative(65, 24)

        if not self.find( "cont_cadastro_de_servico_f10", matching=0.97, waiting_time=10000):
            not_found("cont_cadastro_de_servico_f10")
        self.click()

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.tab()
        self.wait(300)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"12:30")
        self.tab()
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
        self.tab()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
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
        if not self.find( "cont_unidade_mov_cad_servico", matching=0.97, waiting_time=10000):
            not_found("cont_unidade_mov_cad_servico")
        self.click_relative(55, 27)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        self.type_down()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()

        if not self.find( "cont_grupo_fiscal_cad_servico_rel", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_cad_servico_rel")
        self.click_relative(49, 30)
        self.wait(3000)
        self.type_keys_with_interval(100,"006")
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_familia_btn_movimentos_rel_servicos_2407", matching=0.97, waiting_time=10000):
            not_found("cont_familia_btn_movimentos_rel_servicos_2407")
        self.click_relative(54, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        if not self.find( "cont_agrupamento_mov_rel_grupo_", matching=0.97, waiting_time=10000):
            not_found("cont_agrupamento_mov_rel_grupo_")
        self.click_relative(55, 94)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        
        self.wait(2000)
        if not self.find( "cont_achar_sub_grupo_rel_2407_serv", matching=0.97, waiting_time=10000):
            not_found("cont_achar_sub_grupo_rel_2407_serv")
        self.click_relative(54, 23)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        if not self.find( "cont_marca_rel_mov_cad_serv", matching=0.97, waiting_time=10000):
            not_found("cont_marca_rel_mov_cad_serv")
        self.click_relative(51, 29)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_plano_de_contas_rel_mov_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_plano_de_contas_rel_mov_cad_servicos")
        self.click_relative(55, 30)
        self.wait(1000)
        self.type_keys_with_interval(100,"00010")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_ncm_rel_busc_cad_servico", matching=0.97, waiting_time=10000):
            not_found("cont_ncm_rel_busc_cad_servico")
        self.click_relative(105, 28)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_centro_custo_rel_cad_servi", matching=0.97, waiting_time=10000):
            not_found("cont_centro_custo_rel_cad_servi")
        self.click_relative(82, 29)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.backspace()

        self.wait(1000)
        if not self.find( "cont_cardex_cadastro_servicos_mov", matching=0.97, waiting_time=10000):
            not_found("cont_cardex_cadastro_servicos_mov")
        self.click()
        
        # ESTA COM ERRO AO SELECIONAR A DATA, COMENTAR POR ENQUANTO
        self.wait(3000)
        if not self.find( "cont_serv_data_rel_btn_2407", matching=0.97, waiting_time=10000):
            not_found("cont_serv_data_rel_btn_2407")
        self.click_relative(28, 10)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        #if not self.find( "cont_consultar_cardex_cad_servicos", matching=0.97, waiting_time=10000):
        #    not_found("cont_consultar_cardex_cad_servicos")
        #self.click()
        if not self.find( "cont_precos_cad_servicos_mov", matching=0.97, waiting_time=10000):
            not_found("cont_precos_cad_servicos_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        self.click()
        self.wait(1000)
        self.backspace()
        if not self.find( "cont_buscar_tabela_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_tabela_cad_servicos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.backspace()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        
        if not self.find( "cont_gravar_servicos_preco", matching=0.97, waiting_time=10000):
            not_found("cont_gravar_servicos_preco")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_lixo_cad_servico_movimentos_exclusao", matching=0.97, waiting_time=10000):
            not_found("cont_lixo_cad_servico_movimentos_exclusao")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.enter()
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        self.click()
       
        self.wait(2000)

        if not self.find( "cont_servico_relativo_buscar_3_23", matching=0.97, waiting_time=10000):
            not_found("cont_servico_relativo_buscar_3_23")
        self.click_relative(65, 24)

        if not self.find( "cont_localizar_servicos_f10_busc", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_servicos_f10_busc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.space()

        # OPERAÇAO CONTABILIZAÇAO ESTA DESATIVADO

        if not self.find( "cont_centro_de_custo_rel_buscar_mov_itens", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custo_rel_buscar_mov_itens")
        self.click_relative(87, 28)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.enter()

        if not self.find( "cont_classificacao_rel_bsc_mov_itens", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_rel_bsc_mov_itens")
        self.click_relative(65, 26)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_gravar_v_opcao_23_mov_itens", matching=0.97, waiting_time=10000):
            not_found("cont_gravar_v_opcao_23_mov_itens")
        self.click()
        self.wait(3000)

        if not self.find( "cont_rel_movimento_descricao_f2", matching=0.97, waiting_time=10000):
            not_found("cont_rel_movimento_descricao_f2")
        self.click_relative(-22, 22)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_opc_24_04", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_opc_24_04")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_cfop_busc_relativo_item_23", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_busc_relativo_item_23")
        self.click_relative(60, 21)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecionar_opc_24_04", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_opc_24_04")
        self.click()
        self.wait(2000)

        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
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
        while x < 3:
            self.type_keys_with_interval(100,"1")
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
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
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
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        if not self.find( "cont_centro_de_custo_rel_bsc_servic", matching=0.97, waiting_time=10000):
            not_found("cont_centro_de_custo_rel_bsc_servic")
        self.click_relative(78, 23)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        # arquivo vazio, apenas apertar enter
        self.wait(2000)
        self.enter()
        if not self.find( "cont_classificacao_rel_bsc_servic", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_rel_bsc_servic")
        self.click_relative(52, 20)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)
        if not self.find( "cont_4_documentos_referenciados_mov", matching=0.97, waiting_time=10000):
            not_found("cont_4_documentos_referenciados_mov")
        self.click()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        
        self.wait(2000)
        # aqui esta dando um erro de não conseguir modificar os documentos referenciados 
        # ao mudar o MODELO o erro para de aparecer
        if not self.find( "cont_alterar_modelo_rel_nota_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_alterar_modelo_rel_nota_fiscal")
        self.click_relative(57, 22)
        self.wait(500)
        self.type_down()
        self.wait(200)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(1000)
        self.enter()

        if not self.find( "cont_3_servicos_voltar_nota_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_3_servicos_voltar_nota_fisc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_4_documentos_referenciados_dnv", matching=0.97, waiting_time=10000):
            not_found("cont_4_documentos_referenciados_dnv")
        self.click()   
        self.wait(1000)


        if not self.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_tipo_documento_mov_referenciados2", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_documento_mov_referenciados2")
        self.click_relative(48, 25)
        self.wait(1000)
        self.type_down()
        self.enter()
        if not self.find( "cont_data_botao_documentos_referenciados", matching=0.97, waiting_time=10000):
            not_found("cont_data_botao_documentos_referenciados")
        self.click_relative(28, 7)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)

        self.tab()
        self.tab()
        self.type_down()

        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(2000)
        self.type_down()
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        self.wait(1000)
        
        if not self.find( "cont_documentos_referenciados_rel_sel", matching=0.97, waiting_time=10000):
            not_found("cont_documentos_referenciados_rel_sel")
        self.click_relative(23, 47)

        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(1000)

        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()

        self.wait(1000)
        self.enter()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        self.wait(2000)

        if not self.find( "cont_mov_movi_itens_fiscal_data", matching=0.97, waiting_time=10000):
            not_found("cont_mov_movi_itens_fiscal_data")
        self.click_relative(25, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        self.wait(1000)

        if not self.find( "cont_botao_editar_opc_24_08", matching=0.97, waiting_time=10000):
            not_found("cont_botao_editar_opc_24_08")
        self.click()

        if not self.find( "cont_btn_excluir_opcao_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_opcao_24")
        self.click()
        self.wait(1000)
        self.enter()
        self.type_keys_with_interval(100,"1811")
        self.wait(1000)
        self.enter()
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
        self.wait(3000)
        
        # Voltar para apagar o serviço criado, para que nao acomule. NAO PODE ESTAR EM CAPS LOCK

        # if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
        #     not_found("cont_cadastros_menu_princ_opc_08")
        # self.click()
        # self.wait(1000)
        # if not self.find( "cont_menu_servicos_23", matching=0.97, waiting_time=10000):
        #     not_found("cont_menu_servicos_23")
        # self.click()
        # self.wait(2000)
        # self.backspace()
        # if not self.find( "teste_loc_serv", matching=0.97, waiting_time=10000):
        #     not_found("teste_loc_serv")
        # self.click()
        # if not self.find( "teste_achar_qa", matching=0.97, waiting_time=10000):
        #     not_found("teste_achar_qa")
        # self.click()
        # if not self.find( "teste_editar_qa", matching=0.97, waiting_time=10000):
        #     not_found("teste_editar_qa")
        # self.click()
        # if not self.find( "teste_excluir_qa", matching=0.97, waiting_time=10000):
        #      not_found("teste_excluir_qa")
        # self.click()
        # self.wait(1000)
        # self.enter()
        # if not self.find( "teste_retornar_qa", matching=0.97, waiting_time=10000):
        #     not_found("teste_retornar_qa")
        # self.click()
        # self.wait(1000)
        # if not self.find( "teste_loc_serv", matching=0.97, waiting_time=10000):
        #     not_found("teste_loc_serv")
        # self.click()
        # self.wait(1000)
        # if not self.find( "teste_retornar_qa", matching=0.97, waiting_time=10000):
        #     not_found("teste_retornar_qa")
        # self.click()
        # self.wait(1000)

        
        
        ###########################################################
        ###### MOVIMENTOS -> Movimento Conhecimento ( Fiscal ) ######
        ###########################################################
        
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_movimento_conhecimentos_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_menu_movimento_conhecimentos_fisc")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        # Mensagens que aparecem na tela sobre localizar, e que data não foi informada
        self.wait(1000)
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0 # Modelo
        while x < 3:
            self.type_down()
            x += 1
        x = 0
        while x < 3:
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        # Conhecimento
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
        self.type_up()
        self.tab()
        self.type_keys_with_interval(100,"11111111111111111111111111111111111111111111")
        # area de busca

        if not self.find( "cont_codigo_de_operacao_mov_transp_con", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_de_operacao_mov_transp_con")
        self.click_relative(58, 24)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_codigo_fiscal_cfop_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_fiscal_cfop_mov_transp")
        self.click_relative(64, 22)
        self.wait(1000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_remetente_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_remetente_rel_mov_transp")
        self.click_relative(61, 20)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_mov_destinatario_rel_clique_1", matching=0.97, waiting_time=10000):
            not_found("cont_mov_destinatario_rel_clique_1")
        self.click_relative(62, 66)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_pagador_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_pagador_rel_mov_transp")
        self.click_relative(57, 23)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_consignatario_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_consignatario_rel_mov_transp")
        self.click_relative(62, 24)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_motorista_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_motorista_rel_mov_transp")
        self.click_relative(62, 22)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_transportador_proprietario_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_transportador_proprietario_mov_transp")
        self.click_relative(62, 22)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_unidade_transp_mov_rel", matching=0.97, waiting_time=10000):
            not_found("cont_unidade_transp_mov_rel")
        self.click_relative(64, 25)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_municipio_entrega_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_municipio_entrega_rel_mov_transp")
        self.click_relative(67, 22)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)

        if not self.find( "cont_municipio_coleta_rel_transp_mov", matching=0.97, waiting_time=10000):
            not_found("cont_municipio_coleta_rel_transp_mov")
        self.click_relative(59, 24)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(2000)

        if not self.find( "cont_2_valores_mov_transportes_conhe", matching=0.97, waiting_time=10000):
            not_found("cont_2_valores_mov_transportes_conhe")
        self.click()
        self.wait(1000)
        if not self.find( "cont_grupo_fiscal_2_valores_rel_mov", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_2_valores_rel_mov")
        self.click_relative(60, 26)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(500)
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 4:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        
        #Tipo da tributaçao
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        #Situaçao tributaria 
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        x = 0
        while x < 15:
            self.type_up()
            x += 1
        self.tab()
        #MODALIDADE
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        x = 0
        while x < 3:
            self.type_up()
            x += 1
        self.tab()
        x = 0
        while x < 4:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1

        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.tab()

        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1

        x = 0
        while x < 5:
            self.type_down()
            x += 1

        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        
        x = 0
        while x < 5:
            self.type_down()
            x += 1

        self.tab()

        x = 0
        while x < 10:
            self.type_down()
            x += 1
        x = 0
        while x < 9:
            self.type_up()
            x += 1

        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        
        self.tab()
        x = 0 # Situacao Trib. PIS 
        while x < 20:
            self.type_down()
            x += 1
        self.tab()
        x = 0 # Situacao Trib. PIS 
        while x < 20:
            self.type_down()
            x += 1
        self.wait(1000)
        if not self.find( "cont_informacoes_responsavel_frete_mov", matching=0.97, waiting_time=10000):
            not_found("cont_informacoes_responsavel_frete_mov")
        self.click()
        # aqui acontece o erro de "Cannot focus on disabled windown"
        self.wait(2000)
        self.enter()
        self.wait(1000)
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.type_right() # Responsavel pela Carta Frete

        if not self.find( "cont_operacao_rel_bsc_frete_responsavel", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_rel_bsc_frete_responsavel")
        self.click_relative(46, 27)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_grupo_fiscal_mov_rel_conhecimento", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_mov_rel_conhecimento")
        self.click_relative(40, 28)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        
        x = 0
        while x < 6:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        
        self.tab()
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        
        self.tab()
        x = 0
        while x < 15:
            self.type_down()
            x += 1
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        x = 0 # Tipo de Tributaçao
        while x < 6:
            self.type_down()
            x += 1
        
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
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
        if not self.find( "cont_observacoes_mov_2_valores", matching=0.97, waiting_time=10000):
            not_found("cont_observacoes_mov_2_valores")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_3_notas_fiscais_mov_doc", matching=0.97, waiting_time=10000):
            not_found("cont_3_notas_fiscais_mov_doc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_adicionar_3_notas_fiscais_mov", matching=0.97, waiting_time=10000):
            not_found("cont_botao_adicionar_3_notas_fiscais_mov")
        self.click()
        if not self.find( "cont_cliente_fornecedor_busc_rel_1_notas_f", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_fornecedor_busc_rel_1_notas_f")
        self.click_relative(162, 6)
        self.wait(2000)
        self.type_keys_with_interval(100,"0081260")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_cfop_bsc_rel_1_nota_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_bsc_rel_1_nota_fiscal")
        self.click_relative(96, 5)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)

        if not self.find( "cont_unidade_rel_bsc_1_nota_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_unidade_rel_bsc_1_nota_fiscal")
        self.click_relative(109, 6)
        self.wait(2000)
        self.type_keys_with_interval(100,"CJ")
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        x = 0
        while x < 17:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.type_keys_with_interval(10,"11111111111111111111111111111111111111111111")
        self.wait(1000)
        if not self.find( "cont_salvar_botao_notas_fiscais_conhecimentos", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_botao_notas_fiscais_conhecimentos")
        self.click()

        # AQUI ACONTECE UM ERRO Q NAO ESTOU CONSEGUINDO RESOLVER #
        # ###################################################### # 

        self.wait(1000)
        self.enter()
        if not self.find( "cont_cancelar_fiscais_conhecimentos_mov", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_fiscais_conhecimentos_mov")
        self.click()

        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_cadatro_mov_notas", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_cadatro_mov_notas")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retornar_claro_lancamento_conhecimento_mov", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_claro_lancamento_conhecimento_mov")
        self.click()
        if not self.find( "cont_botn_data_rel_mov_conhecimentos", matching=0.97, waiting_time=10000):
            not_found("cont_botn_data_rel_mov_conhecimentos")
        self.click_relative(27, 5)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_edit_opc_2_ver_26", matching=0.97, waiting_time=10000):
            not_found("cont_botao_edit_opc_2_ver_26")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_claro_mov_conhecimentos", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_claro_mov_conhecimentos")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retornar_claro_lancamento_conhecimento_mov", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_claro_lancamento_conhecimento_mov")
        self.click()
        self.wait(500)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        
        #########################################################################
        ################## MOVIMENTOS -> Apuração Presumido #####################
        #########################################################################
        
        
        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_apuracao_presumido_mov_menu", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_presumido_mov_menu")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down() # Imposto
        self.type_down() 
        self.tab()
        x = 0
        while x < 12:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        if not self.find( "cont_achar_data_mov_apuracao_2", matching=0.97, waiting_time=10000):
            not_found("cont_achar_data_mov_apuracao_2")
        self.click_relative(27, 9)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(1000)
        
        if not self.find( "cont_btn_excluir_movimentos_opc_14", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimentos_opc_14")
        self.click()
        self.wait(2000)
        self.enter()
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
        
        ###########################################################
        ######## MOVIMENTOS -> Apuração Simples Nacional  #########
        ###########################################################

        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_apuracao_simples_nacional_menu", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_simples_nacional_menu")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        self.click()
        self.wait(1000)
        self.type_down()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_keys_with_interval(100,"2024")
        self.tab()
        if not self.find( "cont_lupa_movimento_apuracao_simples", matching=0.97, waiting_time=10000):
            not_found("cont_lupa_movimento_apuracao_simples")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        # Vazio, apenas dar OK
        self.wait(1000)
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)

        if not self.find( "cont_btn_salvar_opcao_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_opcao_24")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_adc_imposto_opc_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_adc_imposto_opc_24")
        self.click()
        self.wait(1000)
        self.type_down()
        # acontencendo erro aqui, esperar resolver apenas apertar enter
        self.wait(1000)
        self.tab()
        x = 0
        while x < 17:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(1000)
        if not self.find( "cont_cancelar_cfop_anexo_x_29", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_cfop_anexo_x_29")
        self.click()
        self.wait(1000)
        self.click()
        self.type_right()
        # Informar evento, GRAVAR
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        if not self.find( "cont_data_mov_apuracao_simples_nac_2", matching=0.97, waiting_time=10000):
            not_found("cont_data_mov_apuracao_simples_nac_2")
        self.click_relative(26, 7)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_opc_24_mov_simples", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_opc_24_mov_simples")
        self.click()
        self.wait(1000)
        self.enter()
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
        self.wait(1000)
        
        ###############################################################################################
        ############################# MOVIMENTOS -> Fechamento Fiscal  ################################
        ###############################################################################################

        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_fechamento_fiscal_menu_mov", matching=0.97, waiting_time=10000):
            not_found("cont_fechamento_fiscal_menu_mov")
        self.click()
        self.wait(2000)
        if not self.find( "cont_selecao_mov_fechamento_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_selecao_mov_fechamento_fiscal")
        self.click()
        self.wait(2000)

        # codigo fiscal
        if not self.find( "cont_codigo_fiscal_selecao_rlv", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_fiscal_selecao_rlv")
        self.click_relative(69, 25)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(2000)

        # operação
        if not self.find( "cont_operacao_mov_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_mov_rel_selecao")
        self.click_relative(67, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(2000)
        
        # cliente
        if not self.find( "cont_cliente_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_rel_selecao")
        self.click_relative(71, 21)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()
        self.wait(2000)

        # grupo de empresa
        if not self.find( "cont_grupo_de_empresa_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_rel_selecao")
        self.click_relative(66, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click() 
        self.wait(2000)
        if not self.find( "cont_btn_selec_ver_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selec_ver_24")
        self.click()
        self.wait(2000)

        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)

        if not self.find( "cont_apuracao_de_impostos_fech_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_de_impostos_fech_fiscal")
        self.click()
        self.wait(1000)

        if not self.find( "cont_apuracao_imposto_icms_edit", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_imposto_icms_edit")
        self.click()
        self.wait(2000)

        if not self.find( "cont_outros_debitos_do_imposto_rel", matching=0.97, waiting_time=10000):
            not_found("cont_outros_debitos_do_imposto_rel")
        self.double_click_relative(151, 3)
        self.wait(2000)
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        
        # UF
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.shift_tab()
        # Indicador Ajuste
        x = 0
        while x < 10:
            self.type_down()
            x += 1

        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)


        if not self.find( "cont_info_adicionais_valores_declaratorios", matching=0.97, waiting_time=10000):
            not_found("cont_info_adicionais_valores_declaratorios")
        self.click()

        self.wait(2000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()
        self.wait(2000)
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        self.wait(2000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()

        # OBRIGAÇÕES A RECOLHER

        self.wait(2000)
        if not self.find( "cont_obrigacoes_a_recolher_mov_imp", matching=0.97, waiting_time=10000):
            not_found("cont_obrigacoes_a_recolher_mov_imp")
        self.click()    
        self.wait(2000)
        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()
        self.wait(2000)
        self.wait(1000)
        x = 0 # COD. OBRIGAÇAO
        while x < 5:
            self.type_down()
            x += 1
        self.tab()

        x = 0 # VLR. OBRIGAÇÃO
        while x < 4:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0 # INDICADOR PROCESSO
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        x = 0 # INDICADOR PROCESSO
        while x < 12:
            self.type_down()
            x += 1
        self.tab()

        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()

        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        #self.click()

        # Retornar 
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###################################################################################
        ################################# ICMS ST #########################################
        ###################################################################################
        self.wait(4000)
        if not self.find( "cont_fechamento_fiscal_mo_icms_st", matching=0.97, waiting_time=10000):
            not_found("cont_fechamento_fiscal_mo_icms_st")
        self.click()
        self.wait(1000)
        if not self.find( "cont_apuracao_dos_impostos_detalhes", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_dos_impostos_detalhes")
        self.click()

        ##################
        # COPIA DO CODIGO ACIMA, POIS É A MESMA TELA, TESTAR AGORA # PROXIMAS 150 LINHAS 


        if not self.find( "cont_outros_debitos_do_imposto_rel", matching=0.97, waiting_time=10000):
            not_found("cont_outros_debitos_do_imposto_rel")
        self.click_relative(151, 3)
   
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(1000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        
        # UF
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.shift_tab()
        # Indicador Ajuste
        x = 0
        while x < 10:
            self.type_down()
            x += 1

        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)


        if not self.find( "cont_info_adicionais_valores_declaratorios", matching=0.97, waiting_time=10000):
            not_found("cont_info_adicionais_valores_declaratorios")
        self.click()

        self.wait(1000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()

        # OBRIGAÇÕES A RECOLHER


        if not self.find( "cont_obrigacoes_a_recolher_mov_imp", matching=0.97, waiting_time=10000):
            not_found("cont_obrigacoes_a_recolher_mov_imp")
        self.click()

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(1000)
        x = 0 # COD. OBRIGAÇAO
        while x < 5:
            self.type_down()
            x += 1
        self.tab()

        x = 0 # VLR. OBRIGAÇÃO
        while x < 4:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0 # INDICADOR PROCESSO
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        x = 0 # INDICADOR PROCESSO
        while x < 12:
            self.type_down()
            x += 1
        self.tab()

        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()

        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        # Retornar 
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        # AQUI ACABA O CODIGO QUE SE REPETE 
        #

        
        ####################################################################################
        ############################# FECHAMENTO FISCAL -> IPI #############################
        ####################################################################################
        
        self.wait(3000)
        # AQUI REPETE NOVAMENTE
        #
        # 

        if not self.find( "cont_apuracao_imposto_ipi_mov", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_imposto_ipi_mov")
        self.click()

        if not self.find( "cont_apuracao_dos_impostos_detalhes", matching=0.97, waiting_time=10000):
            not_found("cont_apuracao_dos_impostos_detalhes")
        self.click()

        if not self.find( "cont_outros_debitos_do_imposto_rel", matching=0.97, waiting_time=10000):
            not_found("cont_outros_debitos_do_imposto_rel")
        self.click_relative(151, 3)
   
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()
        self.wait(2000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        self.shift_tab()
        
        # UF
        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.shift_tab()
        # Indicador Ajuste
        x = 0
        while x < 10:
            self.type_down()
            x += 1

        self.shift_tab()
        self.type_keys_with_interval(100,"123")
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)


        if not self.find( "cont_info_adicionais_valores_declaratorios", matching=0.97, waiting_time=10000):
            not_found("cont_info_adicionais_valores_declaratorios")
        self.click()

        self.wait(1000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()

        # OBRIGAÇÕES A RECOLHER


        if not self.find( "cont_obrigacoes_a_recolher_mov_imp", matching=0.97, waiting_time=10000):
            not_found("cont_obrigacoes_a_recolher_mov_imp")
        self.click()

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(1000)
        x = 0 # COD. OBRIGAÇAO
        while x < 5:
            self.type_down()
            x += 1
        self.tab()

        x = 0 # VLR. OBRIGAÇÃO
        while x < 4:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        x = 0 # INDICADOR PROCESSO
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        x = 0 # INDICADOR PROCESSO
        while x < 12:
            self.type_down()
            x += 1
        self.tab()

        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()

        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_excluir_info_adicional_apuracao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_info_adicional_apuracao_imp")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        # Retornar 
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        # CODIGO REPETIDO ACABA AQUI

        self.wait(3000)
        if not self.find( "cont_forma_pagamento_apuracao_icms", matching=0.97, waiting_time=10000):
            not_found("cont_forma_pagamento_apuracao_icms")
        self.click()

        if not self.find( "cont_mov_informe_tipo_de_pagamento_1", matching=0.97, waiting_time=10000):
            not_found("cont_mov_informe_tipo_de_pagamento_1")
        self.click_relative(209, 56)
        
        ########################################
        ### PRIMEIRA FORMA DE PAGAMENTO DARF ###
        ########################################

        if not self.find( "cont_pagamento_com_darf_opcao_1", matching=0.97, waiting_time=10000):
            not_found("cont_pagamento_com_darf_opcao_1")
        self.click()

        if not self.find( "cont_selecionar_mov_apuracao_imposto_pag", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_mov_apuracao_imposto_pag")
        self.click()

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(2000)
        
        self.type_keys_with_interval(100,"12312312312312")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_buscar_tabela_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_tabela_cad_servicos")
        self.click()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()
        # arquivo esta vazio, apenas apertar enter no erro
        self.wait(1000)
        self.tab()
        self.tab()
        x = 0
        while x < 6: 
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()     
        self.wait(1000)

        self.enter()
        self.wait(1000)
    
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        #### SEGUNDA FORMA DE PAGAMENTO ####
        ##### COMPENSACAO DE PAGAMENTO #####

        if not self.find( "cont_forma_pagamento_apuracao_icms", matching=0.97, waiting_time=10000):
            not_found("cont_forma_pagamento_apuracao_icms")
        self.click()

        if not self.find( "cont_mov_informe_tipo_de_pagamento_1", matching=0.97, waiting_time=10000):
            not_found("cont_mov_informe_tipo_de_pagamento_1")
        self.click_relative(209, 56)

        if not self.find( "cont_compensacao_de_pagamento_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_compensacao_de_pagamento_opc_2")
        self.click()

        if not self.find( "cont_selecionar_mov_apuracao_imposto_pag", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_mov_apuracao_imposto_pag")
        self.click()

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(2000)

        if not self.find( "cont_btn_imposto_compensacao_pag", matching=0.97, waiting_time=10000):
            not_found("cont_btn_imposto_compensacao_pag")
        self.click()
        self.wait(2000)


        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_down()
        self.tab()
        self.type_down()
        self.wait(500)
        self.enter()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()     
        self.wait(1000)

        self.enter()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        #### TERCEIRA FORMA DE PAGAMENTO ####
        ######## OUTRAS COMPENSAÇOES ########

        if not self.find( "cont_forma_pagamento_apuracao_icms", matching=0.97, waiting_time=10000):
            not_found("cont_forma_pagamento_apuracao_icms")
        self.click()

        if not self.find( "cont_mov_informe_tipo_de_pagamento_1", matching=0.97, waiting_time=10000):
            not_found("cont_mov_informe_tipo_de_pagamento_1")
        self.click_relative(209, 56)

        self.wait(1000)

        if not self.find( "cont_outras_compensacoes_form_pag_3", matching=0.97, waiting_time=10000):
            not_found("cont_outras_compensacoes_form_pag_3")
        self.click()

        if not self.find( "cont_selecionar_mov_apuracao_imposto_pag", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_mov_apuracao_imposto_pag")
        self.click()
        self.wait(1000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(2000)

        if not self.find( "cont_btn_imposto_compensacao_pag", matching=0.97, waiting_time=10000):
            not_found("cont_btn_imposto_compensacao_pag")
        self.click() # botao com nome reutilizado

        self.wait(2000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        self.tab()
        self.tab()
        self.tab()

        # Tipo de credito

        x = 0
        while x < 10:
            self.type_down()
            x += 1
        self.tab()

        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")

        self.wait(1000)
        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()     
        self.wait(1000)

        self.enter()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ##### QUARTA FORMA DE PAGAMENTO #####
        ####### PAGAMENTO COM DARE-SC #######

        if not self.find( "cont_forma_pagamento_apuracao_icms", matching=0.97, waiting_time=10000):
            not_found("cont_forma_pagamento_apuracao_icms")
        self.click()

        if not self.find( "cont_mov_informe_tipo_de_pagamento_1", matching=0.97, waiting_time=10000):
            not_found("cont_mov_informe_tipo_de_pagamento_1")
        self.click_relative(209, 56)

        self.wait(1000)

        if not self.find( "cont_pagamento_com_dare_opc_4", matching=0.97, waiting_time=10000):
            not_found("cont_pagamento_com_dare_opc_4")
        self.click()

        if not self.find( "cont_selecionar_mov_apuracao_imposto_pag", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_mov_apuracao_imposto_pag")
        self.click()
        self.wait(1000)

        if not self.find( "cont_incluir_ajuste_beneficio_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_ajuste_beneficio_fiscal")
        self.click()

        self.wait(2000)

        x = 0
        while x < 15:
            self.type_down()
            x += 1
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"12312312333")
        self.tab()
        x = 0
        while x < 9:
            self.type_keys_with_interval(100,"123")
            self.tab()
            x += 1
        if not self.find( "cont_btn_imposto_compensacao_pag", matching=0.97, waiting_time=10000):
            not_found("cont_btn_imposto_compensacao_pag")
        self.click()

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        if not self.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        self.click()     
        self.wait(1000)

        self.enter()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        # ACABOU FORMAS DE PAGAMENTO

        if not self.find( "cont_gerar_apuracao_fechamento_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_gerar_apuracao_fechamento_fiscal")
        self.click()

        if not self.find( "cont_relatorio_fechamento_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_fechamento_fiscal")
        self.click()

        if not self.find( "cont_x_vermelho_voltar_relatorio", matching=0.97, waiting_time=10000):
            not_found("cont_x_vermelho_voltar_relatorio")
        self.click()

        # BOTAO FECHAR NAO ESTA ABRINDO NENHUMA JANELA

        #if not self.find( "cont_fechar_fechamento_fiscal", matching=0.97, waiting_time=10000):
        #    not_found("cont_fechar_fechamento_fiscal")
        #self.click()


        # FILTROS

        if not self.find( "cont_filtros_fechamento_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_filtros_fechamento_fiscal")
        self.click()
        # tela de filtros ja foi testada, apenas retornar

        self.wait(1000)
        self.key_esc()

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        #######################################################################################
        #######################################################################################
        ################################# FINAL DE MOVIMENTOS #################################
        #######################################################################################
        #######################################################################################


        #######################################################################################
        #######################################################################################
        ################################ COMEÇO DE CONSULTAS ##################################
        #######################################################################################
        #######################################################################################
        
        
        ########################################################################
        ####### CONSULTAS -> ANALISE DE BALANÇO VERTICAL E HORIZONTAL ##########
        ########################################################################
        self.wait(3000)
        if not self.find( "cont_consultas_menu_prin_2", matching=0.97, waiting_time=10000):
            not_found("cont_consultas_menu_prin_2")
        self.click()
        if not self.find( "cont_consulta_balanco_vertical_horizontal", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_balanco_vertical_horizontal")
        self.click()

        self.wait(2000)
        self.type_keys_with_interval(100,"6")
        
        if not self.find( "cont_consulta_periodo1_data", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_periodo1_data")
        self.click_relative(215, 28)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        
        
        if not self.find( "cont_consulta_periodo2_data", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_periodo2_data")
        self.click_relative(213, 27)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        
        if not self.find( "cont_consulta_grupo_empresa_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grupo_empresa_bsc")
        self.click_relative(54, 30)
        self.wait(1000)
        if not self.find( "cont_rela_consulta_grupo_rel_localizar", matching=0.97, waiting_time=10000):
            not_found("cont_rela_consulta_grupo_rel_localizar")
        self.click_relative(101, 36)
        
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()

        self.wait(1000)
        self.backspace()
        # Aqui eu faço o backspace para apagar o grupo, pois o unico grupo que tem é o de teste e não tem nada nele

        if not self.find( "cont_consulta_reduzido_inicial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_reduzido_inicial_rel")
        self.click_relative(140, 4)
        self.wait(1000)
        
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.wait(1000)
        # While para descer até o item que esta disponivel
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)
        
        
        
        if not self.find( "cont_reduzido_final_rel", matching=0.97, waiting_time=10000):
            not_found("cont_reduzido_final_rel")
        self.click_relative(131, 7)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        x = 0
        while x < 4:
            self.type_down()
            x += 1
        self.wait(1000)
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)
        
        
        if not self.find( "cont_consulta_conta_inicial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_conta_inicial_rel")
        self.click_relative(189, 4)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)
        
        
        if not self.find( "cont_consulta_conta_final_rel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_conta_final_rel")
        self.click_relative(182, 6)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_consultas_horizontal_analise", matching=0.97, waiting_time=10000):
            not_found("cont_consultas_horizontal_analise")
        self.click()
        self.wait(1000)

        if not self.find( "cont_consulta_analise_horizontal_rel_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_analise_horizontal_rel_check")
        self.click_relative(44, 18)

        self.wait(1000)

        if not self.find( "cont_consulta_vertical_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_vertical_check")
        self.click_relative(35, -22)

        if not self.find( "cont_consulta_ambos_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ambos_check")
        self.click_relative(181, -34)
        # ESTE BOTÃO ^^^ CONFIRMA SE AMBOS FOI SELECIONADO E CLICA EM GRADE
        self.wait(1000)
        if not self.find( "cont_consulta_grade_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grade_imprimir")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_grade_imprimir_cancel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grade_imprimir_cancel")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ########################################################################
        ############## CONSULTAS -> CONSULTA TOTAIS DE IMPOSTOS ################
        ########################################################################

        self.wait(2000)
        if not self.find( "cont_consultas_menu_prin_2", matching=0.97, waiting_time=10000):
            not_found("cont_consultas_menu_prin_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_consulta_totais_de_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_totais_de_impostos")
        self.click()
        self.wait(1000)
        #DATA
        if not self.find( "cont_consulta_total_imposto_data", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_total_imposto_data")
        self.click_relative(32, 7)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        # AQUI ESTOU PEGANDO O ANO ANTERIOR POIS 2024 NÃO TEM NENHUM DADO A CONSULTAR 

        self.wait(500)
        self.tab()

        # TABELAS ESTA FECHANDO A JANELA, PROCURAR PARA VER SE É UM ERRO OU NAO

        if not self.find( "cont_consulta_total_imposto_consultar", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_total_imposto_consultar")
        self.click()
        self.wait(6000) # Tempo de consulta
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ########################################################################
        ############## CONSULTAS -> CONSULTA TOTAIS DE IMPOSTOS ################
        ########################################################################


        self.wait(2000)
        if not self.find( "cont_consultas_menu_prin_2", matching=0.97, waiting_time=10000):
            not_found("cont_consultas_menu_prin_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_movimento_de_clientes_ranking", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_movimento_de_clientes_ranking")
        self.click()
        self.wait(2000)
        if not self.find( "cont_consulta_ranking_emissao_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_emissao_check")
        self.click_relative(116, 6)
        # CONFERINDO SE EMISSAO ESTA MARCADO ^ 
        if not self.find( "cont_consulta_ranking_movimento_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_movimento_check")
        self.click_relative(137, 4)
        # CONFERINDO SE MOVIMENTO ESTA MARCADO ^
        if not self.find( "cont_consulta_ranking_lancamento_check", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_lancamento_check")
        self.click_relative(25, 25)
        # CONFERINDO SE LANÇAMENTO ESTA MARCADO E JA CLICA NO BOTÃO DA DATA
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click() # DATA ANTERIOR
        self.wait(1000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_consulta_ranking_grade", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_grade")
        self.click_relative(48, 16)
        self.wait(1000)
        if not self.find( "cont_grade_consultas_imprimir_ranking", matching=0.97, waiting_time=10000):
            not_found("cont_grade_consultas_imprimir_ranking")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_consulta_grade_imprimir_cancel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grade_imprimir_cancel")
        self.click()
        self.wait(1000)

        # ESTA PARTE DO CODIGO CONFERE AS CAIXINHAS "ENTRADA" E "SAIDA"
        if not self.find( "cont_consulta_ranking_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_entrada")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_ranking_saidas", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_saidas")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_ranking_entrada_vazio", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_entrada_vazio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_ranking_saidas_vazio", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_ranking_saidas_vazio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consulta_entrada_check_retorno", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_entrada_check_retorno")
        self.click_relative(-216, -42)
        # AQUI VAI CONFERIR SE ENTRADA ESTA MARCADO, E ENTAO CLICAR NO BOTÃO DE RETORNO ^

        
        ################################################
        ############## FIM DE CONSULTAS ################
        ################################################



        ################################################
        ############# COMEÇO RELATORIOS ################
        ################################################
        self.wait(3000)
        # RELATORIOS -> CADASTROS -> CLASSIFICAÇAO

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_classificacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_classificacao")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorio_cadastro_btn_codigo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cadastro_btn_codigo")
        self.click()
        if not self.find( "cont_relatorio_btn_alfabetica_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_btn_alfabetica_cad")
        self.click()
        self.wait(1000)
        # IMPRIMIR NAO ESTA FUNCIONANDO 
        #if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_imprimir_cad")
        #self.click()
        self.wait(1000)
        #if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
        #   not_found("cont_relatorios_x_fechar_cad")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_relatorio_cod_retorno_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cod_retorno_rel")
        self.click_relative(-68, -86)
        # ESTE CLICK RELATIVO VAI PARA RETORNO, CASO O CÓDIGO ESTEJA DESMARCADO

        # RELATORIOS -> CADASTROS -> CENTRO DE CUSTOS

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cad_centros_de_custo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_centros_de_custo")
        self.click()

        self.wait(1000)
        if not self.find( "cont_relatorio_cadastro_btn_codigo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cadastro_btn_codigo")
        self.click()
        if not self.find( "cont_relatorio_btn_alfabetica_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_btn_alfabetica_cad")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_cod_rel_ativos", matching=0.97, waiting_time=10000):
            not_found("cont_rel_cod_rel_ativos")
        self.click_relative(-81, 64)

        if not self.find( "cont_relatorios_cad_custo_todos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_custo_todos")
        self.click()
        if not self.find( "cont_relatorios_inativos_situacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_inativos_situacao")
        self.click()
        self.wait(1000)

        # IMPRIMIR NAO ESTA FUNCIONANDO

        #if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_imprimir_cad")
        #self.click()
        self.wait(1000)
        #if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_x_fechar_cad")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_relatorio_cod_retorno_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cod_retorno_rel")
        self.click_relative(-68, -86)
        # RETORNO E CONFERINDO SE CODIGO NAO ESTA CLICADO

        # RELATORIOS -> CADASTROS -> CLIENTES, FORNECEDORES E TRANSPORTADORES
        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_clientes_forn_tra", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_clientes_forn_tra")
        self.click()
        self.wait(1000)
        if not self.find( "cont_selecione_a_relacao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_selecione_a_relacao_relatorios")
        self.click_relative(6, 25)
        x = 0
        while x < 4:
            self.type_right()
            x += 1
        if not self.find( "cont_relatorios_clientes_contratos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_clientes_contratos")
        self.click_relative(132, -7)
        # AQUI VAI CONFERIR SE "CONTRATOS" ESTA MARCADA, SE ESTIVER, VAI CLICAR EM "ALFABETICA"
        self.wait(1000)
        self.type_right()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_relatorios_ordem_imp_dia_aniversario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_ordem_imp_dia_aniversario")
        self.click_relative(116, -23)
        # AQUI VAI CONFERIR SE "DIA ANIVERSARIO" ESTA MARCADO, SE ESTIVER, VAI CLICAR EM "ATIVOS"
        self.wait(1000)
        self.type_right()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_relatorios_todos_situacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_todos_situacao")
        self.click_relative(74, -24)
        # AQUI ESTA CONFERINDO SE "TODOS" ESTA MARCADO, SE ESTIVER, CLICA EM "FISICA"
        self.wait(1000)
        self.type_right()
        self.type_right()
        if not self.find( "cont_relatorios_clientes_todos_listar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_clientes_todos_listar")
        self.click_relative(88, -27)

        x = 0
        while x < 10:
            self.type_right()
            x += 1
        
        if not self.find( "cont_relatorios_conferir_btn_nenhum", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_conferir_btn_nenhum")
        self.click_relative(-875, 69)
        self.wait(500)
        # PAÍS
        self.type_down()
        self.enter()
        self.wait(1000)
        # REGIÃO
        self.type_down()
        self.type_down()
        self.enter()
        # ESTADO
        self.type_down()
        self.type_down()
        self.enter()
        # MUNICIPIO
        x = 0
        while x < 7:
            self.type_down()
            x += 1
        self.enter()

        # TIPO DE CONTRATO NAO POSSUI ITENS

        # EXIBIR CONTRATOS
        if not self.find( "cont_exibir_contratos_relatorios_sim", matching=0.97, waiting_time=10000):
            not_found("cont_exibir_contratos_relatorios_sim")
        self.click_relative(7, 26)
        self.wait(500)
        self.type_right()

        if not self.find( "cont_relatorios_cliente_exibir_nao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cliente_exibir_nao")
        self.click_relative(97, -14)
        # CONFERINDO SE "NAO" ESTA MARCADO EM "EXIBIR CONTRATROS", SE ESTIVER, CLICAR EM "CADASTRO"

        self.type_right()
        self.wait(300)
        # DATA PERIODO
        if not self.find( "cont_data_relatorios_contrato_rel", matching=0.97, waiting_time=10000):
            not_found("cont_data_relatorios_contrato_rel")
        self.click_relative(27, 8)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        if not self.find( "cont_relatorios_cliente_data_confere", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cliente_data_confere")
        self.click_relative(-289, 50)
        # AQUI ELE VAI CONFERIR SE A DATA DO ANO ANTERIOR FOI INSERIDA ( ESTE BOTÃO SÓ VAI FUNCIONAR EM 2024)
        # DEPOIS VAI CLICAR EM "CLIENTES" EM "RELACIONAR/APENAS"

        x = 0
        while x < 5:
            self.type_right()
            x += 1
        if not self.find( "cont_contabil_achar_todos_relacionar_apenas", matching=0.97, waiting_time=10000):
            not_found("cont_contabil_achar_todos_relacionar_apenas")
        self.click_relative(153, -14)
        # AQUI VAI CONFERIR SE "TODOS" ESTA MARCADO, SE ESTIVER VAI CLICAR EM "00 CLIENTE PREFERENCIAL"
        
        x = 0
        while x < 9:
            self.type_right()
            x += 1

        self.wait(1000)
        if not self.find( "cont_relatorios_mo_qu_vip_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mo_qu_vip_rel")
        self.click_relative(177, 19)
        # AQUI CONFERE SE "VIP" ESTA MARCADO, CASO SIM, CLICA EM "SIM" DE "LISTA(OBSERV)"
        self.wait(500)
        self.type_right()
        if not self.find( "cont_relatorios_listar_nao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_listar_nao_rel")
        self.click_relative(62, 8)
        # CONFERINDO SE "NAO" ESTA MARCADO, CASO ESTEJA, CLICAR EM "SIM" DE "IMPR.(LIMITE CRED)"

        self.wait(500)
        self.type_right()
        self.wait(1000)


        

        if not self.find( "cont_relatorios_impr_nao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impr_nao_rel")
        self.click_relative(-1120, -247)
        # AQUI CONFERE SE O BOTAO "NAO" ESTA MARCADO EM "IMP.(LIMITE CRED), CASO ESTIVER, CLICAR NO BOTAO DE IMPRESSAO"
        
        self.wait(3000)
        if not self.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ######################################################################
        ######## RELATORIOS -> CADASTROS -> VENDEDORES E COMPRADORES #########
        ######################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_vendedores_compradores", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_vendedores_compradores")
        self.click()
        if not self.find( "cont_relatorios_vendedores_comp_listar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_vendedores_comp_listar")
        self.click_relative(5, 41)
        # RELATIVO PARA CLICAR EM "VENDEDORES"
        self.type_right()
        self.type_right()
        self.wait(1000)

        if not self.find( "cont_relatorios_todos_vendedores_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_todos_vendedores_rel")
        self.click_relative(137, -9)
        # AQUI CONFERE SE "TODOS" ESTA MARCADO E CLICA EM "ATIVOS"
        self.type_right()
        self.type_right()

        if not self.find( "cont_todos_relatorios_situacao_check", matching=0.97, waiting_time=10000):
            not_found("cont_todos_relatorios_situacao_check")
        self.click_relative(142, -24)
        # AQUI CONFERE SE "TODOS" ESTA MARCADO E CLICA EM "NOME"
        self.wait(1000)
        self.type_right()
        self.type_right()
        self.type_right()
        self.wait(500)
        if not self.find( "cont_ordem_impressao_relatorios_bairro", matching=0.97, waiting_time=10000):
            not_found("cont_ordem_impressao_relatorios_bairro")
        self.click_relative(-903, -93)
        # AQUI CONFERE SE "BAIRRO" ESTA MARCADO, SE ESTIVER, RETORNA


        #################################################################
        ####### RELATORIOS -> CADASTROS -> CONDIÇÕES DE PAGAMENTO #######
        #################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_condicoes_pagamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_condicoes_pagamento")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA

        #################################################################
        ############# RELATORIOS -> CADASTROS -> EMPRESAS ###############
        #################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_empresas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_empresas")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        #################################################################
        ######### RELATORIOS -> CADASTROS -> GRUPO DE EMPRESAS ##########
        #################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_grupo_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_grupo_empresa")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA

        
        ##############################################################################################
        ######### RELATORIOS -> CADASTROS -> PARAMETROS FISCAIS -> REGIONALIZAÇÃO -> PAISES ##########
        ##############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_parametros_regio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_parametros_regio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_regionalizacao_paises", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_regionalizacao_paises")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ##############################################################################################
        ######### RELATORIOS -> CADASTROS -> PARAMETROS FISCAIS -> REGIONALIZAÇÃO -> REGIOES ##########
        ##############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_parametros_regio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_parametros_regio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_regionalizacao_regioes", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_regionalizacao_regioes")
        self.click()


        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ##############################################################################################
        ######### RELATORIOS -> CADASTROS -> PARAMETROS FISCAIS -> REGIONALIZAÇÃO -> ESTADOS #########
        ##############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_parametros_regio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_parametros_regio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_regionalizacao_estados", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_regionalizacao_estados")
        self.click()


        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ##############################################################################################
        ############### RELATORIOS -> CADASTROS -> PARAMETROS FISCAIS -> MUNICIPIOS ->  ##############
        ##############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_parametros_regio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_parametros_regio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_regionalizacao_municipios", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_regionalizacao_municipios")
        self.click()


        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA




        ###############################################################################################
        ## RELATORIOS -> CADASTROS ->  PARAMETROS FISCAIS -> SITUAÇÃO FISCAL -> GRUPO FISCAL DE ITEM ##
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()

        if not self.find( "cont_relatorios_cad_situacao_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_situacao_fiscal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_situacao_grupo_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_situacao_grupo_fiscal")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA




        ###############################################################################################
        ## RELATORIOS -> CADASTROS ->  PARAMETROS FISCAIS -> SITUAÇÃO FISCAL -> CODIGOS DE OPERACAO  ##
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()

        if not self.find( "cont_relatorios_cad_situacao_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_situacao_fiscal_2")
        self.click()
        self.wait(1000)

        

        if not self.find( "cont_relatorios_situacao_codigos_operacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_situacao_codigos_operacao")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        
        ###############################################################################################
        ## RELATORIOS -> CADASTROS ->  PARAMETROS FISCAIS -> SITUAÇÃO FISCAL -> DECRETOS E OBSERVACOES ##
        ###############################################################################################
        self.wait(3000)
        
        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()

        if not self.find( "cont_relatorios_cad_situacao_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_situacao_fiscal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_situacao_decretos_observacoes", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_situacao_decretos_observacoes")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ## RELATORIOS -> CADASTROS ->  PARAMETROS FISCAIS -> SITUAÇÃO FISCAL -> CODIGOS FISCAIS CFOP ##
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()

        if not self.find( "cont_relatorios_cad_situacao_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_situacao_fiscal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_situacao_cfop", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_situacao_cfop")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ####### RELATORIOS -> CADASTROS ->  PARAMETROS FISCAIS -> SITUAÇÃO FISCAL -> SITUAÇÕES ########
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_parametros_fiscais")
        self.click()

        if not self.find( "cont_relatorios_cad_situacao_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_situacao_fiscal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_situacao_cfop", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_situacao_cfop")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA





        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> FAMILIA #############
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # FAMILIAS
        if not self.find( "cont_relatorios_cad_itens_familias", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_itens_familias")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA

        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> GRUPOS #############
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # GRUPOS
        if not self.find( "cont_relatorios_cad_itens_grupos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_itens_grupos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> SUBGRUPOS ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # SUB GRUPOS
        if not self.find( "cont_relatoris_agrupamento_subgrupos", matching=0.97, waiting_time=10000):
            not_found("cont_relatoris_agrupamento_subgrupos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        
        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> MARCAS ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # MARCAS
        if not self.find( "cont_relatorios_cad_agrupamento_itens_marcas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_agrupamento_itens_marcas")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA




        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> UNIDADES ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # MARCAS
        if not self.find( "cont_relatorios_cad_agrupamento_itens_unidades", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_agrupamento_itens_unidades")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> UNIDADES ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # UNIDADES
        if not self.find( "cont_relatorios_cad_agrupamento_itens_unidades", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_agrupamento_itens_unidades")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> TIPOS ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # TIPOS
        if not self.find( "cont_relatorios_itens_agrupamento_tipos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_agrupamento_tipos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> SUBTIPOS ###########
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # SUBTIPOS
        if not self.find( "cont_relatorios_agrupamento_itens_subtipos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_agrupamento_itens_subtipos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA

        

        ###############################################################################################
        ########## RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE -> AGRUPAMENTO -> CONTROLES ###########
        ###############################################################################################
        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        # AGRUPAMENTO
        if not self.find( "cont_relatorio__cad_itens_agrupamento", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio__cad_itens_agrupamento")
        self.click()
        self.wait(1000)

        # CONTROLES
        if not self.find( "cont_relatorios_agrupemento_itens_controles", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_agrupemento_itens_controles")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        
        ###############################################################################################
        ################# RELATORIOS -> CADASTROS ->  ITENS DE ESTOQUE ->  ITENS  #####################
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        # ITENS DE ESTOQUE
        if not self.find( "cont_relatorioscad_itens_de_estoque", matching=0.97, waiting_time=10000):
            not_found("cont_relatorioscad_itens_de_estoque")
        self.click()
        self.wait(500)

        if not self.find( "cont_relatorios_cadastro_estoque_itens", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_estoque_itens")
        self.click()

        #
        if not self.find( "cont_relatorio_itens_rel_codigo_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_itens_rel_codigo_imprimir")
        self.click_relative(16, 53)
        # CLICANDO EM "REDUZIDO"

        x = 0
        while x < 3:
            self.type_right()
            x += 1
        
        if not self.find( "cont_relatorio_itens_conf_referencia", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_itens_conf_referencia")
        self.click_relative(-988, 54)
        # AQUI ESTA CONFERINDO SE "REFERENCIA FABRICANTE" ESTA MARCADO, CASO SIM, CLICAR EM "SEM AGRUPAMENTO"

        x = 0
        while x < 3:
            self.type_right()
            x += 1
        
        if not self.find( "cont_relatorio_itens_familia_grupo_conf", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_itens_familia_grupo_conf")
        self.click_relative(-991, 65)
        # AQUI ESTA CONFERINDO SE "FAMILIA + GRUPO + SUBGRUPO" ESTA MARCADO, CASO SIM, CLICAR EM "ATIVOS"

        x = 0
        while x < 2:
            self.type_right()
            x += 1

        if not self.find( "cont_relatorios_itens_conf_todos_situacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_conf_todos_situacao")
        self.click_relative(87, 9)
        # AQUI ESTA CONFERINDO SE "TODOS" ESTA MARCADO, CASO SIM, CLICAR EM "SIM"

        self.type_right()
        if not self.find( "cont_relatorios_itens_pesos_nao_conf", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_pesos_nao_conf")
        self.click_relative(61, 8)
        # AQUI CONFERE SE "NAO" EM "IMPRIMIR PESOS" ESTA MARCADO, AI MARCA "SIM" EM "AGRUPA POR FORNECEDOR"

        self.type_right()

        if not self.find( "cont_relatorios_itens_agrupa_forn_nao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_agrupa_forn_nao")
        self.click_relative(83, -4)
        # CONFERINDO SE "NAO" ESTA MARCADO EM "AGRUPA POR FORNECEDOR" E AI CLICA EM "CUSTOS"

        x = 0
        while x < 3:
            self.type_right()
            x += 1

        if not self.find( "cont_relatorios_itens_valores_nenhum_conf", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_valores_nenhum_conf")
        self.click_relative(187, -1)
        # CONFERINDO SE "NENHUM" ESTA MARCADO E CLICANDO EM "SIM" DE "MARCADOS COM PIN"

        x = 0
        while x < 2:
            self.type_right()
            x += 1

        if not self.find( "cont_relatorios_itens_todos_pis_conf", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_itens_todos_pis_conf")
        self.click_relative(-1123, 65)
        # CONFERINDO SE "TODOS" ESTA MARCADO E CLICA EM "DESCRIÇAO"

        self.type_right()
        if not self.find( "cont_relatorio_itens_codigo_conf_ret", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_itens_codigo_conf_ret")
        self.click_relative(-647, -228)
        # CONFERINDO SE "CODIGO" ESTA MARCADO, CASO SIM, ELE CLICA EM RETORNAR

        ###############################################################################################
        ############################# RELATORIOS -> CADASTROS -> USUARIOS  ############################
        ###############################################################################################


        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_usuario_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_usuario_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ######################### RELATORIOS -> CADASTROS -> PLANO FINANCEIRO  ########################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_plano_financeiro_relatorios_cadastro", matching=0.97, waiting_time=10000):
            not_found("cont_plano_financeiro_relatorios_cadastro")
        self.click()

        self.wait(1000)
        if not self.find( "cont_relatorio_cadastro_btn_codigo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cadastro_btn_codigo")
        self.click()
        if not self.find( "cont_relatorio_btn_alfabetica_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_btn_alfabetica_cad")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_cod_rel_ativos", matching=0.97, waiting_time=10000):
            not_found("cont_rel_cod_rel_ativos")
        self.click_relative(-81, 64)

        if not self.find( "cont_relatorios_cad_custo_todos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_custo_todos")
        self.click()
        if not self.find( "cont_relatorios_inativos_situacao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_inativos_situacao")
        self.click()
        self.wait(1000)

        

        #if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_imprimir_cad")
        #self.click()
        self.wait(1000)
        #if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_x_fechar_cad")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_relatorio_cod_retorno_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cod_retorno_rel")
        self.click_relative(-68, -86)

        
        ###############################################################################################
        ######################### RELATORIOS -> CADASTROS -> PLANO DE CONTAS  #########################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastro_plano_de_contas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastro_plano_de_contas")
        self.click()
        self.wait(2000)

        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"6")
        self.tab()

        if not self.find( "cont_relatorios_cad_livros_oficial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_livros_oficial_rel")
        self.click_relative(46, 26)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorio_cad_conta_inicial_busc", matching=0.97, waiting_time=10000):
            not_found("cont_relatorio_cad_conta_inicial_busc")
        self.click_relative(192, 1)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_cad_conta_final_busc", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_conta_final_busc")
        self.click_relative(192, 7)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ######################### RELATORIOS -> CADASTROS -> LOCAL COBRANÇA  ##########################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_local_cobranca", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_local_cobranca")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ############################ RELATORIOS -> CADASTROS -> HISTORICOS  ###########################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_historicos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_historicos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ###################### RELATORIOS -> CADASTROS -> LINHAS RAMOS -> LINHAS  #####################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_linhas_ramos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_linhas_ramos")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_linhas_linhas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_linhas_linhas")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA



        ###############################################################################################
        ################ RELATORIOS -> CADASTROS -> LINHAS RAMOS -> RAMOS DE ATIVIDADE  ###############
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_linhas_ramos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_linhas_ramos")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros-linhas_ramos_atv", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros-linhas_ramos_atv")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ################# RELATORIOS -> CADASTROS -> LINHAS RAMOS -> ROTAS DE ENTREGA  ################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_linhas_ramos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_linhas_ramos")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_linhas_rotas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_linhas_rotas")
        self.click()


        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA


        ###############################################################################################
        ##################### RELATORIOS -> CADASTROS -> LINHAS RAMOS -> SEGMENTOS ####################
        ###############################################################################################

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_cadastros_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_1")
        self.click_relative(14, -18)
        self.wait(1000)

        if not self.find( "cont_relatorios_cadastros_linhas_ramos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cadastros_linhas_ramos")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_cad_linhas_segmentos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_linhas_segmentos")
        self.click()

        if not self.find( "cont_relatorios_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_condicao_alfabetica")
        self.click_relative(94, 7)
        # AQUI CONFERE SE "ALFABETICA" ESTA MARCADA, CASO SIM, MARCA "CODIGO"
        self.wait(1000)
        if not self.find( "cont_relatorios_cad_condicao_alfabetica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_cad_condicao_alfabetica")
        self.click_relative(13, -84)
        # AQUI CONFERE SE "ALFABETICA" ESTA DESMARCADA, CASO ESTEJA, RETORNA

        # FIM DE RELATORIOS -> CADASTROS

        # COMEÇANDO RELATORIOS -> MOVIMENTO FISCAL

        ###############################################################################################
        ################ RELATORIOS -> MOVIMENTO FISCAL -> LIVRO DE ENTRADA E SAIDAS  #################
        ###############################################################################################
        
        
        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_livro_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_livro_entrada")
        self.click()

        if not self.find( "cont_relatorios_movimento_fiscal_data", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_data")
        self.click_relative(27, 7)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_livro_oficial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_livro_oficial_rel")
        self.click_relative(104, 5)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_movimento_livro_de_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_livro_de_rel")
        self.click_relative(7, 41)
        self.type_right()

        if not self.find( "cont_relatorios_movimentos_fiscal_rel_imprime", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimentos_fiscal_rel_imprime")
        self.click_relative(116, -14)

        x = 0
        while x < 6:
            self.type_down()
            self.space()
            x += 1
        self.wait(1000)

        if not self.find( "cont_relatorios_movimento_fiscal_emi_livro_check", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_emi_livro_check")
        self.click_relative(417, 10)

        x = 0
        while x < 7:
            self.space()
            self.type_down()
            x += 1
        
        if not self.find( "cont_relatorios_movimento_fiscal_centro_ini", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_centro_ini")
        self.click_relative(178, 5)
        self.wait(1000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        
        if not self.find( "cont_btn_selecionar_opc_23_centro_cs", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_opc_23_centro_cs")
        self.click()
        self.wait(1000)
        

        if not self.find( "cont_relatorios_mov_centro_custo_final", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_final")
        self.click_relative(182, 5)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_btn_selecionar_opc_23_centro_cs", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_opc_23_centro_cs")
        self.click()
        self.wait(1000)
        

        self.tab()
        self.tab()
        self.type_right()

        self.wait(1000)
        if not self.find( "cont_rel_mov_cod_fiscal_conf", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_cod_fiscal_conf")
        self.click_relative(209, -11)
        # AQUI CONFERE SE CABEÇALHO ESTA DESMARCADO, CASO SIM, CLICA NA CAIXA "ICMS"
        # A CAIXA VAI SER DESMARCADA

        self.space()

        x = 0
        while x < 6:
            self.type_down()
            self.space()
            x += 1
        
        if not self.find( "cont_rel_mov_fiscal_conf_pis_presu", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fiscal_conf_pis_presu")
        self.click_relative(300, 29)
        self.wait(1000)
        # AQUI CONFERE SE AS CAIXAS DE DESDOBRAMENTOS ESTÃO MARCADAS, CASO SIM, CLICA EM "SIM" EM "AGRUPA TIPO PESSOA"

        self.type_right()
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@") # OBSERVAÇOES
        self.tab()
        self.type_keys_with_interval(100,"1") # ESTADOS
        self.tab()
        self.type_keys_with_interval(100,"2")
        self.tab()
        self.type_keys_with_interval(100,"1") # SERIE
        self.tab()
        self.type_keys_with_interval(100,"2")
        self.tab()
        self.wait(2000)

        if not self.find( "cont_salvar_opc_rel_mov_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_rel_mov_fiscal")
        self.click()

        self.wait(1000)
        self.enter()
        self.wait(5000)
        
        
        ###############################################################################################
        ####################### RELATORIOS -> MOVIMENTO FISCAL -> LIVRO DE ISS  #######################
        ###############################################################################################
        

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_livros_iss", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_livros_iss")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_data_livro_iss", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_data_livro_iss")
        self.click_relative(27, 6)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.tab()
        self.space() # QUEBRA MENSAL
        self.tab()
        self.space() # IMPRIME NOME DO EMISSOR
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"2")
        self.tab()
        self.type_right() # codigo fiscal CABEçalho
        self.tab()
        self.space() # MUNICIPIO
        self.tab()
        self.space() # MUNICIPIO FATO GERADOR
        self.tab()

        if not self.find( "cont_rel_movimentos_livro_oficial_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rel_movimentos_livro_oficial_iss")
        self.click_relative(44, 30)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_right()
        self.tab()
        self.type_right()
        self.type_right()
        self.wait(1000)
        
        # MOUSE ESTA PARANDO EM CIMA DE MATRICAL 

        if not self.find( "cont_rel_mov_matrical_livros_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_matrical_livros_iss")
        self.click()
        
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_rel_mov_fiscal_livro_iss_fechar_matrical", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fiscal_livro_iss_fechar_matrical")
        self.click()

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()



        ###############################################################################################
        ################## RELATORIOS -> MOVIMENTO FISCAL -> APURAÇÃO DE IMPOSTO  #####################
        ###############################################################################################
        

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fis_apuracao_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fis_apuracao_imposto")
        self.click()

        self.wait(1000)

        if not self.find( "cont_data_rela_mov_apuracao_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_data_rela_mov_apuracao_imposto")
        self.click_relative(27, 7)
        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.wait(1000)
        self.tab()

        self.type_keys_with_interval(100,"123")
        self.tab()
        x = 0
        while x < 3:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        
        # GRUPO DE EMPRESAS
        if not self.find( "cont_grupo_empresa_rela_mov_apuracao", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_empresa_rela_mov_apuracao")
        self.click_relative(55, 21)
        self.wait(1000)


        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)


        #CENTRO INICIAL
        if not self.find( "cont_relat_mov_apuracao_centro_inicial", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_apuracao_centro_inicial")
        self.click_relative(147, 2)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)


        # CENTRO FINAL 
        if not self.find( "cont_rela_mov_centro_final_apuracao", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_centro_final_apuracao")
        self.click_relative(152, 2)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)

        self.tab()
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        

        # CLICANDO EM "SIM" EM "VARIOS IMPOSTOS" PARA HABILITAR AS CAIXINHAS DE MARCAÇÃO
        if not self.find( "cont_rela_mov_apuracao_varios_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_apuracao_varios_impostos")
        self.click_relative(6, 43)


        if not self.find( "cont_livro_oficial_relatorios_mov_apuracao", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_relatorios_mov_apuracao")
        self.click_relative(74, 29) # LIVRO OFICIAL

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)

        self.tab()
        self.type_down()
        self.tab()

        # IMPOSTOS 

        x = 0
        while x < 7:
            self.space()
            self.type_down()
            x += 1

        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()

        x = 0
        while x < 3:
            self.space()
            self.type_down()
            x += 1
        self.tab()
        self.type_up()
        self.wait(2000)
        if not self.find( "cont_rela_mov_informacoes_do_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_informacoes_do_imposto")
        self.click()

        self.wait(1000)

        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1

        self.wait(1000)
        if not self.find( "cont_rela_mov_observacoes_apuracao", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_observacoes_apuracao")
        self.click() # OBSERVAÇOES
        self.wait(1000)

        self.type_keys_with_interval(100,"qa12!@")
        self.wait(1000)

        if not self.find( "cont_rel_mov_matrical_livros_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_matrical_livros_iss")
        self.click() # MATRICAL

        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_rel_mov_fiscal_livro_iss_fechar_matrical", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fiscal_livro_iss_fechar_matrical")
        self.click()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ############### RELATORIOS -> MOVIMENTO FISCAL -> DEMONSTRATIVO DE RETENÇÕES  #################
        ###############################################################################################
        

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_demonstrativo_retencoes", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_demonstrativo_retencoes")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_data_retencoes", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_data_retencoes")
        self.click_relative(28, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_rela_mov_retencoes_livro_oficial", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_retencoes_livro_oficial")
        self.click_relative(109, 3)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_centro_custo_ini_retencoes", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_centro_custo_ini_retencoes")
        self.click_relative(79, 22)
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)

        self.enter()
        # arquivo vazio

        if not self.find( "cont_rel_mov_centro_custo_final_retencao", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_centro_custo_final_retencao")
        self.click_relative(77, 26)
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(2000)

        self.enter()

        self.tab()
        self.tab()
        self.tab()

        # Movimento
        self.type_right()
        self.type_right()
        self.wait(1000)
        self.tab()
        self.space()
        self.tab()
        
        # NOTAS FISCAIS

        self.type_right()
        self.type_right()
        

        # mouse parando em cima de MATRICAL 
        self.wait(2000)
        #if not self.find( "cont_rel_mov_matrical_livros_iss", matching=0.97, waiting_time=10000):
        #    not_found("cont_rel_mov_matrical_livros_iss")
        self.click()
        self.wait(1000)

        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ########### RELATORIOS -> MOVIMENTO FISCAL -> Relatorio - Diferencial de Aliquota  ############
        ###############################################################################################
        

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_aliquota_diferencial", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_aliquota_diferencial")
        self.click()
        self.wait(1000)

        if not self.find( "cont_data_rela_mov_dif_aliquota", matching=0.97, waiting_time=10000):
            not_found("cont_data_rela_mov_dif_aliquota")
        self.click_relative(26, 6)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.wait(1000)
        self.tab()
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.type_right()
        self.type_right()
        self.tab()
        self.space() # CONSIDERAR DEVOLUÇÕES
        self.wait(1000)

        

        if not self.find( "cont_rela_mov_imprimir_achar_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_imprimir_achar_iss")
        self.click()

        self.wait(1000)
        if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_fechar_cad")
        self.click()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ########################### RELATORIOS -> MOVIMENTO FISCAL -> DIPI  ###########################
        ###############################################################################################
        
        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_mov_fiscal_dipi", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fiscal_dipi")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_mov_fisc_dipi_data", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_dipi_data")
        self.click_relative(28, 8)
        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        self.wait(500)
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"2024")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.tab()
        self.tab()
        self.space()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_fiscal_dipi_livro", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_dipi_livro")
        self.click_relative(44, 30)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()

        self.wait(1000)
        if not self.find( "cont_relatorios_btn_grafico_geral_opc_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_grafico_geral_opc_1")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)


        # botao de grafico nao esta abrindo nenhuma janela

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ########################## RELATORIOS -> MOVIMENTO FISCAL -> GI/ICMS  #########################
        ###############################################################################################


        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_gi_icms", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_gi_icms")
        self.click()

        self.wait(1000)

        if not self.find( "cont_rel_mov_fisc_dipi_data", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_dipi_data")
        self.click_relative(28, 8)
        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        self.wait(500)
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_fiscal_icms_saidas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_saidas")
        self.click()
        self.tab()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_icms_livro", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_icms_livro")
        self.click_relative(45, 29)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(7000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()

        self.wait(2000)
        self.enter()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()



        ###############################################################################################
        ################### RELATORIOS -> MOVIMENTO FISCAL -> RESUMO P/MUNICIPIO  #####################
        ###############################################################################################


        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_resumo_municipio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_resumo_municipio")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_mov_fisc_dipi_data", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_dipi_data")
        self.click_relative(28, 8)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_mov_relatorios_data_ano_atual", matching=0.97, waiting_time=10000):
            not_found("cont_mov_relatorios_data_ano_atual")
        self.click()

        self.tab()
        self.tab()

        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_livro_oficial_resumo_mun", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_livro_oficial_resumo_mun")
        self.click_relative(109, 3)
        self.wait(1000)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        self.tab()
        self.tab()
        self.type_right()
        self.tab()
        self.type_right()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_centro_custo_resumo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_resumo")
        self.click_relative(77, 25)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        # ARQUIVO VAZIO
        self.enter()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_centro_custo_final_resumo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_final_resumo")
        self.click_relative(76, 24)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        # ARQUIVO VAZIO
        self.enter()
        self.wait(1000)

        #if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        #self.click()
        #self.wait(30000)
        # carregamento devagar

        #if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_x_geral_fechar_mat_imp")
        #self.click()
        self.wait(1000)

        #if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_matrical_opc_1_mov")
        #self.click()

        self.wait(2000)
        #if not self.find( "cont_relatorios_mov_matrical_btn_ok", matching=0.97, waiting_time=10000):
        ##    not_found("cont_relatorios_mov_matrical_btn_ok")
        #self.click()
        self.wait(2000)
        #if not self.find( "cont_relatorios_mov_fechar_matricial_btn", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_mov_fechar_matricial_btn")
        #self.click()
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ################# RELATORIOS -> MOVIMENTO FISCAL -> LIVRO DE ISS (DIARIO)  ####################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_livro_de_iss_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_livro_de_iss_diario")
        self.click()

        self.wait(1000)

        if not self.find( "cont_rel_mov_fisc_dipi_data", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_dipi_data")
        self.click_relative(28, 8)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_mov_relatorios_data_ano_atual", matching=0.97, waiting_time=10000):
            not_found("cont_mov_relatorios_data_ano_atual")
        self.click()

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab() 
        self.tab()
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_relatorios_livro_iss_livro_ofc_btn", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_livro_iss_livro_ofc_btn")
        self.click()
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()
        if not self.find( "cont_relatorios_btn_matrical_ok", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_matrical_ok")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_matrical_btn_fechar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_btn_fechar")
        self.click()
        self.wait(1000)
        # BOTAO IMPRIMIR NAO ESTA FUNCIONANDO

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
           not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        ###############################################################################################
        #################### RELATORIOS -> MOVIMENTO FISCAL -> PIS/COFINS LUCRO  ######################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_fiscal_pis_cofins_lucro", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_pis_cofins_lucro")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_data_relatorios_pis_cofins", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_pis_cofins")
        self.click_relative(27, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_right()
        # BOTAO IMPRIMIR NAO ESTA FUNCIONANDO

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        ###############################################################################################
        #################### RELATORIOS -> MOVIMENTO FISCAL -> PIS/COFINS POR ITENS  ######################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_fiscal_pis_cofins_itens_ncm", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_pis_cofins_itens_ncm")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_data_relatorios_pis_cofins", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_pis_cofins")
        self.click_relative(27, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(2000)

        # tempo de carregamento muito longo

        #if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        #self.click()
        #self.wait(5000)

        #if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_x_geral_fechar_mat_imp")
        #self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        
        ###############################################################################################
        ################ RELATORIOS -> MOVIMENTO FISCAL -> LIVROS PARA COD FISCAL  ####################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_fiscal_livros_p_cod_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_livros_p_cod_fiscal")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_data_relatorios_pis_cofins", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_pis_cofins")
        self.click_relative(27, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.tab()
        self.type_right()
        self.tab()
        x = 0
        while x < 4:
            self.space()
            self.type_down()
            x += 1
        self.wait(500)
        self.space()
        self.tab()

        x = 0
        while x < 5:
            self.space()
            self.type_down()
            x += 1
        self.wait(500)
        self.space()
        self.tab()
        self.wait(1000)

        if not self.find( "cont_relatorios_centro_custo_inicial_emissao_livr", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_centro_custo_inicial_emissao_livr")
        self.click_relative(181, 3)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_rel_fiscal_emissao_livro_centro_final", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_emissao_livro_centro_final")
        self.click_relative(181, 6)
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_right()
        self.tab()
        self.wait(1000)

        if not self.find( "cont_rel_fiscal_emissao_livros_ofc_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_emissao_livros_ofc_rel")
        self.click_relative(105, 5)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        self.wait(1000)
        
        # mouse parando em cima de MATRICAL, apenas clicar 

        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()
        self.wait(3000)
        if not self.find( "cont_relatorios_btn_matrical_ok", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_matrical_ok")
        self.click()
        self.wait(2000)
        
        #if not self.find( "cont_relatorios_matrical_btn_fechar", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_matrical_btn_fechar")
        #self.click()
        # AQUI ESTA DANDO UM ERRO, VERIFICAR DEPOIS, POR ENQUANTO APERTAR ENTER
        self.enter()
        self.wait(1000)

        

        #if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
         #   not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        #self.click()
        self.wait(5000)
        #if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
         #   not_found("cont_relatorios_x_geral_fechar_mat_imp")
        #self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        
        ###############################################################################################
        ################## RELATORIOS -> MOVIMENTO FISCAL -> FATURAMENTO EMPRESA  #####################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_fiscal_faturamento_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_faturamento_empresa")
        self.click()

        if not self.find( "cont_btn_data_relatorios_pis_cofins", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_pis_cofins")
        self.click_relative(27, 8)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_mov_fiscal_nao_fat_semanal", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fiscal_nao_fat_semanal")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ############### RELATORIOS -> MOVIMENTO FISCAL -> DME - DECLARACAO MOVIMENTO ##################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_mov_dme_declaracao", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_dme_declaracao")
        self.click()

        self.wait(2000)
        self.type_keys_with_interval(100,"2024")

        if not self.find( "cont_rela_mov_imprimir_achar_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_imprimir_achar_iss")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)

        ###############################################################################################
        ################## RELATORIOS -> MOVIMENTO FISCAL -> CONTROLE DE IMPOSTOS #####################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_mov_controle_de_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_controle_de_impostos")
        self.click()

        self.wait(2000)
        self.type_keys_with_interval(100,"2024")
        self.tab()
        self.tab()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_right()
        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)


        ###############################################################################################
        ############## RELATORIOS -> MOVIMENTO FISCAL -> MOVIMENTO DE ITENS - IMPOSTOS ################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_mov_movimento_de_itens_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_movimento_de_itens_imposto")
        self.click()

        if not self.find( "cont_rel_data_mov_fiscal_itens_imp", matching=0.97, waiting_time=10000):
            not_found("cont_rel_data_mov_fiscal_itens_imp")
        self.click_relative(31, 8)
        self.wait(1000)
        if not self.find( "cont_data_relatorios_carregar_semana", matching=0.97, waiting_time=10000):
            not_found("cont_data_relatorios_carregar_semana")
        self.click()
        self.wait(1000)
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.tab()
        self.space()

        # A IMPRESSAO NAO ESTA ABRINDO DIRETAMENTE 
        #if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        #self.click()

        self.wait(3000)

        #if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_x_geral_fechar_mat_imp")
        #self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)


        ###############################################################################################
        ################### RELATORIOS -> MOVIMENTO FISCAL -> APURAÇÃO DE IRPJ  #######################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_fisc_apuracao_irpj", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fisc_apuracao_irpj")
        self.click()

        self.wait(1000)

        self.type_keys_with_interval(100,"2024")
        self.tab()
        self.type_right()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)


        ###############################################################################################
        ############### RELATORIOS -> MOVIMENTO FISCAL -> APURAÇÃO SIMPLES NACIONAL  ##################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_fisc_apuracao_simples_nac", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fisc_apuracao_simples_nac")
        self.click()

        self.wait(2000)

        self.type_keys_with_interval(100,"2024")
        self.tab()
        self.type_right()
        self.wait(2000)
        self.tab()
        self.type_right()
        self.wait(1000)


        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)

        
        ###############################################################################################
        ################## RELATORIOS -> MOVIMENTO FISCAL -> LIVRO REG CONTROLE  ######################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_fisc_livro_reg_controle", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fisc_livro_reg_controle")
        self.click()
        self.wait(2000)
        if not self.find( "cont_rela_mov_fiscal_data_livro_reg", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fiscal_data_livro_reg")
        self.click_relative(27, 7)
        self.wait(2000)

        if not self.find( "cont_mov_carregar_mes_data", matching=0.97, waiting_time=10000):
            not_found("cont_mov_carregar_mes_data")
        self.click()
        self.wait(1000)
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        
        self.tab()
        self.type_keys_with_interval(100,"1")

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(45000)

        if not self.find( "cont_cons_mov_x_fechar", matching=0.97, waiting_time=10000):
            not_found("cont_cons_mov_x_fechar")
        self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        
        ###############################################################################################
        ############## RELATORIOS -> MOVIMENTO FISCAL -> MOVIMENTO DE ITENS - FISCAL  #################
        ###############################################################################################


        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rela_mov_fisc_movimento_itens_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fisc_movimento_itens_fiscal")
        self.click()

        self.wait(1000)

        if not self.find( "cont_rela_mov_fiscal_data_livro_reg", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_fiscal_data_livro_reg")
        self.click_relative(27, 7)
        self.wait(2000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.space()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(5000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)

        
        ###############################################################################################
        ########### RELATORIOS -> MOVIMENTO FISCAL -> DEMONSTRATIVO CREDITOS INFORMADO  ###############
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_movimento_fiscal_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_mov_fisc_demonstrativo_cred", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_demonstrativo_cred")
        self.click()

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(7000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)

        
        ###############################################################################################
        ######################## RELATORIOS -> MOVIMENTO CONTABIL -> LOTES  ###########################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()

        if not self.find( "cont_relatorios_mov_cont_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_lotes")
        self.click()
        self.wait(1000)

        if not self.find( "cont_data_relatorios_mov_cont_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_data_relatorios_mov_cont_lotes")
        self.click_relative(29, 8)
        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        if not self.find( "cont_rel_mov_contabil_lote_rela", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_contabil_lote_rela")
        self.click_relative(129, 3)

        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_mov_cont_livro_oficial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_cont_livro_oficial_rel")
        self.click_relative(102, 5)
        self.wait(2000)

        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()
        self.wait(2000)
        self.enter()

        # REGISTRO NAO ENCONTRADO, APENAS CONTINUAR

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        self.wait(2000)
        
        
        ###############################################################################################
        ###################### RELATORIOS -> MOVIMENTO CONTABIL -> BALANCETE  #########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_balancete", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_balancete")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relatorios_mov_contabil_periodo_data_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_contabil_periodo_data_rel")
        self.click_relative(223, 26)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.wait(2000)

        if not self.find( "cont_relatorios_mov_cont_periodo_anterior_data", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_periodo_anterior_data")
        self.click_relative(218, 26)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"10")
        self.tab()

        if not self.find( "cont_rela_mov_cont_grupo_empresa_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_cont_grupo_empresa_rel")
        self.click_relative(54, 24)

        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_mov_cont_reduzido_inicial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_cont_reduzido_inicial_rel")
        self.click_relative(137, 2)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_reduzido_final_relatorio_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_reduzido_final_relatorio_mov_contabil")
        self.click_relative(133, 5)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_cont_livro_oficial_rel_balancete", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_livro_oficial_rel_balancete")
        self.click_relative(108, 4)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_contabil_moedas_rel_balancete", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_contabil_moedas_rel_balancete")
        self.click_relative(49, 23)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)
        # MOEDA NESTA DATABASE NAO TEM COTAÇÃO, O QUE FAZ COM QUE "IMPRIMIR" NAO ABRA NADA
        # POR ENQUANTO APAGAR A MOEDA
        self.backspace()
        self.wait(1000)


        if not self.find( "cont_relatorios_mov_contabil_obs_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_contabil_obs_rel")
        self.click_relative(465, 29)
        self.wait(2000)
        if not self.find( "cont_rela_mov_cont_localizar_observacoes", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_cont_localizar_observacoes")
        self.click()

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(10000)
        # relatorio abrindo porem fechando, solução no momento vai ser abrir pela barra de tarefas do windows
        # esta solução não é ideal pois pode variar sempre

        if not self.find( "cont_barra_tarefas_buscar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_barra_tarefas_buscar_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_balancete_de_verificacao_barra", matching=0.97, waiting_time=10000):
            not_found("cont_balancete_de_verificacao_barra")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        
        ###############################################################################################
        ################### RELATORIOS -> MOVIMENTO CONTABIL -> RAZAO ANALITICO  ######################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_cont_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_razao_analitico")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_contabil_data_rel_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_contabil_data_rel_razao_analitico")
        self.click_relative(27, 5)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"10")

        if not self.find( "cont_relatorios_reduzido_razao_analitico_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_reduzido_razao_analitico_rel")
        self.click_relative(186, 2)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_grupo_empresa_rel_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_grupo_empresa_rel_razao_analitico")
        self.click_relative(145, 3)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_livro_oficial_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_livro_oficial_razao_analitico")
        self.click_relative(109, 2)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_btn_matrical_razao_analitica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_matrical_razao_analitica")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_impressao_relatorios")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_retornar_relatorios_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_btn_retornar_relatorios_razao_analitico")
        self.click()





        
        ###############################################################################################
        ####################### RELATORIOS -> MOVIMENTO CONTABIL -> DIARIO  ###########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_cont_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_diario")
        self.click()

        if not self.find( "cont_relatorios_mov_cont_diario_data_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_diario_data_rel")
        self.click_relative(30, 7)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_grupo_empresa_diario_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_grupo_empresa_diario_rel")
        self.click_relative(42, 29)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_livro_oficial_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_livro_oficial_diario")
        self.click_relative(67, 25)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        # MATRICIAL NAO ESTA ABRINDO AUTOMATICAMENTE, POR ENQUANTO DEIXAR COMENTADO, ESPERAR FUTURAS VERSOES
        # 02/08/24

        #if not self.find( "cont_btn_relatorios_matricial_diario", matching=0.97, waiting_time=10000):
        #   not_found("cont_btn_relatorios_matricial_diario")
        #self.click()
        self.wait(2000)
        #if not self.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_ok_impressao_relatorios")
        #self.click()

        self.wait(3000)

        #if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_fechar_relatorios_matrical_impr")
        #self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_btn_grafica_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_grafica_diario")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_diario_btn_retornar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_diario_btn_retornar")
        self.click()

        
        ###############################################################################################
        ####################### RELATORIOS -> MOVIMENTO CONTABIL -> BALANÇO  ##########################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_balanco")
        self.click()

        if not self.find( "cont_relatorios_mov_cont_periodo_atual_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_periodo_atual_balanco")
        self.click_relative(217, 25)
        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_periodo_anterior_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_periodo_anterior_balanco")
        self.click_relative(216, 25)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_reduzido_ini_balanco_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_reduzido_ini_balanco_relatorios")
        self.click_relative(134, 4)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_reduzido_final_btn_balanco_rel", matching=0.97, waiting_time=10000):
            not_found("cont_reduzido_final_btn_balanco_rel")
        self.click_relative(135, 6)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_grupo_empresa_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_grupo_empresa_balanco")
        self.click_relative(141, 3)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)
        if not self.find( "cont_livro_oficial_btn_relatorios_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_btn_relatorios_balanco")
        self.click_relative(109, 5)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_moedas_balanco_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_moedas_balanco_rel")
        self.click_relative(55, 31)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)
        # MOEDA NAO EXISTENTE, APENAS APAGAR
        self.backspace()

        #if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
        ##    not_found("cont_relatorios_matrical_opc_1_mov")
        #self.click()
        self.wait(2000)
        if not self.find( "cont_btn_grafica_relatorios_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafica_relatorios_balanco")
        self.click()

        # TEMPO DE ESPERA ESTA GRANDE PARA ABRIR O RELATORIO
        self.wait(180000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ############# RELATORIOS -> MOVIMENTO CONTABIL -> Demonstrativo de resultados  ################
        ###############################################################################################

        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_demo_resultados", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_demo_resultados")
        self.click()
        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)


        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_periodo_2_mov_demo_res", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_periodo_2_mov_demo_res")
        self.click_relative(221, 24)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_livro_oficial_demo_res_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_demo_res_relatorios")
        self.click_relative(46, 30)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_grupo_de_empresa_relatorios_demo_res", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_relatorios_demo_res")
        self.click_relative(53, 30)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_moedas_demo_res", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_moedas_demo_res")
        self.click_relative(49, 24)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        # MOEDA NAO ESTA DISPONIVEL, APAGAR E CONTINUAR
        self.backspace()

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ###############################################################################################
        ####################### RELATORIOS -> MOVIMENTO CONTABIL -> D.L.P.A  ##########################
        ###############################################################################################
        self.wait(2000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_contabil_dlpa", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_contabil_dlpa")
        self.click()

        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_livro_oficial_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_livro_oficial_dlpa_relatorios")
        self.click_relative(43, 32)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        if not self.find( "cont_grupo_de_empresa_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_dlpa_relatorios")
        self.click_relative(53, 34)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ###############################################################################################
        ############### RELATORIOS -> MOVIMENTO CONTABIL -> GERENCIAIS -> BALANCETE   #################
        ###############################################################################################
        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_gerenciais_centro", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_gerenciais_centro")
        self.click()
        
        ######### existem dois botoes balancete, clicar relativo aqui pra funcionar no certo ###########
        if not self.find( "cont_relativo_balancete_gerencial_dlpa", matching=0.97, waiting_time=10000):
            not_found("cont_relativo_balancete_gerencial_dlpa")
        self.click_relative(264, 27)

        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_gerenc_balan_grupo_empresas", matching=0.97, waiting_time=10000):
            not_found("cont_rel_gerenc_balan_grupo_empresas")
        self.click_relative(55, 26)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_geren_balancete_conta_inicial", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_geren_balancete_conta_inicial")
        self.click_relative(201, 1)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_gerenc_balanc_conta_final", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_gerenc_balanc_conta_final")
        self.click_relative(194, 3)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()
        # TEMPO DE DEMORA MUITO LONGO
        self.wait(180000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()



        

        ###############################################################################################
        ################## RELATORIOS -> MOVIMENTO CONTABIL -> GERENCIAIS -> RAZAO  ###################
        ###############################################################################################
        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_gerenciais_centro", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_gerenciais_centro")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relat_mov_cont_razao_gerenciais", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_cont_razao_gerenciais")
        self.click()

        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_rel_gerenc_balan_grupo_empresas", matching=0.97, waiting_time=10000):
            not_found("cont_rel_gerenc_balan_grupo_empresas")
        self.click_relative(55, 26)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ################# RELATORIOS -> MOVIMENTO CONTABIL -> GERENCIAIS -> DIARIO   ##################
        ###############################################################################################
        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_cont_gerenciais_centro", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_gerenciais_centro")
        self.click()

        if not self.find( "cont_relatorios_mov_cont_gerencial_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_gerencial_diario")
        self.click()

        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_grafica_diario_02", matching=0.97, waiting_time=10000):
            not_found("cont_relat_grafica_diario_02")
        self.click()
        self.wait(20000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(15000)

        if not self.find( "cont_btn_relatorios_retornar_rela_diario_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_relatorios_retornar_rela_diario_24")
        self.click()
        
        
        
        ###############################################################################################
        ############### RELATORIOS -> MOVIMENTO CONTABIL -> Razão Ordem Alfabetica   ##################
        ###############################################################################################
        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_mov_cont_razao_ordem", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_razao_ordem")
        self.click()

        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"07062024")
        self.tab()


        if not self.find( "cont_relatorios_reduzido_razao_analitico_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_reduzido_razao_analitico_rel")
        self.click_relative(186, 2)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        x = 0 
        while x < 4:
            self.type_down()
            x += 1
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_grupo_empresa_rel_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_grupo_empresa_rel_razao_analitico")
        self.click_relative(145, 3)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_livro_oficial_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_livro_oficial_razao_analitico")
        self.click_relative(109, 2)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        if not self.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_impressao_relatorios")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ############# RELATORIOS -> MOVIMENTO CONTABIL -> Movimento cliente/fornecedor  ###############
        ###############################################################################################
        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_mov_cont_mov_cliente_forn", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_cont_mov_cliente_forn")
        self.click()
        self.wait(1000)

        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        if not self.find( "cont_relat_mov_cont_cliente_forn_grupo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_cont_cliente_forn_grupo")
        self.click_relative(54, 24)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafica_relatorios_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafica_relatorios_balanco")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ################ RELATORIOS -> MOVIMENTO CONTABIL -> Extrato Conta capital  ###################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_mov_cont_extrato_conta_capit", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_cont_extrato_conta_capit")
        self.click()
        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        if not self.find( "cont_relat_mov_cont_cliente_forn_grupo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_cont_cliente_forn_grupo")
        self.click_relative(54, 24)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        self.wait(1000)

        if not self.find( "cont_btn_grafica_relatorios_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafica_relatorios_balanco")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ################### RELATORIOS -> MOVIMENTO CONTABIL -> Livros Oficiais  ######################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_movimento_contabil_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_contabil_relatorios")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_mov_cont_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_cont_livros_oficiais")
        self.click()

        self.wait(1000)
        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()

        self.wait(1000)
        if not self.find( "cont_relat_mov_cont_cliente_forn_grupo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_mov_cont_cliente_forn_grupo")
        self.click_relative(54, 24)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)
        
        x = 0
        while x < 3:
            self.tab()
            x += 1
        
        self.type_keys_with_interval(100,"teste_livro")

        if not self.find( "cont_btn_lupa_livros_oficiais_relat", matching=0.97, waiting_time=10000):
            not_found("cont_btn_lupa_livros_oficiais_relat")
        self.click()

        if not self.find( "cont_relat_livros_localizar_obs_f10", matching=0.97, waiting_time=10000):
            not_found("cont_relat_livros_localizar_obs_f10")
        self.click()
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()

        self.wait(2000)

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        # A IMPRESSAO APARECE NOVAMENTE E CARREGA UM TEMPO. ESPERAR E APENAS CLICAR NOVAMENTE NO X
        self.wait(5000)
        self.click()

        # AS VEZES APARECE UM ERRO DE EXCESSAO, APENAS APERTAR ENTER
        self.enter()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ############## RELATORIOS -> Conferencias -> Conferencias de notas fiscais  ###################
        ###############################################################################################


        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conferencias_1", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferencias_1")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relat_conferencias_notas_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferencias_notas_fiscais")
        self.click()

        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relator_conf_conf_nota_fiscal_codigo", matching=0.97, waiting_time=10000):
            not_found("cont_relator_conf_conf_nota_fiscal_codigo")
        self.click_relative(54, 23)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_conf_centro_de_custo_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_rela_conf_centro_de_custo_fiscal")
        self.click_relative(80, 23)
        self.wait(1000)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        #if not self.find( "cont_relat_conf_codigo_fiscal_rel", matching=0.97, waiting_time=10000):
        #    not_found("cont_relat_conf_codigo_fiscal_rel")
        #self.click_relative(66, 21)

        #self.wait(1000)
        #if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
        #    not_found("cont_localizar_btn_relatorios_mov_contabil")
        #self.click() 
        self.wait(1000)
        #if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_selecionar_relatorios_mov_cont")
        #self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conferen_reduz_inicial", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferen_reduz_inicial")
        self.click_relative(137, 4)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        x = 0
        while x < 4:
            self.type_down()
            x += 1

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conf_reduzido_final_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conf_reduzido_final_fisc")
        self.click_relative(134, 3)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        x = 0
        while x < 4:
            self.type_down()
            x += 1

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()
        self.wait(5000)
        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ############### RELATORIOS -> Conferencias -> CARTAS DE CORREÇÃO EMITIDAS  ####################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conferencias_1", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferencias_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_conf_carta_correcao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_conf_carta_correcao")
        self.click()

        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()

        self.wait(5000)
        # abre uma janelinha de impressao, fechar com esc
        self.key_esc()


        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ################# RELATORIOS -> Conferencias -> EFD REINF - REGISTROS 4000  ###################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conferencias_1", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferencias_1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_conferencia_efd_reinf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conferencia_efd_reinf")
        self.click()

        if not self.find( "cont_periodo_relatorios_mov_demo_res_data", matching=0.97, waiting_time=10000):
            not_found("cont_periodo_relatorios_mov_demo_res_data")
        self.click_relative(216, 24)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_grupo_empresa_efd_reinf", matching=0.97, waiting_time=10000):
            not_found("cont_rel_grupo_empresa_efd_reinf")
        self.click_relative(56, 21)

        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)
        # a janela abre novamente instantaneamente, apenas clicar de novo para selecionar
        self.click()
        self.wait(1000)

        ##########################################################
        ## relatorios de EFD REINF REGISTRO 4000 NAO ENCONTRADO ##
        ##########################################################

        #if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
        #    not_found("cont_btn_grafico_dlpa_relatorios")
        #self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ################################# RELATORIOS -> DOCUMENTOS  ###################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_documentos", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_documentos")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()

        self.wait(2000)
        self.key_esc()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ########################### RELATORIOS -> RECOLHIMENTOS -> DARF  ##############################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_recolhimentos_menu", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_recolhimentos_menu")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_recolhimento_darf", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_recolhimento_darf")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relativo_darf_relatorios_empresa_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_relativo_darf_relatorios_empresa_bsc")
        self.click_relative(219, -3)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)
        if not self.find( "cont_recolhimento_rel_darf_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_recolhimento_rel_darf_imposto")
        self.click_relative(94, 9)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        x = 0
        while x < 9:
            self.tab()
            x +=1 
        
        x = 0
        while x < 6:
            self.type_keys_with_interval(100,"100")
            self.tab()
            x += 1
        
        self.wait(2000)
        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(2000)
        
        if not self.find( "cont_botao_close_impressao", matching=0.97, waiting_time=10000):
            not_found("cont_botao_close_impressao")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_gravar_documento_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_relat_gravar_documento_emissao")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_ok_gravacao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_gravacao")
        self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ###############################################################################################
        ########################### RELATORIOS -> RECOLHIMENTOS -> GR-PR  #############################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_recolhimentos_menu", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_recolhimentos_menu")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_recolhimentos_grpr", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_recolhimentos_grpr")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_emissao_grpr_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_grpr_empresa")
        self.click_relative(44, 19)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(3000)
        if not self.find( "cont_botao_close_impressao", matching=0.97, waiting_time=10000):
            not_found("cont_botao_close_impressao")
        self.click()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ###############################################################################################
        ############################# RELATORIOS -> PATRIMONIOS ->  RAZÃO #############################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_patrimonio_menu", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_patrimonio_menu")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_patrimonio_razao", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_patrimonio_razao")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rel_patro_conta_inicial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rel_patro_conta_inicial_rel")
        self.click_relative(141, 2)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_patro_conta_final_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rela_patro_conta_final_rel")
        self.click_relative(140, 5)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()
        self.wait(5000)

        if not self.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        self.click()

        self.wait(1000)


        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        
        ###############################################################################################
        ########################### RELATORIOS -> PATRIMONIOS ->  CIAP(ICMS) ##########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_patrimonio_menu", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_patrimonio_menu")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relato_patrimonio_ciap_icms", matching=0.97, waiting_time=10000):
            not_found("cont_relato_patrimonio_ciap_icms")
        self.click()

        if not self.find( "cont_rel_patro_conta_inicial_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rel_patro_conta_inicial_rel")
        self.click_relative(141, 2)
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_rela_patro_conta_final_rel", matching=0.97, waiting_time=10000):
            not_found("cont_rela_patro_conta_final_rel")
        self.click_relative(140, 5)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()

        self.wait(15000)

        if not self.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()

        if not self.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_impressao_relatorios")
        self.click()
        self.wait(3000)

        if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        self.click()

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        
        ###############################################################################################
        ########################### RELATORIOS -> PATRIMONIOS ->  ETIQUETAS ###########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_patrimonio_menu", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_patrimonio_menu")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_patrimonio_etiquetas", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_patrimonio_etiquetas")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relat_patrimonio_btn_adicionar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_patrimonio_btn_adicionar")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_seleciona_patrimonio_etiqueta", matching=0.97, waiting_time=10000):
            not_found("cont_btn_seleciona_patrimonio_etiqueta")
        self.click_relative(22, 23)

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_patrimonio_etiqueta_2_impress", matching=0.97, waiting_time=10000):
            not_found("cont_relat_patrimonio_etiqueta_2_impress")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relat_patri_selec_impressora", matching=0.97, waiting_time=10000):
            not_found("cont_relat_patri_selec_impressora")
        self.click_relative(213, 25)

        self.wait(1000)
        self.type_down()
        self.enter()

        if not self.find( "cont_btn_impressao_relat_patri", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impressao_relat_patri")
        self.click()
        # aqui esta acontecendo 2 erros ao tentar imprimir, por enquanto apertar enter nos dois
        self.wait(2000)
        self.enter()
        self.wait(4000)
        self.enter()


        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ######################### RELATORIOS -> EMISSÕES -> VALIDA-PR/SINTEGRA ########################
        ###############################################################################################

        # ESTA PARTE DAS EMISSÕES, JOGARÁ AS GERAÇÕES EM UMA PASTA QUE FOI CRIADA NA ÁREA DE TRABALHO COM
        # O NOME DE "GERAÇÕES RELATORIO CONTABIL"


        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_valida_pr_sintegra", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_valida_pr_sintegra")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_emissoes_integra_empresa_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_integra_empresa_inf")
        self.click_relative(44, 23)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_btn_emissao_data_periodo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_btn_emissao_data_periodo")
        self.click_relative(215, 22)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_btn_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(63000) # espera da geração do arquivo de 1 min
        if not self.find( "cont_btn_arquivo_gerado_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_btn_arquivo_gerado_sucesso")
        self.click_relative(308, 47)

        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ######################### RELATORIOS -> EMISSÕES -> GIAD ########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_giad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_giad")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_relator_emissao_giad_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_btn_relator_emissao_giad_empresa")
        self.click_relative(43, 22)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(3000)

        if not self.find( "cont_btn_importar_emissoes_rel_giad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_importar_emissoes_rel_giad")
        self.click()
        self.wait(3000)

        if not self.find( "cont_btn_import_com_sucesso_ok", matching=0.97, waiting_time=10000):
            not_found("cont_btn_import_com_sucesso_ok")
        self.click_relative(301, 47)
        self.wait(1000)
        if not self.find( "cont_btn_gerar_relator_emissao_giad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_gerar_relator_emissao_giad")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(3000)

        if not self.find( "cont_btn_arquivo_gerado_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_btn_arquivo_gerado_sucesso")
        self.click_relative(308, 47)
        self.wait(2000)
        if not self.find( "cont_btn_impressao_relat_patri", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impressao_relat_patri")
        self.click()
        self.wait(1000)
        if not self.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_impressao_relatorios")
        self.click()

        if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        self.click()


        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ############################# RELATORIOS -> EMISSÕES -> SISCRED ###############################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_siscred", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_siscred")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_emissoes_integra_empresa_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_integra_empresa_inf")
        self.click_relative(44, 23)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_btn_emissao_data_periodo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_btn_emissao_data_periodo")
        self.click_relative(215, 22)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_mov_modalidade_acumulo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_modalidade_acumulo")
        self.click()

        if not self.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_btn_gerar")
        self.click()
        self.wait(2000)
        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(5000) # tempo de geração ( Esta curto pois nao tem dados na base Ictus)


        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ############################### RELATORIOS -> EMISSÕES -> DFC #################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()

        self.wait(1000)

        if not self.find( "cont_relat_emissoes_dfc", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dfc")
        self.click()

        self.wait(2000)

        if not self.find( "cont_relat_emissoes_integra_empresa_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_integra_empresa_inf")
        self.click_relative(44, 23)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_btn_emissao_data_periodo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_btn_emissao_data_periodo")
        self.click_relative(215, 22)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_emissoes_dfc_tipo_do_documento", matching=0.97, waiting_time=10000):
            not_found("cont_emissoes_dfc_tipo_do_documento")
        self.click_relative(221, 24)
        self.wait(1000)
        self.type_down()
        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_btn_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(5000)

        if not self.find( "cont_btn_arquivo_gerado_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_btn_arquivo_gerado_sucesso")
        self.click_relative(308, 47)
        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ############################### RELATORIOS -> EMISSÕES -> SISS ################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_emissoes_siss", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_siss")
        self.click()

        self.wait(2000)

        if not self.find( "cont_relat_emissoes_integra_empresa_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_integra_empresa_inf")
        self.click_relative(44, 23)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_btn_emissao_data_periodo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_btn_emissao_data_periodo")
        self.click_relative(215, 22)
        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        # A GERAÇÃO DO SISS ESTA COM PROBLEMA, ALGUMAS VEZES GERA E OUTRAS NÃO

        # if not self.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
        #     not_found("cont_relatorios_emissao_btn_gerar")
        # self.click()
        # self.wait(2000)

        # if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
        #     not_found("cont_emissao_gerar_area_de_trab")
        # self.click()
        # self.wait(1000)
        # if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
        #     not_found("cont_achar_pasta_area_trab_geracao_rel")
        # self.double_click()
        # self.wait(1000)
        # if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
        #     self("cont_btn_salvar_emissao_geracao")
        # self.click()
        # self.wait(5000)

        # if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
        #     not_found("cont_relat_emissoes_btn_ok_gerar")
        # self.click()
        # self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ############################### RELATORIOS -> EMISSÕES -> DIME ################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_emissoes_dime", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_emissoes_dime_empresa_info", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_empresa_info")
        self.click_relative(45, 22)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        # bota de calcular nao esta calculando por enquanto, apenas usar para tirar mouse de cima de importar
        if not self.find( "cont_relat_emissoes_dime_calcular", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_calcular")
        self.click()

        if not self.find( "cont_relatorios_emissoes_dime_importar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_dime_importar")
        self.click()
        self.wait(2000)
        self.enter()
        # NAO ESTA DANDO PARA GERAR, POR ENQUANTO APENAS APERTAR ENTER
        #if not self.find( "cont_relat_emissoes_dime_imp_sucesso", matching=0.97, waiting_time=10000):
        #    not_found("cont_relat_emissoes_dime_imp_sucesso")
        #self.click_relative(306, 48)

        self.wait(1000)
        if not self.find( "cont_relat_emissoes_dime_gerar_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_gerar_inf")
        self.click()
        self.wait(5000)
        if not self.find( "cont_relat_emissao_inf_gerada_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_inf_gerada_sucesso")
        self.click_relative(306, 49)
        self.wait(2000)

        if not self.find( "cont_relat_emissoes_dime_gerar_arquivo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_gerar_arquivo")
        self.click()

        self.wait(2000)
        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(5000)

        if not self.find( "cont_btn_geracao_ok_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_geracao_ok_emissao")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_impressao_relat_emissao_demi", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impressao_relat_emissao_demi")
        self.click()

        if not self.find( "cont_impressao_grafica_relat_emissao_demi", matching=0.97, waiting_time=10000):
            not_found("cont_impressao_grafica_relat_emissao_demi")
        self.click()

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        ###############################################################################################
        ############################### RELATORIOS -> EMISSÕES -> DIEF ################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_emissao_dief", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_dief")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relat_emissoes_dime_empresa_info", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_empresa_info")
        self.click_relative(45, 22)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relatorios_emissoes_dime_importar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_dime_importar")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relat_emissoes_dime_imp_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_imp_sucesso")
        self.click_relative(306, 48)

        if not self.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_btn_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(5000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        ###############################################################################################
        ######################### RELATORIOS -> EMISSÕES -> DIRF(RETENÇÕES) ###########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_emissoes_princ", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_princ")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relat_emissoes_dirf_ret", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dirf_ret")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_emissao_dirf_empresa_gerac", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_dirf_empresa_gerac")
        self.click_relative(49, 26)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_emissao_empresa_dirf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_empresa_dirf")
        self.click_relative(47, 24)

        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 

        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_relat_emissao_dirf_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_dirf_gerar")
        self.click()

        if not self.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        self.click()
        self.wait(1000)
        if not self.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        self.double_click()
        self.wait(1000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            self("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(5000)
        if not self.find( "cont_btn_arquivo_gerado_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_btn_arquivo_gerado_sucesso")
        self.click_relative(308, 47)
        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        
        ###############################################################################################
        ############################### RELATORIOS -> RELATORIO LMP ###################################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_relatorio_lmp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_relatorio_lmp")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_data_relatorios_lmp", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_lmp")
        self.click_relative(26, 7)
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()

        self.wait(20000)

        if not self.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        self.click()

        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)


        ###############################################################################################
        ######################### RELATORIOS -> RELATORIO DE MAPA RESUMO ECF ##########################
        ###############################################################################################

        self.wait(3000)

        if not self.find( "cont_relatorios_menu_principal_2", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_menu_principal_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_mapa_resumo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mapa_resumo")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_data_relatorios_lmp", matching=0.97, waiting_time=10000):
            not_found("cont_btn_data_relatorios_lmp")
        self.click_relative(26, 7)
        self.wait(1000)

        self.wait(1000)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        self.wait(2000)

        if not self.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        self.click()

        self.wait(10000)

        if not self.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        self.click()

        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)

        #######################################################################################
        ############################## FINAL RELATÓRIOS CONTABIL ##############################
        #######################################################################################


        ################################################################################################
        ################################################################################################
        ############################## COMEÇO DE IMPORTAÇÃO/EXPORTAÇÕES ################################
        ################################################################################################
        ################################################################################################


        ################################################################################################
        ################################ PADRÃO TEOREMA (EXPORTAÇÃO) ###################################
        ################################################################################################
        
        self.wait(3000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        if not self.find( "cont_importacao_exportacao_pad_teo_ex", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_pad_teo_ex")
        self.click()

        if not self.find( "cont_importacao_exportacao_data_rel", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_data_rel")
        self.click_relative(28, 6)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()

        if not self.find( "cont_cadastros_movimentos_rel_importacao", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_movimentos_rel_importacao")
        self.click_relative(13, 21)
        self.wait(1000)
        if not self.find( "cont_cadastro_movimento_impo_flecha", matching=0.97, waiting_time=10000):
            not_found("cont_cadastro_movimento_impo_flecha")
        self.click()
        # MANDAR ARQUIVO PARA "ARQUIVOS SELECIONADOS"
        self.wait(2000)

        if not self.find( "cont_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(2000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(13000) # tempo de espera de geração
        # ARQUIVO GERADO COM SUCESSO
        if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ################################################################################################
        ################################ PADRÃO TEOREMA (IMPORTAÇÃO) ###################################
        ################################################################################################
        
        self.wait(3000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()

        if not self.find( "cont_teorema_importacao_expor_import", matching=0.97, waiting_time=10000):
            not_found("cont_teorema_importacao_expor_import")
        self.click()

        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.space()
        self.type_down()
        self.space()
        self.tab()

        if not self.find( "cont_imp_export_conferencia_fisc", matching=0.97, waiting_time=10000):
            not_found("cont_imp_export_conferencia_fisc")
        self.click_relative(86, 29)
        # CONFERINDO SE OS DOIS ESTAO MARCADOS, AI CLICA NO MODELO MOEDA ^^^ 

        if not self.find( "cont_imp_exp_modelo_moeda_rel_bsc", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_modelo_moeda_rel_bsc")
        self.click_relative(-369, 69)
        # CONFERINDO SE MODELO MOEDA ESTA DESMARCADO COMO DEVE, AI CLICA NO PLANO DE CONTAS ^^^

        if not self.find( "cont_imp_exp_importa_alterados_check", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_importa_alterados_check")
        self.click_relative(-31, 68)
        # CONFERINDO SE "ALTERADOS" ESTA MARCADO, AI CLICA NO BOTAO DE BUSCA "CLIENTE CONSUMIDOR" ^^^^ 
    
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        x = 0
        while x< 21:
            self.type_down()
            x += 1

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_importacoes_exportacoes_livros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_exportacoes_livros_fiscais")
        self.click()

        if not self.find( "cont_imp_exp_reducoes_z", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_reducoes_z")
        self.click()
        self.wait(1000)
        if not self.find( "cont_imp_exp_cont_rel_plano_de_contas", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_cont_rel_plano_de_contas")
        self.click_relative(162, 5)
        # CONFERE SE CONTABILIDADE FOI DESMARCADA E CLICA EM PLANO DE CONTAS
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)

        # ESTA PARTE VAI PEGAR TELA DA MINHA MAQUINA, ENTÃO SÓ VAI FUNCIONAR CORRETAMENTE NESTA MAQUINA,
        # ALTERAR EM CASO DE TESTES EM OUTRA MAQUINA

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(3000)
        
        if not self.find( "cont_botao_abrir_clifor_txt", matching=0.97, waiting_time=10000):
            not_found("cont_botao_abrir_clifor_txt")
        self.click()
        self.wait(4000)
        
        
        if not self.find( "cont_importar_imp_exp_txt", matching=0.97, waiting_time=10000):
            not_found("cont_importar_imp_exp_txt")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(40000)
        # tempo de espera importação

        # Cadastro de lotes
        #self.type_keys_with_interval(100,"teste123")

        #if not self.find( "cont_salvar_opc_rel_mov_fiscal", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_rel_mov_fiscal")
        #self.click()
        #self.wait(2000)

        #if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
        #    not_found("cont_retorn_opc_23_imposto")
        #self.click()
        
        # EXCLUIR

        if not self.find( "cont_btn_excluir_importacoes_export", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_importacoes_export")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_sim_importacoes_exclusao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_sim_importacoes_exclusao")
        self.click()
        # ERRO ACONTECENDO SQL, NAO EXCLUINDO
        self.wait(2000)
        self.enter()

        # grade
        if not self.find( "cont_grade_relativo_imp_exp_txt", matching=0.97, waiting_time=10000):
            not_found("cont_grade_relativo_imp_exp_txt")
        self.click_relative(65, 19)
        self.wait(500)
        if not self.find( "cont_grade_imprimir_imp_exp", matching=0.97, waiting_time=10000):
            not_found("cont_grade_imprimir_imp_exp")
        self.click()
        if not self.find( "cont_grade_cancel_imp_exp", matching=0.97, waiting_time=10000):
            not_found("cont_grade_cancel_imp_exp")
        self.click()
        self.wait(500)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(2000)
        
        ##########################################################################################
        ######################### IMPORTACOES E EXPORTACOES -> EBS ###############################
        ##########################################################################################

        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()

        if not self.find( "cont_importacao_exportacao_ebs", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_ebs")
        self.click()
        self.wait(1000)

        if not self.find( "cont_buscar_tabela_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_tabela_cad_servicos")
        self.click()

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_data_rel_ebs_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_data_rel_ebs_importacoes")
        self.click_relative(27, 5)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)
        #GERAÇAO DE MOVIMENTOS CAIXAS DE MARCAÇÃO
        if not self.find( "cont_geracao_mov_imp_exp_clientes", matching=0.97, waiting_time=10000):
            not_found("cont_geracao_mov_imp_exp_clientes")
        self.click()
        self.wait(1000)
        x = 0
        while x < 7:
            self.tab()
            self.space()
            x += 1
        
        self.wait(1000)
        if not self.find( "cont_click_auxiliar_somente_caixa", matching=0.97, waiting_time=10000):
            not_found("cont_click_auxiliar_somente_caixa")
        self.click_relative(61, 8)
        # CLICK AUXILIAR APENAS PARA TIRAR O MOUSE DE CIMA DAS CAIXAS DE MARCAÇAO
        self.wait(1000)

        if not self.find( "cont_conferencia_marcacoes_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_conferencia_marcacoes_importacoes")
        self.click_relative(60, 140)
        self.wait(1000)
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"12")
            self.tab()
            x += 1
        if not self.find( "cont_clientes_fornecedores_imp_exp", matching=0.97, waiting_time=10000):
            not_found("cont_clientes_fornecedores_imp_exp")
        self.click()
        if not self.find( "cont_imp_exp_notas_fiscas_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_notas_fiscas_entrada")
        self.click()
        self.wait(1000)
        if not self.find( "cont_imp_exp_notas_fiscais_de_saida", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_notas_fiscais_de_saida")
        self.click()
        if not self.find( "cont_cupom_fiscal_imp_exp", matching=0.97, waiting_time=10000):
            not_found("cont_cupom_fiscal_imp_exp")
        self.click()
        self.wait(1000)

        if not self.find( "cont_imp_exp_gerar_ebs", matching=0.97, waiting_time=10000):
            not_found("cont_imp_exp_gerar_ebs")
        self.click()
        self.wait(1000)

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()
        
        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(2000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(12000)
        # ARQUIVO GERADO COM SUCESSO
        
        if not self.find( "cont_btn_geracao_ok_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_geracao_ok_emissao")
        self.click()

        # APARECENDO QUE NAO EXISTE MOVIMENTO, APERTAR ENTER
        self.wait(1000)
        self.enter()
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ##########################################################################################
        ################# IMPORTACOES E EXPORTACOES -> DOMINIO -> EXPORTAÇÃO #####################
        ##########################################################################################

        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_importacoes_menu_dominio_btn", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_menu_dominio_btn")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_07_imp_exportacao_btn_exp", matching=0.97, waiting_time=10000):
            not_found("cont_24_07_imp_exportacao_btn_exp")
        self.click()
        self.wait(1000)
        if not self.find( "cont_import_domin_export_empresa_inf", matching=0.97, waiting_time=10000):
            not_found("cont_import_domin_export_empresa_inf")
        self.click_relative(57, 25)

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_import_btn_data_dominio", matching=0.97, waiting_time=10000):
            not_found("cont_import_btn_data_dominio")
        self.click_relative(26, 5)

        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_geracao_notas_fiscais_saida", matching=0.97, waiting_time=10000):
            not_found("cont_btn_geracao_notas_fiscais_saida")
        self.click()
        self.wait(1000)

        if not self.find( "cont_btn_gerar_relator_emissao_giad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_gerar_relator_emissao_giad")
        self.click()
        self.wait(2000)
        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()
        
        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(2000)
        if not self.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_emissao_geracao")
        self.click()
        self.wait(15000)
        # ARQUIVO GERADO COM SUCESSO
        if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        self.click()

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        
        ##########################################################################################
        ################# IMPORTACOES E EXPORTACOES -> DOMINIO -> IMPORTAÇÃO #####################
        ##########################################################################################

        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_importacoes_menu_dominio_btn", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_menu_dominio_btn")
        self.click()
        self.wait(1000)
        if not self.find( "cont_import_dominio_importacao_24", matching=0.97, waiting_time=10000):
            not_found("cont_import_dominio_importacao_24")
        self.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(1000)
        if not self.find( "cont_import_btn_cliente_cons_rel", matching=0.97, waiting_time=10000):
            not_found("cont_import_btn_cliente_cons_rel")
        self.click_relative(61, 20)

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        x = 0
        while x< 19:
            self.type_down()
            x += 1

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(3000)
        # AQUI VAI ABRIR UM ARQUIVO GERADO NA MAQUINA 

        if not self.find( "cont_geracoes_notasai_area_trab", matching=0.97, waiting_time=10000):
            not_found("cont_geracoes_notasai_area_trab")
        self.double_click()
        self.wait(5000)

        # IMPORTAR E EXCLUIR NAO ESTAO FUNCIONANDO, POR ENQUANTO VOU PULAR 28/06/2024
        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        
        ##########################################################################################
        ############## IMPORTACOES E EXPORTACOES -> CONTABILIZAÇÃO BANCARIA (OFX) ################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_import_contabilizacao_bancaria_ofx", matching=0.97, waiting_time=10000):
            not_found("cont_import_contabilizacao_bancaria_ofx")
        self.click()

        self.wait(2000)
        self.type_keys_with_interval(100,"1")

        self.wait(1000)

        if not self.find( "cont_reduzido_plano_de_contas_banco_rel", matching=0.97, waiting_time=10000):
            not_found("cont_reduzido_plano_de_contas_banco_rel")
        self.click_relative(65, 24)

        self.wait(2000)
        self.type_keys_with_interval(100,"00001")
        if not self.find( "cont_relativo_localizar_consulta_de_contas_24_07", matching=0.97, waiting_time=10000):
            not_found("cont_relativo_localizar_consulta_de_contas_24_07")
        self.click_relative(98, 36)
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_import_btn_historico_rel", matching=0.97, waiting_time=10000):
            not_found("cont_import_btn_historico_rel")
        self.click_relative(64, 20)

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(3000)
        # AQUI VAI ABRIR UM ARQUIVO GERADO NA MAQUINA 

        if not self.find( "cont_geracoes_notasai_area_trab", matching=0.97, waiting_time=10000):
            not_found("cont_geracoes_notasai_area_trab")
        self.double_click()
        self.wait(5000)

        # AQUI NAO ESTA IMPORTANDO NENHUMA INFORMAÇÃO, NAO É POSSIVEL IMPORTAR E NEM EXCLUIR
        # POR ENQUANTO RETORNAR

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        ##########################################################################################
        ################### IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO SINTEGRA #####################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_import_importacao_sintegra_menu", matching=0.97, waiting_time=10000):
            not_found("cont_import_importacao_sintegra_menu")
        self.click()

        # IMPORTAÇÃO SINTEGRA NÃO TEM MOVIMENTOS PARA IMPORTAR
        # POR ENQUANTO DEIXAR

        self.wait(1000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ##########################################################################################
        ############### IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO XML (NF-e / NFC-e) ###############
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_imp_importacao_xml_nfe_nfc", matching=0.97, waiting_time=10000):
            not_found("cont_imp_importacao_xml_nfe_nfc")
        self.click()

        self.wait(1000)

        if not self.find( "cont_impp_operacao_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_impp_operacao_padrao")
        self.click_relative(59, 24)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)


        
        if not self.find( "cont_impp_cfop", matching=0.97, waiting_time=10000):
            not_found("cont_impp_cfop")
        self.click_relative(58, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)


        
        if not self.find( "cont_impp_grp_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_impp_grp_fiscal")
        self.click_relative(60, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)
        


        if not self.find( "cont_impp_cliente", matching=0.97, waiting_time=10000):
            not_found("cont_impp_cliente")
        self.click_relative(59, 26)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)
        x = 0
        while x < 19:
            self.type_down()
            x += 1

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        
        if not self.find( "cont_impp_vendedor", matching=0.97, waiting_time=10000):
            not_found("cont_impp_vendedor")
        self.click_relative(56, 27)
        self.wait(2000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(2000)

        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(2000)

        if not self.find( "cont_impp_tipo_do_item_sped", matching=0.97, waiting_time=10000):
            not_found("cont_impp_tipo_do_item_sped")
        self.click_relative(276, 21)

        self.wait(500)
        self.click()
        self.type_down()
        self.enter()
        self.wait(2000)

        if not self.find( "cont_impp_importar_xml_nfe_nfc", matching=0.97, waiting_time=10000):
            not_found("cont_impp_importar_xml_nfe_nfc")
        self.click()
        self.wait(7000)

        if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ##########################################################################################
        ################## IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO XML (NFS-e) ###################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_imp_importacao_xml_nfse", matching=0.97, waiting_time=10000):
            not_found("cont_imp_importacao_xml_nfse")
        self.click()
        self.wait(2000)

        if not self.find( "cont_imp_grp_fiscal_padrao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_imp_grp_fiscal_padrao_rel")
        self.click_relative(539, 4)
        self.wait(1000)
        self.type_down()
        self.enter()

        self.wait(2000)
        if not self.find( "cont_imp_client_forneced_rel", matching=0.97, waiting_time=10000):
            not_found("cont_imp_client_forneced_rel")
        self.click_relative(439, 22)
        self.wait(1000)
        x = 0
        while x < 19:
            self.type_down()
            x += 1
        self.enter()
        self.wait(2000)

        if not self.find( "cont_importacoes_btn_importar_xml_nfse", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_btn_importar_xml_nfse")
        self.click()
        self.wait(5000)
        if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        self.click()

        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ##########################################################################################
        ################## IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO XML (CT-e) ###################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(1000)

        if not self.find( "cont_importacao_xml_cte_24", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_xml_cte_24")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_1_operacao_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_btn_1_operacao_importacoes")
        self.click_relative(55, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_cfop_padrao_importacoes_2", matching=0.97, waiting_time=10000):
            not_found("cont_btn_cfop_padrao_importacoes_2")
        self.click_relative(53, 24)
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_3_cfop_interestadual", matching=0.97, waiting_time=10000):
            not_found("cont_btn_3_cfop_interestadual")
        self.click_relative(52, 25)
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_4_grupo_fiscal_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_btn_4_grupo_fiscal_importacoes")
        self.click_relative(53, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_5_centro_de_custo_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_btn_5_centro_de_custo_importacoes")
        self.click_relative(81, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_6_classificacao_importacao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_6_classificacao_importacao")
        self.click_relative(56, 30)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()


        if not self.find( "cont_btn_7_plano_financeiro_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_btn_7_plano_financeiro_importacoes")
        self.click_relative(82, 25)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_importacoes_btn_importar_xml_nfse", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_btn_importar_xml_nfse")
        self.click()
        self.wait(5000)
        if not self.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        self.click()

        self.wait(2000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ##########################################################################################
        ################ IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO SPED PIS/COFINS #################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(2000)

        if not self.find( "cont_importacao_sped_pis_cofins", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_sped_pis_cofins")
        self.click()
        self.wait(2000)

        if not self.find( "cont_btn_1_importacao_operacao_padrao_ent", matching=0.97, waiting_time=10000):
            not_found("cont_btn_1_importacao_operacao_padrao_ent")
        self.click_relative(58, 26)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)



        if not self.find( "cont_btn_2_importacao_operacao_padrao_saida", matching=0.97, waiting_time=10000):
            not_found("cont_btn_2_importacao_operacao_padrao_saida")
        self.click_relative(61, 25)
        self.wait(2000)
        self.type_keys_with_interval(100,"0002")
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)



        if not self.find( "cont_btn_3_importacao_grupo_fiscal_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_3_importacao_grupo_fiscal_padrao")
        self.click_relative(65, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)



        if not self.find( "cont_btn_4_importacao_cond_pag_padrao_vista", matching=0.97, waiting_time=10000):
            not_found("cont_btn_4_importacao_cond_pag_padrao_vista")
        self.click_relative(65, 30)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        if not self.find( "cont_btn_5_import_cond_pag_padrao_prazo", matching=0.97, waiting_time=10000):
            not_found("cont_btn_5_import_cond_pag_padrao_prazo")
        self.click_relative(62, 26)
        self.wait(2000)
        
        self.type_keys_with_interval(100,"0002")
        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        if not self.find( "cont_btn_6_importacao_cliente_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_6_importacao_cliente_padrao")
        self.click_relative(61, 27)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        if not self.find( "cont_btn_7_importacao_cfop_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_btn_7_importacao_cfop_entrada")
        self.click_relative(63, 24)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)


        if not self.find( "cont_btn_8_importacao_cfop_saida", matching=0.97, waiting_time=10000):
            not_found("cont_btn_8_importacao_cfop_saida")
        self.click_relative(62, 22)
        self.wait(2000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click()
        self.wait(2000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
        self.wait(2000)

        if not self.find( "cont_importacoes_carregar_arquivo", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_carregar_arquivo")
        self.click()
        self.wait(1000)
        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(3000)
        # AQUI VAI ABRIR UM ARQUIVO GERADO NA MAQUINA 

        if not self.find( "cont_geracoes_notasai_area_trab", matching=0.97, waiting_time=10000):
            not_found("cont_geracoes_notasai_area_trab")
        self.double_click()
        self.wait(5000)

        if not self.find( "cont_importacoes_gerar_movimentacao_pis", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_gerar_movimentacao_pis")
        self.click()
        self.wait(5000)

        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()

        
        ##########################################################################################
        ################ IMPORTACOES E EXPORTACOES -> IMPORTAÇÃO SPED PIS/COFINS #################
        ##########################################################################################
        self.wait(2000)

        if not self.find( "cont_menu_importacoes_exportacos_2", matching=0.97, waiting_time=10000):
            not_found("cont_menu_importacoes_exportacos_2")
        self.click()
        self.wait(2000)

        if not self.find( "cont_importacoes_import_txt_nf_modelo_21", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_import_txt_nf_modelo_21")
        self.click()
        self.wait(2000)
        if not self.find( "cont_import_cfop_padrao_rel_txt", matching=0.97, waiting_time=10000):
            not_found("cont_import_cfop_padrao_rel_txt")
        self.click_relative(537, 2)
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "cont_import_operacao_padrao_rel_txt", matching=0.97, waiting_time=10000):
            not_found("cont_import_operacao_padrao_rel_txt")
        self.click_relative(535, 6)
        self.wait(1000)
        self.enter()
        self.wait(2000)
        if not self.find( "cont_import_arquivo_txt_3_pontos", matching=0.97, waiting_time=10000):
            not_found("cont_import_arquivo_txt_3_pontos")
        self.click()

        if not self.find( "cont_importacoes_area_de_trabalho_pasta", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_area_de_trabalho_pasta")
        self.click()

        if not self.find( "cont_pasta_importacoes_geracoes_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_pasta_importacoes_geracoes_contabil")
        self.double_click()
        self.wait(3000)
        # AQUI VAI ABRIR UM ARQUIVO GERADO NA MAQUINA 

        if not self.find( "cont_geracoes_notasai_area_trab", matching=0.97, waiting_time=10000):
            not_found("cont_geracoes_notasai_area_trab")
        self.double_click()
        self.wait(5000)

        # BOTÃO DE IMPORTAÇÃO ESTÁ DEMORANDO DEMAIS E CRASHANDO O SISTEMA

        #if not self.find( "cont_importacao_btn_importar_txt", matching=0.97, waiting_time=10000):
        #    not_found("cont_importacao_btn_importar_txt")
        #self.click()
        
        self.wait(2000)

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        #######################################################################################
        #######################################################################################
        ########################## FINAL DE IMPORTAÇÕES/EXPORTAÇÕES ###########################
        #######################################################################################
        #######################################################################################





def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()



