from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()





"""
CÓDIGO FEITO PARA SISTEMA FATURAMENTO 24.11 PARTE 2 
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
                bot = self
                """
                                ####---ITENS DE ESTOQUE---####
                self.wait(2000)              
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "grupofiscalIE", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscalIE")
                self.click_relative(73, 46)
                if not self.find( "cod006IE", matching=0.97, waiting_time=10000):
                    self.not_found("cod006IE")
                self.click()            
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                    self.not_found("cancelareditarIE")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "unidadeteste", matching=0.97, waiting_time=10000):
                    self.not_found("unidadeteste")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
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
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                    self.not_found("cancelareditarIE")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
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
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                    
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                

                
                self.wait(2000)
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                    self.not_found("agrupamentoie")
                self.click()
                if not self.find( "NCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("NCMIE")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                    self.not_found("cancelareditarIE")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "descricaoIENCM", matching=0.97, waiting_time=10000):
                    self.not_found("descricaoIENCM")
                self.click_relative(66, 5)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "addnovoregistroNCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("addnovoregistroNCMIE")
                self.click_relative(5, 33)
                if not self.find( "EstadoNCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("EstadoNCMIE")
                self.click_relative(47, 28)
                if not self.find( "cod001NCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("cod001NCMIE")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not bot.find( "fatu_btn_gravar_cadastros_ncm", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_gravar_cadastros_ncm")
                bot.click()
                if not self.find( "paranaNCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("paranaNCMIE")
                self.click()
                if not self.find( "excluirregistroNCMIE", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroNCMIE")
                self.click_relative(7, 57)
                self.enter()
                #if not self.find( "simexcluirNCMIE", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirNCMIE")
                #self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "cadastroncmteste", matching=0.97, waiting_time=10000):
                    self.not_found("cadastroncmteste")
                self.click()                      
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                    self.not_found("agrupamentoie")
                self.click()
                if not self.find( "enderecodeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("enderecodeestoque")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_down()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                    self.not_found("achargrupoteste")
                self.click_relative(5, 30)
                self.type_keys_with_interval(1,'te12')
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()           
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CADASTRO DE ITENS---####
                self.wait(1500)
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                self.wait(2000)
                if not self.find( "cadastrodeitens", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrodeitens")
                self.click()
                self.wait(8000)
                #if not bot.find( "fatu_cad_btn_localizar_cad_itens", matching=0.97, waiting_time=10000):
                #    not_found("fatu_cad_btn_localizar_cad_itens")
                #bot.click()
                
                #if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                #    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                #bot.click()
                #self.wait(6000)
                #if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarfim")
                #self.click()
                #self.wait(6000)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(5000)
                self.type_right()
                self.enter()
                self.wait(4000)
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
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "cadastroitensreferencia", matching=0.97, waiting_time=10000):
                    self.not_found("cadastroitensreferencia")
                self.click_relative(718, 91)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.enter()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
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
                # 
                # if not self.find( "operacaocalculoprecoci", matching=0.97, waiting_time=10000):
                #     self.not_found("operacaocalculoprecoci")
                # self.click_relative(55, 23)
                # self.tab()
                # self.tab()
                # self.tab()
                # self.type_down()
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "regiaocalculoprecoci", matching=0.97, waiting_time=10000):
                #     self.not_found("regiaocalculoprecoci")
                # self.click_relative(52, 25)
                # self.wait(500)
                # if not self.find( "cod001ci", matching=0.97, waiting_time=10000):
                #     self.not_found("cod001ci")
                # self.click()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "grupofiscalcalculodeprecoci", matching=0.97, waiting_time=10000):
                #     self.not_found("grupofiscalcalculodeprecoci")
                # self.click_relative(668, 199)           
                # if not self.find( "cod001ci", matching=0.97, waiting_time=10000):
                #     self.not_found("cod001ci")
                # self.click()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
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
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                
                
                self.wait(1500)
                                ####---A1P1 AGRUPAMENTO---#### 
                
                if not self.find( "familiaCI", matching=0.97, waiting_time=10000):
                    self.not_found("familiaCI")
                self.click_relative(49, 43)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "marcaCI", matching=0.97, waiting_time=10000):
                    self.not_found("marcaCI")
                self.click_relative(51, 85)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "controleCI", matching=0.97, waiting_time=10000):
                    self.not_found("controleCI")
                self.click_relative(49, 128)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "unidadetributariaCI", matching=0.97, waiting_time=10000):
                    self.not_found("unidadetributariaCI")
                self.click_relative(50, 163)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                    self.not_found("codcaixa")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                x=0
                while x<6:
                    self.tab()
                    x=x+1
                if not self.find( "centrocustosCI", matching=0.97, waiting_time=10000):
                    self.not_found("centrocustosCI")
                self.click_relative(85, 204)
                self.backspace()
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                self.backspace()
                if not self.find( "grupoCI", matching=0.97, waiting_time=10000):
                    self.not_found("grupoCI")
                self.click_relative(452, 44)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "tipoCI", matching=0.97, waiting_time=10000):
                    self.not_found("tipoCI")
                self.click_relative(451, 83)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "unidadeestoqueCI", matching=0.97, waiting_time=10000):
                    self.not_found("unidadeestoqueCI")
                self.click_relative(448, 125)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                    self.not_found("codcaixa")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "cadeiaprecoCI", matching=0.97, waiting_time=10000):
                    self.not_found("cadeiaprecoCI")
                self.click_relative(451, 165)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "cod00001testeparadouble", matching=0.97, waiting_time=10000):
                    self.not_found("cod00001testeparadouble")
                self.click()         
                self.wait(1000)  
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "picontas97CI", matching=0.97, waiting_time=10000):
                    self.not_found("picontas97CI")
                self.click_relative(452, 206)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "cod110103001planocontas", matching=0.97, waiting_time=10000):
                    self.not_found("cod110103001planocontas")
                self.click()       
                self.wait(1000)    
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "subgrupoci", matching=0.97, waiting_time=10000):
                    self.not_found("subgrupoci")
                self.click_relative(851, 43)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "subtipoci", matching=0.97, waiting_time=10000):
                    self.not_found("subtipoci")
                self.click_relative(850, 84)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "unidadeetiquetaCI", matching=0.97, waiting_time=10000):
                    self.not_found("unidadeetiquetaCI")
                self.click_relative(850, 124)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                    self.not_found("codcaixa")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "grupofiscalCI", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscalCI")
                self.click_relative(850, 167)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "picontas80CI", matching=0.97, waiting_time=10000):
                    self.not_found("picontas80CI")
                self.click_relative(851, 204)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "cod110103001planocontas", matching=0.97, waiting_time=10000):
                    self.not_found("cod110103001planocontas")
                self.click()   
                self.wait(1000)        
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                self.wait(500)
                self.tab()
                self.tab()
                if not self.find( "moldesCI", matching=0.97, waiting_time=10000):
                    self.not_found("moldesCI")
                self.click_relative(50, 246)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(1000)
                if not self.find( "ncmCI", matching=0.97, waiting_time=10000):
                    self.not_found("ncmCI")
                self.click_relative(503, 241)
                self.wait(1000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                self.wait(500)
                self.tab()
                self.type_keys_with_interval(1,'t1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                
                                ####---A1P1 MARCADORES---####
                
                if not self.find( "materiaprimaci", matching=0.97, waiting_time=10000):
                    self.not_found("materiaprimaci")
                self.click_relative(14, 27)
                self.space()
                self.tab()
                self.space()
                self.space()
                x=0
                while x<14:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                #self.tab()
                self.type_keys_with_interval(1,'87487487487487')
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1    
                
                                ####---ABA1 P2---####
                self.wait(1500)
                if not bot.find( "fatu_cad_itens_5_comissionamento", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_5_comissionamento")
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
                
                self.wait(1500)
                                ####---ABA1 P3---####
                                
                if not self.find( "a1p3CI", matching=0.97, waiting_time=10000):
                    self.not_found("a1p3CI")
                self.click()
                # if not self.find( "a1p3.2CI", matching=0.97, waiting_time=10000):
                #     self.not_found("a1p3.2CI")
                # self.click()
                # if not self.find( "a1p3.3CI", matching=0.97, waiting_time=10000):
                #     self.not_found("a1p3.3CI")
                # self.click()
                if not bot.find( "fatu_cad_itens_7_quantidades", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_7_quantidades")
                bot.click()
                
                self.wait(1500)

                if not bot.find( "fatu_cad_itens_estoque_possui_lote", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_estoque_possui_lote")
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
                if not bot.find( "fatu_cad_itens_7_lotes", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_7_lotes")
                bot.click()
                # if not self.find( "a1p4.1CInovo", matching=0.97, waiting_time=10000):
                #     self.not_found("a1p4.1CInovo")
                # self.click()
                # if not self.find( "a1p4.1CInovo", matching=0.97, waiting_time=10000):
                #     self.not_found("a1p4.1CInovo")
                # self.click_relative(29, 73)
                
                
                                ####---A1 P5---####
                                
                if not self.find( "a1p5CI", matching=0.97, waiting_time=10000):
                    self.not_found("a1p5CI")
                self.click()
                if not self.find( "embalagemCI", matching=0.97, waiting_time=10000):
                    self.not_found("embalagemCI")
                self.click_relative(8, 45)
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
                self.wait(500)
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
                
                self.wait(1500)
                                ####---ABA 2---####
                                            
                if not self.find( "aba2CI", matching=0.97, waiting_time=10000):
                    self.not_found("aba2CI")
                self.click()
                self.wait(1500)
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                self.enter()
                self.enter()
                #if not self.find( "salvar", matching=0.97, waiting_time=10000):
                #    self.not_found("salvar")
                #self.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                self.wait(1500)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "commit_registro_a2p2_CI", matching=0.97, waiting_time=10000):
                    self.not_found("commit_registro_a2p2_CI")
                self.click_relative(16, 184)
                
                if not self.find( "excluir_a2p1_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluir_a2p1_CI")
                self.click_relative(15, 162)
                
                self.enter()
                
                
                
                                ####---ABA2 P2---####
                                
                if not bot.find( "fatu_cad_itens_5_similares", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_5_similares")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                    self.not_found("procuraritensCI")
                self.click_relative(10, 34)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(4000)
                self.type_keys_with_interval(1,'104455')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.type_keys_with_interval(1,'1')
                if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                    self.not_found("confirmaritemCIaba2p2")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroa2p2.1_CI")
                self.click_relative(17, 163)           
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "aba2p2.2CI", matching=0.97, waiting_time=10000):
                    self.not_found("aba2p2.2CI")
                self.click()
                
                                ####---ABA2 P3---####
                
                if not bot.find( "fatu_cad_itens_6_agregados", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_6_agregados")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                    self.not_found("procuraritensCI")
                self.click_relative(10, 34)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(4000)
                self.type_keys_with_interval(1,'104455')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.type_keys_with_interval(1,'1')
                if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                    self.not_found("confirmaritemCIaba2p2")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroa2p2.1_CI")
                self.click_relative(17, 163)
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                self.wait(1500)
                
                                ####---ABA2 P4---####                             
                
                if not bot.find( "fatu_cad_itens_7_composicao", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_7_composicao")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                    self.not_found("procuraritensCI")
                self.click_relative(10, 34)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(4000)
                self.type_keys_with_interval(1,'104455')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.type_keys_with_interval(1,'1')
                if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                    self.not_found("confirmaritemCIaba2p2")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "excluirregistroa2p4_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroa2p4_CI")
                self.click_relative(16, 187)
                        
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                self.wait(2000)
                
                if not bot.find( "fatu_cad_itens_servicos_os", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_servicos_os")
                bot.click()
                self.wait(1000)
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3) 
                self.wait(5000)
                if not bot.find( "fatu_cad_itens_botao_buscar_servicos", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_botao_buscar_servicos")
                bot.click_relative(-155, 71)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
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
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "a2p4.3CI", matching=0.97, waiting_time=10000):
                    self.not_found("a2p4.3CI")
                self.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3) 
                self.wait(4000)
                if not bot.find( "fatu_cad_itens_rel_buscar_etapa_serv", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_rel_buscar_etapa_serv")
                bot.click_relative(-158, 71)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                if not self.find( "cancelara2p4.3CI", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara2p4.3CI")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                self.wait(2000)
                                ####---ABA2 P5---####
                                
                if not bot.find( "fatu_cad_itens_8_referencias_adicionais", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_8_referencias_adicionais")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not bot.find( "fatu_cad_itens_8_referencias_fornecedor_cliente", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_8_referencias_fornecedor_cliente")
                bot.click_relative(-228, 49)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')           
                if not bot.find( "fatu_cad_itens_btn_unidade_referencia", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_btn_unidade_referencia")
                bot.click_relative(60, 24)
                self.tab()
                self.wait(200)
                self.tab()
                self.wait(200)
                self.type_down()                 
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
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
                
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                self.wait(2000)
                                ####---ABA2 P6---####
                                    
                if not bot.find( "fatu_cad_itens_9_precos_pauta", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_9_precos_pauta")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not bot.find( "fatu_cad_9_precos_rel_tabela", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_9_precos_rel_tabela")
                bot.click_relative(-368, 77)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
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
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not bot.find( "fatu_cad_9_precos_pauta_rel_estado", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_9_precos_pauta_rel_estado")
                bot.click_relative(-367, 73)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
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
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                
                                ####---ABA2 P7---####
                                
                if not self.find( "a2p7CI", matching=0.97, waiting_time=10000):
                    self.not_found("a2p7CI")
                self.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not bot.find( "fatu_cad_unidade_adicional_rel_0", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_unidade_adicional_rel_0")
                bot.click_relative(37, 25)
                if not self.find( "codcxunidadea2p7ci", matching=0.97, waiting_time=10000):
                    self.not_found("codcxunidadea2p7ci")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
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
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                                #####################
                                ####---ABA2 P8---####
                                #####################
                self.wait(2000)
                if not bot.find( "fatu_cad_itens_aba_fotos", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_aba_fotos")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
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
                                
                if not bot.find( "fatu_cad_codigo_de_barras_adicionais", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_codigo_de_barras_adicionais")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                self.type_keys_with_interval(1,'12312312312312')
                self.tab()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click() 
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.enter()
                if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroa2p2.1_CI")
                self.click_relative(17, 163)
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                                ####---ABA2 P10---####
                

                self.wait(2000)     
                if not bot.find( "fatu_cad_itens_enderecos_estoque", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_enderecos_estoque")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                if not bot.find( "fatu_endereco_estoque_rel_estoque", matching=0.97, waiting_time=10000):
                    not_found("fatu_endereco_estoque_rel_estoque")
                bot.click_relative(-702, 45)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                self.enter()             
                
                                ####---ABA2 P11---####
                self.wait(2000)

                if not bot.find( "fatu_cad_itens_aba_clientes", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_aba_clientes")
                bot.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)           
                if not bot.find( "fatu_cad_cliente_relativo_buscar_itens", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cliente_relativo_buscar_itens")
                bot.click_relative(68, 26)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.enter()
                if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroa2p2.1_CI")
                self.click_relative(17, 163)
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                                
                                ####---ABA2 P12---####
                                
                if not self.find( "a2p12CI", matching=0.97, waiting_time=10000):
                    self.not_found("a2p12CI")
                self.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
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
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                
                                ####---A2 P13---####
                                
                if not self.find( "a2p13ci", matching=0.97, waiting_time=10000):
                    self.not_found("a2p13ci")
                self.click()
                if not bot.find( "fatu_cad_itens_2_rel_4_forn_incluir", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_2_rel_4_forn_incluir")
                bot.click_relative(-20, 3)
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(1500)
                                                
                                                                    
                                ####---ABA 3---####
                                ##### 3CARDEX #####
                self.wait(2000)
                if not bot.find( "fatu_cad_itens_3_cardex", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_3_cardex")
                bot.click()
                if not bot.find( "fatu_cad_3_cardex_documento_rel", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_3_cardex_documento_rel")
                bot.click_relative(16, 26)
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
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
                if not bot.find( "fatu_cad_itens_local_estoque_rel_bsc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_local_estoque_rel_bsc")
                bot.click_relative(77, 24)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_cad_itens_consulta_btn_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_itens_consulta_btn_retornar")
                bot.click_relative(26, 37)
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
                
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarcodte12!@CI", matching=0.97, waiting_time=10000):
                    self.not_found("localizarcodte12!@CI")
                self.click_relative(4, 33)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                

                self.wait(2000)
                                ####---FORMULAS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "deixarpadrão", matching=0.97, waiting_time=10000):
                    self.not_found("deixarpadrão")
                self.click()
                self.click()
                if not self.find( "cancelarformula", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarformula")
                self.click()   
                self.enter()        
                #if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
                #    self.not_found("simabandonar")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                    self.not_found("okformulas")
                self.click()
                if not self.find( "cancelarformula", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarformula")
                self.click()  
                self.enter()  
                #if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
                #    self.not_found("simabandonar")
                #self.click()
                if not self.find( "consultaform", matching=0.97, waiting_time=10000):
                    self.not_found("consultaform")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---LOCAL DE ESTOQUE---####
                self.wait(2000)

                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                if not self.find( "localdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("localdeestoque")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_down()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---DESCONTO POR AGRUPAMENTO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                if not self.find( "descontoporagrupamento", matching=0.97, waiting_time=10000):
                    self.not_found("descontoporagrupamento")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                    self.not_found("okformulas")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                    self.not_found("okformulas")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                self.wait(2000)
                                ####---TIPO DO ITEM/CONTA CONTABIL---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itensdeestoque")
                self.click()
                if not self.find( "tipodoitemcontacontabil", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoitemcontacontabil")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                x=0
                while x<12:
                    self.type_down()
                    x=x+1
                if not self.find( "contagrupocontabilentrada", matching=0.97, waiting_time=10000):
                    self.not_found("contagrupocontabilentrada")
                self.click_relative(515, 6)
                self.type_down()
                self.enter()
                if not self.find( "saidaspedcitc", matching=0.97, waiting_time=10000):
                    self.not_found("saidaspedcitc")
                self.click_relative(389, 7)
                self.type_down()
                self.enter()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()    
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                """
                                ####---SERVIÇOS---####
                self.wait(2000)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                        self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "servicos", matching=0.97, waiting_time=10000):
                    self.not_found("servicos")
                self.click()
                self.wait(2000)
                y=0                
                while y<2:
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                        not_found("fatu_btn_incluir_opc_1_2411")
                    bot.click()
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=0
                    while x<7:
                        self.type_down()
                        x=x+1
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    self.type_keys_with_interval(1,'t1!')
                    self.tab()
                    self.tab()
                    self.space()
                    self.space()
                    self.tab()
                    if not self.find( "codigostributacoes", matching=0.97, waiting_time=10000):
                        self.not_found("codigostributacoes")
                    self.click_relative(550, 50)
                    x=0
                    while x<5:
                        self.type_down()
                        x=x+1
                    self.enter()
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    x=0
                    while x<31:
                        self.type_down()
                        x=x+1
                    self.tab()
                    x=0
                    while x<100:
                        self.type_down()
                        x=x+1
                    self.tab()
                    if not self.find( "unidadeCS", matching=0.97, waiting_time=10000):
                        self.not_found("unidadeCS")
                    self.click_relative(57, 47)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "grupoCS", matching=0.97, waiting_time=10000):
                        self.not_found("grupoCS")
                    self.click_relative(59, 93)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "planodecontasCS", matching=0.97, waiting_time=10000):
                        self.not_found("planodecontasCS")
                    self.click_relative(59, 138)
                    self.wait(1000)
                    self.type_keys_with_interval(100,"00005")
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "grupofiscalCS", matching=0.97, waiting_time=10000):
                        self.not_found("grupofiscalCS")
                    self.click_relative(436, 47)
                    if not self.find( "cod006fiCS", matching=0.97, waiting_time=10000):
                        self.not_found("cod006fiCS")
                    self.click()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(500)
                    if not self.find( "subgrupoCS", matching=0.97, waiting_time=10000):
                        self.not_found("subgrupoCS")
                    self.click_relative(439, 90)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "ncmCS", matching=0.97, waiting_time=10000):
                        self.not_found("ncmCS")
                    self.click_relative(490, 138)
                    self.type_keys_with_interval(100,"01011100")
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "familiaCS", matching=0.97, waiting_time=10000):
                        self.not_found("familiaCS")
                    self.click_relative(820, 46)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "marcaCS", matching=0.97, waiting_time=10000):
                        self.not_found("marcaCS")
                    self.click_relative(818, 94)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(1000)
                    if not self.find( "centrocustoCS", matching=0.97, waiting_time=10000):
                        self.not_found("centrocustoCS")
                    self.click_relative(846, 141)
                    if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                        self.not_found("localizarfim")
                    self.click()
                    self.type_down()
                    if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                        self.not_found("selecionarmunicipiovcr")
                    self.click()
                    self.wait(2000)
                    
                    
                                    ####---ABA2 CS---####
                    self.wait(2000)

                    if not self.find( "aba2CS", matching=0.97, waiting_time=10000):
                        self.not_found("aba2CS")
                    self.click()
                    if not bot.find( "fatu_cad_btn_achar_data_servicos", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_btn_achar_data_servicos")
                    bot.click_relative(31, 10)
                    if not self.find( "carregaranoCS", matching=0.97, waiting_time=10000):
                        self.not_found("carregaranoCS")
                    self.click()
                    if not self.find( "selecionaranoatualCS", matching=0.97, waiting_time=10000):
                        self.not_found("selecionaranoatualCS")
                    self.click()
                    if not self.find( "consultarcardexCS", matching=0.97, waiting_time=10000):
                        self.not_found("consultarcardexCS")
                    self.click()
                    
                                    ####---ABA3 PRECOS---####
                    
                    if not self.find( "aba3precosCS", matching=0.97, waiting_time=10000):
                        self.not_found("aba3precosCS")
                    self.click()
                    if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                        self.not_found("salvarenquete")
                    self.click()
                    self.wait(1000)    
                    if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                        self.not_found("retornarpe")
                    self.click()
                    y=y+2
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                


                                ####---CADASTROS AUXILIARES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrosauxiliares")
                self.click()
                if not self.find( "fasesdeproducao", matching=0.97, waiting_time=10000):
                    self.not_found("fasesdeproducao")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()    
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrosauxiliares")
                self.click()
                if not self.find( "statusCA", matching=0.97, waiting_time=10000):
                    self.not_found("statusCA")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.space()
                self.type_down()
                self.type_down()
                self.space()
                x=0
                while x<8:
                    self.type_down()
                    self.space()
                    x=x+1
                x=0
                while x<9:
                    self.space()
                    self.type_up() 
                    x=x+1
                self.tab()
                if not self.find( "fechamentosituacaostatus", matching=0.97, waiting_time=10000):
                    self.not_found("fechamentosituacaostatus")
                self.click()
                if not self.find( "situacaoproduzirstatus", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoproduzirstatus")
                self.click()
                if not self.find( "situacaoemproducaostatus", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoemproducaostatus")
                self.click()
                if not self.find( "situacaocancelamentostatus", matching=0.97, waiting_time=10000):
                    self.not_found("situacaocancelamentostatus")
                self.click()
                if not self.find( "estoquereservarstatus", matching=0.97, waiting_time=10000):
                    self.not_found("estoquereservarstatus")
                self.click()
                if not self.find( "reservarnaoreservarstatus", matching=0.97, waiting_time=10000):
                    self.not_found("reservarnaoreservarstatus")
                self.click()
                if not self.find( "situacaoaberturastatus", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoaberturastatus")
                self.click()
                if not self.find( "reservaseminfluenciastatus", matching=0.97, waiting_time=10000):
                    self.not_found("reservaseminfluenciastatus")
                self.click()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                    self.not_found("codte12Cstatus")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrosauxiliares")
                self.click()
                if not self.find( "motivosdequebraCaux", matching=0.97, waiting_time=10000):
                    self.not_found("motivosdequebraCaux")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                    self.not_found("codte12Cstatus")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrosauxiliares")
                self.click()
                if not self.find( "moldesCaux", matching=0.97, waiting_time=10000):
                    self.not_found("moldesCaux")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_up()
                self.type_up()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "fornecedormoldes", matching=0.97, waiting_time=10000):
                    self.not_found("fornecedormoldes")
                self.click_relative(128, 4)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                x=0
                while x<3:
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                    self.not_found("codte12Cstatus")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---PLANO DE CONTAS, CUSTOS E FINANCEIRO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                    self.not_found("planodecontas,custos,financeiro")
                self.click()
                if not self.find( "planodecustos", matching=0.97, waiting_time=10000):
                    self.not_found("planodecustos")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()                 
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "inserirnumeracaoPC", matching=0.97, waiting_time=10000):
                    self.not_found("inserirnumeracaoPC")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                    self.not_found("codte12Cstatus")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                    self.not_found("planodecontas,custos,financeiro")
                self.click()
                if not self.find( "planofinanceiroC", matching=0.97, waiting_time=10000):
                    self.not_found("planofinanceiroC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()                 
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "inserirnumeracaoPC", matching=0.97, waiting_time=10000):
                    self.not_found("inserirnumeracaoPC")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                    self.not_found("codte12Cstatus")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                    self.not_found("planodecontas,custos,financeiro")
                self.click()
                if not self.find( "planocontabilC", matching=0.97, waiting_time=10000):
                    self.not_found("planocontabilC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()                 
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'13')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                if not self.find( "inativasimpc", matching=0.97, waiting_time=10000):
                    self.not_found("inativasimpc")
                self.click()
                if not self.find( "inativanaoPC", matching=0.97, waiting_time=10000):
                    self.not_found("inativanaoPC")
                self.click()
                if not self.find( "centrodecustoinicialPC", matching=0.97, waiting_time=10000):
                    self.not_found("centrodecustoinicialPC")
                self.click_relative(143, 18)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.wait(500)
                #if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
                #    self.not_found("okerronaoencontrado")
                #self.click()
                self.backspace()
                self.wait(500)
                if not self.find( "centrodecustofinalPC", matching=0.97, waiting_time=10000):
                    self.not_found("centrodecustofinalPC")
                self.click_relative(142, 40)
                self.enter()
                self.backspace()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.enter()
                #if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
                #    self.not_found("okerronaoencontrado")
                #self.click()
                self.backspace()
                if not self.find( "grupodeempresaPC", matching=0.97, waiting_time=10000):
                    self.not_found("grupodeempresaPC")
                self.click_relative(44, 31)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click() 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "sairsistemapa", matching=0.97, waiting_time=10000):
                    self.not_found("sairsistemapa")
                self.click()
                if not self.find( "simsairsistemapa", matching=0.97, waiting_time=10000):
                    self.not_found("simsairsistemapa")
                self.click()
                #self.enter()
                            
                        #SESSÃO PÁGINA 6 (Parte 3 Cadastros 14284 - 16783)

                    #######################-----LOGIN-----############################
            
                #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
                self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
                
                if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=100000):
                    self.not_found("btn_codigo_usuario")
                self.click_relative(47, 12)
                        
                self.type_keys_with_interval(1,"999")
                self.wait(500)
                self.type_keys_with_interval(1,"tsfmx24")

                self.enter()

                if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                    self.not_found("btn_login")
                self.click()
                self.enter()

                ###################################################################
                self.wait(2000)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "classificacoes", matching=0.97, waiting_time=10000):
                    self.not_found("classificacoes")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(5000)            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                self.wait(5000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_down()
                self.type_up()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CONDICAO PAGAMENTO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "condicoesdepagamento", matching=0.97, waiting_time=10000):
                    self.not_found("condicoesdepagamento")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
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
                while x<5:
                    self.tab()
                    self.type_keys_with_interval(1,'123')
                    x=x+1
                if not self.find( "somenteavistadesconto", matching=0.97, waiting_time=10000):
                    self.not_found("somenteavistadesconto")
                self.click()
                if not self.find( "permitirsempredesconto", matching=0.97, waiting_time=10000):
                    self.not_found("permitirsempredesconto")
                self.click()
                if not self.find( "naopermitedesconto", matching=0.97, waiting_time=10000):
                    self.not_found("naopermitedesconto")
                self.click()
                self.tab()
                self.type_keys_with_interval(1,'123')
                x=0
                while x<2:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_up()
                self.tab()
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                x=0
                while x<3:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_up()
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
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
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
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
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---COMISSOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "comissoesC", matching=0.97, waiting_time=10000):
                    self.not_found("comissoesC")
                self.click()
                if not self.find( "comissoesCOMC", matching=0.97, waiting_time=10000):
                    self.not_found("comissoesCOMC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "comissoesC", matching=0.97, waiting_time=10000):
                    self.not_found("comissoesC")
                self.click()
                if not self.find( "fatoresdecomissoesC", matching=0.97, waiting_time=10000):
                    self.not_found("fatoresdecomissoesC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "addregistrofaixas", matching=0.97, waiting_time=10000):
                    self.not_found("addregistrofaixas")
                self.click_relative(8, 32)
                x=0
                while x<3:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                if not self.find( "gravarnovoregistro", matching=0.97, waiting_time=10000):
                    self.not_found("gravarnovoregistro")
                self.click()
                if not self.find( "excluirfaixa", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfaixa")
                self.click_relative(12, 54)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---FUNCOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "funcoesC", matching=0.97, waiting_time=10000):
                    self.not_found("funcoesC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                x=0
                while x<6:
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    x=x+1
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---BANCOS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "bancosC", matching=0.97, waiting_time=10000):
                    self.not_found("bancosC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'8748')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CONTAS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "contasC", matching=0.97, waiting_time=10000):
                    self.not_found("contasC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                if not self.find( "ccbancaria", matching=0.97, waiting_time=10000):
                    self.not_found("ccbancaria")
                self.click()
                if not self.find( "cclientesfornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("cclientesfornecedores")
                self.click()
                if not self.find( "numerarioemtransito", matching=0.97, waiting_time=10000):
                    self.not_found("numerarioemtransito")
                self.click()
                #if not self.find( "bancoCC", matching=0.97, waiting_time=10000):
                #    self.not_found("bancoCC")
                #self.click_relative(453, 47)
                if not self.find( "b_banco_CConta", matching=0.97, waiting_time=10000):
                    self.not_found("b_banco_CConta")
                self.click_relative(455, 167)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                #if not self.find( "codigocontabilcontaCC", matching=0.97, waiting_time=10000):
                #   self.not_found("codigocontabilcontaCC")
                #self.click_relative(865, 47)
                if not self.find( "b_codigoContabilConta_CConta", matching=0.97, waiting_time=10000):
                    self.not_found("b_codigoContabilConta_CConta")
                self.click_relative(871, 170)
                if not self.find( "cod00245pcCC", matching=0.97, waiting_time=10000):
                    self.not_found("cod00245pcCC")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                #if not self.find( "empresaCC", matching=0.97, waiting_time=10000):
                #    self.not_found("empresaCC")
                #self.click_relative(49, 95)
                if not self.find( "b_empresa_CContas", matching=0.97, waiting_time=10000):
                    self.not_found("b_empresa_CContas")
                self.click_relative(56, 217)
                self.backspace()
                self.enter()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.tab()
                self.type_keys_with_interval(1,'t')
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---LOCAIS DE COBRANCA---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "locaisdecobranca", matching=0.97, waiting_time=10000):
                    self.not_found("locaisdecobranca")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MOEDAS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "moedasC", matching=0.97, waiting_time=10000):
                    self.not_found("moedasC")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                x=0
                while x<2:
                    self.type_down()
                    x=x+1
                x=0
                while x<2:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<12:
                    self.type_down()
                    x=x+1
                x=0
                while x<12:
                    self.type_up()
                    x=x+1
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "addcotacaodiaria", matching=0.97, waiting_time=10000):
                    self.not_found("addcotacaodiaria")
                self.click_relative(10, 32)
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.enter()
                if not self.find( "excluircotacaodiaria", matching=0.97, waiting_time=10000):
                    self.not_found("excluircotacaodiaria")
                self.click_relative(10, 55)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---TIPOS DE PAGAMENTO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "tiposdepagamento", matching=0.97, waiting_time=10000):
                    self.not_found("tiposdepagamento")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                x=0
                while x<11:
                    self.type_down()
                    x=x+1
                x=0
                while x<9:
                    self.type_up()
                    x=x+1    
                self.tab()
                x=0
                while x<15:
                    self.type_down()
                    x=x+1
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                if not self.find( "agrupamentocontaTP", matching=0.97, waiting_time=10000):
                    self.not_found("agrupamentocontaTP")
                self.click_relative(55, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "agrupamentooperacaoTP", matching=0.97, waiting_time=10000):
                    self.not_found("agrupamentooperacaoTP")
                self.click_relative(475, 42)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "admcartaoplanofinanceiroTP", matching=0.97, waiting_time=10000):
                    self.not_found("admcartaoplanofinanceiroTP")
                self.click_relative(86, 39)
                self.backspace()
                self.enter()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "admclientecartaoTP", matching=0.97, waiting_time=10000):
                    self.not_found("admclientecartaoTP")
                self.click_relative(70, 85)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "tipopagamentoTP", matching=0.97, waiting_time=10000):
                    self.not_found("tipopagamentoTP")
                self.click_relative(539, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'99')
                self.tab()
                self.tab()
                self.tab()
                self.type_up()
                self.type_up()
                self.type_down()
                self.tab()
                x=0
                while x<7:
                    self.type_up()
                    x=x+1
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---TABELA DE IMPOSTOS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "tabeladeimpostos", matching=0.97, waiting_time=10000):
                    self.not_found("tabeladeimpostos")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                x=0
                while x<4:
                    self.tab()
                    x=x+1
                x=0
                while x<65:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                self.space()
                self.space()
                self.space()
                x=0
                while x<4:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                self.type_up()
                self.type_up()
                self.type_down()
                if not self.find( "dsrexpoagentenocivo", matching=0.97, waiting_time=10000):
                    self.not_found("dsrexpoagentenocivo")
                self.click()
                x=0
                while x<30:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                x=0
                p=24
                if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01completo")
                self.click_relative(8, p)
                if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                    self.not_found("dia01metade")
                self.click_relative(85, p)
                if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01nulo")
                self.click_relative(167, p)
                while x<14:                
                    y=p+30
                    if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                        self.not_found("dia01completo")
                    self.click_relative(8, y)
                    if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                        self.not_found("dia01metade")
                    self.click_relative(85, y)
                    if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                        self.not_found("dia01nulo")
                    self.click_relative(167, y)
                    p=p+30
                    x=x+1
                if not self.find( "abaixartelatabelas", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelatabelas")
                self.click()
                x=0
                while x<2:
                    if not self.find( "abaixartelatabelas2", matching=0.97, waiting_time=10000):
                        self.not_found("abaixartelatabelas2")
                    self.double_click()
                    x=x+1
                if not self.find( "dia16completo", matching=0.97, waiting_time=10000):
                    self.not_found("dia16completo")
                self.click_relative(-175, -35)
                if not self.find( "dia16metade", matching=0.97, waiting_time=10000):
                    self.not_found("dia16metade")
                self.click_relative(-96, -35)
                if not self.find( "dia16nulo", matching=0.97, waiting_time=10000):
                    self.not_found("dia16nulo")
                self.click_relative(-18, -35)            
                if not self.find( "subirtelatabela", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelatabela")
                self.click()
                x=0
                while x<2:
                    if not self.find( "subirtelatabela2", matching=0.97, waiting_time=10000):
                        self.not_found("subirtelatabela2")
                    self.double_click()
                    x=x+1
                if not self.find( "subirtelatabela2", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelatabela2")
                self.click()    
                x=0
                p=24
                if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01completo")
                self.click_relative(260, p)
                if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                    self.not_found("dia01metade")
                self.click_relative(338, p)
                if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01nulo")
                self.click_relative(417, p)
                while x<14:                
                    y=p+30
                    if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                        self.not_found("dia01completo")
                    self.click_relative(260, y)
                    if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                        self.not_found("dia01metade")
                    self.click_relative(338, y)
                    if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                        self.not_found("dia01nulo")
                    self.click_relative(417, y)
                    p=p+30
                    x=x+1
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CATEGORIAS DE CAMPANHA---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "categoriasdecampanhas", matching=0.97, waiting_time=10000):
                    self.not_found("categoriasdecampanhas")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---AUTORIZADORES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "autorizadores", matching=0.97, waiting_time=10000):
                    self.not_found("autorizadores")
                self.click()
                if not self.find( "okparametronaodefinido", matching=0.97, waiting_time=10000):
                    self.not_found("okparametronaodefinido")
                self.click()
                
                                ####---CONFIGURACOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                    self.not_found("configuracoes")
                self.click()
                if not self.find( "configuracoesdeformularios", matching=0.97, waiting_time=10000):
                    self.not_found("configuracoesdeformularios")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=0
                while x<9:
                    self.type_down()
                    x=x+1
                if not self.find( "LPPsexto", matching=0.97, waiting_time=10000):
                    self.not_found("LPPsexto")
                self.click_relative(8, 31)
                if not self.find( "LPPoitavos", matching=0.97, waiting_time=10000):
                    self.not_found("LPPoitavos")
                self.click_relative(76, 30)
                if not self.find( "CPP1296", matching=0.97, waiting_time=10000):
                    self.not_found("CPP1296")
                self.click_relative(8, 38)
                if not self.find( "CPP17136", matching=0.97, waiting_time=10000):
                    self.not_found("CPP17136")
                self.click_relative(118, 23)
                if not self.find( "CPP20160", matching=0.97, waiting_time=10000):
                    self.not_found("CPP20160")
                self.click_relative(119, 36)
                if not self.find( "CPP1080", matching=0.97, waiting_time=10000):
                    self.not_found("CPP1080")
                self.click_relative(8, 23)
                if not self.find( "alturalarguramm", matching=0.97, waiting_time=10000):
                    self.not_found("alturalarguramm")
                self.click_relative(22, 26)
                self.backspace()
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "aba2camposFormularios", matching=0.97, waiting_time=10000):
                    self.not_found("aba2camposFormularios")
                self.click()
                if not self.find( "addregistroaba2campos", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2campos")
                self.click_relative(-44, 36)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()                 
                x=0
                while x<23:
                    self.type_down()
                    x=x+1
                self.tab()    
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=0
                while x<16:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_up()
                self.type_down()
                self.type_down()
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1    
                self.tab()
                self.type_down()
                self.type_down()
                self.tab()
                x=0
                while x<16:
                    self.type_down()
                    x=x+1
                x=0
                while x<4:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                self.tab()
                self.enter()
                if not self.find( "excluiraba2campos", matching=0.97, waiting_time=10000):
                    self.not_found("excluiraba2campos")
                self.click_relative(-45, 156)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                if not self.find( "aba3listaformularios", matching=0.97, waiting_time=10000):
                    self.not_found("aba3listaformularios")
                self.click()
                if not self.find( "aba4copiarconfigforms", matching=0.97, waiting_time=10000):
                    self.not_found("aba4copiarconfigforms")
                self.click()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.enter()
                self.enter()
                self.enter()
                if not self.find( "aba5ajustesforms", matching=0.97, waiting_time=10000):
                    self.not_found("aba5ajustesforms")
                self.click()
                x=0
                while x<4:
                    self.type_down()
                    self.enter()
                    self.enter()
                    self.type_up()
                    self.type_up()
                    self.tab()
                    x=x+1
                self.enter()
                self.enter()
                self.enter()
                self.wait(500)
                self.enter()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(500)
                if not self.find( "cancelarformulariosagrvai", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarformulariosagrvai")
                self.click()
                
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                self.enter()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---IMPRESSORA DE CODIGO DE BARRAS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                    self.not_found("configuracoes")
                self.click()
                if not self.find( "impressoradecodigodebarras", matching=0.97, waiting_time=10000):
                    self.not_found("impressoradecodigodebarras")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=0
                while x<10:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "aba2impressoratermica", matching=0.97, waiting_time=10000):
                    self.not_found("aba2impressoratermica")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CONFIG IMPORTACAO EMPORIUM---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                    self.not_found("configuracoes")
                self.click()
                if not self.find( "configimpoemporium", matching=0.97, waiting_time=10000):
                    self.not_found("configimpoemporium")
                self.click()
                if not self.find( "buscarclientecofigemporium", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclientecofigemporium")
                self.click_relative(157, 82)
                self.enter()
                if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260selecaocliente")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "opentradabuscar", matching=0.97, waiting_time=10000):
                    self.not_found("opentradabuscar")
                self.click_relative(151, 2)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "operacaosaidaimpemporium", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosaidaimpemporium")
                self.click_relative(139, 3)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "ecfimpemporium", matching=0.97, waiting_time=10000):
                    self.not_found("ecfimpemporium")
                self.click_relative(81, 2)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'t1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.tab()
                self.space()
                self.space()
                self.tab()
                if not self.find( "cnddepagamentoimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("cnddepagamentoimpemp")
                self.click_relative(163, 0)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "tiporecpagtimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("tiporecpagtimpemp")
                self.click_relative(142, 2)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "itemimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("itemimpemp")
                self.click_relative(89, 3)
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "opvendascanceladasimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("opvendascanceladasimpemp")
                self.click_relative(208, 6)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "cfopimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("cfopimpemp")
                self.click_relative(95, 4)
                #if not self.find( "vendedorimpemp", matching=0.97, waiting_time=10000):
                #    self.not_found("vendedorimpemp")
                #self.click_relative(113, 4)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "tipoimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("tipoimpemp")
                self.click_relative(226, 36)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "empresaimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("empresaimpemp")
                self.click_relative(113, 57)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "clienteimpemptiposreceb", matching=0.97, waiting_time=10000):
                    self.not_found("clienteimpemptiposreceb")
                self.click_relative(113, 82)
                self.enter()
                if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260selecaocliente")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba2impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba2impemp")
                self.click()
                if not self.find( "buscarcontaimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcontaimpemp")
                self.click_relative(73, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba3bancosimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba3bancosimpemp")
                self.click()
                if not self.find( "buscarbancoimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarbancoimpemp")
                self.click_relative(157, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba4impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba4impemp")
                self.click()
                if not self.find( "buscarecfimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarecfimpemp")
                self.click_relative(109, 42)
                if not self.find( "aba5impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba5impemp")
                self.click()
                x=0
                while x<5:
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    x=x+1
                if not self.find( "aba6impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba6impemp")
                self.click()
                if not self.find( "buscarempresaaba6impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaaba6impemp")
                self.click_relative(-141, 49)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarempresaclienteaba6impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaclienteaba6impemp")
                self.click_relative(-138, 74)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarempresaitensaba6impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaitensaba6impemp")
                self.click_relative(-139, 96)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "aba7impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba7impemp")
                self.click()
                if not self.find( "buscarempresaaba7impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaaba7impemp")
                self.click_relative(-413, 36)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba8impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba8impemp")
                self.click()
                if not self.find( "buscarempresaaba8impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaaba8impemp")
                self.click_relative(-536, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba9impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba9impemp")
                self.click()
                if not self.find( "buscartabelaimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscartabelaimpemp")
                self.click_relative(-351, 40)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "aba10impemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba10impemp")
                self.click()
                if not self.find( "buscarempresaaba10impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaaba10impemp")
                self.click_relative(-736, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarvendedoraba10impemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarvendedoraba10impemp")
                self.click_relative(-211, 37)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "excluirimpemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirimpemp")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CONFIG EMP NOVO---####
                                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                    self.not_found("configuracoes")
                self.click()
                if not self.find( "configemporiumnovo", matching=0.97, waiting_time=10000):
                    self.not_found("configemporiumnovo")
                self.click()
                self.enter()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "buscarclienteconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclienteconfigemp")
                self.click_relative(73, 97)
                self.enter()
                if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260selecaocliente")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscaritemconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritemconfigemp")
                self.click_relative(71, 143)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarecfconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarecfconfigemp")
                self.click_relative(50, 186)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscacondpagconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscacondpagconfigemp")
                self.click_relative(468, 99)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarvendedorconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarvendedorconfigemp")
                self.click_relative(469, 143)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscatipopagamentoconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscatipopagamentoconfigemp")
                self.click_relative(872, 95)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarcfopconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcfopconfigemp")
                self.click_relative(871, 144)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'t1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.space()
                self.space()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)            
                if not self.find( "registpconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("registpconfigemp")
                self.click_relative(186, 270)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "regisempresaconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("regisempresaconfigemp")
                self.click_relative(576, 270)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "regisclienteconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("regisclienteconfigemp")
                self.click_relative(102, 314)
                self.enter()
                if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260selecaocliente")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA2
                if not self.find( "aba2regisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba2regisconfigemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregiscontaaba2cemp")
                self.click_relative(152, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA3
                if not self.find( "aba3configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba3configemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregiscontaaba2cemp")
                self.click_relative(152, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA4
                if not self.find( "aba4configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba4configemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregiscontaaba2cemp")
                self.click_relative(152, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA5
                if not self.find( "aba5configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba5configemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "buscaempresaaba5cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaempresaaba5cemp")
                self.click_relative(291, 268)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA6
                if not self.find( "aba6configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba6configemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "buscaempresaaba6configemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaempresaaba6configemp")
                self.click_relative(92, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA7
                if not self.find( "aba7regisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba7regisconfigemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregiscontaaba2cemp")
                self.click_relative(152, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA8
                if not self.find( "aba8configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba8configemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregiscontaaba2cemp")
                self.click_relative(152, 269)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscavendedoraba8configemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscavendedoraba8configemp")
                self.click_relative(545, 266)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA9
                if not self.find( "aba9regisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba9regisconfigemp")
                self.click()
                if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("addregisconfigemp")
                self.click_relative(10, 223)
                if not self.find( "buscaempresaaba9cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaempresaaba9cemp")
                self.click_relative(94, 290)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscaoperacaoaba9cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaoperacaoaba9cemp")
                self.click_relative(491, 294)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregistroconfigemp")
                self.click_relative(12, 266)
                if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                    self.not_found("excluirregisconfigemp")
                self.click_relative(12, 246)
                self.enter()
                #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfaixa")
                #self.click()
                
                #ABA10
                if not self.find( "aba10configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba10configemp")
                self.click()
                if not self.find( "balancaaba10configemp", matching=0.97, waiting_time=10000):
                    self.not_found("balancaaba10configemp")
                self.click_relative(-662, 52)
                x=0
                while x<5:
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    x=x+1
                
                #ABA11
                if not self.find( "aba11configemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba11configemp")
                self.click()
                if not self.find( "buscaempresaaba11cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaempresaaba11cemp")
                self.click_relative(90, 265)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscaCFaba11cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaCFaba11cemp")
                self.click_relative(489, 265)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscaitensaba11cemp", matching=0.97, waiting_time=10000):
                    self.not_found("buscaitensaba11cemp")
                self.click_relative(889, 266)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                #if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("excluirrs")
                #self.click()
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---PDV---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "pdv", matching=0.97, waiting_time=10000):
                    self.not_found("pdv")
                self.click()
                if not self.find( "terminais", matching=0.97, waiting_time=10000):
                    self.not_found("terminais")
                self.click()
                #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                #    self.not_found("localizarpaises")
                #self.click()            
                #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("editarfim")
                #self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_right()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MAPA FISCAL---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "pdv", matching=0.97, waiting_time=10000):
                    self.not_found("pdv")
                self.click()
                if not self.find( "mapafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("mapafiscal")
                self.click()
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'8748')
                self.tab()
                self.type_keys_with_interval(1,'8748')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_down()
                self.type_down()
                if not self.find( "empresareducaoZ", matching=0.97, waiting_time=10000):
                    self.not_found("empresareducaoZ")
                self.click_relative(59, 133)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x<31:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                if not self.find( "aba1reducaoZ", matching=0.97, waiting_time=10000):
                    self.not_found("aba1reducaoZ")
                self.click_relative(25, 165)            
                x=0
                while x<31:
                    self.backspace()
                    self.tab()
                    x=x+1
                    
                if not self.find( "cancelarreducaoZ", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarreducaoZ")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MOTIVOS DIVERSOS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "pdv", matching=0.97, waiting_time=10000):
                    self.not_found("pdv")
                self.click()
                if not self.find( "motivosdiversos", matching=0.97, waiting_time=10000):
                    self.not_found("motivosdiversos")
                self.click()
                #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                #    self.not_found("localizarpaises")
                #self.click()            
                #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("editarfim")
                #self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #   self.not_found("retornarpe")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CADASTRO DE ECF---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "pdv", matching=0.97, waiting_time=10000):
                    self.not_found("pdv")
                self.click()
                if not self.find( "cadastrodeecf", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrodeecf")
                self.click()
                #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                #    self.not_found("localizarpaises")
                #self.click()            
                #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("editarfim")
                #self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'8748')
                self.tab()
                x=0
                while x<7:
                    self.type_keys_with_interval(1,'te12!@')
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---DOCUMENTACOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                    self.not_found("documentacoes")
                self.click()
                if not self.find( "tiposdedocumentos", matching=0.97, waiting_time=10000):
                    self.not_found("tiposdedocumentos")
                self.click()
                #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                #    self.not_found("localizarpaises")
                #self.click()            
                #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("editarfim")
                #self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                    self.not_found("documentacoes")
                self.click()
                if not self.find( "documentos", matching=0.97, waiting_time=10000):
                    self.not_found("documentos")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "buscartipodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("buscartipodocumento")
                self.click_relative(152, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                if not self.find( "buscarclientefornecCadDoc", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclientefornecCadDoc")
                self.click_relative(197, 160)
                self.enter()
                if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260selecaocliente")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "buscararquivoCadDoc", matching=0.97, waiting_time=10000):
                    self.not_found("buscararquivoCadDoc")
                self.click_relative(630, 4)
                if not self.find( "abrirarquivoCadDoc", matching=0.97, waiting_time=10000):
                    self.not_found("abrirarquivoCadDoc")
                self.click_relative(599, 441)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                    self.not_found("documentacoes")
                self.click()
                if not self.find( "documentosreferenciados", matching=0.97, waiting_time=10000):
                    self.not_found("documentosreferenciados")
                self.click()
                #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                #    self.not_found("localizarpaises")
                #self.click()            
                #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #    self.not_found("editarfim")
                #self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                x=0
                while x<9:
                    self.type_down()
                    x=x+1
                if not self.find( "buscaobslancfiscal", matching=0.97, waiting_time=10000):
                    self.not_found("buscaobslancfiscal")
                self.click_relative(154, 24)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.type_down()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcodteteste")
                self.click_relative(12, 29)
                self.type_keys_with_interval(1,'15')
                self.enter()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(1000)
                if not self.find( "fecharsistemaparte3", matching=0.97, waiting_time=10000):
                    self.not_found("fecharsistemaparte3")
                self.click()           
                if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluircft1")
                self.click()
               

                

def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  