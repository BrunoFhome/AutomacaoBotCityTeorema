from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()




"""
CÓDIGO FEITO PARA SISTEMA VENDAS PDV 24.07
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
        bot = self
        """
        #########################################################################
        ###############################---LOGIN---###############################
        #########################################################################

        self.execute(r"C:\Teorema\bin\crm.exe")
        self.wait(8000)
        if not bot.find( "crm_achar_botao_login_inicial", matching=0.97, waiting_time=10000):
            not_found("crm_achar_botao_login_inicial")
        bot.click_relative(-69, 71)
        self.type_keys_with_interval(100,"teorema")
        self.tab()
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"1811")
        if not bot.find( "crm_btn_login_inicio", matching=0.97, waiting_time=10000):
            not_found("crm_btn_login_inicio")
        bot.click()
        self.wait(3000)
        self.enter()
        self.wait(2000)
        self.enter()
        
        ############################################################################################
        ########################### CADASTROS -> EMPRESAS  #############################
        ############################################################################################
        self.wait(3000)
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        
        self.wait(1000)
        if not self.find( "cont_empresas_cad_1_men_", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_cad_1_men_")
        self.click()
        self.wait(1000)

        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_nao_incluir_dados", matching=0.97, waiting_time=10000):
            not_found("crm_btn_nao_incluir_dados")
        bot.click()
        self.wait(3000)
        self.shift_tab()
        self.type_down()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_keys_with_interval(100,"10000598046")
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_usa_clientes_forn_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_usa_clientes_forn_buscar")
        self.click_relative(69, 27)
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_usa_plano_de_custos_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_usa_plano_de_custos_buscar")
        self.click_relative(71, 25)
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_tabela_de_precos", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_precos")
        self.click_relative(66, 27)
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.backspace()
        if not self.find( "cont_usa_contratos_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_contratos_da_empresa")
        self.click_relative(69, 31)
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_planos_de_contas_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_planos_de_contas_da_empresa")
        self.click_relative(68, 30)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_itens_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_itens_da_empresa")
        self.click_relative(67, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_vendedores_da_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_usa_vendedores_da_empresa")
        self.click_relative(68, 27)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_tabela_de_precos_servico_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_precos_servico_busc")
        self.click_relative(66, 23)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.backspace()
        self.backspace()
        self.backspace()
        self.backspace()
        
        self.wait(2000)
        if not self.find( "cont_contabilista_busc", matching=0.97, waiting_time=10000):
            not_found("cont_contabilista_busc")
        self.click_relative(68, 24)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(1000)
        
        self.wait(3000)
        #
        if not self.find( "cont_usa_historico_da_empre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_historico_da_empre_busc")
        self.click_relative(71, 29)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_precos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_precos_da_empresa_busc")
        self.click_relative(67, 29)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_situacao_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_situacao_da_empresa_busc")
        self.click_relative(68, 31)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_usa_veiculos_da_empresa_busc", matching=0.97, waiting_time=10000):
            not_found("cont_usa_veiculos_da_empresa_busc")
        self.click_relative(69, 28)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        
        #MOUSE JA PAROU EM CIMA DO SALVAR
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.click()
        
        
        self.wait(3000)
        if not self.find( "cont_contas_de_cliente_1", matching=0.97, waiting_time=10000):
            not_found("cont_contas_de_cliente_1")
        self.click_relative(123, 26)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        #mouse esta em cima
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_contas_de_fornecedores_2", matching=0.97, waiting_time=10000):
            not_found("cont_contas_de_fornecedores_2")
        self.click_relative(125, 26)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_cad_conta_contabil_96", matching=0.97, waiting_time=10000):
            not_found("cont_cad_conta_contabil_96")
        self.click_relative(120, 24)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_cad_conta_contabil_95", matching=0.97, waiting_time=10000):
            not_found("cont_cad_conta_contabil_95")
        self.click_relative(122, 25)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_conta_contabil_1", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_1")
        self.click_relative(125, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_conta_contabil_2", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_2")
        self.click_relative(126, 28)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_conta_contabil_3", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_3")
        self.click_relative(127, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_conta_contabil_4", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_4")
        self.click_relative(91, 28)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_conta_contabil_5", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_5")
        self.click_relative(126, 27)
        
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_6", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_6")
        self.click_relative(127, 28)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_7", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_7")
        self.click_relative(125, 27)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_8", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_8")
        self.click_relative(124, 25)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_9", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_9")
        self.click_relative(126, 25)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_10", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_10")
        self.click_relative(126, 26)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_11", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_11")
        self.click_relative(126, 26)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_12", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_12")
        self.click_relative(90, 29)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_13", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_13")
        self.click_relative(93, 28)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "cont_conta_contabil_14", matching=0.97, waiting_time=10000):
            not_found("cont_conta_contabil_14")
        self.click_relative(127, 29)
        self.wait(1000)
        if not self.find( "cont_lupta_localizar_f12", matching=0.97, waiting_time=10000):
            not_found("cont_lupta_localizar_f12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.tab()
        self.tab()
        if not self.find( "cont_5_relacionamentos_cad", matching=0.97, waiting_time=10000):
            not_found("cont_5_relacionamentos_cad")
        self.click()
        """
        self.wait(2000)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not self.find( "cont_incluir_A_inscricoes_estaduais", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_A_inscricoes_estaduais")
        self.click()
        if not self.find( "cont_botao_buscar_estado_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_buscar_estado_5")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)

        if not self.find( "btn_retornar_excluir_teste_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_retornar_excluir_teste_apagar")
        self.click()


        #####################################################################################################
        ################################### EXCLUIR O CADASTRO DA EMPRESA ###################################
        #####################################################################################################

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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
            
        self.wait(1000)
        if not self.find( "btn_clicar_teste_qa_12_apagar", matching=0.97, waiting_time=10000):
            not_found("btn_clicar_teste_qa_12_apagar")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "btn_localizar_teste_apagar_qa12", matching=0.97, waiting_time=10000):
            not_found("btn_localizar_teste_apagar_qa12")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()

        self.wait(2000)


        ###############################################################################################
        #################### CADASTROS -> PARAMETROS -> PARAMETROS DA EMPRESA - F9 ####################
        ###############################################################################################
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



def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  

