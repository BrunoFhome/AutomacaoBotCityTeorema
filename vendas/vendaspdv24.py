from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()

"""
CÓDIGO FEITO PARA SISTEMA VENDAS PDV 24.05
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
        
        ##################################################################
                            ####---LOGIN---####
        
        self.execute(r"C:\Teorema\bin\vendas_pdv")
        self.wait(5000)
        self.tab()
        

        self.type_keys_with_interval(100,"teorema")
        self.wait(1000)
        self.tab()
        self.wait(1000)
        self.tab()
        self.type_keys_with_interval(100,"1811")
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        self.enter() 
        
##################################################################

####---Cadastro Terminal---####
        
        #self.type_keys_with_interval(1,"qa12!@")
        #self.tab()
        #self.type_up()
        #self.type_down()
        #self.type_up()
        #self.tab()
        #x = 0
        #y = 0
        #while x < 11 
        #    self.type_up()
        #    self.type_down()
        #    self.type_up()
        #    self.tab()
        #    x += 1 

        #while y < 6 
        #    self.type_down()
        #    y += 1
        #y = 0   
        #while y < 6 
        #    self.type_up()
        #    y += 1
        # 
        #x = 0
        #self.tab()
        #while x < 6 
        #    self.type_up()
        #    self.type_down()
        #    self.type_up()
        #    self.tab()
        #    x += 1
        
        #y = 0
        #while y < 5 
        #    self.type_down()
        #    y += 1
        #y = 0   
        #while y < 5 
        #    self.type_up()
        #    y += 1
        #y = 0
        #self.tab()
        #self.type_up()
        #self.type_down()
        #self.type_up()
        #self.tab()
        #while y < 6 
        #    self.type_down()
        #    y += 1
        #y = 0   
        #while y < 6 
        #    self.type_up()
        #    y += 1
        #y = 0
        #self.tab()
        #self.type_up()
        #self.type_down()
        #self.type_down()
        #self.type_up()
        #self.type_up()
        #self.tab()
        #while y < 8 
        #    self.type_down()
        #    y += 1
        #y = 0   
        #while y < 8 
        #    self.type_up()
        #    y += 1
        #y = 0
        #self.tab()
        #while y < 4 
        #    self.type_down()
        #    y += 1
        #y = 0   
        #while y < 4 
        #    self.type_up()
        #    y += 1
        #y = 0
        #
        #self.tab()       
        #self.type_down()
        #self.type_down()
        #self.type_down()
        #self.type_up()
        #self.type_up()
        #self.type_up()
        #self.find_button( "botao_cadastro_salvar" ) 
        #    #("botao_cadastro_salvar")
        #self.click()

        #########################################################
        ############## PRIMEIRO ABRIR O CAIXA ###################
        #########################################################

        #self.find_button( "caixa_comeco_menu_princi")      
        #self.click()

        self.find_button( "23_caixa_abrir_menu" )
            #("23_caixa_abrir_menu")
        self.click()
        

        self.find_button("abrir_caixa_comecar_aut_1")
        #teste de abrir o caixa
        #mexer aqui amanhã 04/07 ATUALIZAR ZIP NO MAESTRO
        
        #self.find_button( "abrir_caixa_comecar_aut_1" ) 
        #    #("abrir_caixa_comecar_aut_1")
        self.click()

        self.wait(1000)
        self.type_keys_with_interval(10,'100')
        self.find_button( "confirmar_abrir_caixa_menu")    
        self.click()
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        
        

        self.find_button( "23_retornar_caixa_abrir" )
            #("23_retornar_caixa_abrir")
        self.click()
        
        self.wait(2000)
        

        
#################################################################################
#####################--------VENDAS--------#########################
#COMEÇO DE VENDAS
        
        if not self.find( "cont_vendas_pdv_btn_vendas_2407", matching=0.97, waiting_time=10000):
            not_found("cont_vendas_pdv_btn_vendas_2407")
        self.click()

        self.wait(3000)
        
        self.key_f3()
        self.wait(3000)
        self.backspace()
        self.wait(1000)
        self.type_keys_with_interval(1,'0080124')
        self.wait(1000)
        self.enter()
        self.wait(2000)

        self.find_button( "botao_selecionar_1")
        
        self.click()

        self.wait(2000)
        self.key_f4()
        self.wait(2000)
        self.find_button( "localizar_vendedor_menu_vendas")  
        self.click()
        self.wait(2000)
        self.find_button( "selecionar_o_vendedor_menu_venda")
        self.click()

        self.wait(1000)
        # CLICAR EM CAIXAR ANTES DE ACHAR ITEM
        #self.find_button( "clicar_reduzido_vendas_item") 
        #self.click()
        #self.wait(1000)
        #self.click()
        #x = 0
        #while x < 7 :
        #    self.type_right()
        #    self.space()
        #    self.space()
        #    x += 1



        self.find_button( "botao_f2_buscar")
        
        self.click_relative(12, 35)
        self.wait(1000)

        self.type_keys_with_interval(1,"112322")
        self.enter()
        self.wait(2000)
        #apartir daq, antes de selecionar o item, adicionar mudanças
        #
        #
        self.find_button( "f2_similares_vendas_novo_1")
        
        self.click()
        self.find_button( "unid_adicionais_vendas_novo_2")
        
        self.click()
        self.find_button( "f2_cond_pagto_novo_vendas",)
        
        self.click()
        self.find_button( "tabela_precos_vendas_novo_3")
        
        self.click()
        self.wait(1000)
        self.type_down()
        self.enter()
        self.wait(1000)
        self.type_down()
        self.enter()
        self.wait(1000)
        self.key_esc()
        self.find_button( "achar_calculadora_vendas_novo_4")
       
        self.click()
        self.wait(1500)
        self.find_button( "calcu_relativo_clicar_em_fechar_2")
        
        self.click_relative(282, 10)

        self.find_button( "2_lotes_vendas_item_sel")
        
        self.click()
        self.find_button( "3_foto_do_item_vendas_")
        
        self.click()
        self.find_button( "4_fornecedores_vendas_item")
        
        self.click()
        self.find_button( "5_itens_agregados_vendas_item")
        self.click()
        
        #AQUI ESTA A GRADE DA PARTE DO F2, EM VENDAS

        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        

        self.find_button( "botao_imprimir_grade_analise")
            
        self.click()
        self.find_button( "cancelar_impressao_grade")
            
        self.click()
        
        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        
        self.find_button( "armazenar_e_recuperar_grade")
            
        self.click()
        
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.space()
        self.wait(3000)

        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        
        self.find_button( "armazenar_e_recuperar_grade")
            
        self.click()

        self.find_button( "achar_botao_recuperar_grade")
           
        self.click_relative(41, 25)
        
        self.find_button( "excluir_grade_default")
            
        self.click()
        
        self.find_button( "botao_retornar_grade_relativo_salvar")
            
        self.click_relative(-31, 15)
        
        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        #self.find_button( "botao_grade_exportar_para_excel")
        self.find_button( "23_exportar_para_excel_venda" )
            #("23_exportar_para_excel_venda")
        self.click()
        self.wait(2000)

        self.key_esc()

        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        self.find_button( "botao_grade_exportar_para_html")  
        self.click()
        
        self.wait(2000)
        self.key_esc()

        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        
        self.find_button( "botao_grade_exportar_para_texto")
        self.click()
        self.wait(2000)
        self.key_esc()
        
        self.find_button( "grade_botao_vendas_item_1")
            
        self.click()
        
        self.find_button( "botao_grade_exportar_para_xml")
            
        self.click()
        
        self.wait(2000)
        self.key_esc()
        
        self.find_button( "botao_selecionar_item")
            
        self.click()
        self.wait(1000)
        
        if not self.find( "vendas_confirmar_botao_item", matching=0.97, waiting_time=10000):
            not_found("vendas_confirmar_botao_item")
        self.click()
        self.wait(3000)
        self.key_esc()
        self.wait(2000)





        self.find_button( "botao_f9_finaliza")
            
        self.click()
        #self.find_button( "Finalizar_como_venda")
        self.find_button( "23_finalizar_como_venda" )
            #("23_finalizar_como_venda")
        self.click()



        self.click()
        
        self.find_button( "1_venda_loja_botao")
            
        self.click_relative(121, 10)
        self.click()

        x = 0
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        
        self.wait(2000)
        #self.find_button( "clicar_observacoes_buscar")   
        #self.click_relative(86, 8)
        self.find_button( "23_botao_buscar_observacoes" )
            #("23_botao_buscar_observacoes")
        self.click()

        if not self.find( "vendas_pdv_btn_localizar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_localizar_opc_2407")
        self.click()

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        self.find_button( "23_botao_finalizar_f9" )
            #("23_botao_finalizar_f9")
        #mouse parando em cima
        self.wait(2000)
        self.click()
        


        self.find_button( "botao_dinheiro")
        
        self.click()
        self.type_down()
        self.type_up()
        self.find_button( "botao_pix")
            
        self.click()
        self.tab()
        self.backspace()
        self.type_down()
        self.enter()
        self.backspace()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"06891561035")
        self.tab()
        self.find_button( "botao_cheque")
            
        self.click()
        self.find_button( "botao_abrir_bancos")
            
        self.click_relative(-24, 28)
        self.type_down()
        self.enter()
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
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "botao_c_credito")
            
        self.click()
        
        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.find_button("botao_c_debito")
        
        self.click()
        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.find_button( "botao_outros_pagamentos")
            
        self.click()
        self.type_down()
        self.type_up()
        self.tab()
        self.tab()
        self.find_button( "botao_todos_pagamentos")
            
        self.click()
        x = 0
        while x < 15 :
            self.type_down()
            x += 1
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.tab()
        self.enter()
        #self.find_button( "botao_sair_finalizar_orcamento_2" ) 
        #    #("botao_sair_finalizar_orcamento_2")
        #self.click()


        self.find_button( "Botao_nota_fiscal_pagamento")
        
        self.click()
        self.wait(2000)

        self.type_keys_with_interval(1,"1")
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.wait(1000)

        x = 0
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 8 :
            self.type_up()
            x += 1
        x = 0
        self.tab()
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 8 :
            self.type_up()
            x += 1
        x = 0
        self.tab()
        while x < 5 :
            self.type_down()
            x += 1
        x = 0
        while x < 5 :
            self.type_up()
            x += 1
        x = 0
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"12:30")
        self.wait(1000)
        
        self.wait(3000)

        self.find_button( "botao_cliente_fornecedor_nf")  
        self.click_relative(65, 28)
    
        self.wait(2000)

        self.find_button( "botao_localizar_2")
        self.click()
      
        self.wait(2000)

        self.find_button( "botao_selecionar_nfs")
            
        self.click()
        
        
        #self.find_button( "botao_codigo_de_operação")
            
        #self.click_relative(64, 27)
        
        #self.find_button( "botao_localizar_2")
            
        #self.click()
        
        #self.find_button( "botao_selecionar_4")
            
        #self.click()
        self.wait(2000)
        self.find_button( "botao_classificacao_nfs_1")
        self.click_relative(65, 26)
        self.wait(2000)

        self.find_button( "botao_localizar_nfs_1")
        self.click()
        self.wait(2000)
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        
        self.find_button( "botao_transportador(a)_nfs")
        self.click_relative(63, 27)
        
        self.wait(2000)
        
        self.find_button( "botao_localizar_nfs_2")
        self.click()
        self.wait(2000)
        
        self.find_button( "botao_selecionar_nfs_2")
        self.click()
        self.wait(2000)
        
        self.find_button( "botao_local_entrega_nfs")
        self.click_relative(63, 25)
        self.wait(2000)
        
        self.find_button( "botao_localizar_local_entrega")     
        self.click()
        self.wait(2000)
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        
        self.find_button( "ler_codigo_ficcal_cfop")
        self.click_relative(68, 28)
        self.wait(2000)

        #self.backspace()
        self.type_keys_with_interval(1,"5.102")
        self.wait(2000)

        self.find_button( "botao_localizar_codigos_fiscais_1")    
        self.click()
        
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        
        self.find_button( "achar_placa1")
            
        self.click_relative(11, 26)
        
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 25 :
            self.type_down()
            x += 1
        x = 0
        while x <25 :
            self.type_up()
            x += 1
        x = 0
        self.type_down()
        self.tab()
        while x < 6 :
            self.type_down()
            x += 1
        x = 0
        while x <6 :
            self.type_up()
            x += 1
        x = 0
        
        self.find_button( "achar_observações_e_volumes")
            
        self.click_relative(435, 31)
        
        self.find_button( "botao_localizar_observações_1")
            
        self.click()
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        
        self.tab()
        self.space()
        self.space()
        self.tab()

        while x < 6 :
            self.type_keys_with_interval(1,"123")
            self.tab()
            x += 1
        x = 0        
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x <4 :
            self.type_up()
            x += 1
        x = 0
        
        self.tab()
        
        while x < 6 :
            self.type_down()
            x += 1
        x = 0
        while x <6 :
            self.type_up()
            x += 1
        x = 0

        self.tab()
        #### OPÇÃO ESTA INVALIDA PARA PREENCHER
        
        #while x < 3 
        #    self.type_keys_with_interval(1,"0")
        #    self.tab()
        #    x += 1
        
        #adicionar outros botoes aqui, opção
        self.wait(1000)
        self.find_button( "2_itens_final_nota_fiscal_2")
            
        self.click()
        self.wait(1000)
        self.find_button( "engrenagem_2_itens_bot")
        
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        

        self.enter()
        self.find_button( "3_servicos_final_nota_fiscal")
            
        self.click()
        self.find_button( "4_adicionais_cliente_forn_trans_nota")
            
        self.click()
        self.wait(500)
        self.type_keys_with_interval(1,"qa12!@")
        self.wait(1000)
   
        self.find_button( "botao_notas_referenciadas")
        
        self.click()
        self.wait(1000)
        
        self.find_button( "botao_incluir_notas_referenciadas")
            
        self.click()
        self.wait(1000)
        
        self.find_button( "botao_notas_referenciadas_opcoes")
            
        self.click()
        self.click()
            
        while x < 6 :
            self.type_down()
            x += 1
        x = 0
        while x <6 :
            self.type_up()
            x += 1
        x = 0
        
        self.wait(2000)

        self.find_button( "botao_adicionar_notas_referenciadas_2")
        self.click()
        self.wait(2000)
        self.find_button( "achar_chave_nfe")
        self.click_relative(92, 4)
        self.wait(1000)
        self.type_keys_with_interval(1,"11111111111111111111111111111111111111111111")
        self.wait(2000)

        ###
        if not self.find( "vendas_pdv_btn_gravar_nf_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_gravar_nf_2407")
        self.click()
        self.wait(2000)
        

        self.find_button( "botao_finalizar_nota_3")
        #testar aq, dando erro ao finalizar nota
        
        self.click()      
        self.wait(1000)
    
        

        self.find_button( "selecao_modo_nfe_rel_norm")
            
        self.click_relative(8, 24)
        self.wait(500)
        self.type_right()
        self.type_right()
        self.wait(1000)

        self.find_button( "imprimir_vs_nota_fiscal_item_fin")
            
        self.click()
        self.wait(2000)

        self.find_button( "x_verm_fecha_imp_nota")
        
        self.click()
        self.wait(1000)

        self.find_button( "espelho_da_nf_imp_nota")
        self.click()
        self.wait(5000)
        #
        self.find_button( "23_x_vermelho_fechar_nota" )
            #("23_x_vermelho_fechar_nota")
        self.click()
        

        self.wait(1000)
        self.find_button( "fin_fim_nota_eletronica_venda")   
        self.click()
        self.wait(30000)
        self.enter()

       
        self.find_button( "calculadora_final_vendas_1")  
        self.click()
        self.wait(1000)
        self.find_button( "achar_calculadora_finalizar_vend_2")
        self.click_relative(278, 7)
        self.wait(1000)
        #
        
        self.wait(3000)

        if not self.find( "vendas_pdv_btn_entregar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_entregar_opc_2407")
        self.click()
        
        self.wait(1000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.wait(2000)

        if not self.find( "vendas_pdv_data_botao_rel", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_data_botao_rel")
        self.click_relative(28, 10)
        self.find_button( "carregar_ano_data_entrga")
        
        self.click()
        self.find_button( "escolher_atual_data_entrega")
            
        self.click()
        self.wait(2000)
        if not self.find( "vendas_pdv_cliente_buscar_movimentos", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_cliente_buscar_movimentos")
        self.click()
        self.wait(4000)
        self.type_keys_with_interval(1,'0000001')
        self.wait(2000)
        if not self.find( "vendas_pdv_localizar_opc_09", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_localizar_opc_09")
        self.click()
        self.wait(2000)
        self.find_button( "selecionar_cliente_entrega_botao")
           
        self.click()
        self.wait(2000)

        if not self.find( "vendas_pdv_btn_retorno_consulta", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_retorno_consulta")
        self.click()
        self.wait(2000)
        self.wait(2000)

        if not self.find( "vendas_pdv_btn_retorno_consulta", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_retorno_consulta")
        self.click()
        self.wait(2000)
        
        
        #
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_recomecar_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_recomecar_24_07")
        self
        self.click()
        
        self.wait(3000)
        self.enter()
        
        #FIM DE PRIMEIRA VENDA


        self.find_button( "botao_f2_buscar")
            
        self.click_relative(12, 35)
        self.wait(3000)
        self.enter()
        self.wait(3000)

        self.type_keys_with_interval(1,"114801")
        self.enter()
        self.find_button( "botao_selecionar_item")
            
        self.click()
        self.wait(3000)
        
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"0")
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"12345678")
        self.tab()
        self.tab()
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(3000)


        ###OUTRA FORMA DE FINALIZAR### ORÇAMENTO
        self.find_button( "botao_f9_finaliza")
            
        self.click()
        
        #
        self.find_button( "23_finalizar_orcamento" )
            #("23_finalizar_orcamento")
        self.click() 
        
        self.wait(2000)
        self.key_f3()
        self.wait(3000)
      
        
        self.find_button( "botao_de_localizar_orcamento")
        self.click()
        
        self.find_button( "botao_de_selecionar_orcamento")
        self.click()

        self.wait(3000)

        
        self.find_button( "botao_f9_finaliza")
            
        self.click()
        self.find_button( "botao_dinheiro")
            
        self.click()
        self.type_down()
        self.type_up()
        self.find_button( "botao_pix")
            
        self.click()
        self.tab()
        self.backspace()
        self.type_down()
        self.enter()
        self.backspace()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"06891561035")
        self.tab()
        self.find_button( "botao_cheque")
            
        self.click()
        self.find_button( "botao_abrir_bancos")
            
        self.click_relative(-24, 28)
        self.type_down()
        self.enter()
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
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "botao_c_credito")
        
        self.click()
        
        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.find_button( "botao_c_debito")
           
        self.click()
        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.find_button( "botao_outros_pagamentos")
            
        self.click()
        self.type_down()
        self.type_up()
        self.tab()
        self.tab()
        self.find_button( "botao_todos_pagamentos")
            
        self.click()
        x = 0
        while x < 15 :
            self.type_down()
            x += 1
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.tab()
        self.enter()
        

        self.find_button( "botao_para_sair_orcamento")
            
        self.click()
        
        self.find_button( "botao_retornar_finalizar_orcamento")
            
        self.click()
        #
        
        self.wait(3000)

        if not self.find( "vendas_pdv_btn_recomecar_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_recomecar_24_07")
        self.click()
        self.wait(1000)
        self.enter()
        
        ###TERCEIRO TIPO DE FINALIZAÇÃO
        
        self.wait(3000)
        self.key_f3()
        
      
        
        self.find_button( "botao_de_localizar_orcamento")
            
        self.click()
        
        self.find_button( "botao_de_selecionar_orcamento")
            
        self.click()
        
        ###BUSCANDO ITEM COM O F2

        self.find_button( "achar_botao_de_busca_f2")
            
        self.click()
        
        self.wait(1000)
        self.type_keys_with_interval(1,"112322")
        self.enter()
        self.find_button( "botao_selecionar_item")
            
        self.click()
        self.wait(2000)
        
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"12345678")
        self.tab()
        self.tab()
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(2000)

        ###FINALIZAR     COMO CONDICIONAL 
        self.find_button( "botao_f9_finaliza")

        self.click()
        #
        self.find_button( "23_finalizar_condicional" )
            #("23_finalizar_condicional")
        self.click()
        self.wait(2000)

        self.key_f3()
        self.wait(1000)

        self.find_button( "botao_localizar_vendas")
            
        self.click()
        self.wait(1000)
        
        self.find_button( "selecionar_botao_vendas")
        self.wait(1000)
        self.click()
        
        self.tab()
        self.tab()
        self.tab()

        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        x = 0
        while x < 6 :
            self.type_up()
            x += 1
        x = 0
        self.tab()
        #BOTAO OBSEVAÇÕES NAO ESTA ABRINDO NENHUMA JANELA
        self.find_button( "23_botao_buscar_observacoes" )
            #("23_botao_buscar_observacoes")
        self.click()

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.key_f4()
        self.wait(3000)
        #mouse parando em cima
        if not self.find( "vendas_pdv_btn_localizar", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_localizar")
        self.click()
        self.wait(1000)
        
        self.find_button( "selecionar_botao_vendas")
        self.click()
        self.wait(1000)
        
        
        self.find_button( "botao_f9_finaliza")
            
        self.click()
        self.wait(2000)
        
       

        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        x = 0
        self.type_down()
        self.type_down()

        self.tab()
        self.enter()

        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        x = 0
        self.type_down()

        self.tab()
        self.enter()

        self.type_down()
        self.type_down()
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)     
        self.enter()
######################### AQUI ESTA O TAMANHO DA FOLHA  ##################


        self.find_button( "tamanho_folha_achar_A_relativo" )

        self.click_relative(-55, -2)
        self.wait(1000)
        self.click()
        x = 0
        while x < 11 :
            self.type_down()
            x += 1
        x = 0
        while x < 11 :
            self.type_up()
            x += 1
        x = 0

        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        self.enter()
        self.wait(1000)
        self.tab()
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        x = 0

        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_keys_with_interval(1,"1")
        self.tab()
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1
        x = 0
        self.tab()
        self.type_keys_with_interval(1,"2")
        self.tab()
        self.space()
        self.space()
        self.type_down()
        self.space()
        self.space()
        self.tab()
        self.enter()

        #self.find_button( "botao_fechar_para_finalizar")    
        #self.click()
        self.wait(2000)
        self.key_esc()
        
        # self.wait(2000)
        #self.key_esc()
        self.wait(2000)
        self.key_esc()
        self.wait(2000)
        self.enter()
        self.wait(5000)
        #self.key_esc()
         #self.enter()

        if not self.find( "vendas_achar_f8_simulacao", matching=0.97, waiting_time=10000):
            not_found("vendas_achar_f8_simulacao")
        # aqui é apenas para o mouse sair de cima do botao de vendas
        
        self.wait(3000)

        if not self.find( "vendas_pdv_btn_vendas_mais_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_vendas_mais_opc_2407")
        self.click()
        self.wait(4000)
        
        # mouse ja para em cima, apenas clicar
        
        
        self.find_button( "botao_1filtros_vendas")
            
        self.click()
        
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 6 :
            self.type_right()
            x += 1
        x = 0

        self.tab()
        while x < 6 :
            self.type_right()
            x += 1
        x = 0
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        
        self.find_button( "selecionar_data_em_vendas")
            
        self.click_relative(33, 11)
        
        self.find_button( "carregar_ano_data")
            
        self.click()
        
        self.find_button( "data_atual_botao")
            
        self.click()
        
        self.find_button( "achar_botao_cliente_vendas")
            
        self.click_relative(62, 26)
        
        self.wait(1000)
        
        self.find_button( "botao_localizar_2")
            
        self.click()
        

        self.find_button( "botao_para_selecionar_emvendas")
            
        self.click()
        
        
        self.find_button( "achar_botao_vendendor")
            
        self.click_relative(64, 28)
        
        self.find_button( "botao_localizar_2")
            
        self.click()
        #####
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "condicao_de_pagamento_botao")
            
        self.click_relative(63, 28)

        
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        
        
        self.find_button( "botao_item_achar_vendas")
           
        self.click_relative(63, 25)
        
        self.find_button( "botao_localizar_2")
            
        self.click()
        
       
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        
        self.tab()
        self.tab()
        self.space()
        self.space()
        
        ###
        self.find_button( "23_2_consulta_vendas" )
            #("23_2_consulta_vendas")
        self.click()
        
        
        ####
        
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_documentos_24_07", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_documentos_24_07")
        self.click()
        
        
        #VENDAS -> DOCUMENTOS
        self.wait(1000)
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1
        self.tab()
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1
        self.tab()
        self.space()
        self.space()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
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
        self.space()
        self.space()
######################## AQUI ESTA O ERRO COM MARGEM DO DOCUMENTO ###########################
        self.find_button( "botao_matricial_documentos")
            
        self.click()
        
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.type_down()
        self.type_down()
        self.tab()
        self.enter()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.type_down()
        self.tab()
        self.enter()

        self.type_down()
        self.enter()
        self.enter()
        self.wait(1000)
        self.enter()
        

        
        self.find_button( "achar_configurar_impressao_tamanho_folha")
            
        self.click_relative(234, 205)
        

        x = 0
        while x < 10 :
            self.type_down()
            x += 1
        x = 0
        while x < 10 :
            self.type_up()
            x += 1
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        self.enter()
        self.tab()
        x = 0
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1

        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_keys_with_interval(1,"1")
        self.tab()

        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1

        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.enter()
        self.enter()
        self.type_down()
        self.enter()
        self.enter()
        self.tab()
        self.enter()

        #self.find_button( "botao_fechar_impressao_documento")   
        #self.click()
        self.wait(2000)
        self.key_esc()

        self.wait(2000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.key_esc()

        

        
        ###
        #self.find_button( "23_sair_vendas+" )
        #    #("23_sair_vendas+")
        #self.click()
        
        
        
#######################  F7 FINANCEIRO   ######################
        

        self.find_button( "botao_f7_financeiro" )
            
        self.click()

        self.find_button( "botao_cliente_fornecedor_busca" )
            
        self.click_relative(80, 26)
        
        self.find_button( "botao_para_localizar_financeirof7" )
           
        self.click()
        
        self.find_button( "botao_selecionar_financeiros_f7" )
            
        self.click()

        self.find_button( "botao_achar_documento_financeiro" ) 
            #("botao_achar_documento_financeiro")
        self.click_relative(12, 30)
        
        self.type_keys_with_interval(1,"123")
        self.tab()
        
        self.find_button( "achar_botao_de_data_financeiro" ) 
            #("achar_botao_de_data_financeiro")
        self.click_relative(34, 12)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()
        
        self.find_button( "botao_para_datas_financeiro_relativo" ) 
            #("botao_para_datas_financeiro_relativo")
        self.click_relative(-37, 20)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()
        
        self.find_button( "achar_todas_as_empresas_financeiro" ) 
            #("achar_todas_as_empresas_financeiro")
        self.click()
        self.click()
        self.find_button( "achar_ver_titulos_baixados" ) 
            #("achar_ver_titulos_baixados")
        self.click()
        self.click()
        
        self.find_button( "botao_selecao_financeiro_f7" ) 
            #("botao_selecao_financeiro_f7")
        self.click()

        ###
        ### ALTERAR AQUI, GRUPO DE EMPRESAS
        self.find_button( "grupo_de_empresas_botao_busc_1")
            ##("grupo_de_empresas_botao_busc_1")
        self.click_relative(55, 25)
        self.find_button( "localizar_grupo_empresas_rs_f7")
            ##("localizar_grupo_empresas_rs_f7")
        self.click()
        ############
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.enter()

        self.tab()
        self.tab()
        self.tab()
        x = 0
        while x < 3 :
            self.type_right()
            x += 1
        x = 0
        self.tab()
        while x < 8 :
            self.type_right()
            x += 1
        x = 0
        self.wait(1000)
        self.find_button( "localizar_titulos_f7_tes")
            ##("localizar_titulos_f7_tes")
        self.click()
        
        self.wait(1000)
        self.find_button( "botao_para_consulta_financeiros_f7" ) 
            #("botao_para_consulta_financeiros_f7")
        self.click()
        self.wait(1000)
        self.find_button( "botao_localizarr_cliente_financeiro" ) 
            #("botao_localizarr_cliente_financeiro")
        self.click()
        self.wait(4000)
        self.type_keys_with_interval(1,'0000001')
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        self.find_button( "botao_localizarr_financeiro_clientes" ) 
            #("botao_localizarr_financeiro_clientes")
        self.click()
        self.wait(1000)
        self.type_down()
        self.wait(1000)
        if not self.find( "vendas_pdv_btn_selec_24_2", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selec_24_2")
        self.click()
        self.wait(1000)

        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()

        self.find_button( "botao_datas_financeiro_consulta" ) 
            #("botao_datas_financeiro_consulta")
        self.click_relative(32, 10)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()
        
        self.tab()

        x = 0
        while x < 5 :
            self.type_down()
            x += 1
        x = 0
        while x < 5 :
            self.type_up()
            x += 1
        x = 0

        self.find_button( "localizar_data_vencimento_financeiro" ) 
            #("localizar_data_vencimento_financeiro")
        self.click_relative(235, 30)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()
        
        self.find_button( "localizar_baixa_financeiro_data" ) 
            #("localizar_baixa_financeiro_data")
        self.click_relative(229, 25)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()

        self.tab()

        x = 0
        while x < 4 :
            self.type_right()
            x += 1
        x = 0

        self.tab()
        while x < 2 :
            self.type_right()
            x += 1
        x = 0
        ###### ^^^ AQUI PAROU EM 1_CONSULTA 
        ###########TERMINAR FINANCEIRO F7###############
        self.find_button( "consulta_2_selecao_f7financeiro" ) 
            #("consulta_2_selecao_f7financeiro")
        self.click()
        self.wait(500)
        self.click()
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,'123123123')
        self.tab()
        self.type_keys_with_interval(1,'123123123')
        self.tab()
        self.type_keys_with_interval(1,'123123123')
        self.tab()
        self.type_keys_with_interval(1,'123123123')
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123123123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.space()
        self.type_down()
        x = 0
        while x < 22 :
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.tab()
        
        x = 0
        while x < 5 :
            self.type_down()
            x += 1
        x = 0
        while x < 5 :
            self.type_up()
            x += 1
        #
        #
        #
        #
        #ERRO AQUI COM BOTOES DE LOC E SELEC
        self.find_button( "grupo_de_empresas_buscar_botao_f7" ) 
            #("grupo_de_empresas_buscar_botao_f7")
        self.click_relative(79, 22)
        #
        #
        #ERRO AQUI COM LOC E SELEC, USAR RELATIVO
        #
        #
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_localizar_grupo_empresa_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_localizar_grupo_empresa_2407")
        self.click_relative(29, 33)
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_selecionar_rel_grupo_empresas", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_rel_grupo_empresas")
        self.click_relative(96, 32)
        
        self.wait(2000)
        self.enter()
        self.wait(1000)
        self.find_button( "moeda_para_cotacao_buscar_1")
            ##("moeda_para_cotacao_buscar_1")
        self.click_relative(81, 26)
        self.wait(1000)
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_selec_moedas_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selec_moedas_2407")
        self.click_relative(96, 34)
        
        self.wait(1000)
     
        
        self.wait(500)
        self.tab()
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.tab()
        self.tab()
        x = 0
        while x < 2 :
            self.space()
            self.space()
            self.type_right()
            x += 1
        self.tab()
        self.tab()
        self.space()
        self.space()
        self.tab()
        x = 0
        while x < 9 :
            self.type_right()
            x += 1
        
        self.tab()
        x = 0
        while x < 6 :
            self.type_right()
            x += 1
        
        self.tab()
        x = 0
        while x < 2 :
            self.type_right()
            x += 1
        self.tab()
        x = 0
        while x < 2 :
            self.type_right()
            x += 1
        self.find_button( "entrar_em_filtro_f7_fin" ) 
            #("entrar_em_filtro_f7_fin")
        self.click()
        self.find_button( "pre_inicial_filtro_f7" ) 
            #("pre_inicial_filtro_f7")
        self.click_relative(375, 4)
        self.find_button( "nome_relativo_filtro_f7_1" ) 
            #("nome_relativo_filtro_f7_1")
        self.click_relative(22, 23)
        
        self.find_button( "pre_final_filtro_f7" ) 
            #("pre_final_filtro_f7")
        self.click_relative(368, 6)
        self.find_button( "nome_filtro_final_rel_2" ) 
            #("nome_filtro_final_rel_2")
        self.click_relative(25, 24)
        self.find_button( "passar_filtro_direita_1" ) 
            #("passar_filtro_direita_1")
        self.click()
        self.find_button( "passar_filtro_esquerda_f7_2" ) 
            #("passar_filtro_esquerda_f7_2")
        self.click_relative(12, -13)
        

        ### AQUI COMECEI O FILTRO EM F7, POR ENQUANTO IREI RETORNAR E DEPOIS CONTINUO
        
        self.find_button( "vende_compradores_f7_filtro" ) 
            #("vende_compradores_f7_filtro")
        self.click()
        self.find_button( "inicial_filtro_f7_vend" ) 
            #("inicial_filtro_f7_vend")
        self.click_relative(376, 6)
        self.find_button( "achar_nome_relativo_filtro_f7_in" ) 
            #("achar_nome_relativo_filtro_f7_in")
        self.click_relative(18, 21)
        self.find_button( "final_relat_filtro_f7_2" ) 
            #("final_relat_filtro_f7_2")
        self.click_relative(369, 6)
        self.find_button( "achar_nome_rel_f7_filtro_fin" ) 
            #("achar_nome_rel_f7_filtro_fin")
        self.click_relative(20, 21)
        self.tab()
        self.type_down()
        self.type_down()
 
        self.find_button( "codigos_de_operacao_filtro_f7" ) 
            #("codigos_de_operacao_filtro_f7")
        self.click()
        self.find_button( "tipo_f7_codigos_op_filtro" ) 
            #("tipo_f7_codigos_op_filtro")
        self.click_relative(7, 31)
    
        x = 0
        while x < 4 :
            self.type_down()
            x += 1

        self.tab()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1

        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        self.wait(1000)
        self.find_button( "condicao_de_pagamento_filtro_f7" ) 
            #("condicao_de_pagamento_filtro_f7")
        self.click()
        self.wait(1000)
        self.find_button( "centro_de_custo_f7_filtro_bot" ) 
            #("centro_de_custo_f7_filtro_bot")
        self.click()
        self.wait(1000)
        self.find_button( "classificacao_f7_botao_filtr" ) 
            #("classificacao_f7_botao_filtr")
        self.click()
        self.wait(1000)
        self.find_button( "verificar_class_relativo_f7" ) 
            #("verificar_class_relativo_f7")
        self.click_relative(9, 48)
        self.type_down()
        self.type_down()
        self.find_button( "plano_finance_f7_filtro" ) 
            #("plano_finance_f7_filtro")
        self.click()
        self.find_button( "tipo_filtragem_f7_filtro_rel" ) 
            #("tipo_filtragem_f7_filtro_rel")
        self.click_relative(9, 48)
        self.type_down()
        self.type_down()
        self.find_button( "empresas_filtro_f7_botao" ) 
            #("empresas_filtro_f7_botao")
        self.click()
        self.find_button( "tipo_pagamento_f7_filtross" ) 
            #("tipo_pagamento_f7_filtross")
        self.click()
        self.wait(1000)
        self.click()
        self.find_button( "achar_segmentos_filtro_f7_f" ) 
            #("achar_segmentos_filtro_f7_f")
        self.click()
        self.find_button( "botao_adicionar_filtragem_filtro_1_2" ) 
            #("botao_adicionar_filtragem_filtro_1_2")
        self.click()
        
        self.find_button( "seleciona_cnpj_filtro_f7" ) 
            #("seleciona_cnpj_filtro_f7")
        self.click_relative(23, 24)
        self.find_button( "consulta_relativo_selecionar_filtro_f7" ) 
            #("consulta_relativo_selecionar_filtro_f7")
        self.click_relative(183, 39)
        self.find_button( "apagar_filtragem_f7_lixeira" ) 
            #("apagar_filtragem_f7_lixeira")
        self.click()
        self.wait(2000)
        self.wait(1000)
        self.key_esc()
        
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.key_esc()
        self.wait(1000)  

        ##############################################################
        ##############################################################
        ########################   F8 SIMULAÇÃO ######################
        ##############################################################
        ##############################################################
        

        self.wait(3000)
        if not self.find( "vendas_pdv_f8_simulacao_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_f8_simulacao_2407")
        self.click()
        
        self.tab()
        self.type_right()
        self.type_right()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")

        self.find_button( "achar_botao_itens_simulacao") 
            #("achar_botao_itens_simulacao")
        self.click()
        
        
        self.tab()
        self.tab()
        self.type_right()
        
        self.find_button( "botao_buscar_simulacao_item" ) 
            #("botao_buscar_simulacao_item")
        self.click()
        
        self.find_button( "botao_simulacao_localizar" ) 
            #("botao_simulacao_localizar")
        self.click()
        #####
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "botao_retornar_simulacao_itens" ) 
            #("botao_retornar_simulacao_itens")
        self.click()


############# F10 SALVA  #############

        self.find_button( "botao_f10_salva" ) 
            #("botao_f10_salva")
        self.click()
        
        self.find_button( "botao_localizar_f10_salva" ) 
            #("botao_localizar_f10_salva")
        self.click()
        
        self.type_keys_with_interval(1,"teste")
        self.wait(1000)

        self.find_button( "botao_salvar_f10_salva" ) 
            #("botao_salvar_f10_salva")
        self.click()
        
        self.enter()
        self.wait(1000)
        self.enter()

        
#########  F11 RECUPERAR VENDAS  ###########
        self.wait(3000)
        if not self.find( "vendas_pdv_f11_recup_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_f11_recup_2407")
        self.click()
        
        
        self.find_button( "23_recuperar_vendas_2" )
            #("23_recuperar_vendas_2")
        self.click()
        
        self.wait(2000)
        self.enter()

        self.type_keys_with_interval(1,"123")
        self.tab()
        
        self.find_button( "botao_buscar_f11_clientes" ) 
            #("botao_buscar_f11_clientes")
        self.click()
        
        self.find_button( "botao_localizar_f11_clientes" ) 
            #("botao_localizar_f11_clientes")
        self.click()
        
        self.find_button( "botao_selecionar_f11_clientes" ) 
            #("botao_selecionar_f11_clientes")
        self.click()
        
        self.find_button( "data_f11_recup" ) 
            #("data_f11_recup")
        self.click_relative(33, 11)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()

        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.space()
        self.space()
        self.type_left()
        self.type_left()
        self.type_left()
        self.type_left()
        self.space()
        self.space()

        self.find_button( "botao_localizarr_recup_vendas_f11" ) 
            #("botao_localizarr_recup_vendas_f11")
        self.click()
        self.wait(1000)
        self.enter()

        self.find_button( "retornar_de_f11_recup" ) 
            #("retornar_de_f11_recup")
        self.click()


##### CALCULADORA ABRIR E FECHAR #####

        self.find_button( "botao_calculadora_vendas" ) 
            #("botao_calculadora_vendas")
        self.click()
        self.wait(1000)
        self.find_button( "x_para_fechar_calculadoraa" ) 
            #("x_para_fechar_calculadoraa")
        self.click_relative(279, 8)
        
####################################################################
############## SAINDO DE VENDAS, INDO PARA O.S. ####################
        self.wait(3000)

        self.find_button( "retornar_de_vendas_4" ) 
            #("retornar_de_vendas_4")
        self.click()
        self.wait(1000)
        
        self.wait(3000)
        self.find_button( "botao_ir_para_o.s" ) 
            #("botao_ir_para_o.s")
        self.click()
        
        self.wait(1000)
        self.enter()
        self.tab()
        self.space()
        x = 0
        while x < 8 :
            self.type_down()
            self.space()
            x += 1
        x = 0
        self.space()
        while x < 8 :
            self.type_up()
            self.space()
            x += 1
        self.tab()
        self.find_button( "botao_achar_data_em_os" ) 
            #("botao_achar_data_em_os")
        self.click_relative(29, 7)
        
        self.find_button( "botao_carregar_ano_data_financeiro" ) 
            #("botao_carregar_ano_data_financeiro")
        self.click()
        
        self.find_button( "clicar_botao_ano_atual_data" ) 
            #("clicar_botao_ano_atual_data")
        self.click()

        self.tab()
        x = 0 
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x <4 :
            self.type_up()
            x += 1
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        self.type_right()
        self.type_right()
        # POR ENQUANTO DANDO ERRO DE AUTOMAÇÃO AO ACHAR ITEM, VOLTAR EM BREVE
        
        self.find_button( "botao_buscar_cliente_em_os" ) 
            #("botao_buscar_cliente_em_os")
        self.click()
        self.wait(1000)
        
        self.find_button( "relativo_localizar_clientes_os" ) 
            #("relativo_localizar_clientes_os")
        self.click_relative(-49, 15)


        self.find_button( "achar_grade_relativo_selecionar" ) 
            #("achar_grade_relativo_selecionar")
        self.click_relative(-209, 13)
        
        self.wait(1000)

        self.tab()
        
        x = 0
        while x < 5 :
            self.type_down()
            self.space()
            x += 1
        x = 0
        self.space()
        while x < 5 :
            self.type_up()
            self.space()
            x += 1

        self.find_button( "achar_2selecao_os_clientes" ) 
            #("achar_2selecao_os_clientes")
        self.click()
        self.wait(2000)
        self.find_button( "botao_condicaodepagamento_loc" ) 
            #("botao_condicaodepagamento_loc")
        self.click_relative(65, 29)
        self.wait(2000)
        self.find_button( "loc_condicao_pagamento_os" ) 
            #("loc_condicao_pagamento_os")
        self.click()
        self.wait(2000)
        #####
        #####
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "achar_servico_buscar_botao" ) 
            #("achar_servico_buscar_botao")
        self.click_relative(63, 29)
        self.wait(2000)
        self.find_button( "loc_condicao_pagamento_os" ) 
            #("loc_condicao_pagamento_os")
        self.click()
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.find_button( "item_relativo_botao_buscar" ) 
            #("item_relativo_botao_buscar")
        self.click_relative(63, 24)
        self.wait(2000)
        self.find_button( "loc_condicao_pagamento_os" ) 
            #("loc_condicao_pagamento_os")
        self.click()
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "tipo_da_os_botao_buscar" ) 
            #("tipo_da_os_botao_buscar")
        self.click_relative(391, 28)
        
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()

        x = 0
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 8 :
            self.type_up()
            x += 1

        self.tab()
        self.space()
        self.space()

        self.find_button( "botao_loc_ordens_de_servico" ) 
            #("botao_loc_ordens_de_servico")
        self.click()
        
        self.enter()
        self.find_button( "filtro_ordem_de_servico_botao" ) 
            #("filtro_ordem_de_servico_botao")
        self.click()
        self.find_button( "relativo_filtro_inicial" ) 
            #("relativo_filtro_inicial")
        self.click_relative(374, 32)

        self.find_button( "nome_relativo_para_filtro_inicial" ) 
            #("nome_relativo_para_filtro_inicial")
        self.click_relative(20, 23)
        
        
        self.find_button( "achar_final_pre_filtragem" ) 
            #("achar_final_pre_filtragem")
        self.click_relative(373, 6)
        self.find_button( "nome_relativo_filtro_final_2" ) 
            #("nome_relativo_filtro_final_2")
        self.click_relative(13, 22)
        
        
        
        self.wait(2000)
        self.find_button( "filtrar_todos_com_segmento_botao" ) 
            #("filtrar_todos_com_segmento_botao")
        self.click_relative(227, 32)
        
        if not self.find( "vendas_pdv_filtragem_cnpj_dupli_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_filtragem_cnpj_dupli_2407")
        self.click()
        
        
        self.find_button( "situacao_botao_segmento" ) 
            #("situacao_botao_segmento")
        self.click_relative(199, 8)
        self.click()

        x = 0
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        
        self.find_button( "+filtros_botao_clientes" ) 
            #("+filtros_botao_clientes")
        self.click()
        
        self.find_button( "mes_de_aniversario_filtro" ) 
            #("mes_de_aniversario_filtro")
        self.click_relative(110, 47)
        self.click() 
        
        x = 0
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 8 :
            self.type_up()
            x += 1
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()

        x = 0
        while x < 3 :
            self.type_down()
            x += 1

        self.tab()
        x = 0
        while x < 2 :
            self.type_down()
            x += 1

        self.tab()

        x = 0
        while x < 3 :
            self.type_down()
            x += 1

        self.find_button( "botao_vendedores,compradores" ) 
            #("botao_vendedores,compradores")
        self.click()
        
        self.find_button( "achar_inicial_relativo_flecha" ) 
            #("achar_inicial_relativo_flecha")
        self.click_relative(373, 5)
        self.find_button( "achar_nome_relativo_cliente" ) 
            #("achar_nome_relativo_cliente")
        self.click_relative(81, 25)
        
        self.find_button( "achar_final_relativo_flecha" ) 
            #("achar_final_relativo_flecha")
        self.click_relative(372, 7)
        
        self.find_button( "achar_nome_para_final_relativo" ) 
            #("achar_nome_para_final_relativo")
        self.click_relative(42, 23)
        
        self.find_button( "relativo_adicionar_nome" ) 
            #("relativo_adicionar_nome")
        self.click_relative(11, 31)
        self.find_button( "seleciona_relativo_filtro_clientes" ) 
            #("seleciona_relativo_filtro_clientes")
        self.click_relative(22, 26)
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "cond_pagamento_botao_filtro" ) 
            #("cond_pagamento_botao_filtro")
        self.click()
        
        #condicao
        
        self.find_button( "achar_inicial_relativo_flecha" ) 
            #("achar_inicial_relativo_flecha")
        self.click_relative(373, 5)
        self.find_button( "descricao_relativo_filtro_click" ) 
            #("descricao_relativo_filtro_click")
        self.click_relative(18, 24)
        
        
        self.find_button( "achar_final_relativo_flecha" ) 
            #("achar_final_relativo_flecha")
        self.click_relative(372, 7)
        
        self.find_button( "descricao_relativo_filtro_click" ) 
            #("descricao_relativo_filtro_click")
        self.click_relative(18, 24)
        
        self.find_button( "relativo_adicionar_nome" ) 
            #("relativo_adicionar_nome")
        self.click_relative(11, 31)
        self.find_button( "seleciona_relativo_filtro_clientes" ) 
            #("seleciona_relativo_filtro_clientes")
        self.click_relative(22, 26)
        ##
        #
        #
        #
        #

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "cond_pagamento_botao_filtro" ) 
            #("cond_pagamento_botao_filtro")
        self.click()
        
        self.find_button( "botao_limpa_filtro_filtros" ) 
            #("botao_limpa_filtro_filtros")
        self.click()
        
        self.find_button( "botao_retornar_filtragem_clientes" ) 
            #("botao_retornar_filtragem_clientes")
        self.click()
        #INCLUIR
        #INCLUINDO NOVA OS

        self.find_button( "incluir_nova_ordem_servico" ) 
            #("incluir_nova_ordem_servico")
        self.click()
        
        self.find_button( "data_liberacao_ordem_servico_nova" ) 
            #("data_liberacao_ordem_servico_nova")
        self.click_relative(17, 29)
        
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1

        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        
###########################################################################
        ### ATIVAR IDENTIFICACAO PLACA DE VEICULOS #######
        #AJEITAR, MODIFICAR OS BOTOES
        #self.find_button( "botao_placa_veiculo_inserir_1" ) 
            #("botao_placa_veiculo_inserir_1")
        #self.click_relative(-17, 13)
        
        #self.find_button( "botao_incluir_a_placa_veiculo_relat" ) 
            #("botao_incluir_a_placa_veiculo_relat")
        #self.click_relative(-65, 47)
        #self.wait(1000)
        #self.tab()
        #self.wait(1000)
        #self.enter()
        #self.wait(1000)
 
        
        
        
        self.find_button( "achar_cliente_incluir_os" ) 
            #("achar_cliente_incluir_os")
        self.click_relative(132, 46)
        
        
        self.find_button( "achar_nome_cliente_relativo_os" ) 
            #("achar_nome_cliente_relativo_os")
        self.click_relative(38, 21)
        

        #### AQUI COMEÇA A CONSULTA SOBRE O CLIENTE ####
        ################################################

        
        self.find_button( "achar_consulta_historico_cliente_os" ) 
            #("achar_consulta_historico_cliente_os")
        self.click()
        


        self.find_button( "botao_buscar_consulta_clientes_os" ) 
            #("botao_buscar_consulta_clientes_os")
        self.click()
        
        self.find_button( "botao_loc_consulta_clientes_os" ) 
            #("botao_loc_consulta_clientes_os")
        self.click()
        
        self.find_button( "botao_selec_consulta_clientes_os" ) 
            #("botao_selec_consulta_clientes_os")
        self.click()
        #eRRO AQUI, ESTA ABRINDO UMA JANELA A MAIS, O QUE IMPEDE O BOT DE CLICAR CERTO
        #
        #
        #
        
        self.find_button( "achar_observacoes_consulta_os" ) 
            #("achar_observacoes_consulta_os")
        self.click()
        
        x = 0 
        while x < 9 :
            self.type_right()
            x += 1
        x = 0
        while x < 9 :
            self.type_left()
            x += 1
        
        self.find_button( "achar_b_agrupamento_os" ) 
            #("achar_b_agrupamento_os")
        self.click()
        
        self.find_button( "2_movto_financeiro_consulta" ) 
            #("2_movto_financeiro_consulta")
        self.click()
        
        self.find_button( "achar_botao_contas_a_pagar" ) 
            #("achar_botao_contas_a_pagar")
        self.click_relative(118, 20)
        
        self.find_button( "botao_remessa_bancaria_clicar" ) 
            #("botao_remessa_bancaria_clicar")
        self.click_relative(6, 25)
        
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_right()
        self.wait(2000)
        
        #self.key_esc()
        
        self.find_button( "botao_situacao_consulta_clientes_os" ) 
            #("botao_situacao_consulta_clientes_os")
        self.click_relative(9, 24)
        
        self.find_button( "botao_situacao_consulta_clientes_os_2" ) 
            #("botao_situacao_consulta_clientes_os_2")
        self.click_relative(70, 26)
        
        self.find_button( "botao_situacao_consulta_clientes_3" ) 
            #("botao_situacao_consulta_clientes_3")
        self.click_relative(132, 25)
        
        self.find_button( "botao_titulos_consulta_clientes_1" ) 
            #("botao_titulos_consulta_clientes_1")
        self.click_relative(10, 28)
        
        self.find_button( "botao_titulos_consulta_clientes_2" ) 
            #("botao_titulos_consulta_clientes_2")
        self.click_relative(84, 26)
        
        self.find_button( "botao_titulos_consultaa_clientes_3" ) 
            #("botao_titulos_consultaa_clientes_3")
        self.click_relative(162, 28)
        
        self.find_button( "botao_titulos_consultas_clientes_4" ) 
            #("botao_titulos_consultas_clientes_4")
        self.click_relative(230, 25)
        
        self.find_button( "achar_b_cheques_consula_clientes" ) 
            #("achar_b_cheques_consula_clientes")
        self.click()
        
        self.find_button( "c_conta_corrente_botao_consulta_os" ) 
            #("c_conta_corrente_botao_consulta_os")
        self.click()
        
        self.find_button( "botao_conta_buscar_consulta_2" ) 
            #("botao_conta_buscar_consulta_2")
        self.click_relative(64, 22)
        
        self.find_button( "botao_localizar_conta_consulta_cliente" ) 
            #("botao_localizar_conta_consulta_cliente")
        self.click()
        #
        #
        #
        #

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "botao_consultar_conta_consulta_cliente_os" ) 
            #("botao_consultar_conta_consulta_cliente_os")
        self.click()
        
        self.find_button( "botao_d_estatisticas_consulta_clientes" ) 
            #("botao_d_estatisticas_consulta_clientes")
        self.click()
        
        self.find_button( "botao_contas_a_receber_consulta_os" ) 
            #("botao_contas_a_receber_consulta_os")
        self.click()

        self.click()
        self.type_right()
        self.space()
        self.space()
                
        self.find_button( "3_movto_es_e_devolucoes_botao" ) 
            #("3_movto_es_e_devolucoes_botao")
        self.click()
        
        self.find_button( "exibir_itens_e_servicos_consulta_relativo" ) 
            #("exibir_itens_e_servicos_consulta_relativo")
        self.click_relative(10, 23)
        
        self.find_button( "exibir_itens_e_servicos_consulta_nao" ) 
            #("exibir_itens_e_servicos_consulta_nao")
        self.click_relative(70, 24)
        
        self.find_button( "tipo_da_movimentacao_relativo_consulta" ) 
            #("tipo_da_movimentacao_relativo_consulta")
        self.click_relative(10, 21)
        
        self.find_button( "tipo_mov_entrada_consulta_os" ) 
            #("tipo_mov_entrada_consulta_os")
        self.click_relative(231, 23)
        
        self.find_button( "tipo_mov_saidas_consulta_os" ) 
            #("tipo_mov_saidas_consulta_os")
        self.click_relative(448, 22)
        
        self.find_button( "tipo_de_mov_devolucoes_consulta" ) 
            #("tipo_de_mov_devolucoes_consulta")
        self.click_relative(666, 25)
        
        self.find_button( "visualizar_movimentos_consulta_clientes" ) 
            #("visualizar_movimentos_consulta_clientes")
        self.click_relative(10, 23)
        
        self.find_button( "visualizar_movimento_consulta_cliente_os_2" ) 
            #("visualizar_movimento_consulta_cliente_os_2")
        self.click_relative(113, 23)
        
        self.find_button( "visualizar_movimento_consulta_cliente_todos_os" ) 
            #("visualizar_movimento_consulta_cliente_todos_os")
        self.click_relative(220, 22)
        
        self.find_button( "por_itens_consulta_clientes_os" ) 
            #("por_itens_consulta_clientes_os")
        self.click()
        
        self.find_button( "por_servicos_consulta_clientes_os" ) 
            #("por_servicos_consulta_clientes_os")
        self.click()
        
        self.find_button( "5_vendas_orctos_botao_consulta" ) 
            #("5_vendas_orctos_botao_consulta")
        self.click()
        
        self.find_button( "botao_condicionas_consulta_clientes_os" ) 
            #("botao_condicionas_consulta_clientes_os")
        self.click()
        
        self.find_button( "botao_orcamentos_consulta_os" ) 
            #("botao_orcamentos_consulta_os")
        self.click()
        
        self.find_button( "botao_transferencias_consulta_os" ) 
            #("botao_transferencias_consulta_os")
        self.click()
        
        self.find_button( "botao_devolucoes_consulta_cliente" ) 
            #("botao_devolucoes_consulta_cliente")
        self.click()
        
        self.find_button( "botao_pedidos_consulta_os" ) 
            #("botao_pedidos_consulta_os")
        self.click()


        
        self.find_button( "situacao_abertos_rel_1" ) 
            #("situacao_abertos_rel_1")
        self.click_relative(8, 21)
        self.find_button( "situacao_agliberacao_rel_2" ) 
            #("situacao_agliberacao_rel_2")
        self.click_relative(9, 34)
        self.find_button( "situacao_naolibe_rel_3" ) 
            #("situacao_naolibe_rel_3")
        self.click_relative(120, 23)
        self.find_button( "situacao_liberados_rel_4" ) 
            #("situacao_liberados_rel_4")
        self.click_relative(122, 33)
        self.find_button( "situacao_cancelado_rel_5" ) 
            #("situacao_cancelado_rel_5")
        self.click_relative(237, 21)
        self.find_button( "situacao_fechados_rel_6" ) 
            #("situacao_fechados_rel_6")
        self.click_relative(235, 34)
        self.find_button( "situacao_todos_rel_7" ) 
            #("situacao_todos_rel_7")
        self.click_relative(350, 34)
        self.find_button( "situacao_em_producao_rel_8" ) 
            #("situacao_em_producao_rel_8")
        self.click_relative(349, 34)
        self.find_button( "situacao_prodfinalizada_rel_9" ) 
            #("situacao_prodfinalizada_rel_9")
        self.click_relative(464, 24)
        
                
        self.find_button( "6_os_consulta_os" ) 
            #("6_os_consulta_os")
        self.click()
        
        self.find_button( "7_prospeccao_consulta_os" ) 
            #("7_prospeccao_consulta_os")
        self.click()
        
        self.find_button( "8_ultimos_contatos_consulta_os" ) 
            #("8_ultimos_contatos_consulta_os")
        self.click()
        
        self.find_button( "retornar_de_consulta_os_2" ) 
            #("retornar_de_consulta_os_2")
        self.click()
        
        
        #CONSULTA DE CLIENTE VEM ATE AQUI

        self.find_button( "situacao_recepcao_botao_busca" ) 
            #("situacao_recepcao_botao_busca")
        self.click_relative(112, 26)
        
        self.find_button( "botao_localizar_recepcao_os" ) 
            #("botao_localizar_recepcao_os")
        self.click()
        #
        #
        #
        #

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()

        self.find_button( "condicao_de_pagamento_buscar_os" ) 
            #("condicao_de_pagamento_buscar_os")
        self.click_relative(61, 29)
        


        self.find_button( "botao_localizar_recepcao_os" ) 
            #("botao_localizar_recepcao_os")
        self.click()

 
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        #AQUI ENTRA EM 2_ITENS, SERVIÇOS.
        #DENTRO DE O.S.

        self.find_button( "2_itens_servicos_incluir_os" ) 
            #("2_itens_servicos_incluir_os")
        self.click()
        
        self.find_button( "botao_incluir_2_itens,servicos" ) 
            #("botao_incluir_2_itens,servicos")
        self.click()
        

        self.find_button( "f2_codigo_descricao_buscar_os" ) 
            #("f2_codigo_descricao_buscar_os")
        self.click_relative(141, 22)

        self.wait(1000)
        
        self.type_keys_with_interval(1,"109941")
        
        self.wait(1000)
        self.find_button( "botao_localizar_f2_cdg" ) 
            #("botao_localizar_f2_cdg")
        self.click()
        
        self.find_button( "botao_select_f2_itens,servicos" ) 
            #("botao_select_f2_itens,servicos")
        self.click()
        
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.tab()
        self.tab()
        
             
        
        self.find_button( "comissionamento_relativo_flecha_os" ) 
            #("comissionamento_relativo_flecha_os")
        self.click_relative(190, 25)
        self.find_button( "achar_nome_relativo_comissionamento" ) 
            #("achar_nome_relativo_comissionamento")
        self.click_relative(44, 25)
        self.tab()
        self.find_button( "grupo_de_os_buscar_botao" ) 
            #("grupo_de_os_buscar_botao")
        self.click_relative(54, 27)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        #
        #
        #
        #
        #
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.enter()

        self.find_button( "centro_de_custo_busca_os" ) 
            #("centro_de_custo_busca_os")
        self.click_relative(89, 27)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.wait(1000)
        self.enter()

        self.find_button( "botao_para_gravar_ordem_servico" ) 
            #("botao_para_gravar_ordem_servico")
        self.click()
        self.wait(1000)

        
        self.enter()
        self.wait(1000)
        self.enter()
        




        #### ESTA OPÇAO É PARA EXCLUIR, DEIXAR PARA O FINAL
        self.find_button( "excluir_lixeira_item_os" ) 
            #("excluir_lixeira_item_os")
        self.click()
        
        self.enter()
        self.enter()
        self.enter()

        

        ################ SERVICO  #################
        self.wait(3000)

        self.find_button( "clicar_servico_ordem_de_servico_3" ) 
            #("clicar_servico_ordem_de_servico_3")
        self.click()

        self.find_button( "achar_f2_codigo_descricao_os_2" ) 
            #("achar_f2_codigo_descricao_os_2")
        self.click_relative(141, 22)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        #
        #
        ##
        #
        #
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.tab()
        self.tab()
        self.space()
        self.space()
        self.tab()

        x = 0
        while x < 3 :
            self.type_right()
            x += 1
        
        
        
        
        self.find_button( "unidade_clique_relativo_comissionamento_1" ) 
            #("unidade_clique_relativo_comissionamento_1")
        self.click_relative(-78, 66)
        

        
        self.find_button( "nome_comissionamento_2_itens" ) 
            #("nome_comissionamento_2_itens")
        self.click_relative(48, 24)
        
        self.find_button( "achar_unidade_clique_relativo_comissionamento_2" ) 
            #("achar_unidade_clique_relativo_comissionamento_2")
        self.click_relative(204, 67)
        
 
        
        self.find_button( "nome_relativo_comissionamento_pt2" ) 
            #("nome_relativo_comissionamento_pt2")
        self.click_relative(28, 26)
        
        self.find_button( "botao_unidade_para_achar_comissionamento_3" ) 
            #("botao_unidade_para_achar_comissionamento_3")
        self.click_relative(484, 67)
        
        
        
        
        self.find_button( "achar_nome_comissionamento_pt3" ) 
            #("achar_nome_comissionamento_pt3")
        self.click_relative(42, 23)
        
        self.find_button( "botao_buscar_municipio_fator_gerador" ) 
            #("botao_buscar_municipio_fator_gerador")
        self.click_relative(51, 29)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        self.wait(1000)
        self.enter()

        self.find_button( "centro_de_custo_buscar_botao_3" ) 
            #("centro_de_custo_buscar_botao_3")
        self.click_relative(89, 24)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        ###  NAO TEM F2 CODIGO DISPONIVEL PARA SELECIONAR, POR ENQUANTO PULAR ESTA PARTE
        ###
        ###
        self.enter()
        self.tab()
        self.tab()
        self.enter()
        self.wait(3000)
        self.enter()
        self.wait(2000)
        #self.enter()
        self.wait(2000)
        #self.find_button( "excluir_lixeira_item_os" ) 
            #("excluir_lixeira_item_os")
        #self.click()
        self.wait(2000)

        #self.enter()
        #self.enter()
        self.wait(2000)
        #self.enter()
        

#########    observacoes
        self.wait(3000)
        self.enter()
        
        if not self.find( "vendas_pdv_btn_observacoes_os", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_observacoes_os")
        self.click()
        
        
        
        self.find_button( "buscar_outros_acessorios_os" ) 
            #("buscar_outros_acessorios_os")
        self.click()
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()

        x = 0
        while x < 10 :
            self.space()
            self.space()
            self.tab()
            x+=1
        
        self.find_button( "salvar_esta_os" ) 
            #("salvar_esta_os")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        self.wait(1000)
##AQUI VOU COMECAR A PROGRAMAR A PARTE DE ORCAMENTO DENTRO DE OS-> INCLUIR. 
        
        
        self.find_button( "clicar_em_incluir_adiantamento" ) 
            #("clicar_em_incluir_adiantamento")
        self.click_relative(8, -17)
        
        self.type_keys_with_interval(1,"3012")
        self.tab()
        self.type_keys_with_interval(1,"2")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.tab()
        self.enter()
        self.wait(1000)
        self.enter()
        self.find_button( "condicao_de_pagamento_parcela_1" ) 
            #("condicao_de_pagamento_parcela_1")
        self.click_relative(60, 24)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "vendedor_parcelas_buscar" ) 
            #("vendedor_parcelas_buscar")
        self.click_relative(60, 22)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "opcao_incluir_parcelas_linhas" ) 
            #("opcao_incluir_parcelas_linhas")
        self.click()
        
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.tab()
        self.type_keys_with_interval(1,"1")
        self.find_button( "buscar_local_de_cobranca_2" ) 
            #("buscar_local_de_cobranca_2")
        self.click_relative(54, 29)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "classificacao_botao_buscar_parcelas" ) 
            #("classificacao_botao_buscar_parcelas")
        self.click_relative(52, 27)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "sacador_botao_buscar_parcelas" ) 
            #("sacador_botao_buscar_parcelas")
        self.click_relative(51, 29)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()



        if not self.find( "vendas_pdv_btn_opc_24_02_selecionar", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_opc_24_02_selecionar")
        self.click()
        self.wait(1000)
        


        
        self.find_button( "tipo_de_pagamento_buscar_parcelas" ) 
            #("tipo_de_pagamento_buscar_parcelas")
        self.click_relative(50, 30)
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "plano_financeiro_buscar_parcelas" ) 
            #("plano_financeiro_buscar_parcelas")
        self.click_relative(89, 29)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "operacao_buscar_parcelas" ) 
            #("operacao_buscar_parcelas")
        self.click_relative(53, 30)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "comissao_buscar_parcelas" ) 
            #("comissao_buscar_parcelas")
        self.click_relative(54, 28)
        
        self.find_button( "localizar_grupo_de_os_2" ) 
            #("localizar_grupo_de_os_2")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)

        self.tab()
        self.tab()
        self.tab()
        self.tab()

        self.type_keys_with_interval(1,"qa12!@")
    
        

        self.wait(2000)
        if not self.find( "vendas_pdv_btn_continuar_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_continuar_2407")
        self.click()
        
        
        self.find_button( "retornar_parcelas_os_5" ) 
            #("retornar_parcelas_os_5")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.enter()
        
#aqui comeca o codigo q estou editando, teste.
        self.find_button( "acoes_rel_engrenagem_1" ) 
            #("acoes_rel_engrenagem_1")
        self.click_relative(69, 16)
        self.find_button( "importar_ordem_servico_acoes_2" ) 
            #("importar_ordem_servico_acoes_2")
        self.click()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_down()
        self.type_up()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_down()
        self.type_up()
        self.find_button( "loc_data_rel_os_3" ) 
            #("loc_data_rel_os_3")
        self.click_relative(31, 10)
        self.find_button( "carregar_ano_30_os_1" ) 
            #("carregar_ano_30_os_1")
        self.click()
        self.find_button( "atual_data_os_loc_30_2" ) 
            #("atual_data_os_loc_30_2")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.wait(1000)

#aqui acaba o codigo q estou editando
#acontecendo erro ainda, ajeitar para que volte a automação
        self.find_button( "botao_exlucir_consulta_adiantamentos_1" ) 
            #("botao_exlucir_consulta_adiantamentos_1")
        self.click()
        self.enter()
        self.find_button( "salvar_conteudo_os_teste_2" ) 
            #("salvar_conteudo_os_teste_2")
        self.click()
        self.wait(1000)
        self.enter()

        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.enter()
        
        self.find_button( "botao_para_retornar_de_parcelas_os" ) 
            #("botao_para_retornar_de_parcelas_os")
        self.click()
        self.enter()
        

######## GRADE   #############

        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        
        self.find_button( "botao_imprimir_grade_analise" ) 
            #("botao_imprimir_grade_analise")
        self.click()
        self.find_button( "cancelar_impressao_grade" ) 
            #("cancelar_impressao_grade")
        self.click()
        
        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        
        self.find_button( "armazenar_e_recuperar_grade" ) 
            #("armazenar_e_recuperar_grade")
        self.click()
        
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.space()
        self.wait(1000)

        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        self.click()
        self.find_button( "armazenar_e_recuperar_grade" ) 
            #("armazenar_e_recuperar_grade")
        self.click()

        self.find_button( "achar_botao_recuperar_grade" ) 
            #("achar_botao_recuperar_grade")    teorema 
        self.click_relative(41, 25)
        
        self.find_button( "excluir_grade_default" ) 
            #("excluir_grade_default")
        self.click()
        
        self.find_button( "botao_retornar_grade_relativo_salvar" ) 
            #("botao_retornar_grade_relativo_salvar")
        self.click_relative(-31, 15)
        
        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        self.find_button( "botao_grade_exportar_para_excel" ) 
            #("botao_grade_exportar_para_excel")
        self.click()
        self.wait(2000)
        self.key_esc()
        #self.find_button( "cancelar_exportar_para_excel_grade" ) 
            #("cancelar_exportar_para_excel_grade")
        #self.click()
        
        self.find_button( "grade_1_abrir_botao_os_test")
            
        self.click()
        self.find_button( "botao_grade_exportar_para_html" ) 
            #("botao_grade_exportar_para_html")
        self.click()
        self.wait(2000)
        self.key_esc()
        #self.find_button( "cancelar_exportar_para_excel_grade" ) 
            #("cancelar_exportar_para_excel_grade")
        #self.click()

        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        
        self.find_button( "botao_grade_exportar_para_texto" ) 
            #("botao_grade_exportar_para_texto")
        self.click()
        self.wait(2000)
        self.key_esc()
        #self.find_button( "cancelar_exportar_para_excel_grade" ) 
            #("cancelar_exportar_para_excel_grade")
        #self.click()
        
        self.find_button( "grade_1_abrir_botao_os_test")
            ##("grade_1_abrir_botao_os_test")
        self.click()
        
        self.find_button( "botao_grade_exportar_para_xml" ) 
            #("botao_grade_exportar_para_xml")
        self.click()
        self.wait(2000)
        self.key_esc()
        #self.find_button( "cancelar_exportar_para_excel_grade" ) 
            #("cancelar_exportar_para_excel_grade")
        #self.click()

        ##########################################
        ############# AGENDA O.S. ################
        ##########################################
        
        
        self.wait(3000)

        if not self.find( "vendas_pdv_agenda_os_relativo", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_agenda_os_relativo")
        self.click_relative(94, 11)
        
        self.find_button( "achar_data_agenda_os" ) 
            #("achar_data_agenda_os")
        self.click_relative(33, 8)
        self.find_button( "carregar_ano_data_agenda_os" ) 
            #("carregar_ano_data_agenda_os")
        self.click()
        self.find_button( "data_atual_agenda_os" ) 
            #("data_atual_agenda_os")
        self.click()
        self.find_button( "botao_buscar_clientes_agenda_os" ) 
            #("botao_buscar_clientes_agenda_os")
        self.click()
        self.wait(3000)
        self.find_button( "localizar_clientes_agenda_os_botao" ) 
            #("localizar_clientes_agenda_os_botao")
        self.click()
        self.wait(2000)
        self.find_button( "selecionar_clientes_agenda_os_botao" ) 
            #("selecionar_clientes_agenda_os_botao")
        self.click()
        
        self.tab()
        self.tab()
        self.tab()

        x = 0
        while x < 4 :
            self.type_right()
            x += 1
        
        self.find_button( "botao_incluir_agenda_consulta" ) 
            #("botao_incluir_agenda_consulta")
        self.click()
        
        self.hold_shift()
        self.tab()
        self.release_shift()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1

        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()

        self.find_button( "achar_1_consulta_buscar_clientes" ) 
            #("achar_1_consulta_buscar_clientes")
        self.click_relative(69, 84)
        
        self.find_button( "localizar_clientes_agenda_os_botao" ) 
            #("localizar_clientes_agenda_os_botao")
        self.click()
        
        self.find_button( "selecionar_clientes_agenda_os_botao" ) 
            #("selecionar_clientes_agenda_os_botao")
        self.click()
        
        
        self.find_button( "executor_buscar_agendamento_consulta" ) 
            #("executor_buscar_agendamento_consulta")
        self.click_relative(64, 20)
        self.wait(1000)
        
        self.find_button( "localizar_clientes_agenda_os_botao" ) 
            #("localizar_clientes_agenda_os_botao")
        self.click()
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(1000)
        
        self.find_button( "achar_placa_veiculo_agendamento" ) 
            #("achar_placa_veiculo_agendamento")
        self.click_relative(150, 20)
        
        self.find_button( "descricao_agendamento_relativo_botao" ) 
            #("descricao_agendamento_relativo_botao")
        self.click_relative(73, 24)
        
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"123123123")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        
        #mexer aqui, deixar salvando mesmo assim
         
        self.find_button( "botao_salvar_agendamento_oss" ) 
            #("botao_salvar_agendamento_oss")
        self.click()
        
        self.find_button( "botao_retornar_de_consultas_agendamento" ) 
            #("botao_retornar_de_consultas_agendamento")
        self.click()
        self.wait(1000)
        self.click()

        #nao retornar ainda para menu
        #self.click()

        
        
        ################################################
        ################ CADASTROS #####################
        ################################################
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.wait(2000)
        self.find_button( "botao_municipios_cadastro_1" ) 
            #("botao_municipios_cadastro_1")
        self.click()
        self.find_button( "botao_para_incluir_um_municipio_cadastro" ) 
            #("botao_para_incluir_um_municipio_cadastro")
        self.click()
        
        self.find_button( "achar_descricao_cadastro_municiopio" ) 
            #("achar_descricao_cadastro_municiopio")
        self.click_relative(126, 6)
        

        x = 0
        while x < 10 :
            self.backspace()
            x += 1
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "botao_buscar_estado_cadastro_municipios" ) 
            #("botao_buscar_estado_cadastro_municipios")
        self.click_relative(78, 2)
        self.find_button( "clicar_localizar_estados_cadastro_f10" ) 
            #("clicar_localizar_estados_cadastro_f10")
        self.click()
        self.find_button( "localizar_botao_cadastro_municipios_estado" ) 
            #("localizar_botao_cadastro_municipios_estado")
        self.click()
        
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.find_button( "botao_salvar_cadastro_de_municipio" ) 
            #("botao_salvar_cadastro_de_municipio")
        self.click()
        
        self.wait(1000)
        
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_excluir_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_excluir_2407")
        self.click()
    

        self.wait(2000)
        
        self.enter()
        self.find_button( "botao_retornar_cadastro_municipio_salvo" ) 
            #("botao_retornar_cadastro_municipio_salvo")
        self.click()
        #############################################################
        ################## CADASTRO DE TERMINAIS ####################
        #############################################################
        
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "botao_terminais_cadastro_vendass" ) 
            #("botao_terminais_cadastro_vendass")
        self.click()
        self.wait(1000)

        self.find_button( "botao_incluir_terminais_vendas_2" ) 
            #("botao_incluir_terminais_vendas_2")
        self.click()
        self.wait(1000)
        self.tab()
        self.enter()
        self.wait(1000)
        
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_down()
        self.type_up()

        self.tab()
        self.tab()

        x = 0
        while x < 10 :
            self.type_up()
            self.type_down()
            self.type_up()
            self.tab()
            x += 1
        
        x = 0
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        self.tab()
        self.type_up()
        self.type_down()
        self.type_up()
        self.tab()
        self.type_up()
        self.type_down()
        self.tab()

        x = 0
        while x < 4 :
            self.type_up()
            self.type_down()
            self.type_up()
            self.tab()
            x += 1
        
        x = 0
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        self.tab()
        self.type_down()
        self.type_up()
        self.tab()
        x = 0
        while x < 6 :
            self.type_down()
            x += 1
        x = 0
        while x < 6 :
            self.type_up()
            x += 1
        self.tab()
        x = 0
        while x < 3 :
            self.type_down()
            x += 1
        x = 0
        while x < 3 :
            self.type_up()
            x += 1

        self.tab()

        x = 0
        while x < 8 :
            self.type_down()
            x += 1
        x = 0
        while x < 8 :
            self.type_up()
            x += 1

        self.tab()

        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.tab()
        x = 0
        while x < 4 :
            self.type_down()
            x += 1
        x = 0
        while x < 4 :
            self.type_up()
            x += 1
        self.find_button( "salvar_terminal_cadastrado_botao" ) 
            #("salvar_terminal_cadastrado_botao")
        self.click()
        #

        self.find_button( "23_retornar_cadastro_terminal" )
            #("23_retornar_cadastro_terminal")
        self.click()
        
        self.wait(1000)
        self.enter()
        self.wait(1000)
        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "botao_terminais_cadastro_vendass" ) 
            #("botao_terminais_cadastro_vendass")
        self.click()
        self.find_button( "botao_ultimo_cadastro_municipio" ) 
            #("botao_ultimo_cadastro_municipio")
        self.click()
        ##############
        ##############
        ##############
        ##############
        ##############
        self.find_button( "23_excluir_terminal_rel" )
            #("23_excluir_terminal_rel")
        self.click_relative(78, 15)
        self.wait(2000)
        self.click()
        
        self.wait(2000)
        self.enter()
        self.find_button( "23_retornar_cadastro_terminal" )
            #("23_retornar_cadastro_terminal")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        
        ######################################################
        ############## CADASTRO DE EQUIPAMENTOS ##############
        ######################################################

        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "botao_cadastro_de_equipamentos_abrir" ) 
            #("botao_cadastro_de_equipamentos_abrir")
        self.click()
        self.find_button( "botao_incluir_cadastro_equipamentos" ) 
            #("botao_incluir_cadastro_equipamentos")
        self.click()
        
        x = 0
        while x < 9 :
            self.type_keys_with_interval(1,"qa12!@")
            self.tab()
            x += 1
        
        self.find_button( "botao_buscar_cliente_cadastro_equipamento" ) 
            #("botao_buscar_cliente_cadastro_equipamento")
        self.click()
        self.find_button( "botao_para_localizar_cadastro_cliente_equipamento" ) 
            #("botao_para_localizar_cadastro_cliente_equipamento")
        self.click()
        self.find_button( "botao_selecionar_cadastro_equipamento_cliente" ) 
            #("botao_selecionar_cadastro_equipamento_cliente")
        self.click()
        
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "botao_para_salvar_cadastro_de_equipamentos_2" ) 
            #("botao_para_salvar_cadastro_de_equipamentos_2")
        self.click()
        self.find_button( "botao_retornar_cadastro_de_equipamentos" ) 
            #("botao_retornar_cadastro_de_equipamentos")
        self.click()

        self.type_keys_with_interval(10,"qa12")

        self.find_button( "botao_localizar_cadastro_criado_equipamentos" ) 
            #("botao_localizar_cadastro_criado_equipamentos")
        self.click()

        self.find_button( "botao_editar_cadastro_de_veiculo_criado" ) 
            #("botao_editar_cadastro_de_veiculo_criado")
        self.click()
        self.find_button( "botao_para_excluir_equipamento_cadastro_1" ) 
            #("botao_para_excluir_equipamento_cadastro_1")
        self.click()
        self.wait(1000)
        self.enter()
        
        self.find_button( "botao_retornar_cadastro_equipament_4" ) 
            #("botao_retornar_cadastro_equipament_4")
        self.click()
        ##################################################
        ############# CADASTRO TIPO DE OS  ###############
        ##################################################

        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "tipo_os_botao_cadastro" ) 
            #("tipo_os_botao_cadastro")
        self.click()
        self.find_button( "botao_incluir_tipos_de_os_2" ) 
            #("botao_incluir_tipos_de_os_2")
        self.click()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "botao_salvar_tipos_de_os_cadastro" ) 
            #("botao_salvar_tipos_de_os_cadastro")
        self.click()
        self.find_button( "retornar_cadastro_tipo_de_os" ) 
            #("retornar_cadastro_tipo_de_os")
        self.click()
        self.find_button( "localizar_tipo_de_os_cadastro" ) 
            #("localizar_tipo_de_os_cadastro")
        self.click()
        self.find_button( "editar_tipo_de_os_cadastro" ) 
            #("editar_tipo_de_os_cadastro")
        self.click()
        self.find_button( "excluir_tipo_de_os_cadastro_5" ) 
            #("excluir_tipo_de_os_cadastro_5")
        self.click()
        self.wait(1000)
        self.enter()
        self.find_button( "retornar_cadastro_tipo_de_os" ) 
            #("retornar_cadastro_tipo_de_os")
        self.click()

        #####################################################################
        ################### CADASTRO DE GRUPOS DE O.S  ######################
        #####################################################################

        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "botao_cadastro_grupos_de_os" ) 
            #("botao_cadastro_grupos_de_os")
        self.click()
        self.find_button( "botao_incluir_grupos_de_os_cadastros" ) 
            #("botao_incluir_grupos_de_os_cadastros")
        self.click()
        self.type_keys_with_interval(10,"qa12!@")
        self.find_button( "botao_salvar_grupos_de_os_cadastro_2" ) 
            #("botao_salvar_grupos_de_os_cadastro_2")
        self.click()
        self.find_button( "botao_retornar_grupos_de_os_cadastro_4" ) 
            #("botao_retornar_grupos_de_os_cadastro_4")
        self.click()
        self.find_button( "localizar_grupos_de_os_botao_6" ) 
            #("localizar_grupos_de_os_botao_6")
        self.click()
        self.find_button( "editar_botao_grupo_de_os_7" ) 
            #("editar_botao_grupo_de_os_7")
        self.click()
        self.find_button( "botao_excluir_grupo_de_os_8" ) 
            #("botao_excluir_grupo_de_os_8")
        self.click()
        self.enter()
        self.find_button( "botao_retornar_grupos_de_os_cadastro_4" ) 
            #("botao_retornar_grupos_de_os_cadastro_4")
        self.click()
        self.click()
        self.click()
        self.click()
        
        self.wait(2000)

        #####################################################
        ########### CADASTROS CONFIGURAÇÃO BALAÇA ###########
        #####################################################

        if not self.find( "vendas_pdv_btn_cadastros_2407_menu", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_cadastros_2407_menu")
        self.click()
        self.find_button( "cadastros_configuracao_balanca_1" ) 
            #("cadastros_configuracao_balanca_1")
        self.click()
        #1
        x = 0 
        while x < 3 :
            self.type_down()
            x += 1
        x = 0 
        while x < 3 :
            self.type_up()
            x += 1
        self.tab()
        #2
        x = 0 
        while x < 8 :
            self.type_down()
            x += 1
        x = 0 
        while x < 8 :
            self.type_up()
            x += 1
        self.tab()
        #3
        x = 0 
        while x < 8 :
            self.type_down()
            x += 1
        x = 0 
        while x < 8 :
            self.type_up()
            x += 1
        self.tab()
        #4
        x = 0 
        while x < 4 :
            self.type_down()
            x += 1
        x = 0 
        while x < 4 :
            self.type_up()
            x += 1
        self.tab()
        #5
        x = 0 
        while x < 5 :
            self.type_down()
            x += 1
        x = 0 
        while x < 5 :
            self.type_up()
            x += 1
        self.tab()
        #6
        x = 0 
        while x < 3 :
            self.type_down()
            x += 1
        x = 0 
        while x < 3 :
            self.type_up()
            x += 1
        self.tab()
        #7
        x = 0 
        while x < 4 :
            self.type_down()
            x += 1
        x = 0 
        while x < 4 :
            self.type_up()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"1233")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.space()
        self.space()
        self.find_button( "botao_retornar_configuracao_balanca_cadastro" ) 
            #("botao_retornar_configuracao_balanca_cadastro")
        self.click()
        
        ###################################################################################################
        #####################################  AGENDA  ####################################################
        ###################################################################################################

        self.wait(2000)

        self.find_button( "botao_agenda_menu_principal_vendas" ) 
            #("botao_agenda_menu_principal_vendas")
        self.click()
        self.find_button( "achar_refresH_e_relativo_agenda" ) 
            #("achar_refresH_e_relativo_agenda")
        self.double_click_relative(402, 233)
        
        
        
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        x = 0 
        while x < 8 :
            self.type_down()
            x += 1
        x = 0 
        while x < 8 :
            self.type_up()
            x += 1
        self.enter()
        
        self.find_button( "achar_qa_12!_agenda_compromis" ) 
            #("achar_qa_12!_agenda_compromis")
        self.right_click()
        
     
        self.wait(500)
        self.find_button( "achar_x_delete_compromisso_agenda" ) 
            #("achar_x_delete_compromisso_agenda")
        self.click()
        

        self.find_button( "retornar_botao_agenda_compromissos_6" ) 
            #("retornar_botao_agenda_compromissos_6")
        self.click()
        self.wait(2000)
        
        ################################################################
        ######################   CHAMADAS    ###########################
        ################################################################
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_chamadas_menu_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_chamadas_menu_2407")
        self.click()

        
        self.wait(1000)
        self.find_button( "achar_data_dentro_chamadas" ) 
            #("achar_data_dentro_chamadas")
        self.click_relative(31, 6)
        self.find_button( "carregar_ano_chamadas_" ) 
            #("carregar_ano_chamadas_")
        self.click()
        self.find_button( "ano_atual_chamadas_2" ) 
            #("ano_atual_chamadas_2")
        self.click()
        self.tab()
        self.type_right()
        self.type_left()
        self.tab()
        self.space()
        self.type_down()

        x = 0
        while x < 74 :
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.tab()
        self.space()
        self.type_down()
        while x < 4 :
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.tab()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        x = 0
        while x < 12 :
            self.type_right()
            x += 1
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_down()
        self.enter()
        self.wait(2000)
        self.find_button( "abrir_chamado_chamadas_botao" ) 
            #("abrir_chamado_chamadas_botao")
        self.click()
        self.wait(2000)
        self.find_button( "botao_buscar_chamado_incluir_chamados" ) 
            #("botao_buscar_chamado_incluir_chamados")
        self.click()
        #self.find_button( "botao_pesquisar_chamados_incluir" ) 
            #("botao_pesquisar_chamados_incluir")
        #self.click()
        
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_retornar_2407_pesquisa", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_retornar_2407_pesquisa")
        self.click()
        self.wait(2000)
        
        self.find_button( "anexos_chamados_incluir_achar" ) 
            #("anexos_chamados_incluir_achar")
        self.click()

        
        self.find_button( "achar_anexar_chamados_incluir_novo" ) 
            #("achar_anexar_chamados_incluir_novo")
        self.click_relative(-71, 42)
        self.find_button( "achar_cancelar_botao_chamados_3" ) 
            #("achar_cancelar_botao_chamados_3")
        self.click()
        self.find_button( "anexar_relativo_retornar_chamados_6" ) 
            #("anexar_relativo_retornar_chamados_6")
        self.click_relative(-49, 6)
        self.find_button( "anexos_relativo_retornar_chamados_8" ) 
            #("anexos_relativo_retornar_chamados_8")
        self.click_relative(-155, 9)
        self.find_button( "botao_editar_chamados_chamadas" ) 
            #("botao_editar_chamados_chamadas")
        self.click()
        self.wait(1000)
        self.enter()
        self.find_button( "entrar_em_anexos_editar_chamado" ) 
            #("entrar_em_anexos_editar_chamado")
        self.click()
        self.find_button( "botao_anexar_relativo_p_retornar" ) 
            #("botao_anexar_relativo_p_retornar")
        self.click_relative(-47, 12)
        
        
        self.find_button( "achar_anexos_e_retorne_chamadas" ) 
            #("achar_anexos_e_retorne_chamadas")
        self.click_relative(-124, 12)
        self.find_button( "impressao_chamadas_botao_77" ) 
            #("impressao_chamadas_botao_77")
        self.click()
        self.wait(1000)
        self.find_button( "clicar_thumbnails_impressao" ) 
            #("clicar_thumbnails_impressao")
        self.click()
        self.find_button( "outline_impressao_relativo" ) 
            #("outline_impressao_relativo")
        self.click_relative(193, -23)
        self.type_keys_with_interval(1,"10")
        self.tab()
        self.find_button( "achar_botao_binoculos_impressora" ) 
            #("achar_botao_binoculos_impressora")
        self.click()
        self.wait(500)
        self.click()
        self.find_button( "botao_mudar_tamanho_folha_impres" ) 
            #("botao_mudar_tamanho_folha_impres")
        self.click()
        self.find_button( "botao_mudar_tamanho_max_impressao" ) 
            #("botao_mudar_tamanho_max_impressao")
        self.click()
        self.find_button( "botao_medio_impressao_tamanho_folha" ) 
            #("botao_medio_impressao_tamanho_folha")
        self.click()
        self.find_button( "botao_pular_relativo_para_fechar" ) 
            #("botao_pular_relativo_para_fechar")
        self.click_relative(151, -19)

        self.wait(5000)
        self.key_esc()


        ################### GRADE EM CHAMADOS ####################
        ##########################################################
        
        self.find_button( "grade_relativo_chamadas" ) 
            #("grade_relativo_chamadas")
        self.click_relative(48, 14)
        self.find_button( "botao_imprimir_texto_em_grade" ) 
            #("botao_imprimir_texto_em_grade")
        self.click()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_up()
        self.type_up()
        self.type_up()
        self.type_down()
        self.type_down()
        self.tab()
        self.tab()
        self.enter()
        self.type_down()
        self.type_down()
        self.enter()
        self.tab()
        self.enter()
        self.wait(500)
        self.enter()
        self.tab()
        self.enter()
        self.tab()
        self.enter()
        self.wait(1000)
        self.key_esc()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_keys_with_interval(1,'1')
        self.tab()
        self.type_down()
        self.type_down()
        self.type_up()
        self.type_up()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.enter()
        self.tab()
        x = 0 
        while x < 80 :
            self.type_down()
            self.wait(500)
            x += 1
        x = 0 
        while x < 80 :
            self.type_up()
            self.wait(500)
            x += 1
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.space()
        self.space()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.type_keys_with_interval(1,"12")
        self.tab()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_right()
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.enter()
        self.wait(500)
        self.enter()
        self.tab()
        self.enter()
        self.wait(500)
        self.key_esc()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.enter()
        self.wait(500)
        self.enter()
        self.tab()
        self.enter()
        self.wait(500)
        self.key_esc()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_right()
        self.find_button( "achar_fit_to_page_botao_clicar" ) 
            #("achar_fit_to_page_botao_clicar")
        self.click()

        self.find_button( "print_botao_finaliza_impressao" ) 
            #("print_botao_finaliza_impressao")
        self.click()
        self.wait(1000)
        self.find_button( "fechar_janela_de_impressao_x_lar" ) 
            #("fechar_janela_de_impressao_x_lar")
        self.click()
        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "armazena_e_recupera_grade_arquivos" ) 
            #("armazena_e_recupera_grade_arquivos")
        self.click()
        self.wait(500)
        self.type_keys_with_interval(1,'qa12!@')
        self.wait(1000)
        self.find_button( "salvar_grade_feita_qa12" ) 
            #("salvar_grade_feita_qa12")
        self.click()
        

        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "armazena_e_recupera_grade_arquivos" ) 
            #("armazena_e_recupera_grade_arquivos")
        self.click()
        self.wait(500)
        self.find_button( "achar_grade_qa12_apagar" ) 
            #("achar_grade_qa12_apagar")
        self.click()
        self.wait(500)
        self.find_button( "botao_excluir_grade_criada_qa12" ) 
            #("botao_excluir_grade_criada_qa12")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "exportar_para_excel_botao_grade_6" ) 
            #("exportar_para_excel_botao_grade_6")
        self.click()
        self.wait(500)
        self.key_esc()
        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "export_para_html_grade_botao_7" ) 
            #("export_para_html_grade_botao_7")
        self.click()
        self.wait(500)
        self.key_esc()
        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "export_to_texto_grade_4" ) 
            #("export_to_texto_grade_4")
        self.click()
        self.wait(500)
        self.key_esc()
        self.find_button( "relativo_grade_escolher_opcao_2" ) 
            #("relativo_grade_escolher_opcao_2")
        self.click_relative(52, 17)
        self.find_button( "export_to_xml_grade_4" ) 
            #("export_to_xml_grade_4")
        self.click()
        self.wait(500)
        
        self.wait(3000)
        self.key_esc()
        self.wait(2000)
        self.find_button( "botao_para_retorn_de_chamadas_7" ) 
            #("botao_para_retorn_de_chamadas_7")
        self.click()
        
        
        ####################################################################
        ###################### DOC-E #######################################
        ####################################################################
        
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_doc_e_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_doc_e_2407")
        self.click()
        self.wait(2000)
        
        
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        if not self.find( "vendas_contas_datagestao_doce", matching=0.97, waiting_time=10000):
            not_found("vendas_contas_datagestao_doce")
        self.click_relative(31, 9)
        
        
        self.find_button( "carregar_ano_data" ) 
            #("carregar_ano_data")
        self.click()
        
        self.find_button( "data_atual_botao" ) 
            #("data_atual_botao")
        self.click()
        self.find_button( "botao_buscar_achar_empresa_doce" ) 
            #("botao_buscar_achar_empresa_doce")
        self.click()
        #self.find_button( "botao_relativo_localizar_em_doce" ) 
            #("botao_relativo_localizar_em_doce")
        #self.click_relative(-45, 16)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.tab()
        self.space()
        self.type_down()
        self.type_up()
        self.type_up()
        self.type_up()
        self.type_up()
        self.type_up()
        self.type_up()

        x = 0
        while x < 7 :
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.wait(1000)
        self.tab()
        self.space()
        self.type_down()
        x = 0
        while x < 19 :
            self.space()
            self.space()
            self.type_down()
            x += 1
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()
        self.find_button( "achar_selecao_doce" ) 
            #("achar_selecao_doce")
        self.click()
        self.wait(500)
        self.double_click()
        self.tab()
        self.type_right()
        self.type_right()
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.space()
        self.space()
        self.tab()
        self.type_keys_with_interval(1,"123")
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
        self.find_button( "botao_filtro_em_doce" ) 
            #("botao_filtro_em_doce")
        self.click()
        self.find_button( "achar__mesaniversario_filtro" ) 
            #("achar__mesaniversario_filtro")
        self.double_click_relative(112, 48)
        x = 0
        while x < 12 :
            self.type_down()
            x += 1
        x = 0
        while x < 12 :
            self.type_up()
            x += 1
        
        self.tab()
        self.tab()
        self.type_up()
        self.type_up()
        self.type_down()
        self.type_down()
        self.find_button( "data_relativo_doc__filtro" ) 
            #("data_relativo_doc__filtro")
        self.click_relative(33, 9)
        self.find_button( "carregar_ano_chamadas_" ) 
            #("carregar_ano_chamadas_")
        self.click()
        self.find_button( "ano_atual_chamadas_2" ) 
            #("ano_atual_chamadas_2")
        self.click()

        self.tab()
        self.type_up()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_up()
        self.type_up()
        self.type_up()
        self.wait(1000)
        self.find_button( "adicionar_nome_filtro_doce" ) 
            #("adicionar_nome_filtro_doce")
        self.click()
        self.wait(1000)
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_seleciona_cliente_rel_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_seleciona_cliente_rel_2407")
        self.click_relative(26, 23)
        
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.wait(1000)
        
        self.wait(2000)
        self.find_button( "botao_filtros_filtragem_em_doce" ) 
            #("botao_filtros_filtragem_em_doce")
        self.click_relative(8, -17)
        self.find_button( "inicial_pre_filtragem_doce" ) 
            #("inicial_pre_filtragem_doce")
        self.click_relative(373, 4)
        self.find_button( "nome_rel_filtro_inic" ) 
            #("nome_rel_filtro_inic")
        self.click_relative(14, 20)
        
        self.find_button( "final_relativo_pre_filtragem_doce" ) 
            #("final_relativo_pre_filtragem_doce")
        self.click_relative(369, 5)
        self.find_button( "nome_final_filtro_doce_rel" ) 
            #("nome_final_filtro_doce_rel")
        self.click_relative(21, 22)
        
        self.wait(2000)
        self.find_button( "filtrar_todos_com_segmento_doce" ) 
            #("filtrar_todos_com_segmento_doce")
        self.click_relative(229, 35)
        if not self.find( "vendas_pdv_filtragem_cnpj_dupli_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_filtragem_cnpj_dupli_2407")
        self.click()
        self.find_button( "situacao_filtragem_doce_achar" ) 
            #("situacao_filtragem_doce_achar")
        self.double_click_relative(198, 7)
        x = 0
        while x < 7 :
            self.type_down()
            x += 1
        x = 0
        while x < 7 :
            self.type_up()
            x += 1
        self.find_button( "achar_limpa_filtros_relativo_retornar_doce" ) 
            #("achar_limpa_filtros_relativo_retornar_doce")
        self.click_relative(-47, 7)
        self.wait(1000)
        ####### PASSOU PELO DOC-E, POREM APENAS CONSEGUI MEXER EM FILTRO E GRADE, O RESTO NÃO FOI POSSIVEL ABRIR.

        self.find_button( "retornar_botao_de_gestao_doce_fim" ) 
            #("retornar_botao_de_gestao_doce_fim")
        self.click()
        self.wait(1000)

##################################### RECADOS ###############################################
#############################################################################################

        self.find_button( "recados_menu_principal" ) 
            #("recados_menu_principal")
        self.click()
        self.wait(1000)
        self.find_button( "botao_localizar_usar_2_vezes_recados" ) 
            #("botao_localizar_usar_2_vezes_recados")
        self.click()
        self.wait(1000)
        self.find_button( "incluir_um_recado_botao" ) 
            #("incluir_um_recado_botao")
        self.click()
        self.wait(1000)
        self.find_button( "recado_para_botao_buscar" ) 
            #("recado_para_botao_buscar")
        self.click()
        self.wait(1000)
        #self.find_button( "localizar_recado_responsavel" ) 
            #("localizar_recado_responsavel")
        #self.click()
        self.wait(1000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "empresa_cliente_botao_buscar_recado" ) 
            #("empresa_cliente_botao_buscar_recado")
        self.click_relative(489, 30)
        self.wait(2000)
        self.type_keys_with_interval(1,"0000001")
        self.type_down()
        self.wait(1000)
        self.find_button( "botao_localizar_consulta_clientes_recados_2" ) 
            #("botao_localizar_consulta_clientes_recados_2")
        self.click()
        self.find_button( "achar_ultragras_moacir_recado" ) 
            #("achar_ultragras_moacir_recado")
        self.click()
        
        
        if not self.find( "vendas_selecionar_pdv_botao_24", matching=0.97, waiting_time=10000):
            not_found("vendas_selecionar_pdv_botao_24")
        self.click()
        self.wait(2000)
        self.tab()
        self.type_keys_with_interval(1,"123123123")
        self.tab()
        self.type_keys_with_interval(1,"123123123")
        self.tab()
        self.type_keys_with_interval(1,"qa12@teorema.com")
        self.tab()
        self.wait(1000)
        self.space()
        self.wait(1000)
        
        self.tab()
        self.type_keys_with_interval(1,"qa12!@")
        self.find_button( "salvar_recado_criado_1" ) 
            #("salvar_recado_criado_1")
        self.click()
        self.find_button( "responder_recado_botao_1" ) 
            #("responder_recado_botao_1")
        self.click()
        self.type_keys_with_interval(1,"qa12!@")
          
        self.find_button( "salvar_recado_respondido_2" ) 
            #("salvar_recado_respondido_2")
        self.click()

        self.wait(2000)
        self.enter()
        
        
        
        self.find_button( "botao_retornar_de_incluir_recado" ) 
            #("botao_retornar_de_incluir_recado")
        self.click()
        self.find_button( "usuario_achar_relativo_recados" ) 
            #("usuario_achar_relativo_recados")
        self.click_relative(67, 26)
        
        x = 0
        while x < 7 :
            self.backspace()
            x += 1
        self.tab()
        self.tab()
        self.type_up()
        self.type_up()
        self.tab()
        self.type_right()
        self.type_right()
        
        self.wait(1000)
        
        self.find_button( "botao_localizar_usar_2_vezes_recados" ) 
            #("botao_localizar_usar_2_vezes_recados")
        self.click()
        self.wait(1000)
        self.find_button( "qa12!@_achar_botao_recados" ) 
            #("qa12!@_achar_botao_recados")
        self.click()
        self.wait(1000)
        self.find_button( "editar_recados_botao_6" ) 
            #("editar_recados_botao_6")
        self.click()
        self.wait(1000)
        self.find_button( "excluir_recado_criado_8" ) 
            #("excluir_recado_criado_8")
        self.click()
        self.wait(1000)
        self.enter()
        self.find_button( "botao_retornar_cadastro_de_recados_3" ) 
            #("botao_retornar_cadastro_de_recados_3")
        self.click()
        self.find_button( "botao_localizar_usar_2_vezes_recados" ) 
            #("botao_localizar_usar_2_vezes_recados")
        self.click()
        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "botao_imprimir_grade_recados" ) 
            #("botao_imprimir_grade_recados")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "armazenar_e_recuperar_botao_recados_grade" ) 
            #("armazenar_e_recuperar_botao_recados_grade")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "export_para_excel_recados_grade" ) 
            #("export_para_excel_recados_grade")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "export_para_html_grade_botao_7" ) 
            #("export_para_html_grade_botao_7")
        self.click()
        self.wait(1000)
        self.key_esc()


        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "export_to_texto_grade_4" ) 
            #("export_to_texto_grade_4")
        self.click()
        self.wait(1000)
        self.key_esc()


        self.find_button( "achar_grade_e_clique_relativo_recados" ) 
            #("achar_grade_e_clique_relativo_recados")
        self.click_relative(47, 15)
        self.find_button( "export_to_xml_grade_4" ) 
            #("export_to_xml_grade_4")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.find_button( "selecionar_todos_recados_botao" ) 
            #("selecionar_todos_recados_botao")
        self.double_click()
        self.find_button( "exibir_linhas_obs_recados_botao" ) 
            #("exibir_linhas_obs_recados_botao")
        self.double_click()
        self.find_button( "2_geracao_recados_botao" ) 
            #("2_geracao_recados_botao")
        self.click()
        self.find_button( "de_quem_recado_preencher" ) 
            #("de_quem_recado_preencher")
        self.click_relative(112, 9)
        self.wait(1000)
        x = 0
        while x < 9 :
            self.backspace()
            x += 1
        self.type_keys_with_interval(1,"qa12!@")
        self.tab()
        
        self.wait(1000)
        self.find_button( "botao_buscar_empresa_recados_2_ger" ) 
            #("botao_buscar_empresa_recados_2_ger")
        self.click()
        self.wait(3000)
        self.type_keys_with_interval(1,"0000001")
        self.wait(1000)
        self.find_button( "loc_pos_rec_1" ) 
            #("loc_pos_rec_1")
        self.click()
        
        self.wait(1000)
        self.find_button( "selecionar_empresa_ger_recado" ) 
            #("selecionar_empresa_ger_recado")
        self.click()
        self.wait(1000)
        self.tab()
        self.tab()
        self.tab()
        self.type_keys_with_interval(1,"123123123")
        self.tab()
        self.type_keys_with_interval(1,"123123123")
        self.wait(2000)
        self.find_button( "retorne_de_recados_exclusao_tot" ) 
            #("retorne_de_recados_exclusao_tot")
        self.click()
        self.wait(2000)
        self.find_button( "abrir_nov_recados_2" ) 
            #("abrir_nov_recados_2")
        self.click()
        self.wait(2000)
        self.find_button( "origem_destino_rel_filtro" ) 
            #("origem_destino_rel_filtro")
        self.click_relative(-25, 24)
        self.wait(2000)
        self.backspace()
        self.wait(2000)
        self.find_button( "todos_botao_recad_clic" ) 
            #("todos_botao_recad_clic")
        self.click()
        self.wait(3000)
        self.find_button( "loc_todos_recados_2" ) 
            #("loc_todos_recados_2")
        self.click()
        self.wait(3000)
        self.find_button( "achar_cod_qa12_apagar_rec" ) 
            #("achar_cod_qa12_apagar_rec")
        self.click()
        self.wait(3000)
        self.find_button( "editar_tds_recados_1" ) 
            #("editar_tds_recados_1")
        self.click()
        self.wait(3000)
        self.find_button( "excluir_nov_todos_recados" ) 
            #("excluir_nov_todos_recados")
        self.click()
        self.wait(3000)
        self.enter()
        self.find_button( "retornar_seg_exclusao_recados" ) 
            #("retornar_seg_exclusao_recados")
        self.click()
        self.wait(3000)

        self.find_button( "localizar_recados_nov_conferir_2" ) 
            #("localizar_recados_nov_conferir_2")
        self.click()

        self.wait(2000)
        self.key_esc()
        
        
        ###############################################################################
        ################################ PROCESSOS ####################################
        ###############################################################################
        self.wait(2000)

        if not self.find( "vendas_pdv_btn_processos_rel_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_processos_rel_2407")
        self.click_relative(79, 18)
        
        
        self.find_button( "altera_data_processos_botao" ) 
            #("altera_data_processos_botao")
        self.click()
        self.find_button( "altera_data_botao_direita" ) 
            #("altera_data_botao_direita")
        self.click()
        self.find_button( "botao_esquerda_altera_data" ) 
            #("botao_esquerda_altera_data")
        self.click()
        self.find_button( "retorna_altera_data_sis" ) 
            #("retorna_altera_data_sis")
        self.click()
        self.wait(3000)
        self.enter()
        self.wait(3000)
        if not self.find( "vendas_pdv_btn_processos_rel_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_processos_rel_2407")
        self.click_relative(79, 18)
        self.wait(2000)
        self.find_button( "info_da_release_processos" ) 
            #("info_da_release_processos")
        self.click()
        
        self.wait(2000)
        if not self.find( "vendas_pdv_btn_voltar_2407_release", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_voltar_2407_release")
        self.click()
        
        
        self.find_button( "achar_peças_menu_rel" ) 
            #("achar_peças_menu_rel")
        self.click_relative(66, 18)
        self.find_button( "central_de_pecas_oficina_pec" ) 
            #("central_de_pecas_oficina_pec")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.find_button( "ache_a_data_relat_flec" ) 
            #("ache_a_data_relat_flec")
        self.click_relative(24, 7)
        self.find_button( "carregar_ano_chamadas_" ) 
            #("carregar_ano_chamadas_")
        self.click()
        self.find_button( "ano_atual_chamadas_2" ) 
            #("ano_atual_chamadas_2")
        self.click()
        self.find_button( "situacao_rel_empresa_flec" ) 
            #("situacao_rel_empresa_flec")
        self.click_relative(-34, 35)
        self.backspace()
        self.wait(500)
        self.shift_tab()
        self.wait(500)
        self.type_keys_with_interval(1,"1")
        self.wait(300)
        self.enter()


        self.find_button( "solicitante_pecas_botao" ) 
            #("solicitante_pecas_botao")
        self.click()
        self.wait(500)
        if not self.find( "vendas_pdv_flecha_solicitante", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_flecha_solicitante")
        self.click()
        
        self.wait(2000)

        self.find_button( "nome_cadastro_solicitante_pecas" ) 
            #("nome_cadastro_solicitante_pecas")
        self.click_relative(27, 21)
        self.find_button( "cliente_pecas_bot_1" ) 
            #("cliente_pecas_bot_1")
        self.click()
        self.find_button( "botao_buscar_pecas_clientes_2" ) 
            #("botao_buscar_pecas_clientes_2")
        self.click()
        self.wait(4000)
        self.type_keys_with_interval(1,'0000001')
        self.wait(1000)
        self.enter()
        self.type_down()
        self.find_button( "select_cliente_pecas_3" ) 
            #("select_cliente_pecas_3")
        self.click()
        self.find_button( "veiculo_recas_opcao_pecas" ) 
            #("veiculo_recas_opcao_pecas")
        self.click()
        
        self.find_button( "botao_buscar_pecas_clientes_2" ) 
            #("botao_buscar_pecas_clientes_2")
        self.click()
        self.wait(2000)

        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.wait(1000)
        self.enter()
        self.find_button( "placa_pecas_botao_4" ) 
            #("placa_pecas_botao_4")
        self.click()
        self.find_button( "botao_buscar_pecas_clientes_2" ) 
            #("botao_buscar_pecas_clientes_2")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)


        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "2selecao_pecas_clic" ) 
            #("2selecao_pecas_clic")
        self.click()
        self.find_button( "2selecao_pecas_clique_relativo" ) 
            #("2selecao_pecas_clique_relativo")
        self.click_relative(0, 43)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "achar_todos_pecas_botao_situacao" ) 
            #("achar_todos_pecas_botao_situacao")
        self.double_click()
        
        x = 0
        while x < 11 :
            self.type_down()
            x += 1
        x = 0
        while x < 11 :
            self.type_up()
            x += 1
        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)
        self.find_button( "botao_imprimir_grade_recados" ) 
            #("botao_imprimir_grade_recados")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)
        self.find_button( "armazenar_e_recuperar_botao_recados_grade" ) 
            #("armazenar_e_recuperar_botao_recados_grade")
        self.click()
        self.wait(1000)
        self.key_esc()


        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)

        self.find_button( "export_para_excel_recados_grade" ) 
            #("export_para_excel_recados_grade")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)

        self.find_button( "export_para_html_grade_botao_7" ) 
            #("export_para_html_grade_botao_7")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)

        self.find_button( "export_to_texto_grade_4" ) 
            #("export_to_texto_grade_4")
        self.click()
        self.wait(1000)
        self.key_esc()

        self.find_button( "grade_pecas_botao_flecha" ) 
            #("grade_pecas_botao_flecha")
        self.click_relative(49, 14)
        self.find_button( "export_to_xml_grade_4" ) 
            #("export_to_xml_grade_4")
        self.click()
        self.wait(1000)
        self.key_esc()
###### PEÇAS CONTROLE DE ENTREGAS 
###### ALGUMAS OPÇÕES PARECEM ESTAR DESABILITADAS PARA USO

        self.find_button( "achar_peças_menu_rel" ) 
            #("achar_peças_menu_rel")
        self.click_relative(66, 18)
        self.find_button( "pecas_controle_de_entregas_os_menu" ) 
            #("pecas_controle_de_entregas_os_menu")
        self.click()
        self.find_button( "estoquista_relativo_flecha" ) 
            #("estoquista_relativo_flecha")
        self.click_relative(305, 37)
        self.find_button( "nome_cliente_relativo_estoquista" ) 
            #("nome_cliente_relativo_estoquista")
        self.click_relative(57, 23)
        self.find_button( "mecanico_relativo_botao_flecha" ) 
            #("mecanico_relativo_botao_flecha")
        self.click_relative(304, 39)
        self.find_button( "nome_relativo_mecanico_cliente" ) 
            #("nome_relativo_mecanico_cliente")
        self.click_relative(41, 25)
        self.find_button( "requisição_numero_pecas" ) 
            #("requisição_numero_pecas")
        self.click()
        self.shift_tab()
        self.type_keys_with_interval(1,"123")
        self.tab()
        self.tab()
        
        x = 0
        while x < 10 :
            self.type_down()
            x += 1
   
        x = 0
        while x < 10 :
            self.type_up()
            x += 1


        self.find_button( "operacao_pecas_separar" ) 
            #("operacao_pecas_separar")
        self.click_relative(7, 45)
        
        x = 0
        while x < 3 :
            self.type_right()
            x += 1
        self.wait(1000)
        self.find_button( "2_consulta_requisicoes_pecas" ) 
            #("2_consulta_requisicoes_pecas")
        self.click()
        self.wait(1000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,'123')
        self.tab()
        self.find_button( "buscar_item_pecas_consulta_req" ) 
            #("buscar_item_pecas_consulta_req")
        self.click()
        self.wait(3000)
        self.find_button( "localizar_itens_req_pecas_2" ) 
            #("localizar_itens_req_pecas_2")
        self.click()
        self.wait(1000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "cliente_pecas_botao_proc_1" ) 
            #("cliente_pecas_botao_proc_1")
        self.click()
        self.find_button( "cliente_empresa_rel_buscar_botao" ) 
            #("cliente_empresa_rel_buscar_botao")
        self.click_relative(60, 31)
        self.wait(2000)
        self.type_keys_with_interval(1,"0000001")
        self.wait(1000)
        self.find_button( "localizar_itens_req_pecas_2" ) 
            #("localizar_itens_req_pecas_2")
        self.click()
        self.wait(2000)
        self.find_button( "select_pecas_cliente_item_rel" ) 
            #("select_pecas_cliente_item_rel")
        self.click()
        self.find_button( "ach_veiculo_pecas_bot" ) 
            #("ach_veiculo_pecas_bot")
        self.click()
        if not self.find( "vendas_pdv_rel_empresas_busc_veic", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_rel_empresas_busc_veic")
        self.click_relative(79, 28)
        self.find_button( "loc_equi_veiculos_pecas" ) 
            #("loc_equi_veiculos_pecas")
        self.click()
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "botao_placa_pecas_vei_2" ) 
            #("botao_placa_pecas_vei_2")
        self.click()
        self.wait(1000)
        if not self.find( "vendas_pdv_placa_rel_buscar", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_placa_rel_buscar")
        self.click_relative(81, 27)
        self.wait(2000)
        self.find_button( "localizar_placas_veiculos_botao_5" ) 
            #("localizar_placas_veiculos_botao_5")
        self.click()
        self.wait(1000)
        if not self.find( "vendas_pdv_btn_selecionar_opc_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_selecionar_opc_2407")
        self.click()
        self.wait(2000)
        self.find_button( "retornar_de_pecas_fim_1" ) 
            #("retornar_de_pecas_fim_1")
        self.click()
        self.wait(1000)
        self.click()
        
        #ordem de servico -> incluir -> Orcamento
        
        self.wait(2000)
        
        self.find_button( "caixa_menu_princ_botao" ) 
            #("caixa_menu_princ_botao")
        self.click()
        self.wait(1000)
        self.find_button( "impressao_rel_botao_caixa_1" ) 
            #("impressao_rel_botao_caixa_1")
        self.click_relative(86, 15)
        self.wait(1000)
        self.find_button( "impressao_matricial_caixa_1" ) 
            #("impressao_matricial_caixa_1")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.key_esc()
        self.wait(1000)
        self.enter()
        ###
        ###
        
        
        self.wait(1000)

        self.find_button( "impressao_rel_botao_caixa_1" ) 
            #("impressao_rel_botao_caixa_1")
        self.click_relative(86, 15)
        self.wait(1000)

        self.find_button( "impressao_grafica_caixa_menu_1" ) 
            #("impressao_grafica_caixa_menu_1")
        self.click()
        self.wait(1000)
        self.enter()
        self.wait(2000)

        self.find_button( "achar_x_verm_caixa_impressao_2" ) 
            #("achar_x_verm_caixa_impressao_2")
        self.click()
        self.wait(1000)
        
        self.find_button( "impressao_rel_botao_caixa_1" ) 
            #("impressao_rel_botao_caixa_1")
        self.click_relative(86, 15)
        self.wait(1000)

        self.find_button( "vendas_a_prazo_grafico_caixa_1" ) 
            #("vendas_a_prazo_grafico_caixa_1")
        self.click()
        self.wait(8000)

        self.find_button( "achar_x_verm_caixa_impressao_2" ) 
            #("achar_x_verm_caixa_impressao_2")
        self.click()
        self.wait(1000)

        self.find_button( "suprimento_caixa_botao_1" ) 
            #("suprimento_caixa_botao_1")
        self.click()
        self.wait(1000)

        self.find_button( "achar_flecha_suprimento_caixa_2" ) 
            #("achar_flecha_suprimento_caixa_2")
        self.click()
        self.wait(1000)
        

        self.find_button( "nome_finalizadora_caixa_1" ) 
            #("nome_finalizadora_caixa_1")
        self.click_relative(40, 17)

        self.wait(1000)
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,'1')
        self.tab()
        self.tab()
        self.wait(500)

        self.type_keys_with_interval(100,'qa12!@')

        self.find_button( "confirmar_caixa_movimento_1" ) 
            #("confirmar_caixa_movimento_1")
        self.click()
        self.wait(1000)
        self.key_esc()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        
        
        ######################################
        ############### SANGRIA ##############
        ######################################
        self.wait(3000)

        if not self.find( "vendas_pdv_btn_sangria_2407", matching=0.97, waiting_time=10000):
            not_found("vendas_pdv_btn_sangria_2407")
        self.click()
        

        self.find_button( "achar_flecha_suprimento_caixa_2" ) 
            #("achar_flecha_suprimento_caixa_2")
        self.click()
        self.wait(1000)
        

        self.find_button( "nome_finalizadora_caixa_1" ) 
            #("nome_finalizadora_caixa_1")
        self.click_relative(40, 17)

        self.wait(1000)
        self.tab()
        self.wait(1000)
        self.type_keys_with_interval(1,'1')
        self.tab()
        self.wait(1000)
        self.tab()
        self.wait(500)

        self.type_keys_with_interval(100,'qa12!@')

        self.find_button( "confirmar_caixa_movimento_1" ) 
            #("confirmar_caixa_movimento_1")
        self.click()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.key_esc()
        
        
        self.find_button( "fechar_caixa_finalizar_menu" ) 
            #("fechar_caixa_finalizar_menu")
        self.click()

        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.key_esc()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.enter()
        self.wait(2000)
        self.enter()
        self.key_esc()
        self.wait(1000)
        self.enter()
        self.wait(1000)
        self.key_esc()


def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  


