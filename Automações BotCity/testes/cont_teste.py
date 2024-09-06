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
        
       
        if not bot.find( "cont_cad_btn_selec_opc_22_03", matching=0.97, waiting_time=10000):
            not_found("cont_cad_btn_selec_opc_22_03")
        bot.click()
       
        if not bot.find( "vendas_pdv_data_botao_rel", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_data_botao_rel")
        bot.click_relative(28, 10)
        if not bot.find( "vendas_pdv_cliente_buscar_movimentos", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_cliente_buscar_movimentos")
        bot.click()
        if not bot.find( "vendas_pdv_localizar_opc_09", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_localizar_opc_09")
        bot.click()
        if not bot.find( "vendas_pdv_btn_retorno_consulta", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_retorno_consulta")
        bot.click()
        if not bot.find( "vendas_pdv_btn_entregas_vendas_24", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_entregas_vendas_24")
        bot.click()
        if not bot.find( "vendas_pdv_24_recomecar_venda", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_24_recomecar_venda")
        bot.click()
        if not bot.find( "vendas_pdv_btn_localizar", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_localizar")
        bot.click()
        if not bot.find( "vendas_pdv_btn_vendas_mais_2", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_vendas_mais_2")
        bot.click()
        if not bot.find( "vendaspdv_btn_documentos_vendas", matching=0.97, waiting_time=10000):
            not_found("vendaspdv_btn_documentos_vendas")
        bot.click()
        if not bot.find( "vendas_pdv_btn_f8simulacao_2", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_f8simulacao_2")
        bot.click()
        if not bot.find( "vendas_pdv_f11_recuperar_vendas_btn", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_f11_recuperar_vendas_btn")
        bot.click()
        if not bot.find( "vendas_pdv_cnpj_duplicado_btn", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_cnpj_duplicado_btn")
        bot.click()
        if not bot.find( "cont_data_relatorios_carregar_semana", matching=0.97, waiting_time=10000):
            not_found("cont_data_relatorios_carregar_semana")
        bot.click()
        if not bot.find( "cont_relatorios_mov_cont_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_mov_cont_lotes")
        bot.click()
        if not bot.find( "cont_data_relatorios_mov_cont_lotes", matching=0.97, waiting_time=10000):
            not_found("cont_data_relatorios_mov_cont_lotes")
        bot.click_relative(29, 8)
        
        if not bot.find( "cont_localizar_btn_relatorios_mov_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_localizar_btn_relatorios_mov_contabil")
        bot.click()
        if not bot.find( "cont_btn_selecionar_relatorios_mov_cont", matching=0.97, waiting_time=10000):
            not_found("cont_btn_selecionar_relatorios_mov_cont")
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
       
        if not bot.find( "cont_barra_tarefas_buscar_contabil", matching=0.97, waiting_time=10000):
            not_found("cont_barra_tarefas_buscar_contabil")
        bot.click()
        if not bot.find( "cont_balancete_de_verificacao_barra", matching=0.97, waiting_time=10000):
            not_found("cont_balancete_de_verificacao_barra")
        bot.click()
        
        if not bot.find( "cont_relatorios_btn_matrical_razao_analitica", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_matrical_razao_analitica")
        bot.click()
        if not bot.find( "cont_btn_ok_impressao_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_impressao_relatorios")
        bot.click()
        
        if not bot.find( "cont_btn_fechar_relatorios_matrical_impr", matching=0.97, waiting_time=10000):
            not_found("cont_btn_fechar_relatorios_matrical_impr")
        bot.click()
        if not bot.find( "cont_btn_retornar_relatorios_razao_analitico", matching=0.97, waiting_time=10000):
            not_found("cont_btn_retornar_relatorios_razao_analitico")
        bot.click()
        
       
        if not bot.find( "cont_btn_relatorios_matricial_diario", matching=0.97, waiting_time=10000):
            not_found("cont_btn_relatorios_matricial_diario")
        bot.click()
        if not bot.find( "cont_relatorios_btn_grafica_diario", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_btn_grafica_diario")
        bot.click()
        if not bot.find( "cont_relatorios_diario_btn_retornar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_diario_btn_retornar")
        bot.click()
        
       
        
        if not bot.find( "cont_btn_grafica_relatorios_balanco", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafica_relatorios_balanco")
        bot.click()
        
       
       
        if not bot.find( "cont_btn_grafico_dlpa_relatorios", matching=0.97, waiting_time=10000):
            not_found("cont_btn_grafico_dlpa_relatorios")
        bot.click()
        
        
       
        if not bot.find( "cont_botao_close_impressao", matching=0.97, waiting_time=10000):
            not_found("cont_botao_close_impressao")
        bot.click()
        if not bot.find( "cont_relat_gravar_documento_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_relat_gravar_documento_emissao")
        bot.click()
        if not bot.find( "cont_btn_ok_gravacao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_gravacao")
        bot.click()
        
        if not bot.find( "cont_relat_patrimonio_btn_adicionar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_patrimonio_btn_adicionar")
        bot.click()
        
        
        
        if not bot.find( "cont_btn_impressao_relat_patri", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impressao_relat_patri")
        bot.click()
        
        
        if not bot.find( "cont_relatorios_emissao_btn_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissao_btn_gerar")
        bot.click()
        if not bot.find( "cont_emissao_gerar_area_de_trab", matching=0.97, waiting_time=10000):
            not_found("cont_emissao_gerar_area_de_trab")
        bot.click()
        if not bot.find( "cont_achar_pasta_area_trab_geracao_rel", matching=0.97, waiting_time=10000):
            not_found("cont_achar_pasta_area_trab_geracao_rel")
        bot.click()
        if not bot.find( "cont_btn_salvar_emissao_geracao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_salvar_emissao_geracao")
        bot.click()
        if not bot.find( "cont_btn_ok_geracao_sucedida", matching=0.97, waiting_time=10000):
            not_found("cont_btn_ok_geracao_sucedida")
        bot.click()
        
        if not bot.find( "cont_btn_geracao_ok_emissao", matching=0.97, waiting_time=10000):
            not_found("cont_btn_geracao_ok_emissao")
        bot.click()
        
        if not bot.find( "cont_btn_importar_emissoes_rel_giad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_importar_emissoes_rel_giad")
        bot.click()
        
        if not bot.find( "cont_btn_gerar_relator_emissao_giad", matching=0.97, waiting_time=10000):
            not_found("cont_btn_gerar_relator_emissao_giad")
        bot.click()
       
        if not bot.find( "cont_btn_excluir_movimentos_opc_14", matching=0.97, waiting_time=10000):
            not_found("cont_btn_excluir_movimentos_opc_14")
        bot.click()
        
       
        if not bot.find( "cont_relat_emissoes_btn_ok_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_btn_ok_gerar")
        bot.click()
        
        
        if not bot.find( "cont_relat_emissoes_dime_calcular", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_calcular")
        bot.click()
        if not bot.find( "cont_relatorios_emissoes_dime_importar", matching=0.97, waiting_time=10000):
            not_found("cont_relatorios_emissoes_dime_importar")
        bot.click()
        
        if not bot.find( "cont_relat_emissoes_dime_gerar_inf", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_gerar_inf")
        bot.click()
        
        if not bot.find( "cont_relat_emissoes_dime_gerar_arquivo", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissoes_dime_gerar_arquivo")
        bot.click()
        if not bot.find( "cont_btn_impressao_relat_emissao_demi", matching=0.97, waiting_time=10000):
            not_found("cont_btn_impressao_relat_emissao_demi")
        bot.click()
        
        if not bot.find( "cont_relat_emissao_dirf_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_relat_emissao_dirf_gerar")
        bot.click()
        
        if not bot.find( "cont_vendas_pdv_btn_vendas_2407", matching=0.97, waiting_time=10000):
            not_found("cont_vendas_pdv_btn_vendas_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_localizar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_localizar_opc_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_gravar_nf_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_gravar_nf_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_entregar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_entregar_opc_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_recomecar_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_recomecar_24_07")
        bot.click()
        if not bot.find( "vendas_pdv_btn_vendas_mais_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_vendas_mais_opc_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_documentos_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_documentos_24_07")
        bot.click()
        
        if not bot.find( "vendas_pdv_f8_simulacao_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_f8_simulacao_2407")
        bot.click()
        if not bot.find( "vendas_pdv_f11_recup_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_f11_recup_2407")
        bot.click()
        if not bot.find( "vendas_pdv_filtragem_cnpj_dupli_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_filtragem_cnpj_dupli_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_continuar_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_continuar_2407")
        bot.click()
        if not bot.find( "vendas_pdv_agenda_os_relativo", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_agenda_os_relativo")
        bot.click_relative(94, 11)
        if not bot.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        bot.click()
        if not bot.find( "vendas_pdv_btn_excluir_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_excluir_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_chamadas_menu_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_chamadas_menu_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_retornar_2407_pesquisa", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_retornar_2407_pesquisa")
        bot.click()
        if not bot.find( "vendas_pdv_btn_doc_e_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_doc_e_2407")
        bot.click()
        
        if not bot.find( "vendas_pdv_btn_processos_rel_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_processos_rel_2407")
        bot.click_relative(79, 18)
        if not bot.find( "vendas_pdv_btn_voltar_2407_release", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_voltar_2407_release")
        bot.click()
        if not bot.find( "vendas_pdv_btn_sangria_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_sangria_2407")
        bot.click()
        if not bot.find( "vendas_pdv_btn_sangria_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_sangria_24_07")
        bot.click()
        
        
      





def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()



