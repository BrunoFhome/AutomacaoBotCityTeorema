from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()


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
        self.space()
        if not bot.find( "cont_cadastros_menu_pri_1", matching=0.97, waiting_time=10000):
            not_found("cont_cadastros_menu_pri_1")
        bot.click()
        if not bot.find( "cont_selecc_opc_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecc_opc_23")
        bot.click()
        if not bot.find( "cont_empresas_menu_1_pri_e", matching=0.97, waiting_time=10000):
            not_found("cont_empresas_menu_1_pri_e")
        bot.click()
       
        
        if not bot.find( "cont_selecionar_situacoes_op_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_situacoes_op_23")
        bot.click() #opcao janela grande
        if not self.find( "cont_opcao_2_23_selec", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_2_23_selec")
        self.click() # opcao janela pequena
        
        if not bot.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        bot.click()
        if not bot.find( "cont_cod_fisc_busc_impos_23", matching=0.97, waiting_time=10000):
            not_found("cont_cod_fisc_busc_impos_23")
        bot.click()
        if not bot.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        bot.click()
        
        if not bot.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        bot.click()
        
       
        if not bot.find( "cont_itens_menu_tipo_do_item", matching=0.97, waiting_time=10000):
            not_found("cont_itens_menu_tipo_do_item")
        bot.click()
        if not bot.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        bot.click()
     
        if not bot.find( "cont_editar_opc_23_impostos", matching=0.97, waiting_time=10000):
            not_found("cont_editar_opc_23_impostos")
        bot.click()
        
        if not bot.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
        bot.click()
        if not bot.find( "cont_opc_excluir_plano_contas", matching=0.97, waiting_time=10000):
            not_found("cont_opc_excluir_plano_contas")
        bot.click()
        
        if not bot.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        bot.click()
        if not bot.find( "cont_incluir_botao_contabilizacao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_botao_contabilizacao_imp")
        bot.click()
        if not bot.find( "cont_busc_imp_contabilizacao_23", matching=0.97, waiting_time=10000):
            not_found("cont_busc_imp_contabilizacao_23")
        bot.click()
        if not bot.find( "cont_confirma_opcao_contabilizacao_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_opcao_contabilizacao_imp")
        bot.click()
        if not bot.find( "cont_lixeira_20_imp", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_20_imp")
        bot.click()
        if not bot.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        bot.click()
        
        if not bot.find( "cont_btn_excluir_azul_escuro", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_azul_escuro")
        bot.click()
        if not bot.find( "cont_incluir_opc_imposto_pres_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_opc_imposto_pres_23")
        bot.click()
        if not bot.find( "cont_opc_3_conta_busc_btn", matching=0.97, waiting_time=10000):
            not_found("cont_opc_3_conta_busc_btn")
        bot.click()
        
        if not bot.find( "cont_btn_busc_ncm_23", matching=0.97, waiting_time=10000):
            not_found("cont_btn_busc_ncm_23")
        bot.click()
       
        if not bot.find( "cont_cancelar_referencias_itens", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_referencias_itens")
        bot.click()
        if not bot.find( "cont_cancelar_bot_itens_23", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_bot_itens_23")
        bot.click()
        
        if not bot.find( "cont_inserir_ale_codigo_bens", matching=0.97, waiting_time=10000):
            not_found("cont_inserir_ale_codigo_bens")
        bot.click()
        
        if not bot.find( "cont_bens_btn_loc_fornecedor", matching=0.97, waiting_time=10000):
            not_found("cont_bens_btn_loc_fornecedor")
        bot.click()
        
        if not bot.find( "cont_menu_servicos_23", matching=0.97, waiting_time=10000):
            not_found("cont_menu_servicos_23")
        bot.click()
        
        if not bot.find( "cont_selecionar_opcao_5_23_peq", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_opcao_5_23_peq")
        bot.click()
        
        if not bot.find( "cont_carregar_ano_servico_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_carregar_ano_servico_cardex")
        bot.click()
        if not bot.find( "cont_data_atual_servicos_cardex", matching=0.97, waiting_time=10000):
            not_found("cont_data_atual_servicos_cardex")
        bot.click()
        
        if not bot.find( "cont_precos_servicos_incluir_btn", matching=0.97, waiting_time=10000):
            not_found("cont_precos_servicos_incluir_btn")
        bot.click()
        if not bot.find( "cont_servicos_precos_btn_buscar", matching=0.97, waiting_time=10000):
            not_found("cont_servicos_precos_btn_buscar")
        bot.click()
        if not bot.find( "cont_gravar_servicos_preco", matching=0.97, waiting_time=10000):
            not_found("cont_gravar_servicos_preco")
        bot.click()
       
        
        if not bot.find( "cont_incluir_livros_oficiais_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_livros_oficiais_23")
        bot.click()
        if not bot.find( "cont_salvar_opcao_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opcao_livros_oficiais")
        bot.click()
        if not bot.find( "cont_retornar_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_retornar_livros_oficiais")
        bot.click()
        if not bot.find( "cont_excluir_livros_oficiais", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_livros_oficiais")
        bot.click()
        if not bot.find( "cont_botao_selec_pl_5", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_pl_5")
        bot.click()
        if not bot.find( "cont_botao_selec_tela_maior_2", matching=0.97, waiting_time=10000):
            not_found("cont_botao_selec_tela_maior_2")
        bot.click()
        if not bot.find( "cont_opc_editar_mov_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_opc_editar_mov_fiscal_2")
        bot.click()
        if not bot.find( "cont_excluir_botao_mov_fiscal_opc5", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_botao_mov_fiscal_opc5")
        bot.click()
        
        if not bot.find( "cont_lixeira_mov_contabil_f7_2", matching=0.97, waiting_time=10000):
            not_found("cont_lixeira_mov_contabil_f7_2")
        bot.click()
        if not bot.find( "cont_cancelar_opc_mov_contabil_f7", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_opc_mov_contabil_f7")
        bot.click()
        
        if not bot.find( "cont_bot_excluir_opc_3_mov_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_bot_excluir_opc_3_mov_lotes")
        bot.click()
        if not bot.find( "cont_encontrar_data_mov_ger_cont", matching=0.97, waiting_time=10000):
            not_found("cont_encontrar_data_mov_ger_cont")
        bot.click_relative(33, 7)
        if not bot.find( "cont_contabilizacao_mov_ger_cont", matching=0.97, waiting_time=10000):
            not_found("cont_contabilizacao_mov_ger_cont")
        bot.click()
        if not bot.find( "cont_confirmar_inventario_itens", matching=0.97, waiting_time=10000):
            not_found("cont_confirmar_inventario_itens")
        bot.click()
        
        if not bot.find( "cont_incluir_6_itens_bloco_k", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_6_itens_bloco_k")
        bot.click()
        
       
        if not bot.find( "cont_data_rel_cardox_cad_servico", matching=0.97, waiting_time=10000):
            not_found("cont_data_rel_cardox_cad_servico")
        bot.click_relative(30, 7)
        if not bot.find( "cont_consultar_cardex_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_consultar_cardex_cad_servicos")
        bot.click()
        
        if not bot.find( "cont_buscar_tabela_cad_servicos", matching=0.97, waiting_time=10000):
            not_found("cont_buscar_tabela_cad_servicos")
        bot.click()
        if not bot.find( "cont_lixo_cad_servico_movimentos_exclusao", matching=0.97, waiting_time=10000):
            not_found("cont_lixo_cad_servico_movimentos_exclusao")
        bot.click()
        
        if not bot.find( "cont_gravar_v_opcao_23_mov_itens", matching=0.97, waiting_time=10000):
            not_found("cont_gravar_v_opcao_23_mov_itens")
        bot.click()
        
        
        if not bot.find( "cont_selecionar_documentos_fiscais_item_23", matching=0.97, waiting_time=10000):
            not_found("cont_selecionar_documentos_fiscais_item_23")
        bot.click()
        if not bot.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        bot.click()
        
        if not bot.find( "cont_consulta_rel_localizar_selc", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_rel_localizar_selc")
        bot.click_relative(-42, 12)
        
        
        
        
        
        if not bot.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        bot.click()
        
        if not bot.find( "cont_consulta_grade_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grade_imprimir")
        bot.click()
        if not bot.find( "cont_consulta_grade_imprimir_cancel", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_grade_imprimir_cancel")
        bot.click()
        
        if not bot.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        bot.click()
        
        
        
        if not bot.find( "cont_consulta_total_imposto_consultar", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_total_imposto_consultar")
        bot.click()
        if not bot.find( "cont_data_anterior_ano", matching=0.97, waiting_time=10000):
            not_found("cont_data_anterior_ano")
        bot.click()
        
        if not bot.find( "cont_importacoes_exportacoes_menu", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_exportacoes_menu")
        bot.click()
        if not bot.find( "cont_importacao_exportacao_pad_teo_ex", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_pad_teo_ex")
        bot.click()
        
        if not bot.find( "cont_importacao_exportacao_data_rel", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_data_rel")
        bot.click_relative(28, 6)
        
        
        
        if not bot.find( "cont_cadastro_movimento_impo_flecha", matching=0.97, waiting_time=10000):
            not_found("cont_cadastro_movimento_impo_flecha")
        bot.click()
        if not bot.find( "cont_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_gerar")
        bot.click()
        if not bot.find( "cont_cancelar_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_importacao_exportacao_gerar")
        bot.click()
        
        
        
        if not bot.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        bot.click()
        
        
        
        if not bot.find( "cont_botao_editar_26_02_opc", matching=0.97, waiting_time=10000):
            not_found("cont_botao_editar_26_02_opc")
        bot.click()
        if not bot.find( "cont_excluir_opcao_26_02", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_opcao_26_02")
        bot.click()
        if not bot.find( "cont_cancelar_opc_26_02", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_opc_26_02")
        bot.click()
        
        
        if not bot.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        bot.click()
        if not bot.find( "cont_relatorios_movimento_livro_de_rel", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_livro_de_rel")
        bot.click_relative(7, 41)
        if not bot.find( "cont_relatorios_movimentos_fiscal_rel_imprime", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimentos_fiscal_rel_imprime")
        bot.click_relative(116, -14)
        if not bot.find( "cont_relatorios_movimento_fiscal_emi_livro_check", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_emi_livro_check")
        bot.click_relative(417, 10)
        if not bot.find( "cont_relatorios_movimento_fiscal_centro_ini", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_movimento_fiscal_centro_ini")
        bot.click_relative(178, 5)
        if not bot.find( "cont_salvar_mov_btn_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_mov_btn_opc_8")
        bot.click()
        if not bot.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        bot.click()
        
       
        
        if not bot.find( "cont_editar_mov_opc_08_3", matching=0.97, waiting_time=10000):
            not_found("cont_editar_mov_opc_08_3")
        bot.click()
        
        
        
        if not bot.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        bot.click()

        if not bot.find( "cont_btn_excluir_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_opc_08_03")
        bot.click()
        
        if not bot.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        bot.click()
        if not bot.find( "cont_btn_excluir_movimento_presumido_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimento_presumido_opc_8")
        bot.click()
        
      





def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()


