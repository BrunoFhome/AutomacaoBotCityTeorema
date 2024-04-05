from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA CONTABIL 23.07 - PARTE DE CONSULTAS/RELATORIOS
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
        if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_imprimir_cad")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
           not_found("cont_relatorios_x_fechar_cad")
        self.click()
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

        if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_imprimir_cad")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_fechar_cad")
        self.click()
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
        
        self.wait(1000)
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

        

        if not self.find( "cont_relatorios_imprimir_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_imprimir_cad")
        self.click()
        self.wait(1000)
        if not self.find( "cont_relatorios_x_fechar_cad", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_fechar_cad")
        self.click()
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
        
        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)

        if not self.find( "cont_relatorios_mov_centro_custo_final", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_final")
        self.click_relative(182, 5)

        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()

        if not self.find( "cont_24_btn_selecionar_opc_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_24_btn_selecionar_opc_relatorios")
        self.click()
        self.wait(1000)
        self.enter()
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

        if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        self.click()
        self.wait(15000)
        # carregamento devagar

        if not self.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        self.click()
        self.wait(1000)

        if not self.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        self.click()

        self.wait(2000)
        if not self.find( "cont_relatorios_mov_matrical_btn_ok", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_matrical_btn_ok")
        self.click()
        self.wait(2000)
        if not self.find( "cont_relatorios_mov_fechar_matricial_btn", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fechar_matricial_btn")
        self.click()
        self.wait(1000)
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###############################################################################################
        ################# RELATORIOS -> MOVIMENTO FISCAL -> LIVRO DE ISS (DIARIO)  ####################
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

        # if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #     not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        # self.click()

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

        # if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #     not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        # self.click()

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
        if not self.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        self.click()
        self.wait(1000)

        # IMPRIMIR NAO ESTA FUNCIONANDO

        # if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #     not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        # self.click()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()
        self.wait(1000)
        """
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
        if not self.find( "cont_relatorios_matrical_btn_fechar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_btn_fechar")
        self.click()
        self.wait(1000)

        # IMPRIMIR NAO ESTA FUNCIONANDO

        # if not self.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
        #     not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        # self.click()

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

        if not self.find( "cont_rel_fiscal_faturamento_empresa", matching=0.97, waiting_time=10000):
            not_found("cont_rel_fiscal_faturamento_empresa")
        self.click()



















































        





































        


        

        























        
        

























        
        



def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()