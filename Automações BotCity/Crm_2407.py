from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()




"""
CÓDIGO FEITO PARA SISTEMA CRM 24.07
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - SPINNER 0041284
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
        self.wait(2000)
        self.enter()
        
        self.wait(2000)
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
        self.wait(2000)
        self.enter()
        self.wait(1000)
        self.enter()
        
        
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
        
        self.wait(2000)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(1000)
        self.enter()
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
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)

        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()


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
    
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
            
        self.wait(1000)
        if not bot.find( "crm_achar_empresa_qa12_deletar", matching=0.97, waiting_time=10000):
            not_found("crm_achar_empresa_qa12_deletar")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(4000)


        if not self.find( "cont_nao_importar_dados", matching=0.97, waiting_time=10000):
            not_found("cont_nao_importar_dados")
        self.click()
        if not self.find( "cont_buscar_lupa_parametro_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_lupa_parametro_empresa")
        self.click()
        self.wait(1000)

        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)

        if not bot.find( "crm_achar_empresa_teste_parametros", matching=0.97, waiting_time=10000):
            not_found("crm_achar_empresa_teste_parametros")
        bot.click()
        self.wait(1000)

        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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

        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_relativo_itens_lista_abrir", matching=0.97, waiting_time=10000):
            not_found("crm_relativo_itens_lista_abrir")
        bot.click_relative(-15, 73)
        
        self.wait(4000)
        if not bot.find( "crm_codigos_padroes_reliativo_item_lista", matching=0.97, waiting_time=10000):
            not_found("crm_codigos_padroes_reliativo_item_lista")
        bot.click_relative(-5, 75)
        
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
        
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_2_cadastro_mod_busc", matching=0.97, waiting_time=10000):
            not_found("cont_2_cadastro_mod_busc")
        self.click_relative(101, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_3_local_estoque_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_local_estoque_busc")
        self.click_relative(88, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_1_transf_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_transf_busc")
        self.click_relative(82, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_2_inventario_busc", matching=0.97, waiting_time=10000):
            not_found("cont_2_inventario_busc")
        self.click_relative(80, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_3_producao_osm_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_producao_osm_busc")
        self.click_relative(88, 28)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_4_item_kit_busc", matching=0.97, waiting_time=10000):
            not_found("cont_4_item_kit_busc")
        self.click_relative(79, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_5_item_mestre_busc", matching=0.97, waiting_time=10000):
            not_found("cont_5_item_mestre_busc")
        self.click_relative(84, 28)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_6_almoxarifado_busc", matching=0.97, waiting_time=10000):
            not_found("cont_6_almoxarifado_busc")
        self.click_relative(80, 24)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_7_desmembra_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_7_desmembra_itens_busc")
        self.click_relative(83, 25)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_devoluca_iten_busc", matching=0.97, waiting_time=10000):
            not_found("cont_devoluca_iten_busc")
        self.click_relative(78, 25)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "cont_3_operacao_saida_1", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_1")
        self.click_relative(83, 44)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_2", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_2")
        self.click_relative(484, 43)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        
        self.wait(3000)
        if not self.find( "cont_3_operacao_saida_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_3")
        self.click_relative(883, 45)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_4", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_4")
        self.click_relative(80, 86)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacoes_saida_5", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacoes_saida_5")
        self.click_relative(486, 85)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_saida_6", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_saida_6")
        self.click_relative(882, 85)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacoes_saida_7", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacoes_saida_7")
        self.click_relative(82, 129)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacaoes_saida_8", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacaoes_saida_8")
        self.click_relative(485, 128)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_b_vendas_parametros", matching=0.97, waiting_time=10000):
            not_found("cont_b_vendas_parametros")
        self.click()
        if not self.find( "cont_1_padroes_venda_1", matching=0.97, waiting_time=10000):
            not_found("cont_1_padroes_venda_1")
        self.click_relative(100, 46)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        ###
        
        self.wait(1000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_2_vendedor_padrao_2", matching=0.97, waiting_time=10000):
            not_found("cont_2_vendedor_padrao_2")
        self.click_relative(85, 22)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_condicao_pagamento_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_condicao_pagamento_3")
        self.click_relative(83, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_padroes_operacoes_1", matching=0.97, waiting_time=10000):
            not_found("cont_2_padroes_operacoes_1")
        self.click_relative(84, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_operacao_saida_padrao_2", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_saida_padrao_2")
        self.click_relative(82, 27)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_nfe_3", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_nfe_3")
        self.click_relative(88, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_4_operacao_nfe_4", matching=0.97, waiting_time=10000):
            not_found("cont_4_operacao_nfe_4")
        self.click_relative(84, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_vendedor_clientes_disp", matching=0.97, waiting_time=10000):
            not_found("cont_2_vendedor_clientes_disp")
        self.click_relative(82, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_plano_preco_min", matching=0.97, waiting_time=10000):
            not_found("cont_3_plano_preco_min")
        self.click_relative(78, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_4_plano_preco_max", matching=0.97, waiting_time=10000):
            not_found("cont_4_plano_preco_max")
        self.click_relative(80, 27)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_1_cliente_4", matching=0.97, waiting_time=10000):
            not_found("cont_1_cliente_4")
        self.click_relative(82, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        self.wait(2000)

        ###
        ###
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not self.find( "cont_2_operacao_saida", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_saida")
        self.click_relative(84, 32)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_cfop_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_cfop_busc")
        self.click_relative(83, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_4_cfop_sub", matching=0.97, waiting_time=10000):
            not_found("cont_4_cfop_sub")
        self.click_relative(79, 27)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_5_cfop_iss", matching=0.97, waiting_time=10000):
            not_found("cont_5_cfop_iss")
        self.click_relative(83, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_6_operacao_saida_iss", matching=0.97, waiting_time=10000):
            not_found("cont_6_operacao_saida_iss")
        self.click_relative(82, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_moedapadrao", matching=0.97, waiting_time=10000):
            not_found("cont_2_moedapadrao")
        self.click_relative(83, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_tipo_pagamento_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_tipo_pagamento_busc")
        self.click_relative(82, 22)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_4_tipo_pagamento_troc", matching=0.97, waiting_time=10000):
            not_found("cont_4_tipo_pagamento_troc")
        self.click_relative(78, 24)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_5_tipo_pag_entra", matching=0.97, waiting_time=10000):
            not_found("cont_5_tipo_pag_entra")
        self.click_relative(81, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_6_tipo_pag_saida", matching=0.97, waiting_time=10000):
            not_found("cont_6_tipo_pag_saida")
        self.click_relative(80, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_7_tipo_pag_baixa", matching=0.97, waiting_time=10000):
            not_found("cont_7_tipo_pag_baixa")
        self.click_relative(81, 24)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_1_conta_busc", matching=0.97, waiting_time=10000):
            not_found("cont_1_conta_busc")
        self.click_relative(84, 24)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_tipo_pag_bus", matching=0.97, waiting_time=10000):
            not_found("cont_2_tipo_pag_bus")
        self.click_relative(80, 24)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_operacao_busc", matching=0.97, waiting_time=10000):
            not_found("cont_3_operacao_busc")
        self.click_relative(83, 24)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_2_operacao_padrao", matching=0.97, waiting_time=10000):
            not_found("cont_2_operacao_padrao")
        self.click_relative(80, 30)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_3_cond_de_pag", matching=0.97, waiting_time=10000):
            not_found("cont_3_cond_de_pag")
        self.click_relative(80, 27)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_4_plano_preco", matching=0.97, waiting_time=10000):
            not_found("cont_4_plano_preco")
        self.click_relative(81, 23)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        

        self.wait(1000)
        if not bot.find( "crm_achar_empresa_teste_parametros_ex", matching=0.97, waiting_time=10000):
            not_found("crm_achar_empresa_teste_parametros_ex")
        bot.click()
        self.wait(2000)

        if not self.find( "cont_btn_editar_parametros_empresa_excluir", matching=0.97, waiting_time=10000):
            not_found("cont_btn_editar_parametros_empresa_excluir")
        self.click()
        self.wait(1000)
        
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_btn_sim_exclusao_parametros_teste", matching=0.97, waiting_time=10000):
            not_found("cont_btn_sim_exclusao_parametros_teste")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.click()
        self.wait(2000)

       
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
        self.wait(1000)
        if not self.find( "cont_regionalizacao_23_fin_2", matching=0.97, waiting_time=10000):
            not_found("cont_regionalizacao_23_fin_2")
        self.click()
        self.wait(1000)
        if not bot.find( "crm_btn_paises_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("crm_btn_paises_parametros_fiscais")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.wait(2000)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"q")
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_regioes_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("crm_regioes_parametros_fiscais")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        ####
        ####
        if not self.find( "cont_busc_pais_parame", matching=0.97, waiting_time=10000):
            not_found("cont_busc_pais_parame")
        self.click()
        
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_param_regiao_1_entrada", matching=0.97, waiting_time=10000):
            not_found("cont_param_regiao_1_entrada")
        self.click_relative(-8, 8)
        if not self.find( "cont_5_saida_param_regioes", matching=0.97, waiting_time=10000):
            not_found("cont_5_saida_param_regioes")
        self.click_relative(-10, 7)
        self.wait(3000)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        
        self.wait(2000)
        self.type_keys_with_interval(100,"q")
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_estados_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("crm_estados_parametros_fiscais")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.tab()
        self.tab()
        self.type_down()
        self.wait(3000)
        #mouse esta parando em cima de salvar
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(3000)
        self.click()
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> REGIONALIZAÇÃO -> MUNICIPIOS ###########
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
        if not bot.find( "crm_municipios_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("crm_municipios_parametros_fiscais")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.click()
        
        ############################################################################################
        ############### CADASTROS -> PARAMETROS FISCAIS  -> GRUPO FISCAL DE PRODUTOS  ##############
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
        if not bot.find( "crm_grupo_fiscal_de_itens", matching=0.97, waiting_time=10000):
            not_found("crm_grupo_fiscal_de_itens")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"123")
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_codigos_de_operacao_parametros_fiscais", matching=0.97, waiting_time=10000):
            not_found("crm_codigos_de_operacao_parametros_fiscais")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        ###
        ###
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_busc")
        self.click_relative(69, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()

        if not self.find( "cont_tabela_precos_servicos_busc", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_servicos_busc")
        self.click_relative(60, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        
        ##########################################################################################
        ################ CADASTROS -> PARAMETROS FISCAIS  -> CODIGOS FISCAIS (CFOP) ################
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
        if not self.find( "cont_codigos_fiscais_cfop_1_23_f", matching=0.97, waiting_time=10000):
            not_found("cont_codigos_fiscais_cfop_1_23_f")
        self.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        ###
        ###
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!@")
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.wait(3000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        self.type_keys_with_interval(100,"qa12!")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_qa12_ex", matching=0.97, waiting_time=10000):
            not_found("cont_achar_qa12_ex")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_operacao_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_selec_busc")
        self.click_relative(53, 28)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)

        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not self.find( "cont_regiao_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_regiao_selec_busc")
        self.click_relative(48, 28)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_grupo_fiscal_selec_busc", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_fiscal_selec_busc")
        self.click_relative(51, 26)
        
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_decreto_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_decreto_2_busc_")
        self.click_relative(46, 30)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_obs_1_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_1_busc_")
        self.click_relative(43, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_obs_2_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_obs_2_busc_")
        self.click_relative(43, 30)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_cfop_busc_", matching=0.97, waiting_time=10000):
            not_found("cont_cfop_busc_")
        self.click_relative(60, 25)
        self.wait(2000)
        self.backspace()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(2000)
        self.wait(2000)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "cont_achar_123_situacoes", matching=0.97, waiting_time=10000):
            not_found("cont_achar_123_situacoes")
        self.click()
        
        self.wait(2000)
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.wait(1000)
        self.click()
        
        ############################################################################################
        ############################################################################################
        ############### CADASTROS -> CLIENTES, FORNECEDORES E TRANSPORTADORES - F3 #################
        ############################################################################################
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
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(2000)

        if not bot.find( "crm_btn_cadastro_cliente_fisica", matching=0.97, waiting_time=10000):
            not_found("crm_btn_cadastro_cliente_fisica")
        bot.click()
        self.wait(2000)
        self.tab()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
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
        
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(3000)
        self.enter()
        

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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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

        ###########################################################
        ##################### 2 AGRUPAMENTOS ######################
        ###########################################################

        self.wait(2000)
        if not self.find( "cont_2_agrupamento_clientes", matching=0.97, waiting_time=10000):
            not_found("cont_2_agrupamento_clientes")
        self.click()
        
        self.wait(3000)
        if not self.find( "cont_local_de_cobranca_11", matching=0.97, waiting_time=10000):
            not_found("cont_local_de_cobranca_11")
        self.click_relative(68, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        
        self.wait(2000)
        if not self.find( "cont_ramo_de_atividade_12", matching=0.97, waiting_time=10000):
            not_found("cont_ramo_de_atividade_12")
        self.click_relative(68, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not self.find( "cont_comissao_13", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_13")
        self.click_relative(70, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        if not self.find( "cont_vendedor_compr_14", matching=0.97, waiting_time=10000):
            not_found("cont_vendedor_compr_14")
        self.click_relative(65, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        
        
        self.wait(2000)
        if not self.find( "cont_classificacao_17", matching=0.97, waiting_time=10000):
            not_found("cont_classificacao_17")
        self.click_relative(67, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_conta_corrente_18", matching=0.97, waiting_time=10000):
            not_found("cont_conta_corrente_18")
        self.click_relative(70, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_cod_con_cliente_19", matching=0.97, waiting_time=10000):
            not_found("cont_cod_con_cliente_19")
        self.click_relative(64, 25)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_fornecedor_fix", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_fornecedor_fix")
        self.click_relative(69, 26)
        self.wait(2000)
        self.type_keys_with_interval(100,"1")
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_segmento_busc_rel_21", matching=0.97, waiting_time=10000):
            not_found("cont_segmento_busc_rel_21")
        self.click_relative(67, 30)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_linha_rel_busc_22", matching=0.97, waiting_time=10000):
            not_found("cont_linha_rel_busc_22")
        self.click_relative(71, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_tabela_precos_itens_bsc_23", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_precos_itens_bsc_23")
        self.click_relative(67, 28)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)

        if not self.find( "cont_tabela_de_preco_servico_24", matching=0.97, waiting_time=10000):
            not_found("cont_tabela_de_preco_servico_24")
        self.click_relative(71, 26)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.backspace()
        self.wait(1000)
        if not self.find( "cont_operacao_pdv_busc_25", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_pdv_busc_25")
        self.click_relative(69, 29)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_transportador_busc_26", matching=0.97, waiting_time=10000):
            not_found("cont_transportador_busc_26")
        self.click_relative(83, 25)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_btn_clientes_cond_pagamento_rel_2407", matching=0.97, waiting_time=10000):
            not_found("cont_btn_clientes_cond_pagamento_rel_2407")
        self.click_relative(67, 25)
        self.wait(3000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)

        if not bot.find( "crm_cadastro_cliente_origem_cliente_rel", matching=0.97, waiting_time=10000):
            not_found("crm_cadastro_cliente_origem_cliente_rel")
        bot.click_relative(64, 27)
        self.wait(3000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)

        if not self.find( "cont_operacao_nfs_e_ordem_28", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_nfs_e_ordem_28")
        self.click_relative(72, 32)
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        
        #########################################################################################
        # CADASTROS -> CLIENTES...->INCLUIR -> 2 AGRUPAMENTO -> CODIGOS CONTABEIS MULTI EMPRESA # 
        #########################################################################################


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
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_codigo_contabil_forne_23", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_contabil_forne_23")
        self.click_relative(65, 27)
        self.wait(2000)
        self.type_keys_with_interval(100,"00001")
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_confirmar_codigos_contabeis_multi", matching=0.97, waiting_time=10000):
            not_found("crm_btn_confirmar_codigos_contabeis_multi")
        bot.click()

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
        
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_excluir_representantes_rel", matching=0.97, waiting_time=10000):
            not_found("crm_excluir_representantes_rel")
        bot.click_relative(-22, 25)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not self.find( "cont_comissao_contratos_bsc_rel", matching=0.97, waiting_time=10000):
            not_found("cont_comissao_contratos_bsc_rel")
        self.click_relative(58, 26)
        self.wait(1000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(100,"qa12!@")
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        self.wait(2000)
        if not self.find( "cont_concluir_inclusao_spc", matching=0.97, waiting_time=10000):
            not_found("cont_concluir_inclusao_spc")
        self.click()
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_excluir_spc_relativo", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_spc_relativo")
        bot.click_relative(-52, 29)
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
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
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
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)

        self.wait(1000)
        if not bot.find( "crm_situacao_de_cadastro_ativo", matching=0.97, waiting_time=10000):
            not_found("crm_situacao_de_cadastro_ativo")
        bot.click_relative(111, 27)
        self.wait(3000)
        if not bot.find( "crm_cadastro_cliente_ativo", matching=0.97, waiting_time=10000):
            not_found("crm_cadastro_cliente_ativo")
        bot.click()

        self.wait(3000)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        
        self.type_keys_with_interval(100,"qa12")
        self.wait(2000)
        
        self.wait(2000)

        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        self.wait(3000)
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)
        



        #####################################################################################
        ################## CADASTROS -> PREVISAO DE ENTREGA P/TRANSPORTADOR #################
        #####################################################################################



        
        #####################################################################################
        ######## CADASTROS -> LINHAS, RAMOS ATIVIDADE, ROTAS DE ENTREGA E SEGMENTOS #########
        #####################################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not self.find( "linha", matching=0.97, waiting_time=10000):
            self.not_found("linha")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
                    
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not self.find( "ramodeatividade", matching=0.97, waiting_time=10000):
            self.not_found("ramodeatividade")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()            
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
            self.not_found("localizaramo")
        self.click_relative(17, 26)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        
        
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not self.find( "rotasdeentrega", matching=0.97, waiting_time=10000):
            self.not_found("rotasdeentrega")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()            
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
            self.not_found("localizaramo")
        self.click_relative(17, 26)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        
        
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not self.find( "segmento", matching=0.97, waiting_time=10000):
            self.not_found("segmento")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()  
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()                    
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        
        
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not self.find( "tiposdecontratos", matching=0.97, waiting_time=10000):
            self.not_found("tiposdecontratos")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()  
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()                    
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()

        ###### origem cliente ######

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
            self.not_found("linhasramosetc")
        self.click()
        if not bot.find( "crm_linhas_origem_cliente", matching=0.97, waiting_time=10000):
            not_found("crm_linhas_origem_cliente")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()

        

        
        #####################################################################################
        ########################### CADASTROS -> ITENS DE ESTOQUE ###########################
        #####################################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "familiasIE", matching=0.97, waiting_time=10000):
            self.not_found("familiasIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "gruposIE", matching=0.97, waiting_time=10000):
            self.not_found("gruposIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not self.find( "grupofiscalIE", matching=0.97, waiting_time=10000):
            self.not_found("grupofiscalIE")
        self.click_relative(73, 46)
                   
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "subgruposIE", matching=0.97, waiting_time=10000):
            self.not_found("subgruposIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "marcasIE", matching=0.97, waiting_time=10000):
            self.not_found("marcasIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        self.wait(2000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "unidadesIE", matching=0.97, waiting_time=10000):
            self.not_found("unidadesIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        self.enter()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "unidadeteste", matching=0.97, waiting_time=10000):
            self.not_found("unidadeteste")
        self.click()            
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "cadeiadeprecosIE", matching=0.97, waiting_time=10000):
            self.not_found("cadeiadeprecosIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not self.find( "preçovenda1", matching=0.97, waiting_time=10000):
            self.not_found("preçovenda1")
        self.click_relative(11, 33)
        if not self.find( "preçovenda1", matching=0.97, waiting_time=10000):
            self.not_found("preçovenda1")
        self.click_relative(11, 33)
        if not self.find( "precosugestao1", matching=0.97, waiting_time=10000):
            self.not_found("precosugestao1")
        self.click_relative(11, 65)
        if not self.find( "precosugestao1", matching=0.97, waiting_time=10000):
            self.not_found("precosugestao1")
        self.click_relative(11, 65)
        if not self.find( "custoprodutoIE", matching=0.97, waiting_time=10000):
            self.not_found("custoprodutoIE")
        self.click_relative(16, 34)
        if not self.find( "custoprodutoIE", matching=0.97, waiting_time=10000):
            self.not_found("custoprodutoIE")
        self.click_relative(16, 34)
        if not self.find( "custodiretoIE", matching=0.97, waiting_time=10000):
            self.not_found("custodiretoIE")
        self.click_relative(15, 63)
        if not self.find( "custodiretoIE", matching=0.97, waiting_time=10000):
            self.not_found("custodiretoIE")
        self.click_relative(15, 63)
        if not self.find( "custosimplesIE", matching=0.97, waiting_time=10000):
            self.not_found("custosimplesIE")
        self.click_relative(174, 34)
        if not self.find( "custosimplesIE", matching=0.97, waiting_time=10000):
            self.not_found("custosimplesIE")
        self.click_relative(174, 34)
        if not self.find( "custorealIE", matching=0.97, waiting_time=10000):
            self.not_found("custorealIE")
        self.click_relative(176, 65)
        if not self.find( "custorealIE", matching=0.97, waiting_time=10000):
            self.not_found("custorealIE")
        self.click_relative(176, 65)
        if not self.find( "custousuarioIE", matching=0.97, waiting_time=10000):
            self.not_found("custousuarioIE")
        self.click_relative(355, 33)
        if not self.find( "custousuarioIE", matching=0.97, waiting_time=10000):
            self.not_found("custousuarioIE")
        self.click_relative(355, 33)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()           
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "tabeladeprecosIE", matching=0.97, waiting_time=10000):
            self.not_found("tabeladeprecosIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        self.enter()
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        x=0
        while x<8:
            if not self.find( "valorbaseIE", matching=0.97, waiting_time=10000):
                self.not_found("valorbaseIE")
            self.click_relative(157, 26)
            self.type_down()
            self.enter()
            x=x+1
        if not self.find( "atualizaprecoIE1", matching=0.97, waiting_time=10000):
            self.not_found("atualizaprecoIE1")
        self.click_relative(103, 30)
        if not self.find( "atualizaprecoIE2", matching=0.97, waiting_time=10000):
            self.not_found("atualizaprecoIE2")
        self.click_relative(7, 30)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()           
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
            
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "tiposIE", matching=0.97, waiting_time=10000):
            self.not_found("tiposIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()           
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "subtiposIE", matching=0.97, waiting_time=10000):
            self.not_found("subtiposIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()           
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
            self.not_found("agrupamentoie")
        self.click()
        if not self.find( "controlesIE", matching=0.97, waiting_time=10000):
            self.not_found("controlesIE")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
            self.not_found("achargrupoteste")
        self.click_relative(5, 30)
        self.type_keys_with_interval(1,'te12')
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()           
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        self.wait(2000)
        
        ############################################################################################
        #############################---CADASTRO DE ITENS---########################################
        ############################################################################################
        self.wait(3000)

        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "cadastrodeitens", matching=0.97, waiting_time=10000):
            self.not_found("cadastrodeitens")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(3000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_right()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        #if not self.find( "retornarconsultaitensgambiarra", matching=0.97, waiting_time=10000):
        #    self.not_found("retornarconsultaitensgambiarra")
        #self.click_relative(42, -77)
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'1231231231')
        self.tab()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not self.find( "cadastroitensreferencia", matching=0.97, waiting_time=10000):
            self.not_found("cadastroitensreferencia")
        self.click_relative(718, 91)
        self.type_keys_with_interval(1,'te12!@')
        self.wait(1000)
        if not self.find( "referencia2cadastroitens", matching=0.97, waiting_time=10000):
            self.not_found("referencia2cadastroitens")
        self.click_relative(883, 89)
        self.type_keys_with_interval(1,'te12!@')
        if not self.find( "subirtelaCI", matching=0.97, waiting_time=10000):
            self.not_found("subirtelaCI")
        self.click()
        x=0
        while x<10:
            if not self.find( "subirtelaCI2", matching=0.97, waiting_time=10000):
                self.not_found("subirtelaCI2")
            self.double_click()
            x=x+1
        
                        ####---ABA1 P1---####
        
        if not self.find( "Descricaodadosprincipais", matching=0.97, waiting_time=10000):
            self.not_found("Descricaodadosprincipais")
        self.click_relative(11, 46)
        self.enter()
        self.type_keys_with_interval(1,'te12!@')
        self.enter()
        self.type_keys_with_interval(1,'87487487')
        self.enter()
        self.type_keys_with_interval(1,'te12!@')
        self.enter()
        self.type_keys_with_interval(1,'t1!')
        self.tab()
        self.tab()
        x=0
        while x<12:
            if not self.find( "tipodoitemsped1", matching=0.97, waiting_time=10000):
                self.not_found("tipodoitemsped1")
            self.click_relative(223, 27)
            self.type_down()
            self.enter()
            x=x+1
        
        self.type_down()    
        self.type_up()
        self.enter()
                
        x=0
        while x<250:
            self.type_down()
            x=x+1
        
                        ####---A1P1 PRECOS E CUSTOS---####
                        
        if not self.find( "custounitario", matching=0.97, waiting_time=10000):
            self.not_found("custounitario")
        self.click_relative(77, 45)
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.enter()
        
        self.wait(2000)
        if not bot.find( "crm_operacao_calculo_rel_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_operacao_calculo_rel_buscar")
        bot.click_relative(51, 22)
        
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not bot.find( "crm_regiao_calculo_rel_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_regiao_calculo_rel_buscar")
        bot.click_relative(54, 23)
        self.wait(500)
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_grupo_fiscal_rel_buscar_calculo", matching=0.97, waiting_time=10000):
            not_found("crm_grupo_fiscal_rel_buscar_calculo")
        bot.click_relative(52, 20)         
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.tab()
        self.enter()
        if not self.find( "tabelaprecooperacaoci", matching=0.97, waiting_time=10000):
            self.not_found("tabelaprecooperacaoci")
        self.click_relative(340, 25)
        self.enter()
        if not self.find( "regiaotabelaprecocadastroitens", matching=0.97, waiting_time=10000):
            self.not_found("regiaotabelaprecocadastroitens")
        self.click_relative(268, 27)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        self.enter()
        self.type_keys_with_interval(1,'123')
        
                        ####---A1P1 AGRUPAMENTO---#### 
        
        if not self.find( "familiaCI", matching=0.97, waiting_time=10000):
            self.not_found("familiaCI")
        self.click_relative(49, 43)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "marcaCI", matching=0.97, waiting_time=10000):
            self.not_found("marcaCI")
        self.click_relative(51, 85)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "controleCI", matching=0.97, waiting_time=10000):
            self.not_found("controleCI")
        self.click_relative(49, 128)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "unidadetributariaCI", matching=0.97, waiting_time=10000):
            self.not_found("unidadetributariaCI")
        self.click_relative(50, 163)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
            self.not_found("codcaixa")
        self.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        
        if not bot.find( "crm_cadeia_preços_botao_rel_cad", matching=0.97, waiting_time=10000):
            not_found("crm_cadeia_preços_botao_rel_cad")
        bot.click_relative(46, 24)
        self.backspace()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        self.backspace()
        if not self.find( "grupoCI", matching=0.97, waiting_time=10000):
            self.not_found("grupoCI")
        self.click_relative(452, 44)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        if not self.find( "tipoCI", matching=0.97, waiting_time=10000):
            self.not_found("tipoCI")
        self.click_relative(451, 83)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        
        self.wait(1000)
        if not self.find( "unidadeestoqueCI", matching=0.97, waiting_time=10000):
            self.not_found("unidadeestoqueCI")
        self.click_relative(448, 125)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "cadeiaprecoCI", matching=0.97, waiting_time=10000):
            self.not_found("cadeiaprecoCI")
        self.click_relative(451, 165)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
                
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "picontas97CI", matching=0.97, waiting_time=10000):
            self.not_found("picontas97CI")
        self.click_relative(452, 206)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
                  
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "subgrupoci", matching=0.97, waiting_time=10000):
            self.not_found("subgrupoci")
        self.click_relative(851, 43)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "subtipoci", matching=0.97, waiting_time=10000):
            self.not_found("subtipoci")
        self.click_relative(850, 84)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "unidadeetiquetaCI", matching=0.97, waiting_time=10000):
            self.not_found("unidadeetiquetaCI")
        self.click_relative(850, 124)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        if not self.find( "grupofiscalCI", matching=0.97, waiting_time=10000):
            self.not_found("grupofiscalCI")
        self.click_relative(850, 167)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        
        if not bot.find( "crm_centro_custos_cad_itens_estoque", matching=0.97, waiting_time=10000):
            not_found("crm_centro_custos_cad_itens_estoque")
        bot.click_relative(82, 30)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.wait(1000)


        if not bot.find( "crm_pi_contas_97_rel_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_pi_contas_97_rel_buscar")
        bot.click_relative(44, 22)
        self.type_keys_with_interval(100,"1")
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
              
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        if not bot.find( "crm_ncm_botao_buscar_cad_itens", matching=0.97, waiting_time=10000):
            not_found("crm_ncm_botao_buscar_cad_itens")
        bot.click_relative(102, 22)
        self.wait(1000)
        self.type_keys_with_interval(100,"2")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_pi_contas_80_rel_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_pi_contas_80_rel_buscar")
        bot.click_relative(47, 23)
        self.type_keys_with_interval(100,"1")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.wait(500)
        
        self.type_keys_with_interval(1,'!')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        
        ####---A1P1 MARCADORES---####
        self.wait(2000)
        if not self.find( "materiaprimaci", matching=0.97, waiting_time=10000):
            self.not_found("materiaprimaci")
        self.click_relative(14, 27)
        self.space()
        self.tab()
        self.space()
        self.space()
        x=0
        while x<13:
            self.tab()
            self.space()
            self.space()
            x=x+1
        self.tab()
        self.type_keys_with_interval(1,'87487487487487')
        self.tab()
        x=0
        while x<3:
            self.type_down()
            x=x+1    
        
                        ####---ABA1 P2---####
        self.wait(3000)

        if not bot.find( "crm_cadastro_item_5_comissionamento", matching=0.97, waiting_time=10000):
            not_found("crm_cadastro_item_5_comissionamento")
        bot.click()
        
        x=0
        while x<7:
            self.type_down()
            x=x+1
        x=0
        while x<7:
            self.type_up()
            x=x+1
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.backspace()
        self.backspace()
        self.backspace()
        self.type_keys_with_interval(1,'0')            
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.backspace()
        self.backspace()
        self.backspace()
        self.type_keys_with_interval(1,'0')
        self.tab()
        x=0
        while x<5:
            self.type_down()
            x=x+1
        x=0
        while x<2:
            self.type_up()
            x=x+1
        self.tab()
        self.type_down()
        self.type_up()
        self.type_up()
        self.backspace()
        self.type_keys_with_interval(1,'0')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'t1!')
        self.tab()
        self.tab()
        x=0
        while x<8:
            self.type_down()
            x=x+1
        x=0
        while x<4:
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            x=x+1
        
                        ####---ABA1 P3---####
                        #preços
        self.wait(2000)

        if not self.find( "a1p3CI", matching=0.97, waiting_time=10000):
            self.not_found("a1p3CI")
        self.click() 
        if not bot.find( "crm_cad_itens_ofertas_6_precos", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_ofertas_6_precos")
        bot.click() # ofertas
        if not self.find( "a1p3.3CI", matching=0.97, waiting_time=10000):
            self.not_found("a1p3.3CI")
        self.click()

        #### 7 Quantidades ####
        if not bot.find( "crm_cad_itens_7_quantidades", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_7_quantidades")
        bot.click()
        if not bot.find( "crm_cadastro_itens_7_possui_lote", matching=0.97, waiting_time=10000):
            not_found("crm_cadastro_itens_7_possui_lote")
        bot.click()
        self.tab()
        x=0
        while x<6:
            self.type_down()
            x=x+1
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        x=0
        while x<3:
            self.type_down()
            x=x+1
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        
        #######################
        ######## LOTES ########
        #######################
        self.wait(2000)
        if not bot.find( "crm_btn_lotes_cad_itens", matching=0.97, waiting_time=10000):
            not_found("crm_btn_lotes_cad_itens")
        bot.click()
        
        
        self.wait(2000)
                        ####---A1 P5---####
                
        if not self.find( "a1p5CI", matching=0.97, waiting_time=10000):
            self.not_found("a1p5CI")
        self.click()
        
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'12')
        self.tab()
        self.type_keys_with_interval(1,'12')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.tab()
        x=0
        while x<13:
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=x+1
        x=0
        while x<5:
            self.type_down()
            x=x+1
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,'12')
        self.tab()
        x=0
        while x<6:
            self.type_keys_with_interval(1,'te12!@')    
            self.tab()
            x=x+1
        self.space()
        self.space()
        self.space()
        self.wait(500)
        self.tab()
        self.space()
        self.space()
        self.space() 
        self.tab()
        x=0
        while x<7:
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            x=x+1
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_down()
        self.type_up()
        self.type_up()
        if not self.find( "outrasinegracoes1ci", matching=0.97, waiting_time=10000):
            self.not_found("outrasinegracoes1ci")
        self.click_relative(14, 44)
        if not self.find( "outrasintegracoes2ci", matching=0.97, waiting_time=10000):
            self.not_found("outrasintegracoes2ci")
        self.click_relative(147, 45)
        
                        ####---ABA 2---####
                                        
        if not self.find( "aba2CI", matching=0.97, waiting_time=10000):
            self.not_found("aba2CI")
        self.click()
        if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
            self.not_found("salvarenquete")
        self.click()
        self.enter()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "commit_registro_a2p2_CI", matching=0.97, waiting_time=10000):
            self.not_found("commit_registro_a2p2_CI")
        self.click_relative(16, 184)
        
        if not self.find( "excluir_a2p1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluir_a2p1_CI")
        self.click_relative(15, 162)
        
        self.enter()
        
        
        
                        ####---ABA2 P2---####
                            
        if not bot.find( "crm_cad_itens_5_similares", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_5_similares")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
            self.not_found("procuraritensCI")
        self.click_relative(10, 34)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(4000)
        
        self.wait(500)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        #self.wait(500)
        #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
        #    self.not_found("quantidade_lancitens")
        #self.click_relative(336, 280)
        #self.backspace()
        #self.enter()
        #x=0
        #while x<31:
        #    self.type_down()
        #    x=x+1
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        self.wait(500)
        self.type_keys_with_interval(1,'1')
        if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
            self.not_found("botaoconfirmaritensreqcompras")
        self.click()
        self.wait(3000)
        
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)           
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not self.find( "aba2p2.2CI", matching=0.97, waiting_time=10000):
            self.not_found("aba2p2.2CI")
        self.click()
        
                        ####---ABA2 P3---####
            
        if not bot.find( "crm_cad_itens_6_agregados", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_6_agregados")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
            self.not_found("procuraritensCI")
        self.click_relative(10, 34)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(4000)
        
        
        self.wait(500)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        #self.wait(500)
        #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
        #    self.not_found("quantidade_lancitens")
        #self.click_relative(336, 280)
        #self.backspace()
        #self.enter()
        #x=0
        #while x<31:
        #    self.type_down()
        #    x=x+1
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        self.wait(500)
        self.type_keys_with_interval(1,'1')
        if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
            self.not_found("botaoconfirmaritensreqcompras")
        self.click()
        self.wait(3000)
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        self.enter()
        
                        ####---ABA2 P4---####                             
                        #### 7COMPOSIÇÃO ####            
        if not bot.find( "crm_itens_cad_7_composicao", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_7_composicao")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
            self.not_found("procuraritensCI")
        self.click_relative(10, 34)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        self.wait(4000)
        
        self.wait(500)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.wait(500)
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        #self.wait(500)
        #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
        #    self.not_found("quantidade_lancitens")
        #self.click_relative(336, 280)
        #self.backspace()
        #self.enter()
        #x=0
        #while x<31:
        #    self.type_down()
        #    x=x+1
        #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
        #    self.not_found("selecionarmunicipiovcr")
        #self.click()
        self.wait(500)
        self.type_keys_with_interval(1,'1')
        if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
            self.not_found("botaoconfirmaritensreqcompras")
        self.click()
        self.wait(3000)
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "excluirregistroa2p4_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p4_CI")
        self.click_relative(16, 187)
                    
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_itens_cad_servicos_osm", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_servicos_osm")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30) 
        if not bot.find( "crm_servicos_osm_relativo_servico", matching=0.97, waiting_time=10000):
            not_found("crm_servicos_osm_relativo_servico")
        bot.click_relative(25, 43)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.space()
        self.space()
        if not self.find( "cancelara2p4.2CI", matching=0.97, waiting_time=10000):
            self.not_found("cancelara2p4.2CI")
        self.click()           
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
        if not self.find( "a2p4.3CI", matching=0.97, waiting_time=10000):
            self.not_found("a2p4.3CI")
        self.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30) 
        if not bot.find( "crm_item_cad_fases_busc_etapa_serv", matching=0.97, waiting_time=10000):
            not_found("crm_item_cad_fases_busc_etapa_serv")
        bot.click_relative(-69, 43)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        if not self.find( "cancelara2p4.3CI", matching=0.97, waiting_time=10000):
            self.not_found("cancelara2p4.3CI")
        self.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
        self.wait(2000)
                        ####---ABA2 P5---####
                  ### 8 REFERENCIAS ADICIONAIS ###
        if not bot.find( "crm_itens_cad_8_referencias_ad", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_8_referencias_ad")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not bot.find( "crm_fornecedor_cliente_cad_itens", matching=0.97, waiting_time=10000):
            not_found("crm_fornecedor_cliente_cad_itens")
        bot.click_relative(60, 23)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'te12!@')           
        if not bot.find( "crm_itens_cad_unidade_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_unidade_buscar")
        bot.click_relative(63, 24)
        self.tab()
        self.wait(200)
        self.tab()
        self.wait(200)
        self.tab()
        self.wait(200)
        self.type_down()                 
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'t1!')
        self.tab()
        self.type_keys_with_interval(1,'123')
        if not self.find( "salvarregistro_a2p5_CI", matching=0.97, waiting_time=10000):
            self.not_found("salvarregistro_a2p5_CI")
        self.click_relative(16, 183)
        if not self.find( "cancelarregistro_a2p5_CI", matching=0.97, waiting_time=10000):
            self.not_found("cancelarregistro_a2p5_CI")
        self.click_relative(16, 206)
        self.enter() 
        if not self.find( "excluirregistro_a2p5_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistro_a2p5_CI")
        self.click_relative(15, 164)
        
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
        self.wait(2000)
        
                        ####---ABA2 P6---####
                        ## PREÇOS E PAUTAS ##

                                
        if not bot.find( "crm_itens_cad_9_precos_pauta", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_9_precos_pauta")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not bot.find( "crm_tabela_precos_tabela_bsc", matching=0.97, waiting_time=10000):
            not_found("crm_tabela_precos_tabela_bsc")
        bot.click_relative(49, 47)
        self.wait(2000)
        
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.enter()
        if not self.find( "a2p6.2CI", matching=0.97, waiting_time=10000):
            self.not_found("a2p6.2CI")
        self.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not bot.find( "crm_itens_cad_valor_pauta_buscar", matching=0.97, waiting_time=10000):
            not_found("crm_itens_cad_valor_pauta_buscar")
        bot.click_relative(54, 26)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "voltarparacodigoa2p6.2ci", matching=0.97, waiting_time=10000):
            self.not_found("voltarparacodigoa2p6.2ci")
        self.click_relative(-63, 53)          
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.enter()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
                        ####---ABA2 P7---####
                         ###  UNIDADES  ###
        if not self.find( "a2p7CI", matching=0.97, waiting_time=10000):
            self.not_found("a2p7CI")
        self.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not bot.find( "crm_unidade_adicional_cad_itens", matching=0.97, waiting_time=10000):
            not_found("crm_unidade_adicional_cad_itens")
        bot.click_relative(41, 23)
        if not self.find( "codcxunidadea2p7ci", matching=0.97, waiting_time=10000):
            self.not_found("codcxunidadea2p7ci")
        self.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.tab()
        self.enter()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
                        ####---ABA2 P8---####
                        #FOTOS#
        if not bot.find( "crm_fotos_cad_itens_f2", matching=0.97, waiting_time=10000):
            not_found("crm_fotos_cad_itens_f2")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        self.type_keys_with_interval(1,'te12!@')
        x=0
        while x<6:
            self.backspace()
            x=x+1
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.enter() 
        if not self.find( "excluir_foto_a2p8_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluir_foto_a2p8_CI")
        self.click_relative(16, 184)
        
        
        self.enter()
        
                        ####---ABA2 P9---#####
                  ## CODIGOS DE BARRA ADICIONAIS ##
        
        if not bot.find( "crm_cad_itens_cod_barras_adicionais", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_cod_barras_adicionais")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        self.type_keys_with_interval(1,'12312312312312')
        self.tab()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click() 
        self.enter()
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.enter()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
                        ####---ABA2 P10---####
                            
        if not bot.find( "crm_cad_itens_endereco_de_estoque", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_endereco_de_estoque")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        if not bot.find( "crm_cad_itens_endereco_busc", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_endereco_busc")
        bot.click_relative(58, 23)
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.enter()             
        
                        ####---ABA2 P11---####
                            
        if not bot.find( "crm_cad_itens_clientes_07", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_clientes_07")
        bot.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)           
        if not bot.find( "crm_cad_itens_cliente_rel_busc", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_cliente_rel_busc")
        bot.click_relative(66, 25)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        x=0
        while x<18:
            self.type_down()
            x=x+1
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.enter()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        
                        ####---ABA2 P12---####
                            
        if not self.find( "a2p12CI", matching=0.97, waiting_time=10000):
            self.not_found("a2p12CI")
        self.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.enter()
        if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
            self.not_found("excluirregistroa2p2.1_CI")
        self.click_relative(17, 163)
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()

                        ####---A2 P13---####
                            
        if not self.find( "a2p13ci", matching=0.97, waiting_time=10000):
            self.not_found("a2p13ci")
        self.click()
        if not bot.find( "crm_cad_itens_2_relacionamento_add", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_2_relacionamento_add")
        bot.click_relative(-81, 30)
        self.wait(1500)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1500)
                                            
                                                                          
                        ####---ABA 3---####
                        ### CARDEX ###
        if not bot.find( "crm_cad_itens_3_cardex", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_3_cardex")
        bot.click()
        if not bot.find( "crm_cad_itens_3_cardex_documento_rel", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_3_cardex_documento_rel")
        bot.double_click_relative(62, 21)
        self.type_keys_with_interval(1,'123')
        
        if not self.find( "periodoaba3ci", matching=0.97, waiting_time=10000):
            self.not_found("periodoaba3ci")
        self.click_relative(31, 11)
        if not self.find( "carregaranoaba3", matching=0.97, waiting_time=10000):
            self.not_found("carregaranoaba3")
        self.click()
        if not self.find( "anoatualaba3CI", matching=0.97, waiting_time=10000):
            self.not_found("anoatualaba3CI")
        self.click()
        self.tab()
        x=0
        while x<11:
            self.type_down()
            x=x+1
        if not bot.find( "crm_cad_itens_3_cardex_local_estoque", matching=0.97, waiting_time=10000):
            not_found("crm_cad_itens_3_cardex_local_estoque")
        bot.click_relative(76, 24)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        
        self.tab()
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
        
                        ####---FINALIZACAO---####
        
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not self.find( "localizarcodte12!@CI", matching=0.97, waiting_time=10000):
            self.not_found("localizarcodte12!@CI")
        self.click_relative(4, 33)
        self.type_keys_with_interval(1,'te12')
        self.enter()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        
               
        #####################################################################
        ############################---FORMULAS---###########################
        #####################################################################
                            
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "formulas", matching=0.97, waiting_time=10000):
            self.not_found("formulas")
        self.click()
        if not self.find( "buscarempresaformulas", matching=0.97, waiting_time=10000):
            self.not_found("buscarempresaformulas")
        self.click_relative(178, 38)           
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'te12!@')
        if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
            self.not_found("salvarenquete")
        self.click()
        if not bot.find( "crm_cad_formulas_padroes", matching=0.97, waiting_time=10000):
            not_found("crm_cad_formulas_padroes")
        bot.click()
        self.click()
        if not self.find( "cancelarformula", matching=0.97, waiting_time=10000):
            self.not_found("cancelarformula")
        self.click()           
        ### abandonar operação ###
        self.wait(1000)
        self.enter()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
            self.not_found("salvarenquete")
        self.click()
        self.wait(1000)
        if not self.find( "consultaform", matching=0.97, waiting_time=10000):
            self.not_found("consultaform")
        self.click()
        if not bot.find( "crm_btn_selecionar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_selecionar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
        #####################################################################
                          ####---LOCAL DE ESTOQUE---####
        #####################################################################                            
        if not self.find( "cont_cad_menu_princ_opc_19_2", matching=0.97, waiting_time=10000):
            not_found("cont_cad_menu_princ_opc_19_2")
        self.click()
        if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("itensdeestoque")
        self.click()
        if not self.find( "localdeestoque", matching=0.97, waiting_time=10000):
            self.not_found("localdeestoque")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.type_down()
        if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
            self.not_found("salvarenquete")
        self.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(100,"te12")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        
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
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(1000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
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
        if not bot.find( "crm_plano_financeiro_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_plano_financeiro_24_07")
        bot.click()

        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
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
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        self.wait(2000)
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(1000)
        self.type_keys_with_interval(100,"qa12")
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        self.wait(1000)
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        self.wait(2000)
        # mouse parou em cima de retornar, apenas clicar para voltar ao menu
        self.click()
        

        ######################################################
        ############ CLASSIFICACOES #########################
        ######################################################
        self.wait(2000)

        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
        self.click()
        if not self.find( "classificacoes", matching=0.97, waiting_time=10000):
            self.not_found("classificacoes")
        self.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()            
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.type_keys_with_interval(1,'te12!@')
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
            self.not_found("buscarcodteteste")
        self.click_relative(12, 29)
        self.type_keys_with_interval(1,'te12')
        self.enter()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
            
        
        ################################################################################################
        ############### CADASTRO -> CONDICAO DE PAGAMENTO ##########################
        ################################################################################################

        if not self.find( "cont_cadastros_menu_princ_opc_08", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_princ_opc_08")
        self.click()
        if not self.find( "condicoesdepagamento", matching=0.97, waiting_time=10000):
            self.not_found("condicoesdepagamento")
        self.click()
        self.wait(2000)
        if not bot.find( "crm_btn_incluir_princ_24_07", matching=0.97, waiting_time=10000):
            not_found("crm_btn_incluir_princ_24_07")
        bot.click()
        self.wait(1000)
        if not bot.find( "crm_cad_cond_pagamento_nao", matching=0.97, waiting_time=10000):
            not_found("crm_cad_cond_pagamento_nao")
        bot.click()
        self.wait(2000)
        self.type_keys_with_interval(1,'te12!@')
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        self.type_up()
        self.type_up()
        self.type_down()
        self.type_down()
        x=0
        while x<4:
            self.tab()
            self.type_keys_with_interval(1,'123')
            x=x+1
        self.tab()    
        self.type_down()
        self.type_down()
        self.type_up()
        self.tab()
        self.type_down()
        self.type_up()
        self.type_down()
        x=0
        while x<6:
            self.tab()
            self.type_keys_with_interval(1,'123')
            x=x+1
        
        if not self.find( "tipodepagamentoprevisto", matching=0.97, waiting_time=10000):
            self.not_found("tipodepagamentoprevisto")
        self.click_relative(60, 47)
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not self.find( "operacaobaixafinanceiro", matching=0.97, waiting_time=10000):
            self.not_found("operacaobaixafinanceiro")
        self.click_relative(58, 87)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not self.find( "planofinanceiro", matching=0.97, waiting_time=10000):
            self.not_found("planofinanceiro")
        self.click_relative(487, 46)
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not self.find( "comissaoCP", matching=0.97, waiting_time=10000):
            self.not_found("comissaoCP")
        self.click_relative(461, 88)
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not self.find( "oplancfinanceiroCP", matching=0.97, waiting_time=10000):
            self.not_found("oplancfinanceiroCP")
        self.click_relative(859, 46)
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not self.find( "localcobrancaCP", matching=0.97, waiting_time=10000):
            self.not_found("localcobrancaCP")
        self.click_relative(862, 89)
        if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            self.not_found("selecionarmunicipiovcr")
        self.click()
        self.wait(500)
        if not bot.find( "crm_btn_salvar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_salvar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
            self.not_found("buscarcodteteste")
        self.click_relative(12, 29)
        self.type_keys_with_interval(1,'te12')
        self.enter()
        if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
            self.not_found("redesocialteste")
        self.click()
        if not bot.find( "crm_btn_editar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_editar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_excluir_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_excluir_opc1_2407")
        bot.click()
        #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
        #    self.not_found("simexcluirrs")
        #self.click()
        self.enter()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_localizar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_localizar_opc1_2407")
        bot.click()
        if not bot.find( "crm_btn_retornar_opc1_2407", matching=0.97, waiting_time=10000):
            not_found("crm_btn_retornar_opc1_2407")
        bot.click()



def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  

