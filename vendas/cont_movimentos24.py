from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA CONTABIL 23.07 - PARTE DE MOVIMENTOS
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
        
        #########################################################################################
        ################################ COMEÇO DE MOVIMENTOS ###################################
        #########################################################################################
        """
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
        self.wait(4000)
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

        if not self.find( "cont_operacao_relativo_desdobramento", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_relativo_desdobramento")
        self.click_relative(116, 25)
        self.wait(500)
        self.type_down()
        self.wait(500)
        self.enter()
        
        # x = 0
        # while x < 6:
        #     self.type_down()
        #     x += 1
        self.tab()
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
        if not self.find( "cont_excluir_24_opcao_nova", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_24_opcao_nova")
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
        
        ###
        #######################################################
        ########### MOVIMENTOS -> CONTABIL F7 ################
        #######################################################
        ###
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
        
        ##################################################
        ########### MOVIMENTOS -> LOTES  ##############
        #################################################
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
        
        
        # MOVIMENTOS -> INVENTARIO
        #
        # 

        
        self.wait(2000)

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
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        self.type_keys_with_interval(100,"123")
        self.tab()
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
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
        
        # MOVIMENTOS -> REDUÇÕES Z 
        #
        #
        #
        
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
        
        ########################################################
        #########    MOVIMENTOS -> INF. EXTRAS ->   ############
        ########################################################
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

        
        # MOVIMENTOS -> FECHAMENTOS CONTABEIS 
        #
        #
        #

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
        if not self.find( "cont_tipo_de_ajuste_mov_2060", matching=0.97, waiting_time=10000):
            not_found("cont_tipo_de_ajuste_mov_2060")
        self.click_relative(6, 28)
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
        if not self.find( "cont_cad_btn_selec_opc_22_03", matching=0.97, waiting_time=10000):
            not_found("cont_cad_btn_selec_opc_22_03")
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
        
        ##############################################
        ####### MOVIMENTOS -> Movimento CIAP #########
        ##############################################
        
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
        
        ###########################################################
        ###### MOVIMENTOS -> Movimento Fiscal - Inutilizadas ######
        ###########################################################
        
        
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
        """
        ###################################################
        ### MOVIMENTOS -> Movimento Documentos (Fiscal) ###
        ###################################################

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
        #########################################################
        ######### movimento de itens 2 ##########################
        ########################  #########################
        
        self.wait(1000)
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
        
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #

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
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        if not self.find( "cont_familia_cad_servicos_rel_mov", matching=0.97, waiting_time=10000):
            not_found("cont_familia_cad_servicos_rel_mov")
        self.click_relative(56, 29)
        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        if not self.find( "cont_grupo_agrupamento_cad_servicos_rel", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_agrupamento_cad_servicos_rel")
        self.click_relative(53, 30)

        self.wait(1000)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        self.wait(1000)
        if not self.find( "cont_24_botao_selecionar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_24_botao_selecionar_contabil")
        self.click()

        if not self.find( "cont_sub_grupo_rel_mov_cad_serv", matching=0.97, waiting_time=10000):
            not_found("cont_sub_grupo_rel_mov_cad_serv")
        self.click_relative(52, 26)
        self.wait(1000)
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
        self.enter()

        self.wait(1000)
        if not self.find( "cont_cardex_cadastro_servicos_mov", matching=0.97, waiting_time=10000):
            not_found("cont_cardex_cadastro_servicos_mov")
        self.click()

        if not self.find( "cont_data_rel_cardox_cad_servico", matching=0.97, waiting_time=10000):
            not_found("cont_data_rel_cardox_cad_servico")
        self.click_relative(30, 7)
        if not self.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        self.click()
        if not self.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        self.click()
        self.wait(1000)
        if not self.find( "cont_consultar_cardex_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_consultar_cardex_cad_servicos")
        self.click()
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
        self.wait(1000)
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
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
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
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
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

        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
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

        if not self.find( "cont_editar_mov_opc_08_3", matching=0.97, waiting_time=10000):
            not_found("cont_editar_mov_opc_08_3")
        self.click()

        if not self.find( "cont_excluir_24_opcao_nova", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_24_opcao_nova")
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
        self.wait(2000)

        # Voltar para apagar o serviço criado, para que nao acomule. NAO PODE ESTAR EM CAPS LOCK

        if not self.find( "cont_cadastros_men_prin_op4", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_men_prin_op4")
        self.click()
        self.wait(1000)
        if not self.find( "cont_menu_servicos_23", matching=0.97, waiting_time=10000):
            not_found("cont_menu_servicos_23")
        self.click()
        self.wait(2000)
        self.backspace()
        if not self.find( "teste_loc_serv", matching=0.97, waiting_time=10000):
            not_found("teste_loc_serv")
        self.click()
        if not self.find( "teste_achar_qa", matching=0.97, waiting_time=10000):
            not_found("teste_achar_qa")
        self.click()
        if not self.find( "teste_editar_qa", matching=0.97, waiting_time=10000):
            not_found("teste_editar_qa")
        self.click()
        if not self.find( "teste_excluir_qa", matching=0.97, waiting_time=10000):
             not_found("teste_excluir_qa")
        self.click()
        self.wait(1000)
        self.enter()
        if not self.find( "teste_retornar_qa", matching=0.97, waiting_time=10000):
            not_found("teste_retornar_qa")
        self.click()
        self.wait(1000)
        if not self.find( "teste_loc_serv", matching=0.97, waiting_time=10000):
            not_found("teste_loc_serv")
        self.click()
        self.wait(1000)
        if not self.find( "teste_retornar_qa", matching=0.97, waiting_time=10000):
            not_found("teste_retornar_qa")
        self.click()
        self.wait(1000)

        
        
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

        if not self.find( "cont_destinatario_rel_mov_transp", matching=0.97, waiting_time=10000):
            not_found("cont_destinatario_rel_mov_transp")
        self.click_relative(65, 23)
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

        
        ###########################################################
        ###### MOVIMENTOS -> Apuração Presumido ######
        ###########################################################
        
        
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

        if not self.find( "cont_btn_excluir_movimento_presumido_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimento_presumido_opc_8")
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
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        self.click()
        # Vazio, apenas dar OK
        self.wait(1000)
        self.enter()
        self.tab()
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
        self.wait(1000)
        if not self.find( "cont_incluir_imposto_por_cfop", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_imposto_por_cfop")
        self.click()
        self.wait(1000)
        self.type_down()
        # acontencendo erro aqui, esperar resolver apenas apertar enter
        self.wait(1000)
        self.enter()
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
        if not self.find( "cont_btn_excluir_movimento_presumido_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimento_presumido_opc_8")
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
        
        ###########################################################
        ############ MOVIMENTOS -> Fechamento Fiscal  #############
        ###########################################################

        self.wait(2000)
        if not self.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        self.click()
        self.wait(1000)
        if not self.find( "cont_fechamento_fiscal_menu_mov", matching=0.97, waiting_time=10000):
            not_found("cont_fechamento_fiscal_menu_mov")
        self.click()
        if not self.find( "cont_selecao_mov_fechamento_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_selecao_mov_fechamento_fiscal")
        self.click()
        self.wait(1000)

        # codigo fiscal
        if not self.find( "cont_codigo_fiscal_selecao_rlv", matching=0.97, waiting_time=10000):
            not_found("cont_codigo_fiscal_selecao_rlv")
        self.click_relative(69, 25)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        self.click()
        

        # operação
        if not self.find( "cont_operacao_mov_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_operacao_mov_rel_selecao")
        self.click_relative(67, 24)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        self.click()
        
        # cliente
        if not self.find( "cont_cliente_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_cliente_rel_selecao")
        self.click_relative(71, 21)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        self.click()

        # grupo de empresa
        if not self.find( "cont_grupo_de_empresa_rel_selecao", matching=0.97, waiting_time=10000):
            not_found("cont_grupo_de_empresa_rel_selecao")
        self.click_relative(66, 24)
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
        if not self.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        self.click()

        self.wait(1000)
        self.enter()
        # aqui o arquivo esta vazio, apenas apertar enter

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

        if not self.find( "cont_outros_debitos_do_imposto_rel", matching=0.97, waiting_time=10000):
            not_found("cont_outros_debitos_do_imposto_rel")
        self.click_relative(151, 3)

        
        x = 0
        while x < 5:
            self.type_keys_with_interval(100,"1")
            self.tab()
            x += 1
        self.wait(1000)

        #if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
        #    not_found("cont_salvar_opc_23_plano_c")
        #self.click()
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

        if not self.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        self.click()

        # Retornar 
        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ###########
        # ICMS ST #
        ###########
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
        



def not_found(label) :


    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()


