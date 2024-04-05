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
        
      
       
        
        
        
        if not bot.find( "cont_incluir_cod_fisc_impo_23", matching=0.97, waiting_time=10000):
            not_found("cont_incluir_cod_fisc_impo_23")
        bot.click()
        if not bot.find( "cont_cod_fisc_busc_impos_23", matching=0.97, waiting_time=10000):
            not_found("cont_cod_fisc_busc_impos_23")
        bot.click()
        
        
        if not bot.find( "cont_confirma_incluir_cod_fisc_imp", matching=0.97, waiting_time=10000):
            not_found("cont_confirma_incluir_cod_fisc_imp")
        bot.click()
        
       
        if not bot.find( "cont_itens_menu_tipo_do_item", matching=0.97, waiting_time=10000):
            not_found("cont_itens_menu_tipo_do_item")
        bot.click()
        
        
        if not bot.find( "cont_salvar_opc_23_plano_c", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_23_plano_c")
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
        
        if not bot.find( "cont_opc_editar_mov_fiscal_2", matching=0.97, waiting_time=10000):
            not_found("cont_opc_editar_mov_fiscal_2")
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
        
        
       
        
        
        
        if not bot.find( "cont_cadastro_movimento_impo_flecha", matching=0.97, waiting_time=10000):
            not_found("cont_cadastro_movimento_impo_flecha")
        bot.click()
        if not bot.find( "cont_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_gerar")
        bot.click()
        
        
        
        if not bot.find( "cont_relatorios_impressao_btn_x_verm", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_impressao_btn_x_verm")
        bot.click()
        
        
        
        
        if not bot.find( "cont_cancelar_opc_26_02", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_opc_26_02")
        bot.click()
        
        
        if not bot.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        bot.click()
        
        if not bot.find( "cont_salvar_mov_btn_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_mov_btn_opc_8")
        bot.click()
        if not bot.find( "cont_movimentos_menu_opc_2", matching=0.97, waiting_time=10000):
            not_found("cont_movimentos_menu_opc_2")
        bot.click()
        
       
        
        if not bot.find( "cont_editar_mov_opc_08_3", matching=0.97, waiting_time=10000):
            not_found("cont_editar_mov_opc_08_3")
        bot.click()
        
        
        
       

       
        
        if not bot.find( "cont_mov_select_opc_08_03", matching=0.97, waiting_time=10000):
            not_found("cont_mov_select_opc_08_03")
        bot.click()
        if not bot.find( "cont_btn_excluir_movimento_presumido_opc_8", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimento_presumido_opc_8")
        bot.click()
        
       
        if not bot.find( "cont_salvar_opc_rel_mov_fiscal", matching=0.97, waiting_time=10000):
            not_found("cont_salvar_opc_rel_mov_fiscal")
        bot.click()
        
        if not bot.find( "cont_rel_mov_matrical_livros_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_matrical_livros_iss")
        bot.click()
        if not bot.find( "cont_rel_mov_fiscal_livro_iss_fechar_matrical", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fiscal_livro_iss_fechar_matrical")
        bot.click()
        
        if not bot.find( "cont_rela_mov_imprimir_achar_iss", matching=0.97, waiting_time=10000):
            not_found("cont_rela_mov_imprimir_achar_iss")
        
        if not bot.find( "cont_relatorios_mov_fis_apuracao_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fis_apuracao_imposto")
        bot.click()
        
        if not bot.find( "cont_data_rela_mov_apuracao_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_data_rela_mov_apuracao_imposto")
        bot.click_relative(27, 7)
        if not bot.find( "cont_rel_mov_fisc_dipi_data", matching=0.97, waiting_time=10000):
            not_found("cont_rel_mov_fisc_dipi_data")
        bot.click_relative(28, 8)
        
        
        
        if not bot.find( "cont_relatorios_btn_grafico_geral_opc_1", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_grafico_geral_opc_1")
        bot.click()
        if not bot.find( "cont_relatorios_x_geral_fechar_mat_imp", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_x_geral_fechar_mat_imp")
        bot.click()
        if not bot.find( "cont_relatorios_opc_selecionar_22_03", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_opc_selecionar_22_03")
        bot.click()
        
        if not bot.find( "cont_relatorios_mov_fiscal_icms_imprimir", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_icms_imprimir")
        bot.click()
        
        if not bot.find( "cont_relatorios_matrical_opc_1_mov", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_matrical_opc_1_mov")
        bot.click()
        if not bot.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        bot.click()
        
        if not bot.find( "cont_relatorios_mov_resumo_municipio", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_resumo_municipio")
        bot.click()
        if not bot.find( "cont_relatorios_mov_livro_oficial_resumo_mun", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_livro_oficial_resumo_mun")
        bot.click_relative(109, 3)
        if not bot.find( "cont_relatorios_mov_centro_custo_resumo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_resumo")
        bot.click_relative(77, 25)
        if not bot.find( "cont_relatorios_mov_centro_custo_final_resumo", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_centro_custo_final_resumo")
        bot.click_relative(76, 24)
        if not bot.find( "cont_mov_relatorios_data_ano_atual", matching=0.97, waiting_time=10000):
            not_found("cont_mov_relatorios_data_ano_atual")
        bot.click()
        if not bot.find( "cont_relatorios_mov_matrical_btn_ok", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_matrical_btn_ok")
        bot.click()
        if not bot.find( "cont_relatorios_mov_fechar_matricial_btn", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fechar_matricial_btn")
        bot.click()
        if not bot.find( "cont_relatorios_mov_fiscal_livro_de_iss_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_fiscal_livro_de_iss_diario")
        bot.click()
        if not bot.find( "cont_cad_btn_selec_opc_22_03", matching=0.97, waiting_time=10000):
            not_found("cont_cad_btn_selec_opc_22_03")
        bot.click()
        if not bot.find( "cont_parametro_empresa_qa12_achar", matching=0.97, waiting_time=10000):
            not_found("cont_parametro_empresa_qa12_achar")
        bot.click()
        
        
        
      





def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()



