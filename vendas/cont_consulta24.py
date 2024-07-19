from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA CONTABIL 24.05 - PARTE DE CONSULTAS/RELATORIOS
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
        
        ######################### COMEÇO DE CONSULTAS ##########################

        ########################################################################
        ####### CONSULTAS -> ANALISE DE BALANÇO VERTICAL E HORIZONTAL ##########
        ########################################################################
        self.wait(2000)
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

        #if not self.find( "cont_rel_mov_matrical_livros_iss", matching=0.97, waiting_time=10000):
        #    not_found("cont_rel_mov_matrical_livros_iss")
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

        #if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
        #    not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()
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

        self.wait(15000)

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

        self.wait(2000)

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

        self.wait(2000)

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

        if not self.find( "cont_btn_relatorios_matricial_diario", matching=0.97, waiting_time=10000):
            not_found("cont_btn_relatorios_matricial_diario")
        self.click()

        self.wait(3000)

        if not self.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        self.click()
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
        self.wait(55000)

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
        self.wait(8000)
        if not self.find( "cont_btn_retornar_relacao_diario_24", matching=0.97, waiting_time=10000):
            not_found("cont_btn_retornar_relacao_diario_24")
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

        if not self.find( "cont_relat_conf_codigo_fiscal_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relat_conf_codigo_fiscal_rel")
        self.click_relative(66, 21)

        self.wait(1000)
        if not self.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        self.click() 
        self.wait(1000)
        if not self.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
        self.click()
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

        if not self.find( "cont_relatorios_recolhimento_darf_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_recolhimento_darf_empresa")
        self.click_relative(93, 7)
        self.wait(1000)
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
        if not self.find( "cont_relat_emissoes_dime_imp_sucesso", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_imp_sucesso")
        self.click_relative(306, 48)

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

        self.wait(12000)

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



def not_found(label) :

    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()