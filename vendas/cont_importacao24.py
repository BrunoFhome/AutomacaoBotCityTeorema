from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA CONTABIL 24.05 - PARTE DE IMPORTAÇÕES E EXPORTAÇÕES 
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - ICTUS 0000024
"""

"""
ESTA PARTE DO CÓDIGO LIDA COM GERAÇÕES, CRIEI UMA PASTA NA AREÁ DE TRABALHO DESTA MAQUINA COM O NOME "IMPORTAÇÕES
GERAÇÕES CONTABIL" PARA GRAVAR OS ARQUIVOS GERADOS NELA.
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
        self.wait(40000) # tempo de espera importação

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
        if not self.find( "cont_importacoes_dominio_export", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_dominio_export")
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
        self.wait(7000)
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

        if not self.find( "cont_import_rel_reduzido_plano_banco", matching=0.97, waiting_time=10000):
            not_found("cont_import_rel_reduzido_plano_banco")
        self.click_relative(63, 20)

        self.wait(2000)
        self.type_keys_with_interval(100,"00001")
        if not self.find( "cont_opcao_loc_imp_23", matching=0.97, waiting_time=10000):
            not_found("cont_opcao_loc_imp_23")
        self.click()
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

        if not self.find( "cont_importacao_btn_importar_txt", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_btn_importar_txt")
        self.click()
        
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