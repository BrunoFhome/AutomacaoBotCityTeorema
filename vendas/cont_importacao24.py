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

        #########################################################
        ############ COMEÇO DE IMPORTAÇÃO/EXPORTAÇÕES ############
        ##########################################################
        self.wait(2000)

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

        if not self.find( "cont_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_exportacao_gerar")
        self.click()
        self.wait(2000)

        if not self.find( "cont_cancelar_importacao_exportacao_gerar", matching=0.97, waiting_time=10000):
            not_found("cont_cancelar_importacao_exportacao_gerar")
        self.click()

        self.wait(1000)
        # Erro aparece por ter cancelado geração
        self.enter()

        if not self.find( "cont_retorn_opc_23_imposto", matching=0.97, waiting_time=10000):
            not_found("cont_retorn_opc_23_imposto")
        self.click()


        ######### IMPORTAÇÃO EXPORTAÇÕES -> PADRAO TEOREMA (IMPORTACOES)

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
        if not self.find( "cont_consulta_selecionar_opc1", matching=0.97, waiting_time=10000):
            not_found("cont_consulta_selecionar_opc1")
        self.click()
        self.wait(1000)

        if not self.find( "cont_importacoes_exportacoes_livros_fiscais", matching=0.97, waiting_time=10000):
            not_found("cont_importacoes_exportacoes_livros_fiscais")
        self.click()

        if not self.find( "cont_movimento_de_itens_rel_importacoes", matching=0.97, waiting_time=10000):
            not_found("cont_movimento_de_itens_rel_importacoes")
        self.click_relative(4, 25)

        self.wait(1000)
        # voltar para OPERAÇÃO
        self.shift_tab()
        self.wait(1000)
        self.type_right()
        self.wait(1000)
        if not self.find( "cont_importacao_livros_operacao_ok", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_livros_operacao_ok")
        self.click()
        self.wait(1000)
        self.type_right()

        if not self.find( "cont_importacao_importa_cfop_rel", matching=0.97, waiting_time=10000):
            not_found("cont_importacao_importa_cfop_rel")
        self.click_relative(-212, 36)
        # CONFERE "IMPORTA PELO CFOP" E VAI PARA CONTABILIDADE

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

        if not self.find( "cont_area_de_trabalho_pc", matching=0.97, waiting_time=10000):
            not_found("cont_area_de_trabalho_pc")
        self.click()
        self.wait(1000)
        if not self.find( "cont_arquivo_clifor_txt", matching=0.97, waiting_time=10000):
            not_found("cont_arquivo_clifor_txt")
        self.click()
        self.wait(1000)
        if not self.find( "cont_botao_abrir_clifor_txt", matching=0.97, waiting_time=10000):
            not_found("cont_botao_abrir_clifor_txt")
        self.click()
        self.wait(1000)
        self.enter()
        # aqui da um erro de uma linha com INT invalido, apenas dar enter e vai puxar igual
        
        
        if not self.find( "cont_importar_imp_exp_txt", matching=0.97, waiting_time=10000):
            not_found("cont_importar_imp_exp_txt")
        self.click()
        # IMPORTAR 
        # ERRO DE NAO EXISTE NADA PARA IMPORTAR
        self.wait(1000)
        self.enter()

        if not self.find( "cont_excluir_opc_23_imp_exp", matching=0.97, waiting_time=10000):
            not_found("cont_excluir_opc_23_imp_exp")
        self.click()
        # EXCLUIR
        # ERRO DE NAO EXISTE NADA PARA EXCLUIR
        self.wait(1000)
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

        ####################################
        # IMPORTACOES E EXPORTACOES -> EBS #
        ####################################

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





        


















    

def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()