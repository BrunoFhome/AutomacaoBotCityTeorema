from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()




"""
CÓDIGO FEITO PARA SISTEMA CRM 24.07
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - SPINNER 0041284
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
                
                #SESSÃO PÁGINA 1 (Empresas 26 - 2424)
            #######################-----LOGIN-----############################
                
                #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
                """self.execute(r"C:\Teorema\bin\faturamento.exe")
                 
                if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=10000):
                    self.not_found("btn_codigo_usuario")
                self.click_relative(47, 12)
                        
                self.paste("002")
                self.wait(500)
                self.paste("1811")
                self.enter()

                if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                    self.not_found("btn_login")
                self.click()
                self.enter()    
                
                
                """
                #################-----CADASTRO DE EMPRESAS-----####################
                
                #################-----TESTE INCLUIR/EDITAR-----####################
                self.wait(1500)
                if not bot.find( "fatu_btn_cadastros_menu", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_cadastros_menu")
                self.click()
                self.wait(1000)
                
                if not bot.find( "fatu_cadastros_empresas_menu", matching=0.97, waiting_time=10000):
                    not_found("fatu_cadastros_empresas_menu")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cadastros_empresas_menu", matching=0.97, waiting_time=10000):
                    not_found("fatu_cadastros_empresas_menu")
                bot.click()
                
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_right()
                self.enter()
                
                ####################-----CADASTRO ABA 1-----#######################
                
                self.wait(1500)
                if not self.find( "cadastro_empresa_nome2", matching=0.97, waiting_time=10000):
                    self.not_found("cadastro_empresa_nome2")
                self.click_relative(232, 89)
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<3:
                    if not self.find( "empresa_ident1", matching=0.97, waiting_time=10000):
                        self.not_found("empresa_ident1")
                    self.click_relative(37, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "empresa_cpf1", matching=0.97, waiting_time=10000):
                    self.not_found("empresa_cpf1")
                self.click_relative(41, 25)
                self.type_keys_with_interval(1,'08658033902')
                if not self.find( "empresa_rg1", matching=0.97, waiting_time=10000):
                    self.not_found("empresa_rg1")
                self.click_relative(-5, 26)
                self.type_keys_with_interval(1,'147345348')
                if not self.find( "ativo", matching=0.97, waiting_time=10000):
                    self.not_found("ativo")
                self.click()
                if not self.find( "inativo", matching=0.97, waiting_time=10000):
                    self.not_found("inativo")
                self.click()
                
                self.type_up()
                
                                ###---ABA 1 PRINCIPAL---###
                                ####---DADOS DA EMPRESA---####
                
                if not self.find( "nome_fantasia", matching=0.97, waiting_time=10000):
                    self.not_found("nome_fantasia")
                self.click_relative(73, 25)
                self.type_keys_with_interval(1,'te12!@')
                
            
                x = 0
                while x < 5:           
                    if not self.find( "ramo_atividade", matching=0.97, waiting_time=10000):
                        self.not_found("ramo_atividade")
                    self.click_relative(57, 25)
                    self.type_down()
                    self.enter()
                    x = x+1 
                
                
                y = 0
                while y < 7:
                    if not self.find( "tipora2", matching=0.97, waiting_time=10000):
                        self.not_found("tipora2")
                    self.click_relative(57, 24)
                    self.type_down()
                    self.enter()
                    y = y+1
                    
                
                
        
                if not self.find( "im1", matching=0.97, waiting_time=10000):
                    self.not_found("im1")
                self.click_relative(39, 25)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "iest", matching=0.97, waiting_time=10000):
                    self.not_found("iest")
                self.click_relative(61, 24)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "rantt", matching=0.97, waiting_time=10000):
                    self.not_found("rantt")
                self.click_relative(33, 28)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "especiempresa", matching=0.97, waiting_time=10000):
                    self.not_found("especiempresa")
                self.click_relative(53, 26)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "cdgagente", matching=0.97, waiting_time=10000):
                    self.not_found("cdgagente")
                self.click_relative(43, 26)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "cinstanp", matching=0.97, waiting_time=10000):
                    self.not_found("cinstanp")
                self.click_relative(33, 26)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ENDEREÇO---###
                
                if not self.find( "rua", matching=0.97, waiting_time=10000):
                    self.not_found("rua")
                self.click_relative(50, 28)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "numerorua", matching=0.97, waiting_time=10000):
                    self.not_found("numerorua")
                self.click_relative(17, 29)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "municipio", matching=0.97, waiting_time=10000):
                    self.not_found("municipio")
                self.click_relative(377, 24)
                self.type_down()
                self.enter()
                if not self.find( "municipioloop1", matching=0.97, waiting_time=10000):
                    self.not_found("municipioloop1")
                self.double_click_relative(17, 25)
                self.backspace()
                self.wait(100)
                self.backspace()
                self.wait(500)
                self.enter()
                if not self.find( "municipioloop2", matching=0.97, waiting_time=10000):
                    self.not_found("municipioloop2")
                self.click_relative(51, 29)       
                self.backspace(wait=100)
                if not self.find( "localizarbuscar", matching=0.97, waiting_time=10000):
                    self.not_found("localizarbuscar")
                self.click()
                self.type_keys_with_interval(1,'Guarapuava')
                if not self.find( "gorpacity", matching=0.97, waiting_time=10000):
                    self.not_found("gorpacity")
                self.click()
                if not self.find( "selecionar", matching=0.97, waiting_time=10000):
                    self.not_found("selecionar")
                self.click()
                self.wait(1000)
                if not self.find( "cep", matching=0.97, waiting_time=10000):
                    self.not_found("cep")
                self.click_relative(28, 28)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "complemento", matching=0.97, waiting_time=10000):
                    self.not_found("complemento")
                self.click_relative(80, 31)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "bairro", matching=0.97, waiting_time=10000):
                    self.not_found("bairro")
                self.click_relative(53, 27)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'(42)98411-9244')
                if not self.find( "fax", matching=0.97, waiting_time=10000):
                    self.not_found("fax")
                self.click_relative(62, 28)
                self.type_keys_with_interval(1,'123123123123')
                
                                ####---DADOS DE CONTATO---####
                
                self.tab()
                self.type_keys_with_interval(1,'emaildetesteteorema@gmail.com')
                
                if not self.find( "site", matching=0.97, waiting_time=10000):
                    self.not_found("site")
                self.click_relative(106, 30)
                self.type_keys_with_interval(1,'www.google.com')
                   
                if not self.find( "responsavel", matching=0.97, waiting_time=10000):
                    self.not_found("responsavel")
                self.click_relative(55, 25)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "funcaoresp", matching=0.97, waiting_time=10000):
                    self.not_found("funcaoresp")
                self.click_relative(400, 27)
                self.type_down(wait=10)
                self.enter()
                #if not self.find( "codigo_funcresp", matching=0.97, waiting_time=10000):
                #    self.not_found("codigo_funcresp")
                #self.click()
                if not self.find( "funcaoresp", matching=0.97, waiting_time=10000):
                    self.not_found("funcaoresp")
                self.click_relative(400, 27)
                self.backspace()
                self.wait(100)
                self.backspace()
                self.wait(500)
                if not self.find( "loopfresp1", matching=0.97, waiting_time=10000):
                    self.not_found("loopfresp1")
                self.double_click_relative(55, 28)
                if not self.find( "selecaofuncao", matching=0.97, waiting_time=10000):
                    self.not_found("selecaofuncao")
                self.click()
                if not self.find( "selecionarfuncao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarfuncao")
                self.click()
                if not self.find( "titular", matching=0.97, waiting_time=10000):
                    self.not_found("titular")
                self.click_relative(55, 29)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "funcaotitular", matching=0.97, waiting_time=10000):
                    self.not_found("funcaotitular")
                self.click_relative(36, 26)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "cpftitular", matching=0.97, waiting_time=10000):
                    self.not_found("cpftitular")
                self.click_relative(53, 24)
                self.type_keys_with_interval(1,'086.580.339-02')
                
                                ####---DADOS DE CONTADOR---####
                
                if not self.find( "dados_nome_outro3", matching=0.97, waiting_time=10000):
                    self.not_found("dados_nome_outro3")
                self.click_relative(66, 25)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "dados_cpf_outro", matching=0.97, waiting_time=10000):
                    self.not_found("dados_cpf_outro")
                self.click_relative(52, 27)
                self.type_keys_with_interval(1,'086.580.339-02')
                if not self.find( "dados_crc", matching=0.97, waiting_time=10000):
                    self.not_found("dados_crc")
                self.click_relative(30, 27)
                self.type_keys_with_interval(1,'te12!@')
                #if not self.find( "dados_funcao_outro2", matching=0.97, waiting_time=10000):
                #    self.not_found("dados_funcao_outro2")
                #self.click_relative(58, 25)
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixar_tela", matching=0.97, waiting_time=10000):
                    self.not_found("abaixar_tela")
                self.click()
                
                                
                t = 0
                while t < 22:                        
                    if not self.find( "seta_baixo", matching=0.97, waiting_time=10000):
                        self.not_found("seta_baixo")
                    self.doubleclick()         
                    t = t+1
                
                                ####---CONTINUACAO DADOS DE CONTADOR---####                         
                
                if not self.find( "email_outro_dados_2", matching=0.97, waiting_time=10000):
                    self.not_found("email_outro_dados_2")
                self.click_relative(77, 29)
                self.type_keys_with_interval(1,'testeemailteorema@teste.com.br')
                
                if not self.find( "telefone", matching=0.97, waiting_time=10000):
                    self.not_found("telefone")
                self.click_relative(40, 27)
                self.type_keys_with_interval(1,'(42)98411-9244')
                if not self.find( "numerocontrato", matching=0.97, waiting_time=10000):
                    self.not_found("numerocontrato")
                self.click_relative(21, 28)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "postoselagem", matching=0.97, waiting_time=10000):
                    self.not_found("postoselagem")
                self.click_relative(-98, 29)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---DATAS---####
                
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                if not self.find( "datacadastro", matching=0.97, waiting_time=10000):
                    self.not_found("datacadastro")
                self.click_relative(89, 27)
                if not self.find( "limpadata", matching=0.97, waiting_time=10000):
                    self.not_found("limpadata")
                self.click()
                self.type_keys_with_interval(1,'123')
                self.enter(wait=100)
                self.enter(wait=100)
                if not self.find( "vencimentoalvara", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentoalvara")
                self.click_relative(91, 28)
                if not self.find( "limpar2", matching=0.97, waiting_time=10000):
                    self.not_found("limpar2")
                self.click()
                self.type_keys_with_interval(1,'123')
                self.enter(wait=100)
                
              
                ##################-----CADASTRO ABA 2-----#######################
                    ####---PERCENTUAIS, DIAS, ARREDONDAMENTO---####

                if not self.find( "a2_cad_empresas", matching=0.97, waiting_time=10000):
                    self.not_found("a2_cad_empresas")
                self.click()
                
                self.type_keys_with_interval(1,'123')
                if not self.find( "arredondamento", matching=0.97, waiting_time=10000):
                    self.not_found("arredondamento")
                self.click_relative(89, 28)
                self.type_keys_with_interval(1,'123')
                self.enter(wait=100)
                self.enter(wait=100)
                self.type_keys_with_interval(1,'123')
                if not self.find( "arredferias", matching=0.97, waiting_time=10000):
                    self.not_found("arredferias")
                self.click_relative(88, 28)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "adiantamento", matching=0.97, waiting_time=10000):
                    self.not_found("adiantamento")
                self.click_relative(91, 31)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "anuenio", matching=0.97, waiting_time=10000):
                    self.not_found("anuenio")
                self.click_relative(90, 29)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "trienio", matching=0.97, waiting_time=10000):
                    self.not_found("trienio")
                self.click_relative(89, 31)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "quinquenio", matching=0.97, waiting_time=10000):
                    self.not_found("quinquenio")
                self.click_relative(88, 28)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "issporcentagem", matching=0.97, waiting_time=10000):
                    self.not_found("issporcentagem")
                self.click_relative(91, 29)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "pisfolha", matching=0.97, waiting_time=10000):
                    self.not_found("pisfolha")
                self.click_relative(88, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "contribsocial", matching=0.97, waiting_time=10000):
                    self.not_found("contribsocial")
                self.click_relative(87, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "desoneracao", matching=0.97, waiting_time=10000):
                    self.not_found("desoneracao")
                self.click_relative(87, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                if not self.find( "examemedico", matching=0.97, waiting_time=10000):
                    self.not_found("examemedico")
                self.double_click_relative(64, 19)
                if not self.find( "examemedico2", matching=0.97, waiting_time=10000):
                    self.not_found("examemedico2")
                self.double_click_relative(62, 30)
                if not self.find( "diaexpvamo2", matching=0.97, waiting_time=10000):
                    self.not_found("diaexpvamo2")
                self.click_relative(63, 23)
                self.click()                        
                if not self.find( "diaexpvamo2", matching=0.97, waiting_time=10000):
                    self.not_found("diaexpvamo2")            
                self.click_relative(64, 32)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "contribconf", matching=0.97, waiting_time=10000):
                    self.not_found("contribconf")
                self.click_relative(64, 28)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                
                z = 0
                while z < 5:
                    if not self.find( "aliquotaebase", matching=0.97, waiting_time=10000):
                        self.not_found("aliquotaebase")
                    self.click_relative(85, 26)
                    self.type_down()
                    self.enter()
                    z = z+1
            
                x = 0
                while x < 4:
                    if not self.find( "contrataaprendiz", matching=0.97, waiting_time=10000):
                        self.not_found("contrataaprendiz")
                    self.click_relative(54, 28)
                    self.type_down()
                    self.enter()
                    x = x+1
                
                y = 0
                while y < 4:
                    if not self.find( "PCD", matching=0.97, waiting_time=10000):
                        self.not_found("PCD")
                    self.click_relative(-32, 29)
                    self.type_down()
                    self.enter()
                    y = y+1
                
                if not self.find( "cnpjentidade", matching=0.97, waiting_time=10000):
                        self.not_found("cnpjentidade")
                self.click_relative(16, 30)
                self.type_keys_with_interval(1,'te12!@')
            
                            ####---CÓDIGOS---####
                                
                if not self.find( "fpas", matching=0.97, waiting_time=10000):
                    self.not_found("fpas")
                self.click_relative(28, 26)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "cnae", matching=0.97, waiting_time=10000):
                    self.not_found("cnae")
                self.click_relative(30, 32)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "contafgts", matching=0.97, waiting_time=10000):
                    self.not_found("contafgts")
                self.click_relative(39, 26)
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                #if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                #    self.not_found("codcaixa")
                #self.click_relative(43, 29)
                self.type_keys_with_interval(1,'t1!')
            
                z = 0
                while z < 6:
                    if not self.find( "categoria", matching=0.97, waiting_time=10000):
                        self.not_found("categoria")
                    self.click_relative(69, 24)
                    self.type_up()
                    self.enter()
                    z = z+1
                
                                ####---EMPRESAS ISENTAS---####
                #if not self.find( "siglaenome", matching=0.97, waiting_time=10000):
                #    self.not_found("siglaenome")
                #self.click_relative(71, 25)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "entbene", matching=0.97, waiting_time=10000):
                    self.not_found("entbene")
                self.click_relative(-21, 25)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "emicertf", matching=0.97, waiting_time=10000):
                    self.not_found("emicertf")
                self.click_relative(88, 27)
                if not self.find( "clearempisen", matching=0.97, waiting_time=10000):
                    self.not_found("clearempisen")
                self.click_relative(26, 11)
                if not self.find( "emicertf2", matching=0.97, waiting_time=10000):
                    self.not_found("emicertf2")
                self.click_relative(3, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "venccert", matching=0.97, waiting_time=10000):
                    self.not_found("venccert")
                self.click_relative(89, 28)
                if not self.find( "clearvenccert", matching=0.97, waiting_time=10000):
                    self.not_found("clearvenccert")
                self.click()
                self.enter()
                if not self.find( "venccert2", matching=0.97, waiting_time=10000):
                    self.not_found("venccert2")
                self.click_relative(7, 29)
                self.type_keys_with_interval(1,'123')
                self.enter
                
                
                if not self.find( "protoped", matching=0.97, waiting_time=10000):
                    self.not_found("protoped")
                self.click_relative(39, 28)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "renodata", matching=0.97, waiting_time=10000):
                    self.not_found("renodata")
                self.click_relative(168, 26)
                if not self.find( "clearempisen4", matching=0.97, waiting_time=10000):
                    self.not_found("clearempisen4")
                self.click()
                if not self.find( "renodata2", matching=0.97, waiting_time=10000):
                    self.not_found("renodata2")
                self.click_relative(83, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "pubdou", matching=0.97, waiting_time=10000):
                    self.not_found("pubdou")
                self.click_relative(88, 26)
                if not self.find( "clearempisen5", matching=0.97, waiting_time=10000):
                    self.not_found("clearempisen5")
                self.click()
                if not self.find( "pubdou2", matching=0.97, waiting_time=10000):
                    self.not_found("pubdou2")
                self.click_relative(3, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "numeropagina", matching=0.97, waiting_time=10000):
                    self.not_found("numeropagina")
                self.click_relative(86, 19)
                if not self.find( "numeropagina2", matching=0.97, waiting_time=10000):
                    self.not_found("numeropagina2")
                self.click_relative(87, 31)
                
                                ####---ABA 2 P.2---####
                                
                if not bot.find( "fatu_cad_empresa_6_dsr_gps", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_empresa_6_dsr_gps")
                bot.click()
                
                if not self.find( "subirtela", matching=0.97, waiting_time=10000):
                    self.not_found("subirtela")
                self.click()
                
                
                if not self.find( "codmuni", matching=0.97, waiting_time=10000):
                    self.not_found("codmuni")
                self.click_relative(24, 28)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                
                
                if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                    self.not_found("enquadramento2")
                self.click_relative(105, 25)
                self.type_down()
                self.type_down()
                self.enter()
                if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                    self.not_found("enquadramento2")
                self.click_relative(105, 25)
                self.type_up()
                self.enter()
                if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                    self.not_found("enquadramento2")
                self.click_relative(105, 25)
                self.type_down()
                self.type_down()
                self.enter()
                            
                    
                    
                    
                if not self.find( "enceatv", matching=0.97, waiting_time=10000):
                    self.not_found("enceatv")
                self.click_relative(-25, 28)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "enc_atv2", matching=0.97, waiting_time=10000):
                    self.not_found("enc_atv2")
                self.click_relative(61, 27)
                if not self.find( "clearp2", matching=0.97, waiting_time=10000):
                    self.not_found("clearp2")
                self.click()
                if not self.find( "enc_atv2", matching=0.97, waiting_time=10000):
                    self.not_found("enc_atv2")
                self.click_relative(61, 27)
                if not self.find( "data1", matching=0.97, waiting_time=10000):
                    self.not_found("data1")
                self.click_relative(97, 73)
                self.enter()
                if not self.find( "nproprietarios", matching=0.97, waiting_time=10000):
                    self.not_found("nproprietarios")
                self.click_relative(65, 23)
                if not self.find( "nproprietarios2", matching=0.97, waiting_time=10000):
                    self.not_found("nproprietarios2")
                self.click_relative(65, 34)
                if not self.find( "mesdatabase", matching=0.97, waiting_time=10000):
                    self.not_found("mesdatabase")
                self.click_relative(25, 29)
                self.type_keys_with_interval(1,'01')
                self.enter()
                if not self.find( "mesdatabase2", matching=0.97, waiting_time=10000):
                    self.not_found("mesdatabase2")
                self.click_relative(29, 32)
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.enter()
                if not self.find( "nat_esta", matching=0.97, waiting_time=10000):
                    self.not_found("nat_esta")
                self.click_relative(24, 28)
                self.type_keys_with_interval(1,'t1!@')
                
                
                                ####---OUTRAS INF.---####
                                
                if not self.find( "calcrefldsr49", matching=0.97, waiting_time=10000):
                    self.not_found("calcrefldsr49")
                self.click_relative(-10, 5)                
                self.wait(200)
                if not self.find( "reflexodsr0049", matching=0.97, waiting_time=10000):
                    self.not_found("reflexodsr0049")
                self.click()
                self.click()        
                if not self.find( "dsr18", matching=0.97, waiting_time=10000):
                    self.not_found("dsr18")
                self.click()                       
                self.wait(200)
                if not self.find( "dsr18", matching=0.97, waiting_time=10000):
                    self.not_found("dsr18")
                self.click()
                self.click()
                
                if not self.find( "refhoraextra", matching=0.97, waiting_time=10000):
                    self.not_found("refhoraextra")
                self.click()
                self.wait(200)
                if not self.find( "reflexohoraextramarcado", matching=0.97, waiting_time=10000):
                    self.not_found("reflexohoraextramarcado")
                self.click()
                self.click()
                        
                if not self.find( "addnot", matching=0.97, waiting_time=10000):
                    self.not_found("addnot")
                self.click_relative(-67, 8)
                self.wait(200)
                if not self.find( "gerainteaddnotmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("gerainteaddnotmarcado")
                self.click()
                self.click()        
                
                
                                ####---OUTRAS INF. PT.2---####
                                
                z = 0                 
                while z < 7:                 
                    if not self.find( "controleponto", matching=0.97, waiting_time=10000):
                        self.not_found("controleponto")
                    self.click_relative(43, 27)
                    self.type_down()
                    self.enter()
                    z = z+1
                    
                y = 0
                while y < 2:
                    if not self.find( "regeletroemp", matching=0.97, waiting_time=10000):
                        self.not_found("regeletroemp")
                    self.click_relative(66, 30)
                    self.type_down()
                    self.enter()
                    y = y+1
                    
                                ####---SEFIP---####
                                
                self.enter()                 
                if not self.find( "sefipsemmarca", matching=0.97, waiting_time=10000):
                    self.not_found("sefipsemmarca")
                self.click()        
                self.wait(200)
                if not self.find( "gerarsefip", matching=0.97, waiting_time=10000):
                    self.not_found("gerarsefip")
                self.click_relative(69, 8)
                
                if not self.find( "dadosadd", matching=0.97, waiting_time=10000):
                    self.not_found("dadosadd")
                self.click_relative(102, 7)
                self.wait(200)
                if not self.find( "geradadosmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("geradadosmarcado")
                self.click()
                self.click()        
                if not self.find( "altend", matching=0.97, waiting_time=10000):
                    self.not_found("altend")
                self.click_relative(92, 7)
                self.wait(200)
                if not self.find( "alteraenderecomarcado", matching=0.97, waiting_time=10000):
                    self.not_found("alteraenderecomarcado")
                self.click()
                self.click()
                
                
                
                x = 0
                while x < 2:
                    if not self.find( "alteracnae", matching=0.97, waiting_time=10000):
                        self.not_found("alteracnae")
                    self.click_relative(80, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "alteracnae", matching=0.97, waiting_time=10000):
                        self.not_found("alteracnae")
                self.click_relative(80, 28)
                self.type_up()
                self.type_up()
                self.enter()    
                    
                self.enter()    
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "isenfilan", matching=0.97, waiting_time=10000):
                    self.not_found("isenfilan")
                self.click_relative(65, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                
                z = 0
                while z < 3:
                    if not self.find( "tipocentr", matching=0.97, waiting_time=10000):
                        self.not_found("tipocentr")
                    self.click_relative(105, 26)
                    self.type_down()
                    self.enter()
                    z=z+1
                    
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixatela2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatela2")
                self.click()
                
                t = 0
                while t < 15:
                    if not self.find( "abaixatela3", matching=0.97, waiting_time=10000):
                        self.not_found("abaixatela3")
                    self.double_click()
                    t=t+1
                    
                                ####---CAGED---####
                                
                if not self.find( "geracagedmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("geracagedmarcado")
                self.click()        
                self.wait(200)
                if not self.find( "geracagedmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("geracagedmarcado")
                self.click()
                if not self.find( "declara", matching=0.97, waiting_time=10000):
                    self.not_found("declara")
                self.click_relative(82, 9)
                self.wait(200)
                if not self.find( "primeiradecmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("primeiradecmarcado")
                self.click()
                self.click()
                if not self.find( "nconv", matching=0.97, waiting_time=10000):
                    self.not_found("nconv")
                self.click_relative(41, 28)
                self.type_keys_with_interval(1,'te12!@')
                
                
                x = 0
                while x < 3:
                    if not self.find( "info", matching=0.97, waiting_time=10000):
                        self.not_found("info")
                    self.click_relative(43, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---GPS---####
                
                if not self.find( "codgps", matching=0.97, waiting_time=10000):
                    self.not_found("codgps")
                self.click_relative(49, 26)
                self.type_keys_with_interval(1,'t1@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "inss", matching=0.97, waiting_time=10000):
                    self.not_found("inss")
                self.click_relative(91, 29)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'t1@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "terce", matching=0.97, waiting_time=10000):
                    self.not_found("terce")
                self.click_relative(91, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'t1@')
                self.enter()
                if not self.find( "rat", matching=0.97, waiting_time=10000):
                    self.not_found("rat")
                self.click_relative(89, 24)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "fap", matching=0.97, waiting_time=10000):
                    self.not_found("fap")
                self.click_relative(87, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "incra", matching=0.97, waiting_time=10000):
                    self.not_found("incra")
                self.click_relative(89, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "sebrae", matching=0.97, waiting_time=10000):
                    self.not_found("sebrae")
                self.click_relative(89, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "saledu", matching=0.97, waiting_time=10000):
                    self.not_found("saledu")
                self.click_relative(85, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "sesi", matching=0.97, waiting_time=10000):
                    self.not_found("sesi")
                self.click_relative(90, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                if not self.find( "senai", matching=0.97, waiting_time=10000):
                    self.not_found("senai")
                self.click_relative(88, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                if not self.find( "emprural", matching=0.97, waiting_time=10000):
                    self.not_found("emprural")
                self.click_relative(78, 6)
                self.wait(200)
                if not self.find( "emprural", matching=0.97, waiting_time=10000):
                    self.not_found("emprural")
                self.click()
                
                
                                ####---E SOCIAL---####
                                
                self.tab()
                if not self.find( "certificado", matching=0.97, waiting_time=10000):
                    self.not_found("certificado")
                self.click_relative(33, 25)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA 2 P.3---####
                                
                if not self.find( "aba2p3", matching=0.97, waiting_time=10000):
                    self.not_found("aba2p3")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA 3---####
                            ####---INF.FISCAIS---####
                                
                if not self.find( "aba3", matching=0.97, waiting_time=10000):
                    self.not_found("aba3")
                self.click()
                if not self.find( "nojunta", matching=0.97, waiting_time=10000):
                    self.not_found("nojunta")
                self.click_relative(21, 24)
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---INF.SIMPLES---####
                
                x = 0
                while x < 6:
                    if not self.find( "simples", matching=0.97, waiting_time=10000):
                        self.not_found("simples")
                    self.click_relative(464, 45)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "simples", matching=0.97, waiting_time=10000):
                        self.not_found("simples")
                self.click_relative(464, 45)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "icmssimples", matching=0.97, waiting_time=10000):
                    self.not_found("icmssimples")
                self.click_relative(71, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "diferenciado", matching=0.97, waiting_time=10000):
                    self.not_found("diferenciado")
                self.click_relative(-2, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                y = 0
                while y < 4:
                    if not self.find( "estadual", matching=0.97, waiting_time=10000):
                        self.not_found("estadual")
                    self.click_relative(145, 27)
                    self.type_down()
                    self.enter()
                    y=y+1
                    
                z = 0
                while z < 12:
                    if not self.find( "federal", matching=0.97, waiting_time=10000):
                        self.not_found("federal")
                    self.click_relative(145, 27)
                    self.type_down()
                    self.enter()
                    z=z+1
                    
                                ####---INF.EFD---####
                                                        
                x=0
                while x < 3:                
                    if not self.find( "juridica", matching=0.97, waiting_time=10000):
                        self.not_found("juridica")
                    self.click_relative(182, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                y=0
                while y < 6:
                    if not self.find( "atvprepon", matching=0.97, waiting_time=10000):
                        self.not_found("atvprepon")
                    self.click_relative(244, 27)
                    self.type_down()
                    self.enter()
                    y=y+1
                    
                                ####---INF.ISS---####
                         
                if not bot.find( "fatu_cad_empresas_informações_incent_fiscal", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_empresas_informações_incent_fiscal")
                bot.click()
                self.wait(2000)
                self.tab()
                self.space()
                self.tab()        
                
                self.type_keys_with_interval(1,'t1')
                self.enter()
                if not self.find( "regimetrib", matching=0.97, waiting_time=10000):
                    self.not_found("regimetrib")
                self.click_relative(36, 28)
                self.backspace()
                self.type_keys_with_interval(1,'!')
                
                                ####---INF.DMED---####
                                
                if not self.find( "cnes", matching=0.97, waiting_time=10000):
                    self.not_found("cnes")
                self.click_relative(36, 27)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                
                x=0
                while x < 3:
                    if not self.find( "tipodeclarante", matching=0.97, waiting_time=10000):
                        self.not_found("tipodeclarante")
                    self.click_relative(186, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---E SOCIAL---####
                                
                z=0
                while z < 19:
                    if not self.find( "tributaria", matching=0.97, waiting_time=10000):
                        self.not_found("tributaria")
                    self.click_relative(394, 25)
                    self.type_down()
                    self.enter()
                    z=z+1
                
                y=0
                while y < 14:
                    if not self.find( "lotacao", matching=0.97, waiting_time=10000):
                        self.not_found("lotacao")
                    self.click_relative(464, 25)
                    self.type_down()
                    self.enter()
                    y=y+1
                    
                                ####---OUTRAS INF.---####
                                
                if not self.find( "escolarmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("escolarmarcado")
                self.click()
                if not self.find( "escolarmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("escolarmarcado")
                self.click()
                if not self.find( "ipi", matching=0.97, waiting_time=10000):
                    self.not_found("ipi")
                self.click()
                if not self.find( "temipimarcado", matching=0.97, waiting_time=10000):
                    self.not_found("temipimarcado")
                self.click() 
                self.click()       
                if not self.find( "issno", matching=0.97, waiting_time=10000):
                    self.not_found("issno")
                self.click()
                if not self.find( "issicmsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("issicmsmarcado")
                self.click()
                self.click()        
                if not self.find( "darfserv", matching=0.97, waiting_time=10000):
                    self.not_found("darfserv")
                self.click()
                if not self.find( "darfservmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("darfservmarcado")
                self.click()
                if not self.find( "icmsno", matching=0.97, waiting_time=10000):
                    self.not_found("icmsno")
                self.click()
                if not self.find( "icmsnomarcado", matching=0.97, waiting_time=10000):
                    self.not_found("icmsnomarcado")
                self.click()
                self.click()
                if not self.find( "construtora", matching=0.97, waiting_time=10000):
                    self.not_found("construtora")
                self.click()
                if not self.find( "construtoramarcado", matching=0.97, waiting_time=10000):
                    self.not_found("construtoramarcado")
                self.click()
                if not self.find( "construtoramarcado", matching=0.97, waiting_time=10000):
                    self.not_found("construtoramarcado")
                self.click()
                self.space()
                
                z=0
                while z < 3:
                    if not self.find( "coop", matching=0.97, waiting_time=10000):
                        self.not_found("coop")
                    self.click_relative(143, 27)
                    self.type_down()
                    self.enter()
                    z=z+1
                    
                if not self.find( "coop", matching=0.97, waiting_time=10000):
                        self.not_found("coop")
                self.click_relative(143, 27)
                self.type_up()
                self.type_up()
                self.type_up()
                self.enter()
                
                                ####---ABA 4---####
                                
                if not self.find( "aba4", matching=0.97, waiting_time=10000):
                    self.not_found("aba4")
                self.click()
                if not self.find( "grupoempresaaba4", matching=0.97, waiting_time=10000):
                    self.not_found("grupoempresaaba4")
                self.click_relative(66, 27)        
                if not self.find( "aba4localizar1", matching=0.97, waiting_time=10000):
                    self.not_found("aba4localizar1")
                self.click()
                if not self.find( "aba4selecionar1", matching=0.97, waiting_time=10000):
                    self.not_found("aba4selecionar1")
                self.click()
                if not self.find( "cfempresa", matching=0.97, waiting_time=10000):
                    self.not_found("cfempresa")
                self.click_relative(41, 24)
                if not self.find( "aba4cod1", matching=0.97, waiting_time=10000):
                    self.not_found("aba4cod1")
                self.click()
                if not self.find( "aba4selecionar2", matching=0.97, waiting_time=10000):
                    self.not_found("aba4selecionar2")
                self.click()
                if not self.find( "pcpfaba4", matching=0.97, waiting_time=10000):
                    self.not_found("pcpfaba4")
                self.click_relative(45, 28)
                if not self.find( "aba4cod2", matching=0.97, waiting_time=10000):
                    self.not_found("aba4cod2")
                self.click()
                if not self.find( "aba4selecionar3", matching=0.97, waiting_time=10000):
                    self.not_found("aba4selecionar3")
                self.click()
                if not self.find( "tpitens", matching=0.97, waiting_time=10000):
                    self.not_found("tpitens")
                self.click_relative(-22, 26)
                if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("localizartpitens")
                self.click()
                if not self.find( "tabelaprecoszerado01", matching=0.97, waiting_time=10000):
                    self.not_found("tabelaprecoszerado01")
                self.click()            
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                    self.not_found("codigozeradotabelapreco")
                self.double_click()
                self.backspace()
                
                if not self.find( "contratos", matching=0.97, waiting_time=10000):
                    self.not_found("contratos")
                self.click_relative(40, 23)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "pcempresa", matching=0.97, waiting_time=10000):
                    self.not_found("pcempresa")
                self.click_relative(42, 25)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "usait", matching=0.97, waiting_time=10000):
                    self.not_found("usait")
                self.click_relative(68, 25)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "vendedores", matching=0.97, waiting_time=10000):
                    self.not_found("vendedores")
                self.click_relative(41, 24)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "precosservico", matching=0.97, waiting_time=10000):
                    self.not_found("precosservico")
                self.click_relative(-21, 25)
                if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("localizartpitens")
                self.click()
                if not self.find( "tabelaprecoszerado01", matching=0.97, waiting_time=10000):
                    self.not_found("tabelaprecoszerado01")
                self.click() 
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                    self.not_found("codigozeradotabelapreco")
                self.double_click()
                self.backspace()
                if not self.find( "contabilista", matching=0.97, waiting_time=10000):
                    self.not_found("contabilista")
                self.click_relative(67, 26)
                if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("localizartpitens")
                self.click()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "historicos", matching=0.97, waiting_time=10000):
                    self.not_found("historicos")
                self.click_relative(47, 28)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                #if not self.find( "usapreços", matching=0.97, waiting_time=10000):
                #    self.not_found("usapreços")
                #self.click_relative(44, 25)
                #if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionartpitens")
                #self.click()
                #if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                #    self.not_found("aba4codcontratos")
                #self.click()
                #if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionartpitens")
                #self.click()
                if not self.find( "situaçoesempresa", matching=0.97, waiting_time=10000):
                    self.not_found("situaçoesempresa")
                self.click_relative(44, 26)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                if not self.find( "veículos", matching=0.97, waiting_time=10000):
                    self.not_found("veículos")
                self.click_relative(46, 25)
                if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                    self.not_found("aba4codcontratos")
                self.click()
                if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartpitens")
                self.click()
                
                
                                ####---GRUPOS CONTABEIS---####
                                
                #if not self.find( "salvar_reposicao", matching=0.97, waiting_time=10000):
                #    self.not_found("salvar_reposicao")
                #self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.enter()
                
                                
                if not self.find( "contacliente", matching=0.97, waiting_time=10000):
                    self.not_found("contacliente")
                self.click_relative(122, 22)        
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()
                
                
                if not self.find( "contafornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("contafornecedores")
                self.click_relative(102, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()
                
                if not self.find( "codclientes", matching=0.97, waiting_time=10000):
                    self.not_found("codclientes")
                self.click_relative(42, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()

                if not self.find( "codforne", matching=0.97, waiting_time=10000):
                    self.not_found("codforne")
                self.click_relative(42, 24)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99994", matching=0.97, waiting_time=10000):
                    self.not_found("99994")
                self.click_relative(46, 24)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99993", matching=0.97, waiting_time=10000):
                    self.not_found("99993")
                self.click_relative(48, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99992", matching=0.97, waiting_time=10000):
                    self.not_found("99992")
                self.click_relative(49, 24)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99991", matching=0.97, waiting_time=10000):
                    self.not_found("99991")
                self.click_relative(47, 22)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99990", matching=0.97, waiting_time=10000):
                    self.not_found("99990")
                self.click_relative(48, 24)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99989", matching=0.97, waiting_time=10000):
                    self.not_found("99989")
                self.click_relative(47, 24)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99988", matching=0.97, waiting_time=10000):
                    self.not_found("99988")
                self.click_relative(47, 25)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99987", matching=0.97, waiting_time=10000):
                    self.not_found("99987")
                self.click_relative(48, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99986", matching=0.97, waiting_time=10000):
                    self.not_found("99986")
                self.click_relative(47, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99985", matching=0.97, waiting_time=10000):
                    self.not_found("99985")
                self.click_relative(47, 25)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99984", matching=0.97, waiting_time=10000):
                    self.not_found("99984")
                self.click_relative(48, 26)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99983", matching=0.97, waiting_time=10000):
                    self.not_found("99983")
                self.click_relative(47, 27)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99982", matching=0.97, waiting_time=10000):
                    self.not_found("99982")
                self.click_relative(49, 27)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()


                if not self.find( "99981", matching=0.97, waiting_time=10000):
                    self.not_found("99981")
                self.click_relative(47, 25)
                if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                    self.not_found("localizagrupos")
                self.click()
                if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("localizarplanodecontas")
                self.click()
                if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                    self.not_found("codigobensnumerarios")
                self.click()
                if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarplanodecontas")
                self.click()



                if not self.find( "contpatri", matching=0.97, waiting_time=10000):
                    self.not_found("contpatri")
                self.click_relative(-2, 19)
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                
                                ####---ABA 5---####
                            ####---ABA5 P1---####
                                
                if not self.find( "aba5", matching=0.97, waiting_time=10000):
                    self.not_found("aba5")
                self.click()
                if not self.find( "salvar", matching=0.97, waiting_time=10000):
                    self.not_found("salvar")
                self.click()
                self.enter()
                if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistro")
                self.click()
                if not self.find( "estadoaba5", matching=0.97, waiting_time=10000):
                    self.not_found("estadoaba5")
                self.click_relative(43, 27)
                

                
                if not self.find( "selecionaraba5", matching=0.97, waiting_time=10000):
                    self.not_found("selecionaraba5")
                self.click()
                if not self.find( "inscricaoestad", matching=0.97, waiting_time=10000):
                    self.not_found("inscricaoestad")
                self.click_relative(40, 30)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                if not self.find( "gravar", matching=0.97, waiting_time=10000):
                    self.not_found("gravar")
                self.click()
                if not self.find( "cancelarcertoa5p1", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarcertoa5p1")
                self.click_relative(11, 8)                
                if not self.find( "abandonarop", matching=0.97, waiting_time=10000):
                    self.not_found("abandonarop")
                self.click_relative(16, 63) 
                if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p2")
                self.click()
                
                if not self.find( "aba5p1_inscricao", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p1_inscricao")
                self.click()
                
                if not self.find( "a5p1inscri", matching=0.97, waiting_time=10000):
                    self.not_found("a5p1inscri")
                self.click()
                if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("deletara5p2")
                self.click()
                self.enter()
                
                    
                
                
                
                                ####---ABA5 P2---####
                                
                if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p2")
                self.click()
                if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistro")
                self.click()
                #if not self.find( "cadnomeaba5", matching=0.97, waiting_time=10000):
                #    self.not_found("cadnomeaba5")
                #self.click_relative(107, 56)        
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "nascimentoaba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("nascimentoaba5p2")
                self.click_relative(76, 27)
                if not self.find( "clearaba5p2normal", matching=0.97, waiting_time=10000):
                    self.not_found("clearaba5p2normal")
                self.click()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'086.580.339-02')
                self.enter()
                self.type_keys_with_interval(1,'14.734.534-8')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                
                                ####---ENDERECO ABA 5---####
                
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ufaba5", matching=0.97, waiting_time=10000):
                    self.not_found("ufaba5")
                self.click_relative(209, 28)
                x=0
                while x < 27:
                    self.type_down()
                    self.enter()
                    if not self.find( "ufaba5", matching=0.97, waiting_time=10000):
                        self.not_found("ufaba5")
                    self.click_relative(209, 28)
                    x=x+1
                    
                self.enter()
                self.type_keys_with_interval(1,'85055-370')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'(42)98411-9244')
                self.enter()
                self.type_keys_with_interval(1,'testeteorema@teste.com.br')
                self.enter()
                
                                ####---CARACTERISTICAS---####
                                
                if not self.find( "ocorrenciaaba5", matching=0.97, waiting_time=10000):
                    self.not_found("ocorrenciaaba5")
                self.click_relative(316, 26)
                self.type_down()
                self.type_down()
                self.enter()
                
                y=0
                while y < 8:
                    if not self.find( "ocorrenciaaba5", matching=0.97, waiting_time=10000):
                        self.not_found("ocorrenciaaba5")
                    self.click_relative(316, 26)
                    self.type_down()
                    self.enter()
                    y=y+1
                    
                if not self.find( "classeaba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("classeaba5p2")
                self.click_relative(10, 25)
                self.type_keys_with_interval(1,'t1')
                self.enter()
                if not self.find( "classeaba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("classeaba5p2")
                self.click_relative(10, 25)
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.enter()
                if not self.find( "ndepende", matching=0.97, waiting_time=10000):
                    self.not_found("ndepende")
                self.click_relative(73, 21)
                if not self.find( "ndependes3", matching=0.97, waiting_time=10000):
                    self.not_found("ndependes3")
                self.click_relative(73, 31)
                self.enter()
                
                x=0
                while x<22:
                    if not self.find( "categ", matching=0.97, waiting_time=10000):
                        self.not_found("categ")
                    self.click_relative(320, 21)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "admissaodataaba5", matching=0.97, waiting_time=10000):
                    self.not_found("admissaodataaba5")
                self.click_relative(55, 23)
                if not self.find( "clearadmissao", matching=0.97, waiting_time=10000):
                    self.not_found("clearadmissao")
                self.click()
                if not self.find( "admissaodataaba5", matching=0.97, waiting_time=10000):
                    self.not_found("admissaodataaba5")
                self.click_relative(55, 23)
                if not self.find( "dataadmis", matching=0.97, waiting_time=10000):
                    self.not_found("dataadmis")
                self.click_relative(93, 65)
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "saidaaba5", matching=0.97, waiting_time=10000):
                    self.not_found("saidaaba5")
                self.click_relative(47, 21)
                if not self.find( "clearsaida", matching=0.97, waiting_time=10000):
                    self.not_found("clearsaida")
                self.click()
                if not self.find( "saidaaba5", matching=0.97, waiting_time=10000):
                    self.not_found("saidaaba5")
                self.click_relative(47, 21)
                if not self.find( "datasaida", matching=0.97, waiting_time=10000):
                    self.not_found("datasaida")
                self.click_relative(9, 64)
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "prolabore", matching=0.97, waiting_time=10000):
                    self.not_found("prolabore")
                self.click_relative(105, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "vinculos", matching=0.97, waiting_time=10000):
                    self.not_found("vinculos")
                self.click_relative(51, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "inssdatabela", matching=0.97, waiting_time=10000):
                    self.not_found("inssdatabela")
                self.click_relative(32, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "inssempresa", matching=0.97, waiting_time=10000):
                    self.not_found("inssempresa")
                self.click_relative(58, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("recolhefgtsmarcado")
                self.click()
                self.wait(100)
                if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("recolhefgtsmarcado")
                self.click()
                if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("recolhefgtsmarcado")
                self.click()
                self.enter()
                if not self.find( "isentoinssaba5", matching=0.97, waiting_time=10000):
                    self.not_found("isentoinssaba5")
                self.click()
                self.wait(100)
                if not self.find( "isentoinssaba5", matching=0.97, waiting_time=10000):
                    self.not_found("isentoinssaba5")
                self.click()
                self.enter()
                if not self.find( "isentoirmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("isentoirmarcado")
                self.click()
                self.wait(100)
                if not self.find( "isentoirmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("isentoirmarcado")
                self.click()
                self.enter()
                if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                    self.not_found("spedcontabilaba5")
                self.click()
                self.wait(100)
                if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                    self.not_found("spedcontabilaba5")
                self.click()
                if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                    self.not_found("spedcontabilaba5")
                self.click()
                
                                ####---AGRUPAMENTO---####
                self.wait(2000)
                if not self.find( "funcaoagrupa", matching=0.97, waiting_time=10000):
                    self.not_found("funcaoagrupa")
                self.click_relative(331, 26)
                self.type_up()
                self.enter()
                if not self.find( "departagrupa", matching=0.97, waiting_time=10000):
                    self.not_found("departagrupa")
                self.click_relative(328, 23)
                self.type_up()
                self.enter()
                if not self.find( "setoragrupa", matching=0.97, waiting_time=10000):
                    self.not_found("setoragrupa")
                self.click_relative(327, 27)
                self.type_up()
                self.enter()
                if not self.find( "secaoagrupa", matching=0.97, waiting_time=10000):
                    self.not_found("secaoagrupa")
                self.click_relative(325, 24)
                self.type_up()
                self.enter()
                if not self.find( "bancoagrupa", matching=0.97, waiting_time=10000):
                    self.not_found("bancoagrupa")
                self.click_relative(327, 25)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                
                                ####---ABAIXAR TELA---####

                if not self.find( "abaixatelaa5p2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatelaa5p2")
                self.click()
                
                z=0
                while z < 12:
                    if not self.find( "abaixatelaa5b2m", matching=0.97, waiting_time=10000):
                        self.not_found("abaixatelaa5b2m")
                    self.double_click()
                    z=z+1
                #######
                ########
                ######
                ######
                ######
                ########
                ########
                ########
                ########
                                ####---OBSERVACOES---####

                if not bot.find( "fatu_cad_empresa_observacao_info_btn", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_empresa_observacao_info_btn")
                bot.click_relative(14, 29)
                
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---SALVAR E CONSULTAR---####

                if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("salvara5p2")
                self.click()        
                if not self.find( "consultara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("consultara5p2")
                self.click()  
                self.wait(1000)          
                if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara5p2")
                self.click()
                self.wait(1000)
                self.enter()
                self.wait(1000)
                self.click()
                self.enter()
                
                if not self.find( "aba5p3", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p3")
                self.click()
                if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p2")
                self.click()
                

                            ####---ABA5 P3---####

                if not self.find( "aba5p3", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p3")
                self.click()
                if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistro")
                self.click()
                if not self.find( "tipodoca5p3", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoca5p3")
                self.click_relative(348, 26)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "vencimentoa5p3", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentoa5p3")
                self.click_relative(74, 27)
                if not self.find( "cleara5p3", matching=0.97, waiting_time=10000):
                    self.not_found("cleara5p3")
                self.click()
                if not self.find( "vencimentoa5p3", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentoa5p3")
                self.click_relative(74, 27)
                if not self.find( "datasa5p3", matching=0.97, waiting_time=10000):
                    self.not_found("datasa5p3")
                self.click_relative(92, 67)
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "abrirdoca5p3", matching=0.97, waiting_time=10000):
                    self.not_found("abrirdoca5p3")
                self.click()
                self.wait(1000)
                self.key_esc()
                self.wait(1000)
                if not self.find( "obsa5p3", matching=0.97, waiting_time=10000):
                    self.not_found("obsa5p3")
                self.click_relative(36, 34)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("salvara5p2")
                self.click()
                if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara5p2")
                self.click()
                self.enter()
                #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
                #    self.not_found("sima5p2")
                #self.click()
                #if not self.find( "arqte12!@", matching=0.97, waiting_time=10000):
                #    self.not_found("arqte12!@")
                #self.click()
                if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("deletara5p2")
                self.click()
                self.enter()
                #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
                #    self.not_found("sima5p2")
                #self.click()
                
                                ####---ABA5 P4---####
                self.wait(1000)
                if not self.find( "a5p4_cad_empresa", matching=0.97, waiting_time=10000):
                    self.not_found("a5p4_cad_empresa")
                self.click()  
                if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistro")
                self.click()
                if not self.find( "aba5p4cliente", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p4cliente")
                self.click_relative(67, 25)
                if not self.find( "localizarcliente", matching=0.97, waiting_time=10000):
                    self.not_found("localizarcliente")
                self.click()
                #if not self.find( "codclientea5p4", matching=0.97, waiting_time=10000):
                #    self.not_found("codclientea5p4")
                #self.click()
                if not self.find( "selecionaraba5p4", matching=0.97, waiting_time=10000):
                    self.not_found("selecionaraba5p4")
                self.click()
                if not self.find( "obsaba5p4", matching=0.97, waiting_time=10000):
                    self.not_found("obsaba5p4")
                self.click_relative(28, 39)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("salvara5p2")
                self.click()
                if not self.find( "consultara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("consultara5p2")
                self.click()
                if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara5p2")
                self.click()
                self.enter()
                #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
                #    self.not_found("sima5p2")
                #self.click()
                self.wait(1000)   
                if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                    self.not_found("deletara5p2")
                self.click()
                self.enter()
                #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
                #    self.not_found("sima5p2")
                #self.click()
                
                                ####---GNRE---####

                if not self.find( "GNRE", matching=0.97, waiting_time=10000):
                    self.not_found("GNRE")
                self.click()
                if not self.find( "a6tipo", matching=0.97, waiting_time=10000):
                    self.not_found("a6tipo")
                self.click_relative(98, 25)
                self.type_down()
                self.enter()
                if not self.find( "a6tipo", matching=0.97, waiting_time=10000):
                    self.not_found("a6tipo")
                self.click_relative(98, 25)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "arquivoaba6", matching=0.97, waiting_time=10000):
                    self.not_found("arquivoaba6")
                self.click_relative(437, 25)
                self.wait(1000)
                self.key_esc()

                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "pastaschema", matching=0.97, waiting_time=10000):
                    self.not_found("pastaschema")
                self.click_relative(384, 25)
                if not self.find( "cancelar", matching=0.97, waiting_time=10000):
                    self.not_found("cancelar")
                self.click()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "gerados", matching=0.97, waiting_time=10000):
                    self.not_found("gerados")
                self.click_relative(340, 26)
                if not self.find( "cancelar", matching=0.97, waiting_time=10000):
                    self.not_found("cancelar")
                self.click()
                if not self.find( "ambiente", matching=0.97, waiting_time=10000):
                    self.not_found("ambiente")
                self.click_relative(97, 27)
                self.type_up()
                self.enter()
                if not self.find( "ambiente", matching=0.97, waiting_time=10000):
                    self.not_found("ambiente")
                self.click_relative(97, 27)
                self.type_down()
                self.enter()
                if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                    self.not_found("imprimir")
                self.click_relative(45, 27)
                self.type_down()
                self.enter()
                if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                    self.not_found("imprimir")
                self.click_relative(45, 27)
                self.type_down()
                self.enter()
                if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                    self.not_found("imprimir")
                self.click_relative(45, 27)
                self.type_up()
                self.type_up()
                self.enter()
                
                            ####---FINALIZAÇÃO (SALVAMENTO E EXCLUSÃO)---####

                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                self.wait(1000)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarempresafim", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarempresafim")
                self.click()
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                self.wait(500)
                if not self.find( "ativo", matching=0.97, waiting_time=10000):
                    self.not_found("ativo")
                self.click()
                if not self.find( "inativo", matching=0.97, waiting_time=10000):
                    self.not_found("inativo")
                self.click()
                if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                    self.not_found("fimsalvar")
                self.click()
                self.wait(1000)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "a2_cadastro_empresa", matching=0.97, waiting_time=10000):
                    self.not_found("a2_cadastro_empresa")
                self.click()            
                if not self.find( "todosfiltro", matching=0.97, waiting_time=10000):
                    self.not_found("todosfiltro")
                self.click()
                if not self.find( "1consulta", matching=0.97, waiting_time=10000):
                    self.not_found("1consulta")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not bot.find( "fatu_cad_empresas_achar_te12", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_empresas_achar_te12")
                bot.click()
                self.wait(1000)
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                
                self.wait(500)
                if not self.find( "excluirfim", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfim")
                self.click()
                #if not self.find( "simexcluirfim", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirfim")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                ###############################################################################
                ############################ ---GRUPO DE EMPRESAS--- ##########################
                ###############################################################################
                self.wait(3000)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                self.wait(1500)
                if not self.find( "abrir_menu_cadastro_empresa2", matching=0.97, waiting_time=10000):
                    self.not_found("abrir_menu_cadastro_empresa2")
                self.click()
                self.wait(1500)
    
                self.wait(1500)
                if not self.find( "grupodeempresas", matching=0.97, waiting_time=10000):
                    self.not_found("grupodeempresas")
                self.click()
                if not self.find( "empresas_localizar", matching=0.97, waiting_time=10000):
                    self.not_found("empresas_localizar")
                self.click()
                if not self.find( "empresas_incluir", matching=0.97, waiting_time=10000):
                    self.not_found("empresas_incluir")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
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
                if not self.find( "selecionarempresafim", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarempresafim")
                self.click()
                
                self.wait(1000)
                if not bot.find( "fatu_btn_editar_opc_cad_empresa_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_editar_opc_cad_empresa_2411")
                bot.click()
                self.wait(500)
                if not self.find( "excluirfim", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfim")
                self.click()
                #if not self.find( "simexcluirfim", matching=0.97, waiting_time=10000):
                #        self.not_found("simexcluirfim")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                
                        
                        #SESSÃO PÁGINA 2 (Parametros Fiscais 2426 - 6445)
                #######################-----LOGIN-----############################

                ###################################################################
            
            
            
                            ####---ABRINDO PARAMETROS---####
                
                self.wait(1500)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                self.wait(1500)
                if not self.find( "parametros", matching=0.97, waiting_time=10000):
                    self.not_found("parametros")
                self.click()
                if not self.find( "parametros", matching=0.97, waiting_time=10000):
                    self.not_found("parametros")
                self.click()
                self.type_down()
                self.wait(1500)
                if not self.find( "parametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosempresa")
                self.click()
                
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "naope", matching=0.97, waiting_time=10000):
                    self.not_found("naope")
                self.click()
                if not self.find( "buscaempresape", matching=0.97, waiting_time=10000):
                    self.not_found("buscaempresape")
                self.click()
                self.backspace()
                self.wait(1000)
                self.type_keys_with_interval(100,"0002")
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                
                                        
                if not self.find( "selecionarpe", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarpe")
                self.click()
                
                                ####---TITULOS COM ATRASOS---####
                
                if not self.find( "tituloatrasopagamentoapartir1", matching=0.97, waiting_time=10000):
                    self.not_found("tituloatrasopagamentoapartir1")
                self.click_relative(25, 19)
                if not self.find( "titulopagamentoapartir2", matching=0.97, waiting_time=10000):
                    self.not_found("titulopagamentoapartir2")            
                self.click_relative(27, 29)            
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'874')
                
                
                
                                ####---INTEGRACOES ERP---####
                
                if not self.find( "administrativo_com_livros_fiscais", matching=0.97, waiting_time=10000):
                    self.not_found("administrativo_com_livros_fiscais")
                self.click_relative(163, 27)
                self.type_down()
                self.enter()
                if not self.find( "administrativo_com_livros_fiscais", matching=0.97, waiting_time=10000):
                    self.not_found("administrativo_com_livros_fiscais")
                self.click_relative(163, 27)
                self.type_up()
                self.enter()
                if not self.find( "financeirocomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("financeirocomcontabilidade")
                self.click_relative(160, 22)
                self.type_down()
                self.enter()
                if not self.find( "financeirocomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("financeirocomcontabilidade")
                self.click_relative(160, 22)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_parametros_empresa_3_livros_conta", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_parametros_empresa_3_livros_conta")
                bot.click_relative(162, 28)
                self.click()
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_parametros_empresa_3_livros_conta", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_parametros_empresa_3_livros_conta")
                bot.click_relative(162, 28)
                self.type_up()
                self.enter()
                if not self.find( "estoquecomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("estoquecomcontabilidade")
                self.click_relative(164, 24)
                self.type_down()
                self.enter()
                if not self.find( "estoquecomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("estoquecomcontabilidade")
                self.click_relative(164, 24)
                self.type_up()
                self.enter()
                if not self.find( "gestaopessoalcomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("gestaopessoalcomcontabilidade")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                if not self.find( "gestaopessoalcomcontabilidade", matching=0.97, waiting_time=10000):
                    self.not_found("gestaopessoalcomcontabilidade")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                if not bot.find( "fatu_cad_parametros_6_alterar_lanc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_parametros_6_alterar_lanc")
                bot.click_relative(161, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_parametros_6_alterar_lanc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_parametros_6_alterar_lanc")
                bot.click_relative(161, 26)
                self.type_up()
                self.enter()
                if not self.find( "conhecimentoscomlivrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("conhecimentoscomlivrosfiscais")
                self.click_relative(165, 25)
                self.type_up()
                self.enter()
                if not self.find( "conhecimentoscomlivrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("conhecimentoscomlivrosfiscais")
                self.click_relative(165, 25)
                self.type_down()
                self.enter()
                
                                ####---DOC E---####
                                
                if not self.find( "utilizanfe", matching=0.97, waiting_time=10000):
                    self.not_found("utilizanfe")
                self.click_relative(161, 23)
                self.type_down()
                self.enter()
                if not self.find( "utilizanfe", matching=0.97, waiting_time=10000):
                    self.not_found("utilizanfe")
                self.click_relative(161, 23)
                self.type_up()
                self.enter()
                if not self.find( "mododeenvionfe", matching=0.97, waiting_time=10000):
                    self.not_found("mododeenvionfe")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                if not self.find( "mododeenvionfe", matching=0.97, waiting_time=10000):
                    self.not_found("mododeenvionfe")
                self.click_relative(162, 24)
                self.type_up()
                self.enter()
                if not self.find( "mododeenvionfce", matching=0.97, waiting_time=10000):
                    self.not_found("mododeenvionfce")
                self.click_relative(164, 24)
                self.type_down()
                self.enter()
                if not self.find( "mododeenvionfce", matching=0.97, waiting_time=10000):
                    self.not_found("mododeenvionfce")
                self.click_relative(164, 24)
                self.type_up()
                self.enter()
                if not self.find( "mododefinalizacaonfse", matching=0.97, waiting_time=10000):
                    self.not_found("mododefinalizacaonfse")
                self.click_relative(164, 27)
                self.type_down()
                self.enter()
                if not self.find( "mododefinalizacaonfse", matching=0.97, waiting_time=10000):
                    self.not_found("mododefinalizacaonfse")
                self.click_relative(164, 27)
                self.type_up()
                self.enter()
                if not self.find( "utilizanfsenfem", matching=0.97, waiting_time=10000):
                    self.not_found("utilizanfsenfem")
                self.click_relative(165, 25)
                self.type_up()
                self.enter()
                if not self.find( "utilizanfsenfem", matching=0.97, waiting_time=10000):
                    self.not_found("utilizanfsenfem")
                self.click_relative(165, 25)
                self.type_down()
                self.enter()
                
                                ####---VERIFICACOES E EXIGENCIAS---####
                                
                x=0
                while x < 4:
                    if not self.find( "verificarlimitedecredito", matching=0.97, waiting_time=10000):
                        self.not_found("verificarlimitedecredito")
                    self.click_relative(161, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x < 4:
                    if not self.find( "verificarlimitedecredito", matching=0.97, waiting_time=10000):
                        self.not_found("verificarlimitedecredito")
                    self.click_relative(161, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x < 4:
                    if not self.find( "verificasituacaocadastro", matching=0.97, waiting_time=10000):
                        self.not_found("verificasituacaocadastro")
                    self.click_relative(162, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x < 4:
                    if not self.find( "verificasituacaocadastro", matching=0.97, waiting_time=10000):
                        self.not_found("verificasituacaocadastro")
                    self.click_relative(162, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                    
                x=0
                while x<2:
                    if not self.find( "verificacnpjcpfduplicado", matching=0.97, waiting_time=10000):
                        self.not_found("verificacnpjcpfduplicado")
                    self.click_relative(164, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "verificacnpjcpfduplicado", matching=0.97, waiting_time=10000):
                        self.not_found("verificacnpjcpfduplicado")
                    self.click_relative(164, 24)
                    self.type_up()
                    self.enter()
                    x=x+1


                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_4_nivel_exigencia", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_nivel_exigencia")
                    bot.click_relative(163, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_4_nivel_exigencia", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_nivel_exigencia")
                    bot.click_relative(163, 23)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                if not bot.find( "fatu_cad_param_5_cadastro_macros", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_5_cadastro_macros")
                bot.click_relative(162, 27)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_5_cadastro_macros", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_5_cadastro_macros")
                bot.click_relative(162, 27)
                self.type_up()
                self.enter()
                
                x=0
                while x<4:
                    if not self.find( "atrasospagamentos", matching=0.97, waiting_time=10000):
                        self.not_found("atrasospagamentos")
                    self.click_relative(164, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                x=0
                while x<4:
                    if not self.find( "atrasospagamentos", matching=0.97, waiting_time=10000):
                        self.not_found("atrasospagamentos")
                    self.click_relative(164, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                
                x=0
                while x<3:
                    if not self.find( "verificarchequesnolimite", matching=0.97, waiting_time=10000):
                        self.not_found("verificarchequesnolimite")
                    self.click_relative(162, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "verificarchequesnolimite", matching=0.97, waiting_time=10000):
                        self.not_found("verificarchequesnolimite")
                    self.click_relative(162, 23)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                self.wait(1000)
                if not bot.find( "fatu_cad_param_9_modo_checagem", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_9_modo_checagem")
                bot.click_relative(163, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_9_modo_checagem", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_9_modo_checagem")
                bot.click_relative(163, 26)
                self.type_down()
                self.enter()
                
                self.wait(2000)
                            ####---ABA2 FINANCEIRO---####

                if not self.find( "aba2parametros", matching=0.97, waiting_time=10000):
                    self.not_found("aba2parametros")
                self.click()
                
                if not self.find( "baixaarecebermultiempresas", matching=0.97, waiting_time=10000):
                    self.not_found("baixaarecebermultiempresas")
                self.click_relative(160, 24)
                self.type_down()
                self.enter()
                if not self.find( "baixaarecebermultiempresas", matching=0.97, waiting_time=10000):
                    self.not_found("baixaarecebermultiempresas")
                self.click_relative(160, 24)
                self.type_up()
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "exportarobservacaonabaixa", matching=0.97, waiting_time=10000):
                        self.not_found("exportarobservacaonabaixa")
                    self.click_relative(162, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                y=0
                while y<3:
                    if not self.find( "exportarobservacaonabaixa", matching=0.97, waiting_time=10000):
                        self.not_found("exportarobservacaonabaixa")
                    self.click_relative(162, 27)
                    self.type_down()
                    self.enter()
                    y=y+1    
                
                
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_3_exigencia_financeiro", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_3_exigencia_financeiro")
                    bot.click_relative(163, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                y=0
                while y<3:
                    if not bot.find( "fatu_cad_param_3_exigencia_financeiro", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_3_exigencia_financeiro")
                    bot.click_relative(163, 25)        
                    self.type_down()
                    y=y+1
                self.enter()
                
                
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_4_exigencia_centro_custo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_exigencia_centro_custo")
                    bot.click_relative(223, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:
                    if not bot.find( "fatu_cad_param_4_exigencia_centro_custo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_exigencia_centro_custo")
                    bot.click_relative(223, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_4_exigencia_centro_custo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_exigencia_centro_custo")
                    bot.click_relative(223, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_5_exigencia_classificacao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_5_exigencia_classificacao")
                    bot.click_relative(162, 22)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_5_exigencia_classificacao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_5_exigencia_classificacao")
                    bot.click_relative(162, 22)
                    self.type_down()
                    self.enter()
                    x=x+1
                

                x=0
                while x<2:
                    if not self.find( "exigencialocaldecobranca", matching=0.97, waiting_time=10000):
                        self.not_found("exigencialocaldecobranca")
                    self.click_relative(162, 24)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "exigencialocaldecobranca", matching=0.97, waiting_time=10000):
                        self.not_found("exigencialocaldecobranca")
                self.click_relative(162, 24)
                self.type_down()
                self.type_down()
                self.enter()
                
                x=0
                while x<2:
                    if not self.find( "quandodiavencefds", matching=0.97, waiting_time=10000):
                        self.not_found("quandodiavencefds")
                    self.click_relative(163, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "quandodiavencefds", matching=0.97, waiting_time=10000):
                    self.not_found("quandodiavencefds")
                self.click_relative(163, 25)
                self.type_up()
                self.type_up()
                self.enter()
                
                x=0
                while x<4:
                    if not self.find( "valordaparcelamenorqueminimo", matching=0.97, waiting_time=10000):
                        self.not_found("valordaparcelamenorqueminimo")
                    self.click_relative(163, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "valordaparcelamenorqueminimo", matching=0.97, waiting_time=10000):
                        self.not_found("valordaparcelamenorqueminimo")
                    self.click_relative(163, 26)
                    self.type_up() 
                    self.enter()               
                    x=x+1                   
        
                
                if not self.find( "somarcobrancabancariaavalor", matching=0.97, waiting_time=10000):
                    self.not_found("somarcobrancabancariaavalor")
                self.click_relative(162, 23)
                self.type_up()
                self.enter()
                if not self.find( "somarcobrancabancariaavalor", matching=0.97, waiting_time=10000):
                    self.not_found("somarcobrancabancariaavalor")
                self.click_relative(162, 23)
                self.type_down()
                self.enter()
                
                if not bot.find( "fatu_cad_param_10_operacao_cheques", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_10_operacao_cheques")
                bot.click_relative(162, 27)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_10_operacao_cheques", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_10_operacao_cheques")
                bot.click_relative(162, 27)
                self.type_up()
                self.enter()
                
                if not self.find( "tipocontabilizacaobaixa", matching=0.97, waiting_time=10000):
                    self.not_found("tipocontabilizacaobaixa")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                if not self.find( "tipocontabilizacaobaixa", matching=0.97, waiting_time=10000):
                    self.not_found("tipocontabilizacaobaixa")
                self.click_relative(161, 24)
                self.type_up()
                self.enter()
                
                x=0
                while x < 2:
                    if not bot.find( "fatu_cad_param_12_permitir_desconto_durante_baixa", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_12_permitir_desconto_durante_baixa")
                    bot.click_relative(161, 25)

                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_12_permitir_desconto_durante_baixa", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_12_permitir_desconto_durante_baixa")
                    bot.click_relative(161, 25)

                    self.type_up()
                    x=x+1
                self.enter()
                
                if not self.find( "chequeemitidocamponominal", matching=0.97, waiting_time=10000):
                    self.not_found("chequeemitidocamponominal")
                self.click_relative(159, 24)
                self.type_down()
                self.enter()
                if not self.find( "chequeemitidocamponominal", matching=0.97, waiting_time=10000):
                    self.not_found("chequeemitidocamponominal")
                self.click_relative(159, 24)
                self.type_up()
                self.enter()
                
                if not self.find( "op_encontrodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("op_encontrodecontas")
                
                self.click_relative(164, 27)
                self.type_up()
                self.enter()
                if not self.find( "op_encontrodecontas", matching=0.97, waiting_time=10000):
                    self.not_found("op_encontrodecontas")
                self.click_relative(164, 27)
                self.type_down()
                self.enter()
                
                
                
                x=0
                while x<2:
                    if not self.find( "agrupartitulosfornecedores", matching=0.97, waiting_time=10000):
                        self.not_found("agrupartitulosfornecedores")
                    self.click_relative(167, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "agrupartitulosfornecedores", matching=0.97, waiting_time=10000):
                        self.not_found("agrupartitulosfornecedores")
                    self.click_relative(167, 24)
                    self.type_up()
                    x=x+1
                
                self.enter()
                
                if not self.find( "prazominimoconvenio", matching=0.97, waiting_time=10000):
                    self.not_found("prazominimoconvenio")
                self.click_relative(99, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "prazominimoconvenio", matching=0.97, waiting_time=10000):
                    self.not_found("prazominimoconvenio")
                self.click_relative(163, 23)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                                ####---REAJUSTES JUROS MORA E MULTA---####
                                
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "jurosdemora", matching=0.97, waiting_time=10000):
                    self.not_found("jurosdemora")
                self.click_relative(167, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "tipodoreajustejurosdemora", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoreajustejurosdemora")
                self.click_relative(165, 27)
                self.type_down()
                self.enter()
                if not self.find( "tipodoreajustejurosdemora", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoreajustejurosdemora")
                self.click_relative(165, 27)
                self.type_up()
                self.enter()
                if not self.find( "tipocalculojuros1", matching=0.97, waiting_time=10000):
                    self.not_found("tipocalculojuros1")
                self.click_relative(164, 25)           
                self.type_down()
                self.enter()
                if not self.find( "tipocalculojuros1", matching=0.97, waiting_time=10000):
                    self.not_found("tipocalculojuros1")
                self.click_relative(164, 25)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "multa", matching=0.97, waiting_time=10000):
                    self.not_found("multa")
                self.click_relative(161, 24)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "tipodoreajustemulta", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoreajustemulta")
                self.click_relative(163, 23)
                self.type_down()
                self.enter()
                if not self.find( "tipodoreajustemulta", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoreajustemulta")
                self.click_relative(163, 23)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.tab()                       
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "diastoleranciavencimentoparcial", matching=0.97, waiting_time=10000):
                    self.not_found("diastoleranciavencimentoparcial")
                self.click_relative(165, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "diastoleranciaatrasobalcao", matching=0.97, waiting_time=10000):
                    self.not_found("diastoleranciaatrasobalcao")
                self.click_relative(165, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                            ####---DESCONTO DE RECEBIMENTOS---####
        
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "desconto", matching=0.97, waiting_time=10000):
                    self.not_found("desconto")
                self.click_relative(162, 23)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "tipododesconto", matching=0.97, waiting_time=10000):
                        self.not_found("tipododesconto")
                    self.click_relative(162, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:
                    if not bot.find( "fatu_cad_empresas_2_tipo_de_desconto", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_empresas_2_tipo_de_desconto")
                    bot.click_relative(163, 24)
                    self.type_up()
                    x=x+1
                
                self.enter()
                
                if not self.find( "tipocalculoquevaidarcerto", matching=0.97, waiting_time=10000):
                    self.not_found("tipocalculoquevaidarcerto")
                self.click_relative(654, 43)           
                self.type_down()
                self.enter()
                if not self.find( "tipocalculoquevaidarcerto", matching=0.97, waiting_time=10000):
                    self.not_found("tipocalculoquevaidarcerto")
                self.click_relative(654, 43) 
                self.type_up()
                self.enter()            
                self.type_keys_with_interval(1,'123')
                if not self.find( "diascarenciareajuste", matching=0.97, waiting_time=10000):
                    self.not_found("diascarenciareajuste")
                self.click_relative(163, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                if not self.find( "valorbordero", matching=0.97, waiting_time=10000):
                    self.not_found("valorbordero")
                self.click_relative(164, 24)
                self.type_down()
                self.enter()
                if not self.find( "valorbordero", matching=0.97, waiting_time=10000):
                    self.not_found("valorbordero")
                self.click_relative(164, 24)
                self.type_up()
                self.enter()
                

                ###################################################################################
                ##########################---ABA 3 GESTAO ADM/VAREJO---############################
                self.wait(2000)     
                if not self.find( "aba3paemp", matching=0.97, waiting_time=10000):
                    self.not_found("aba3paemp")
                self.click()
                if not self.find( "subir_tela_parametros", matching=0.97, waiting_time=10000):
                    self.not_found("subir_tela_parametros")
                self.click()
                x=0
                while x<7:
                    if not self.find( "subir_tela_parametros2", matching=0.97, waiting_time=10000):
                        self.not_found("subir_tela_parametros2")
                    self.double_click()
                    x=x+1

                x=0
                while x<8:
                    if not self.find( "tipodametadosvendedores", matching=0.97, waiting_time=10000):
                        self.not_found("tipodametadosvendedores")
                    self.click_relative(211, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<8:
                    if not self.find( "tipodametadosvendedores", matching=0.97, waiting_time=10000):
                        self.not_found("tipodametadosvendedores")
                    self.click_relative(211, 24)
                    self.type_up()
                    self.enter()
                    x=x+1

                
                if not self.find( "calculocomissaoitens", matching=0.97, waiting_time=10000):
                    self.not_found("calculocomissaoitens")
                self.click_relative(216, 25)
                self.type_down()
                self.enter()
                if not self.find( "calculocomissaoitens", matching=0.97, waiting_time=10000):
                    self.not_found("calculocomissaoitens")
                self.click_relative(216, 25)
                self.type_up()
                self.enter()
                
                
                x=0
                while x<6:
                    if not self.find( "tipolimiteparacompradores", matching=0.97, waiting_time=10000):
                        self.not_found("tipolimiteparacompradores")               
                    self.click_relative(215, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                    
                x=0
                while x<5:
                    if not self.find( "tipolimiteparacompradores", matching=0.97, waiting_time=10000):
                        self.not_found("tipolimiteparacompradores")
                    self.click_relative(215, 27)
                    self.type_up()
                    self.enter()
                    x=x+1    
                    
                
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_4_empresa_metas_limites", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_empresa_metas_limites")
                    bot.click_relative(215, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_4_empresa_metas_limites", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_4_empresa_metas_limites")
                    bot.click_relative(215, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                self.enter()
                    
                                ####---GERAIS---####
                                
                if not self.find( "recalculocustomediotravaperiodo", matching=0.97, waiting_time=10000):
                    self.not_found("recalculocustomediotravaperiodo")
                self.click_relative(210, 24)
                self.type_up()
                self.enter()
                if not self.find( "recalculocustomediotravaperiodo", matching=0.97, waiting_time=10000):
                    self.not_found("recalculocustomediotravaperiodo")
                self.click_relative(210, 24)
                self.type_down()
                self.enter()
                
                if not bot.find( "fatu_cad_param_2_calcular_precos_pre_lanc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_calcular_precos_pre_lanc")
                bot.click_relative(213, 25)
                self.type_up()
                self.enter()
                if not bot.find( "fatu_cad_param_2_calcular_precos_pre_lanc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_calcular_precos_pre_lanc")
                bot.click_relative(213, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "abrirteladecalculodepreco", matching=0.97, waiting_time=10000):
                    self.not_found("abrirteladecalculodepreco")
                self.click_relative(212, 22)
                self.type_up()
                self.enter()
                if not self.find( "abrirteladecalculodepreco", matching=0.97, waiting_time=10000):
                    self.not_found("abrirteladecalculodepreco")
                self.click_relative(212, 22)
                self.type_down()
                self.enter()
                
                if not self.find( "adicionarfornecedorepreconositens", matching=0.97, waiting_time=10000):
                    self.not_found("adicionarfornecedorepreconositens")
                self.click_relative(210, 23)
                self.type_up()
                self.enter()
                if not self.find( "adicionarfornecedorepreconositens", matching=0.97, waiting_time=10000):
                    self.not_found("adicionarfornecedorepreconositens")
                self.click_relative(210, 23)
                self.type_down()
                self.enter()
                
                x=0
                while x<9:
                    if not self.find( "situacaofiscalnaoencontrada", matching=0.97, waiting_time=10000):
                        self.not_found("situacaofiscalnaoencontrada")
                    self.click_relative(212, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<9:
                    if not self.find( "situacaofiscalnaoencontrada", matching=0.97, waiting_time=10000):
                        self.not_found("situacaofiscalnaoencontrada")
                    self.click_relative(212, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "codificarocusto", matching=0.97, waiting_time=10000):
                    self.not_found("codificarocusto")
                self.click_relative(211, 26)
                self.type_up()
                self.enter()
                if not self.find( "codificarocusto", matching=0.97, waiting_time=10000):
                    self.not_found("codificarocusto")
                self.click_relative(211, 26)
                self.type_down()
                self.enter()
                
                if not bot.find( "fatu_cad_param_7_codificao_do_custo", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_7_codificao_do_custo")
                bot.click_relative(33, 22)
                self.type_keys_with_interval(1,'te12!@')
                
                if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                    self.not_found("letraduplicidade")
                self.click_relative(41, 27)
                self.type_keys_with_interval(1,'t')
                self.enter()
                if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                    self.not_found("letraduplicidade")
                self.click_relative(41, 27)
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.enter()
                if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                    self.not_found("letraduplicidade")
                self.click_relative(41, 27)
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.enter()
                
                x=0
                while x<6:
                    if not bot.find( "fatu_cad_param_9_duplicidade_es_movt", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_9_duplicidade_es_movt")
                    bot.click_relative(214, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<6:
                    if not bot.find( "fatu_cad_param_9_duplicidade_es_movt", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_9_duplicidade_es_movt")
                    bot.click_relative(214, 24)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                                ####---ITENS---####
                                
                x=0
                while x<6:
                    if not self.find( "custodoitemaexibirnaconsulta", matching=0.97, waiting_time=10000):
                        self.not_found("custodoitemaexibirnaconsulta")
                    self.click_relative(210, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<6:
                    if not self.find( "custodoitemaexibirnaconsulta", matching=0.97, waiting_time=10000):
                        self.not_found("custodoitemaexibirnaconsulta")
                    self.click_relative(210, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                if not self.find( "permitecadastraritens", matching=0.97, waiting_time=10000):
                    self.not_found("permitecadastraritens")
                self.click_relative(210, 24)
                self.type_up()
                self.enter()
                if not self.find( "permitecadastraritens", matching=0.97, waiting_time=10000):
                    self.not_found("permitecadastraritens")
                self.click_relative(210, 24)
                self.type_down()
                self.enter()
                
                x=0
                while x<2:
                    if not self.find( "exigenciadocentrodecusto", matching=0.97, waiting_time=10000):
                        self.not_found("exigenciadocentrodecusto")
                    self.click_relative(212, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "exigenciadocentrodecusto", matching=0.97, waiting_time=10000):
                        self.not_found("exigenciadocentrodecusto")
                    self.click_relative(212, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "tipodocodigodebarrasdoitem", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocodigodebarrasdoitem")
                    self.click_relative(213, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "tipodocodigodebarrasdoitem", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocodigodebarrasdoitem")
                    self.click_relative(213, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                                ####---MOVIMENTOS---####

                if not self.find( "entradadeitenscontabilizacao", matching=0.97, waiting_time=10000):
                    self.not_found("entradadeitenscontabilizacao")
                self.click_relative(211, 23)
                self.type_up()
                self.enter()
                if not self.find( "entradadeitenscontabilizacao", matching=0.97, waiting_time=10000):
                    self.not_found("entradadeitenscontabilizacao")
                self.click_relative(211, 23)
                self.type_down()
                self.enter()
                
                if not bot.find( "fatu_cad_param_2_permite_inclusao_de_itens_importacao", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_permite_inclusao_de_itens_importacao")
                bot.click_relative(213, 23)
                self.type_up()
                self.enter()
                if not bot.find( "fatu_cad_param_2_permite_inclusao_de_itens_importacao", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_permite_inclusao_de_itens_importacao")
                bot.click_relative(213, 23)
                self.type_down()
                self.enter()
                
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_3_manutencao_preco_abaixo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_3_manutencao_preco_abaixo")
                    bot.click_relative(212, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_3_manutencao_preco_abaixo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_3_manutencao_preco_abaixo")
                    bot.click_relative(212, 24)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "percentualdetolerancia", matching=0.97, waiting_time=10000):
                    self.not_found("percentualdetolerancia")
                self.click_relative(212, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                if not self.find( "valoresdemovimentacao", matching=0.97, waiting_time=10000):
                    self.not_found("valoresdemovimentacao")
                self.click_relative(212, 26)
                self.type_down()
                self.enter()
                if not self.find( "valoresdemovimentacao", matching=0.97, waiting_time=10000):
                    self.not_found("valoresdemovimentacao")
                self.click_relative(212, 26)
                self.type_up()
                self.enter()
                
                if not bot.find( "fatu_cad_param_5_transferencias_itens_empresa", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_5_transferencias_itens_empresa")
                bot.click_relative(207, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_5_transferencias_itens_empresa", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_5_transferencias_itens_empresa")
                bot.click_relative(207, 26)
                self.type_up()
                self.enter()
                
                if not self.find( "geratransferencialiberada", matching=0.97, waiting_time=10000):
                    self.not_found("geratransferencialiberada")
                self.click_relative(210, 26)
                self.type_down()
                self.enter()
                if not self.find( "geratransferencialiberada", matching=0.97, waiting_time=10000):
                    self.not_found("geratransferencialiberada")
                self.click_relative(210, 26)
                self.type_up()
                self.enter()
                
                if not self.find( "exigirlancamentocentrocustos", matching=0.97, waiting_time=10000):
                    self.not_found("exigirlancamentocentrocustos")
                self.click_relative(208, 25)
                self.type_up()
                self.enter()
                if not self.find( "exigirlancamentocentrocustos", matching=0.97, waiting_time=10000):
                    self.not_found("exigirlancamentocentrocustos")
                self.click_relative(208, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                    self.not_found("bloquearliberacaomovitens")
                self.click_relative(258, 25)
                self.type_down()
                self.enter()
                if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                    self.not_found("bloquearliberacaomovitens")
                self.click_relative(258, 25)
                self.type_down()
                self.enter()
                if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                    self.not_found("bloquearliberacaomovitens")
                self.click_relative(258, 25)
                self.type_up()
                self.enter()
                
                                ####---PERCENTUAIS E ARREDONDAMENTOS---####     

                
                if not self.find( "numerocasasdecimaiscustos", matching=0.97, waiting_time=10000):
                    self.not_found("numerocasasdecimaiscustos")
                self.double_click_relative(122, 22)            
                if not self.find( "numerocasasdecimaiscustos", matching=0.97, waiting_time=10000):
                    self.not_found("numerocasasdecimaiscustos")
                self.click_relative(121, 31)    
                self.backspace()
                self.type_keys_with_interval(1,'1')
                
                if not self.find( "ncasasdecimaisprecovenda1", matching=0.97, waiting_time=10000):
                    self.not_found("ncasasdecimaisprecovenda1")
                self.double_click_relative(122, 19)
                self.backspace()
                self.type_keys_with_interval(1,'1') 
                if not self.find( "numerocasasdecimaisquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("numerocasasdecimaisquantidade")
                self.double_click_relative(125, 23)
                if not self.find( "numerocasasdecimaisquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("numerocasasdecimaisquantidade")
                self.click_relative(123, 30)             
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'1')            
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "calculocustooperacional", matching=0.97, waiting_time=10000):
                    self.not_found("calculocustooperacional")
                self.click_relative(15, 25)             
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "calculopis", matching=0.97, waiting_time=10000):
                    self.not_found("calculopis")
                self.click_relative(-1, 27)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "calculocofins", matching=0.97, waiting_time=10000):
                    self.not_found("calculocofins")
                self.click_relative(2, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "calculodebitoicms", matching=0.97, waiting_time=10000):
                    self.not_found("calculodebitoicms")
                self.click_relative(-1, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                #if not self.find( "calculoprecoscomissao", matching=0.97, waiting_time=10000):
                #    self.not_found("calculoprecoscomissao")
                #self.click_relative(125, 26)           
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not bot.find( "fatu_cad_param_9_origem_pis_cofins", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_9_origem_pis_cofins")
                bot.click_relative(122, 25)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_9_origem_pis_cofins", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_9_origem_pis_cofins")
                bot.click_relative(122, 25)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "curvaA", matching=0.97, waiting_time=10000):
                    self.not_found("curvaA")
                self.click_relative(122, 22)
                self.type_keys_with_interval(1,'20')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "curvaB", matching=0.97, waiting_time=10000):
                    self.not_found("curvaB")
                self.click_relative(125, 25)
                self.type_keys_with_interval(1,'20')
                self.enter()
                self.enter()
                if not self.find( "curvaC", matching=0.97, waiting_time=10000):
                    self.not_found("curvaC")
                self.click_relative(124, 27)
                self.type_keys_with_interval(1,'60')
                self.enter()
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixatelaparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatelaparametrosempresa")
                self.click()
                
                x=0
                while x<7:
                    if not self.find( "abaixartelamarcadaparametrosempresa", matching=0.97, waiting_time=10000):
                        self.not_found("abaixartelamarcadaparametrosempresa")
                    self.double_click()
                    x=x+1
                
                                ####--- VENDAS---####
                self.wait(2000)

                if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                    self.not_found("infopadraofrete")
                self.click_relative(213, 25)
                self.type_up()
                self.enter()
                
                x=0
                while x<5:
                    if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                        self.not_found("infopadraofrete")
                    self.click_relative(213, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                            self.not_found("infopadraofrete")
                    self.click_relative(213, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                self.wait(2000)
                if not bot.find( "fatu_cad_param_2_situacao_cliente_gerar_pedido", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_situacao_cliente_gerar_pedido")
                bot.click_relative(209, 24)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_2_situacao_cliente_gerar_pedido", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_situacao_cliente_gerar_pedido")
                bot.click_relative(209, 24)
                self.type_down()
                self.enter()
                if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                    self.not_found("validarsituacaoclientegerarpedido")
                self.click_relative(213, 25)
                self.type_up()
                self.enter() 
                
                if not bot.find( "fatu_cad_param_3_reservar_esto_orc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_3_reservar_esto_orc")
                bot.click_relative(212, 25)
                self.type_down()
                self.enter() 
                if not bot.find( "fatu_cad_param_3_reservar_esto_orc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_3_reservar_esto_orc")
                bot.click_relative(212, 25)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_3_reservar_esto_orc", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_3_reservar_esto_orc")
                bot.click_relative(212, 25)
                self.type_up()
                self.enter()
                
                x=0
                while x<5:
                    if not self.find( "custoparacalculodasmargens", matching=0.97, waiting_time=10000):
                        self.not_found("custoparacalculodasmargens")
                    self.click_relative(215, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<5:
                    if not self.find( "custoparacalculodasmargens", matching=0.97, waiting_time=10000):
                        self.not_found("custoparacalculodasmargens")
                    self.click_relative(215, 24)
                    self.type_up()
                    self.enter()
                    x=x+1 
                
                x=0
                while x<2:
                    if not self.find( "utilizadataentregavendas", matching=0.97, waiting_time=10000):
                        self.not_found("utilizadataentregavendas")
                    self.click_relative(214, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<2:
                    if not self.find( "utilizadataentregavendas", matching=0.97, waiting_time=10000):
                        self.not_found("utilizadataentregavendas")
                    self.click_relative(214, 27)
                    self.type_up()
                    self.enter()
                    x=x+1    
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_6_lancar_itens_sem_data_entrega", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_6_lancar_itens_sem_data_entrega")
                    bot.click_relative(211, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<2:
                    if not bot.find( "fatu_cad_param_6_lancar_itens_sem_data_entrega", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_6_lancar_itens_sem_data_entrega")
                    bot.click_relative(211, 27)
                    self.type_up()
                    self.enter()
                    x=x+1     
                x=0
                while x<2:
                    if not self.find( "calcularquantidadeparaconfirmacao", matching=0.97, waiting_time=10000):
                        self.not_found("calcularquantidadeparaconfirmacao")
                    self.click_relative(215, 24)
                    self.type_down()
                    self.enter()
                    x=x+1 
                x=0
                while x<2:
                    if not self.find( "calcularquantidadeparaconfirmacao", matching=0.97, waiting_time=10000):
                        self.not_found("calcularquantidadeparaconfirmacao")
                    self.click_relative(215, 24)
                    self.type_up
                    ()
                    self.enter()
                    x=x+1
                
                self.wait(2000)
                                ####---ABA 4 VENDAS---####

                if not self.find( "aba4vendasparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("aba4vendasparametrosempresa")
                self.click()
                
                                ####---SUBIR TELA---####
                
                if not self.find( "subirtelaparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelaparametrosempresa")
                self.click()
                
                x=0
                while x<5:
                    if not self.find( "subirtelaparametrosempresa2", matching=0.97, waiting_time=10000):
                        self.not_found("subirtelaparametrosempresa2")
                    self.click()
                    x=x+1
                
                                ####---CONFIGURACOES---####
                
                if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                    self.not_found("informarcomissao")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                    
                x=0
                while x<3:
                    if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                        self.not_found("informarcomissao")
                    self.click_relative(162, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                        self.not_found("informarcomissao")
                    self.click_relative(162, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "lotedeitensnospedidosdevenda", matching=0.97, waiting_time=10000):
                    self.not_found("lotedeitensnospedidosdevenda")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                if not self.find( "lotedeitensnospedidosdevenda", matching=0.97, waiting_time=10000):
                    self.not_found("lotedeitensnospedidosdevenda")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
            
                if not self.find( "saldodopedidonanfdesaida", matching=0.97, waiting_time=10000):
                    self.not_found("saldodopedidonanfdesaida")
                self.click_relative(163, 27)
                self.type_up()
                self.enter()
                if not self.find( "saldodopedidonanfdesaida", matching=0.97, waiting_time=10000):
                    self.not_found("saldodopedidonanfdesaida")
                self.click_relative(163, 27)
                self.type_down()
                self.enter()
            
                x=0
                while x<6:
                    if not self.find( "senhamargemminimavendas", matching=0.97, waiting_time=10000):
                        self.not_found("senhamargemminimavendas")
                    self.click_relative(162, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<6:
                    if not self.find( "senhamargemminimavendas", matching=0.97, waiting_time=10000):
                        self.not_found("senhamargemminimavendas")
                    self.click_relative(162, 28)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                if not self.find( "margemminimavendas", matching=0.97, waiting_time=10000):
                    self.not_found("margemminimavendas")
                self.click_relative(162, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                x=0
                while x<2:
                    if not self.find( "custoparachecagemdamargemminima", matching=0.97, waiting_time=10000):
                        self.not_found("custoparachecagemdamargemminima")
                    self.click_relative(159, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:
                    if not self.find( "custoparachecagemdamargemminima", matching=0.97, waiting_time=10000):
                        self.not_found("custoparachecagemdamargemminima")
                    self.click_relative(159, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "aoimprimirvendasexibir", matching=0.97, waiting_time=10000):
                    self.not_found("aoimprimirvendasexibir")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                
                x=0
                while x<23:
                    if not self.find( "aoimprimirvendasexibir", matching=0.97, waiting_time=10000):
                        self.not_found("aoimprimirvendasexibir")
                    self.click_relative(161, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_8_item_sem_estoque_pedido", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_8_item_sem_estoque_pedido")
                    bot.click_relative(161, 23)
                    self.type_down()    
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:
                    if not self.find( "ordemdeimpressaopedidosenf", matching=0.97, waiting_time=10000):
                        self.not_found("ordemdeimpressaopedidosenf")
                    self.click_relative(159, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_10_cdg_imprimir_pedidos", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_10_cdg_imprimir_pedidos")
                    bot.click_relative(162, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_11_cdg_imprimir_ballcao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_11_cdg_imprimir_ballcao")
                    bot.click_relative(162, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_12_cdg_imprimir_condicionais", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_12_cdg_imprimir_condicionais")
                    bot.click_relative(161, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "linhasimpressaoformulariovendas", matching=0.97, waiting_time=10000):
                    self.not_found("linhasimpressaoformulariovendas")
                self.double_click_relative(159, 20)
                if not self.find( "linhasimpressaoformulariovendas2", matching=0.97, waiting_time=10000):
                    self.not_found("linhasimpressaoformulariovendas2")
                self.click_relative(160, 30)
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.enter()
                
                if not self.find( "ondeimprimironomedovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("ondeimprimironomedovendedor")
                self.click_relative(161, 27)
                self.type_up()
                self.enter()
                
                x=0
                while x<11:
                    if not self.find( "ondeimprimironomedovendedor", matching=0.97, waiting_time=10000):
                        self.not_found("ondeimprimironomedovendedor")
                    self.click_relative(161, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "mascaranrocontrole", matching=0.97, waiting_time=10000):
                    self.not_found("mascaranrocontrole")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                
                if not self.find( "vendaitemsemestoque", matching=0.97, waiting_time=10000):
                    self.not_found("vendaitemsemestoque")
                self.click_relative(161, 24)
                self.type_up()
                self.enter()
                if not self.find( "vendaitemsemestoque", matching=0.97, waiting_time=10000):
                    self.not_found("vendaitemsemestoque")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()        
                
                x=0
                while x<4:
                    if not self.find( "lancamentoitememduplicidade", matching=0.97, waiting_time=10000):
                        self.not_found("lancamentoitememduplicidade")
                    self.click_relative(162, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "itenscomtabeladopcalc", matching=0.97, waiting_time=10000):
                    self.not_found("itenscomtabeladopcalc")
                self.click_relative(165, 28)
                self.type_down()
                self.enter()
                if not self.find( "itenscomtabeladopcalc", matching=0.97, waiting_time=10000):
                    self.not_found("itenscomtabeladopcalc")
                self.click_relative(165, 28)
                self.type_up()
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "exigenciadotransportadornavenda", matching=0.97, waiting_time=10000):
                        self.not_found("exigenciadotransportadornavenda")
                    self.click_relative(165, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "exigenciadeclassificacao", matching=0.97, waiting_time=10000):
                        self.not_found("exigenciadeclassificacao")
                    self.click_relative(162, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "exigenciadovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadovendedor")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                if not self.find( "exigenciadovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadovendedor")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                
                x=0
                while x<4:
                    if not bot.find( "fatu_cad_param_23_margem_minima_vendas_balcao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_23_margem_minima_vendas_balcao")
                    bot.click_relative(160, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not bot.find( "fatu_cad_param_24_modo_valida_pedido", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_24_modo_valida_pedido")
                bot.click_relative(160, 27)
                self.type_down()
                self.enter()  
                if not bot.find( "fatu_cad_param_24_modo_valida_pedido", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_24_modo_valida_pedido")
                bot.click_relative(160, 27)
                self.type_up()
                self.enter()
                
                if not self.find( "capturapeso", matching=0.97, waiting_time=10000):
                    self.not_found("capturapeso")
                self.click_relative(163, 27)
                self.type_up()
                self.enter()
                if not self.find( "capturapeso", matching=0.97, waiting_time=10000):
                    self.not_found("capturapeso")
                self.click_relative(163, 27)
                self.type_down()
                self.enter() 
                    
                if not self.find( "planoprecoaotrocarcliente", matching=0.97, waiting_time=10000):
                    self.not_found("planoprecoaotrocarcliente")
                self.click_relative(163, 26)
                self.type_up()
                self.enter()
                if not self.find( "planoprecoaotrocarcliente", matching=0.97, waiting_time=10000):
                    self.not_found("planoprecoaotrocarcliente")
                self.click_relative(163, 26)
                self.type_down()
                self.enter() 
                
                if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                    self.not_found("ordemdeservicoopcoes")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                    self.not_found("ordemdeservicoopcoes")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                    self.not_found("ordemdeservicoopcoes")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "alteracaodovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodovendedor")
                self.click_relative(164, 25)
                self.type_down()
                self.enter() 
                if not self.find( "alteracaodovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodovendedor")
                self.click_relative(164, 25)
                self.type_up()
                self.enter()
                
                if not bot.find( "fatu_cad_param_29_mostrar_autom_itens", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_29_mostrar_autom_itens")
                bot.click_relative(160, 23)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_29_mostrar_autom_itens", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_29_mostrar_autom_itens")
                bot.click_relative(160, 23)
                self.type_up()
                self.enter()
                
                if not self.find( "conferenciarecuperarvenda", matching=0.97, waiting_time=10000):
                    self.not_found("conferenciarecuperarvenda")
                self.click_relative(164, 23)
                self.type_down()
                self.enter()
                if not self.find( "conferenciarecuperarvenda", matching=0.97, waiting_time=10000):
                    self.not_found("conferenciarecuperarvenda")
                self.click_relative(164, 23)
                self.type_up()
                self.enter()
                
                if not self.find( "vendapdvfechapedidoimportado", matching=0.97, waiting_time=10000):
                    self.not_found("vendapdvfechapedidoimportado")
                self.click_relative(161, 26)
                self.type_down()
                self.enter()
                if not self.find( "vendapdvfechapedidoimportado", matching=0.97, waiting_time=10000):
                    self.not_found("vendapdvfechapedidoimportado")
                self.click_relative(161, 26)
                self.type_up()
                self.enter()
                
                                ####---ABAIXAR TELA---####
                
                if not self.find( "abaixatelaparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatelaparametrosempresa")
                self.click()
                
                x=0
                while x<17:
                    if not self.find( "abaixartelamarcadaparametrosempresa", matching=0.97, waiting_time=10000):
                        self.not_found("abaixartelamarcadaparametrosempresa")
                    self.double_click()
                    x=x+1
                    
                                ####---PERMISSOES 1---####
                                
                if not self.find( "informardatavencimentoitem", matching=0.97, waiting_time=10000):
                    self.not_found("informardatavencimentoitem")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                if not self.find( "informardatavencimentoitem", matching=0.97, waiting_time=10000):
                    self.not_found("informardatavencimentoitem")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "permitealterarquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("permitealterarquantidade")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                if not self.find( "permitealterarquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("permitealterarquantidade")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                
                if not self.find( "utilizarplanodeprecosdeitens", matching=0.97, waiting_time=10000):
                    self.not_found("utilizarplanodeprecosdeitens")
                self.click_relative(163, 25)
                self.type_up()
                self.enter()
                if not self.find( "utilizarplanodeprecosdeitens", matching=0.97, waiting_time=10000):
                    self.not_found("utilizarplanodeprecosdeitens")
                self.click_relative(163, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                    self.not_found("impressaodedocumentosposvenda")
                self.click_relative(163, 25)
                self.type_up()
                self.enter()
                if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                    self.not_found("impressaodedocumentosposvenda")
                self.click_relative(163, 25)
                self.type_up()
                self.enter()
                x=0
                while x<3:
                    if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                        self.not_found("impressaodedocumentosposvenda")
                    self.click_relative(163, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "impressaoderecibodeentrada", matching=0.97, waiting_time=10000):
                    self.not_found("impressaoderecibodeentrada")
                self.click_relative(165, 26)
                self.type_up()
                self.enter()
                if not self.find( "impressaoderecibodeentrada", matching=0.97, waiting_time=10000):
                    self.not_found("impressaoderecibodeentrada")
                self.click_relative(165, 26)
                self.type_down()
                self.enter()
                
                if not bot.find( "fatu_cad_param_6_utilizar_cartao_fechamento", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_6_utilizar_cartao_fechamento")
                bot.click_relative(164, 28)
                self.type_up()
                self.enter()
                if not bot.find( "fatu_cad_param_6_utilizar_cartao_fechamento", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_6_utilizar_cartao_fechamento")
                bot.click_relative(164, 28)
                self.type_down()
                self.enter()
                if not self.find( "utilizarcartaodefechamento", matching=0.97, waiting_time=10000):
                    self.not_found("utilizarcartaodefechamento")
                self.click_relative(164, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "exigirobsparacheques", matching=0.97, waiting_time=10000):
                    self.not_found("exigirobsparacheques")
                self.click_relative(164, 25)
                self.type_up()
                self.enter()
                if not self.find( "exigirobsparacheques", matching=0.97, waiting_time=10000):
                    self.not_found("exigirobsparacheques")
                self.click_relative(164, 25)
                self.type_down()
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "alterardescricaodoitem", matching=0.97, waiting_time=10000):
                        self.not_found("alterardescricaodoitem")
                    self.click_relative(161, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "permitirdescontoindividual", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontoindividual")
                self.click_relative(162, 24)
                self.type_up()
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "permitirdescontoindividual", matching=0.97, waiting_time=10000):
                        self.not_found("permitirdescontoindividual")
                    self.click_relative(162, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                if not self.find( "quandoemofertabalcao", matching=0.97, waiting_time=10000):
                    self.not_found("quandoemofertabalcao")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                if not self.find( "quandoemofertabalcao", matching=0.97, waiting_time=10000):
                    self.not_found("quandoemofertabalcao")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                
                if not self.find( "permitirdescontogeralna", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontogeralna")
                self.click_relative(161, 27)
                self.type_up()
                self.enter()
                if not self.find( "permitirdescontogeralna", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontogeralna")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                #if not self.find( "percentualmaximodescontogeral", matching=0.97, waiting_time=10000):
                #    self.not_found("percentualmaximodescontogeral")
                #self.click_relative(160, 26)
                self.type_keys_with_interval(1,'123')
                
                if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodeprecounitarioitem")
                self.click_relative(165, 23)
                self.type_up()
                self.enter()
                if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodeprecounitarioitem")
                self.click_relative(165, 23)
                self.type_down()
                self.enter()
                if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodeprecounitarioitem")
                self.click_relative(165, 23)
                self.type_down()
                self.enter()
                
                if not self.find( "diasvalidadeorcamento1", matching=0.97, waiting_time=10000):
                    self.not_found("diasvalidadeorcamento1")
                self.double_click_relative(162, 21)
                ##if not self.find( "diasvalidadeorcamento2", matching=0.97, waiting_time=10000):
                #    self.not_found("diasvalidadeorcamento2")
                #self.click_relative(162, 30)
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'1')
                
                x=0
                while x<4:
                    if not self.find( "precoaorecuperarorcamento", matching=0.97, waiting_time=10000):
                        self.not_found("precoaorecuperarorcamento")
                    self.click_relative(161, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "precoaorecuperarorcamento", matching=0.97, waiting_time=10000):
                        self.not_found("precoaorecuperarorcamento")
                    self.click_relative(161, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:    
                    if not self.find( "tipodoagrupamentodedesconto", matching=0.97, waiting_time=10000):
                        self.not_found("tipodoagrupamentodedesconto")
                    self.click_relative(160, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<5:    
                    if not self.find( "tipodoagrupamentodedesconto", matching=0.97, waiting_time=10000):
                        self.not_found("tipodoagrupamentodedesconto")
                    self.click_relative(160, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not bot.find( "fatu_cad_param_19_alteracao_unitario_servico", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_19_alteracao_unitario_servico")
                bot.click_relative(161, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_19_alteracao_unitario_servico", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_19_alteracao_unitario_servico")
                bot.click_relative(161, 26)
                self.type_down()
                self.enter()
                
                if not self.find( "vendaitemkit", matching=0.97, waiting_time=10000):
                    self.not_found("vendaitemkit")
                self.click_relative(168, 25)
                self.type_down()
                self.enter()
                
                x=0
                while x<3:
                    if not bot.find( "fatu_cad_param_21_venda_a_prazo", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_param_21_venda_a_prazo")
                    bot.click_relative(161, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'123')
                if not self.find( "vendasemsenhaate", matching=0.97, waiting_time=10000):
                    self.not_found("vendasemsenhaate")
                self.click_relative(161, 24)
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                x=0
                while x<3:                 
                    if not self.find( "validarquantidadeimportacaopedido", matching=0.97, waiting_time=10000):
                        self.not_found("validarquantidadeimportacaopedido")
                    self.click_relative(160, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                                ####---PERMISSOES 2---####
                
                
                x=0
                while x<4:                
                    if not self.find( "itemsemestoque", matching=0.97, waiting_time=10000):
                        self.not_found("itemsemestoque")
                    self.click_relative(159, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<4:
                    if not self.find( "descontosuperioraolimiteunegeral", matching=0.97, waiting_time=10000):
                        self.not_found("descontosuperioraolimiteunegeral")
                    self.click_relative(162, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                    
                x=0
                while x<2:    
                    if not self.find( "unitariovalortabelaminimo", matching=0.97, waiting_time=10000):
                        self.not_found("unitariovalortabelaminimo")
                    self.click_relative(161, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "cancelarvendasostransformacao", matching=0.97, waiting_time=10000):
                        self.not_found("cancelarvendasostransformacao")
                    self.click_relative(162, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodevaloresnabaixa")
                self.click_relative(162, 26)
                self.type_up()
                self.enter()
                if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodevaloresnabaixa")
                self.click_relative(162, 26)
                self.type_down()
                self.enter()
                if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                    self.not_found("alteracaodevaloresnabaixa")
                self.click_relative(162, 26)
                self.type_down()
                self.enter()
                
                if not self.find( "usarcondicaoespecial", matching=0.97, waiting_time=10000):
                    self.not_found("usarcondicaoespecial")
                self.click_relative(166, 27)
                self.type_up()
                self.enter()
                if not self.find( "usarcondicaoespecial", matching=0.97, waiting_time=10000):
                    self.not_found("usarcondicaoespecial")
                self.click_relative(166, 27)
                self.type_down()
                self.enter()
                if not self.find( "datavencimentoparcialmaiorqueliberado", matching=0.97, waiting_time=10000):
                    self.not_found("datavencimentoparcialmaiorqueliberado")
                self.click_relative(159, 26)
                self.type_up()
                self.enter()
                if not self.find( "datavencimentoparcialmaiorqueliberado", matching=0.97, waiting_time=10000):
                    self.not_found("datavencimentoparcialmaiorqueliberado")
                self.click_relative(159, 26)
                self.type_down()
                self.enter()
                if not self.find( "acessoaocaixa", matching=0.97, waiting_time=10000):
                    self.not_found("acessoaocaixa")
                self.click_relative(161, 28)
                self.type_up()
                self.enter()
                if not self.find( "acessoaocaixa", matching=0.97, waiting_time=10000):
                    self.not_found("acessoaocaixa")
                self.click_relative(161, 28)
                self.type_down()
                self.enter()
                if not self.find( "recuperardevolvercondicionais", matching=0.97, waiting_time=10000):
                    self.not_found("recuperardevolvercondicionais")
                self.click_relative(169, 30)
                self.type_up()
                self.enter()
                if not self.find( "recuperardevolvercondicionais", matching=0.97, waiting_time=10000):
                    self.not_found("recuperardevolvercondicionais")
                self.click_relative(169, 30)
                self.type_down()
                self.enter()
                if not self.find( "reimpressaodevendasfechadasbalcao", matching=0.97, waiting_time=10000):
                    self.not_found("reimpressaodevendasfechadasbalcao")
                self.click_relative(159, 23)
                self.type_up()
                self.enter()
                if not self.find( "reimpressaodevendasfechadasbalcao", matching=0.97, waiting_time=10000):
                    self.not_found("reimpressaodevendasfechadasbalcao")
                self.click_relative(159, 23)
                self.type_down()
                self.enter()
                if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                    self.not_found("tipoliberacoespedidos")
                self.click_relative(163, 28)
                self.type_down()
                self.enter()
                if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                    self.not_found("tipoliberacoespedidos")
                self.click_relative(163, 28)
                self.type_down()
                self.enter()
                if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                    self.not_found("tipoliberacoespedidos")
                self.click_relative(163, 28)
                self.type_up()
                self.enter()
                if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                    self.not_found("tipoliberacoespedidos")
                self.click_relative(163, 28)
                self.type_up()
                self.enter()
                
                x=0
                while x<4:
                    if not self.find( "itemsemestoqueorcamento", matching=0.97, waiting_time=10000):
                        self.not_found("itemsemestoqueorcamento")
                    self.click_relative(163, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<4:
                    if not self.find( "itemsemestoqueorcamento", matching=0.97, waiting_time=10000):
                        self.not_found("itemsemestoqueorcamento")
                    self.click_relative(163, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                if not self.find( "alterametragenstelaconfirmacao", matching=0.97, waiting_time=10000):
                    self.not_found("alterametragenstelaconfirmacao")
                self.click_relative(162, 24)
                self.type_up()
                self.enter()   
                if not self.find( "alterametragenstelaconfirmacao", matching=0.97, waiting_time=10000):
                    self.not_found("alterametragenstelaconfirmacao")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                
                if not self.find( "alteravendedorvendaos", matching=0.97, waiting_time=10000):
                    self.not_found("alteravendedorvendaos")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                if not self.find( "alteravendedorvendaos", matching=0.97, waiting_time=10000):
                    self.not_found("alteravendedorvendaos")
                self.click_relative(161, 27)
                self.type_up()
                self.enter()
                
                if not self.find( "fechamentoorcamentovenda", matching=0.97, waiting_time=10000):
                    self.not_found("fechamentoorcamentovenda")
                self.click_relative(160, 26)
                self.type_up()
                self.enter()
                if not self.find( "fechamentoorcamentovenda", matching=0.97, waiting_time=10000):
                    self.not_found("fechamentoorcamentovenda")
                self.click_relative(160, 26)
                self.type_down()
                self.enter()
                
                if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                    self.not_found("excluiralteraritensvendas")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                    self.not_found("excluiralteraritensvendas")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                    self.not_found("excluiralteraritensvendas")
                self.click_relative(161, 27)
                self.type_up()
                self.enter()
                if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                    self.not_found("excluiralteraritensvendas")
                self.click_relative(161, 27)
                self.type_up()
                self.enter() 
                
                                ####---ABA5 COMPRAS---####
                                
                if not self.find( "aba5compras", matching=0.97, waiting_time=10000):
                    self.not_found("aba5compras")
                self.click()
                
                x=0
                while x<3:
                    if not self.find( "utilizarusuarioautorizadornocompras", matching=0.97, waiting_time=10000):
                        self.not_found("utilizarusuarioautorizadornocompras")
                    self.click_relative(161, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "utilizarusuarioautorizadornocompras", matching=0.97, waiting_time=10000):
                        self.not_found("utilizarusuarioautorizadornocompras")
                    self.click_relative(161, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "exigeliberacaorejeicaodanalisecotacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigeliberacaorejeicaodanalisecotacao")
                self.click_relative(161, 27)
                self.type_up()
                self.enter()    
                if not self.find( "exigeliberacaorejeicaodanalisecotacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigeliberacaorejeicaodanalisecotacao")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                if not self.find( "margenslibentrada", matching=0.97, waiting_time=10000):
                    self.not_found("margenslibentrada")
                self.click_relative(110, 25)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "cpedidocustoqtde", matching=0.97, waiting_time=10000):
                    self.not_found("cpedidocustoqtde")
                self.click_relative(102, 26)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "tipomargemliberacaoentrada", matching=0.97, waiting_time=10000):
                    self.not_found("tipomargemliberacaoentrada")
                self.click_relative(160, 25)
                self.type_down()
                self.enter()
                if not self.find( "tipomargemliberacaoentrada", matching=0.97, waiting_time=10000):
                    self.not_found("tipomargemliberacaoentrada")
                self.click_relative(160, 25)
                self.type_up()
                self.enter()
                    
                x=0
                while x<3:
                    if not self.find( "itememcotacaoaberta", matching=0.97, waiting_time=10000):
                        self.not_found("itememcotacaoaberta")
                    self.click_relative(76, 24)
                    self.type_down()
                    self.enter()
                    x=x+1     
                x=0
                while x<3:
                    if not self.find( "itememcotacaoaberta", matching=0.97, waiting_time=10000):
                        self.not_found("itememcotacaoaberta")
                    self.click_relative(76, 24)
                    self.type_up()
                    self.enter()
                    x=x+1 
                
                x=0
                while x<3:
                    if not self.find( "itemempedidosabertos", matching=0.97, waiting_time=10000):
                        self.not_found("itemempedidosabertos")
                    self.click_relative(74, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "itemempedidosabertos", matching=0.97, waiting_time=10000):
                        self.not_found("itemempedidosabertos")
                    self.click_relative(74, 24)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                x=0
                while x<3:    
                    if not self.find( "itememrequisicoesabertas", matching=0.97, waiting_time=10000):
                        self.not_found("itememrequisicoesabertas")
                    self.click_relative(76, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("mostrarobsnaimportacao")
                self.click_relative(161, 24)
                self.type_down()
                self.enter() 
                if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("mostrarobsnaimportacao")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("mostrarobsnaimportacao")
                self.click_relative(161, 24)
                self.type_up()
                self.enter()
                
                if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("codigodeoperacaonaimportacao")
                self.click_relative(163, 26)
                self.type_down()
                self.enter()     
                if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("codigodeoperacaonaimportacao")
                self.click_relative(163, 26)
                self.type_down()
                self.enter()
                if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("codigodeoperacaonaimportacao")
                self.click_relative(163, 26)
                self.type_up()
                self.enter()
                
                x=0
                while x<3:     
                    if not self.find( "bloquear1parcelamenoracond", matching=0.97, waiting_time=10000):
                        self.not_found("bloquear1parcelamenoracond")
                    self.click_relative(164, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:     
                    if not self.find( "bloquear1parcelamenoracond", matching=0.97, waiting_time=10000):
                        self.not_found("bloquear1parcelamenoracond")
                    self.click_relative(164, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                    self.not_found("cotacaoautomaticaparaitensnaomarca")
                self.click_relative(159, 25)
                self.type_down()
                self.enter()
                if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                    self.not_found("cotacaoautomaticaparaitensnaomarca")
                self.click_relative(159, 25)
                self.type_down()
                self.enter()
                if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                    self.not_found("cotacaoautomaticaparaitensnaomarca")
                self.click_relative(159, 25)
                self.type_up()
                self.enter() 
                
                x=0
                while x<3:
                    if not self.find( "liberacaolimitedecompra", matching=0.97, waiting_time=10000):
                        self.not_found("liberacaolimitedecompra")
                    self.click_relative(162, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "liberacaolimitedecompra", matching=0.97, waiting_time=10000):
                        self.not_found("liberacaolimitedecompra")
                    self.click_relative(162, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "bloqueiafornecedorimppedcomp", matching=0.97, waiting_time=10000):
                        self.not_found("bloqueiafornecedorimppedcomp")
                    self.click_relative(161, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<2:
                    if not self.find( "bloqueiafornecedorimppedcomp", matching=0.97, waiting_time=10000):
                        self.not_found("bloqueiafornecedorimppedcomp")
                    self.click_relative(161, 23)
                    self.type_up()
                    self.enter()
                    x=x+1 
                    
                
                x=0
                while x<2:
                    if not self.find( "condicaopagtoimppedcomp", matching=0.97, waiting_time=10000):
                        self.not_found("condicaopagtoimppedcomp")
                    self.click_relative(94, 23)
                    self.type_up()
                    self.enter()
                    x=x+1
                x=0
                while x<2:
                    if not self.find( "condicaopagtoimppedcomp", matching=0.97, waiting_time=10000):
                        self.not_found("condicaopagtoimppedcomp")
                    self.click_relative(94, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                
                x=0
                while x<2:
                    if not self.find( "compradorimppedcompras", matching=0.97, waiting_time=10000):
                        self.not_found("compradorimppedcompras")
                    self.click_relative(94, 22)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "verificaipistdositens", matching=0.97, waiting_time=10000):
                    self.not_found("verificaipistdositens")
                self.click_relative(162, 24)
                self.type_up()
                self.enter()        
                if not self.find( "verificaipistdositens", matching=0.97, waiting_time=10000):
                    self.not_found("verificaipistdositens")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                
                x=0
                while x<2:
                    if not self.find( "exigirclassificacaopedidodecompra", matching=0.97, waiting_time=10000):
                        self.not_found("exigirclassificacaopedidodecompra")
                    self.click_relative(162, 26)                
                    self.type_down()
                    self.enter()
                    x=x+1    
                x=0
                while x<2:
                    if not self.find( "exigirclassificacaopedidodecompra", matching=0.97, waiting_time=10000):
                        self.not_found("exigirclassificacaopedidodecompra")
                    self.click_relative(162, 26)                
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<6:
                    if not self.find( "acordocialfinanceiropedidocompra", matching=0.97, waiting_time=10000):
                        self.not_found("acordocialfinanceiropedidocompra")
                    self.click_relative(161, 23)                                
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<6:
                    if not self.find( "acordocialfinanceiropedidocompra", matching=0.97, waiting_time=10000):
                        self.not_found("acordocialfinanceiropedidocompra")
                    self.click_relative(161, 23)                                
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "variacaonocustoentradas", matching=0.97, waiting_time=10000):
                        self.not_found("variacaonocustoentradas")
                    self.click_relative(162, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "variacaonocustoentradas", matching=0.97, waiting_time=10000):
                        self.not_found("variacaonocustoentradas")
                    self.click_relative(162, 23)
                    self.type_up()
                    self.enter()
                    x=x+1        
                self.type_keys_with_interval(1,'123')
                if not self.find( "percentualmacvariacaocusto", matching=0.97, waiting_time=10000):
                    self.not_found("percentualmacvariacaocusto")
                self.click_relative(113, 22)
                self.type_keys_with_interval(1,'123')
                
                                ####---ABA6 MENSAGENS---####
                                
                if not self.find( "aba6mensagens", matching=0.97, waiting_time=10000):
                    self.not_found("aba6mensagens")
                self.click()
                self.type_keys_with_interval(1,'te12!@') 
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')    
                
                                ####---ABA7 PRODUCAO, OS, CRM---####
                                
                if not self.find( "aba7producaooscrm", matching=0.97, waiting_time=10000):
                    self.not_found("aba7producaooscrm")
                self.click()
                
                                ####---PRODUCAO/TRANSFORMACAO---####
                                
                if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                    self.not_found("custoautilizarnoproducao")
                self.click_relative(160, 25)
                self.type_up()
                self.enter()
                
                x=0
                while x<4:    
                    if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                        self.not_found("custoautilizarnoproducao")
                    self.click_relative(160, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:    
                    if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                        self.not_found("custoautilizarnoproducao")
                    self.click_relative(160, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not bot.find( "fatu_cad_param_2_composicao_em_estoque", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_composicao_em_estoque")
                bot.click_relative(162, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_2_composicao_em_estoque", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_2_composicao_em_estoque")
                bot.click_relative(162, 26)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_3_liberacao_transf", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_3_liberacao_transf")
                bot.click_relative(164, 25)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_3_liberacao_transf", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_3_liberacao_transf")
                bot.click_relative(164, 25)
                self.type_down()
                self.enter()
                
                                ####---PRODUCAO/TRANSFORMACAO/OSM---####
                                
                x=0
                while x<7:
                    if not self.find( "gerarnovocontatoapartir", matching=0.97, waiting_time=10000):
                        self.not_found("gerarnovocontatoapartir")
                    self.click_relative(160, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "gerarpusuario", matching=0.97, waiting_time=10000):
                    self.not_found("gerarpusuario")
                self.click_relative(379, 24)
                self.type_down()
                self.enter()
                if not self.find( "gerarpusuario", matching=0.97, waiting_time=10000):
                    self.not_found("gerarpusuario")
                self.click_relative(379, 24)
                self.backspace()
                self.backspace()
                if not self.find( "gerarpusuario3", matching=0.97, waiting_time=10000):
                    self.not_found("gerarpusuario3")
                self.double_click_relative(82, 25)
                if not self.find( "gerarpusuario4", matching=0.97, waiting_time=10000):
                    self.not_found("gerarpusuario4")
                self.click()
                
                self.wait(2000)
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "diasaposvendaocontato", matching=0.97, waiting_time=10000):
                    self.not_found("diasaposvendaocontato")
                self.click_relative(160, 25)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aofinalizaratendimentodotelemarkting", matching=0.97, waiting_time=10000):
                    self.not_found("aofinalizaratendimentodotelemarkting")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                if not self.find( "aofinalizaratendimentodotelemarkting", matching=0.97, waiting_time=10000):
                    self.not_found("aofinalizaratendimentodotelemarkting")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                if not self.find( "telemarketingexibenegociacao", matching=0.97, waiting_time=10000):
                    self.not_found("telemarketingexibenegociacao")
                self.click_relative(161, 26)
                self.type_up()
                self.enter()
                if not self.find( "telemarketingexibenegociacao", matching=0.97, waiting_time=10000):
                    self.not_found("telemarketingexibenegociacao")
                self.click_relative(161, 26)
                self.type_down()
                self.enter()
                if not self.find( "baixaitemsemestoqueosm", matching=0.97, waiting_time=10000):
                    self.not_found("baixaitemsemestoqueosm")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                if not self.find( "baixaitemsemestoqueosm", matching=0.97, waiting_time=10000):
                    self.not_found("baixaitemsemestoqueosm")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                
                                ####---GERAL---####

                x=0
                while x<4:
                    if not self.find( "ramodeatividadeos", matching=0.97, waiting_time=10000):
                        self.not_found("ramodeatividadeos")
                    self.click_relative(161, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<4:
                    if not self.find( "ramodeatividadeos", matching=0.97, waiting_time=10000):
                        self.not_found("ramodeatividadeos")
                    self.click_relative(161, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                self.type_keys_with_interval(1,'123')
                if not self.find( "acrescimonaos", matching=0.97, waiting_time=10000):
                    self.not_found("acrescimonaos")
                self.click_relative(165, 26)
                self.type_up()
                self.enter()
                if not self.find( "acrescimonaos", matching=0.97, waiting_time=10000):
                    self.not_found("acrescimonaos")
                self.click_relative(165, 26)
                self.type_down()
                self.enter()
                if not self.find( "linhasimpressaoformularioos", matching=0.97, waiting_time=10000):
                    self.not_found("linhasimpressaoformularioos")
                self.double_click_relative(165, 19)
                if not self.find( "linhasimpressaoformularioos2", matching=0.97, waiting_time=10000):
                    self.not_found("linhasimpressaoformularioos2")
                self.click_relative(164, 31)
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'1')
                
                if not self.find( "exigiralocacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigiralocacao")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                if not self.find( "exigiralocacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigiralocacao")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                if not bot.find( "fatu_cad_param_7_tipo_da_nf_servicos", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_7_tipo_da_nf_servicos")
                bot.click_relative(160, 25)
                self.type_up()
                self.enter()
                if not bot.find( "fatu_cad_param_7_tipo_da_nf_servicos", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_7_tipo_da_nf_servicos")
                bot.click_relative(160, 25)
                self.type_down()
                self.enter()
                
                if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                    self.not_found("enviaremailosnassituacoes")
                self.click_relative(160, 24)
                if not self.find( "fechadasemailos", matching=0.97, waiting_time=10000):
                    self.not_found("fechadasemailos")
                self.click()
                if not self.find( "canceladasemailos", matching=0.97, waiting_time=10000):
                    self.not_found("canceladasemailos")
                self.click()
                if not self.find( "finalizadooficinaemailos", matching=0.97, waiting_time=10000):
                    self.not_found("finalizadooficinaemailos")
                self.click()
                if not self.find( "emandamentoemailos", matching=0.97, waiting_time=10000):
                    self.not_found("emandamentoemailos")
                self.click()
                if not self.find( "abertasemailos", matching=0.97, waiting_time=10000):
                    self.not_found("abertasemailos")
                self.click()
                if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                    self.not_found("enviaremailosnassituacoes")
                self.click_relative(160, 24)
                if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                    self.not_found("enviaremailosnassituacoes")
                self.click_relative(160, 24)
                if not self.find( "fechadasemailos2", matching=0.97, waiting_time=10000):
                    self.not_found("fechadasemailos2")
                self.click()
                if not self.find( "canceladasemailos2", matching=0.97, waiting_time=10000):
                    self.not_found("canceladasemailos2")
                self.click()
                if not self.find( "finalizadooficinaemailos2", matching=0.97, waiting_time=10000):
                    self.not_found("finalizadooficinaemailos2")
                self.click()
                if not self.find( "emandamentoemailosmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("emandamentoemailosmarcado")
                self.click()      
                if not self.find( "enviaremailosaberta2", matching=0.97, waiting_time=10000):
                    self.not_found("enviaremailosaberta2")
                self.click()
                
                        
                        
                x=0
                while x<3:
                    if not self.find( "baixaparcialos", matching=0.97, waiting_time=10000):
                        self.not_found("baixaparcialos")
                    self.click_relative(163, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "baixaparcialos", matching=0.97, waiting_time=10000):
                        self.not_found("baixaparcialos")
                    self.click_relative(163, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                x=0
                while x<2:
                    if not self.find( "baixadoestoquecentraldepecas", matching=0.97, waiting_time=10000):
                        self.not_found("baixadoestoquecentraldepecas")
                    self.click_relative(160, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---DESCRICAO DOS CAMPOS DE EQUIP---####

                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
        
                                ####---CAMPOS DE CHECAGEM NA OS---####
                
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()

                                ####---CUSTOM VANS---####

                self.type_keys_with_interval(1,'123')
                if not self.find( "percentualminimoentrada", matching=0.97, waiting_time=10000):
                    self.not_found("percentualminimoentrada")
                self.click_relative(161, 24)
                self.type_keys_with_interval(1,'123')
                
                                ####---PARAMETROS NOTA FISCAL---####
                                ####---PRODUCAO/TRANSFORMACAO---####

                if not self.find( "aba8parametrosnotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("aba8parametrosnotafiscal")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12@!')

                                ####---COMPRIMENTO M2---####

                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()

                                ####---PARAMETRIZACAO---####

                self.type_keys_with_interval(1,'t1!')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "aocancelarnotafiscalcereal", matching=0.97, waiting_time=10000):
                    self.not_found("aocancelarnotafiscalcereal")
                self.click_relative(210, 26)
                self.type_up()
                self.enter()
                if not self.find( "aocancelarnotafiscalcereal", matching=0.97, waiting_time=10000):
                    self.not_found("aocancelarnotafiscalcereal")
                self.click_relative(210, 26)
                self.type_down()
                self.enter()
                if not self.find( "acrescentarficatecnicadoitem", matching=0.97, waiting_time=10000):
                    self.not_found("acrescentarficatecnicadoitem")
                self.click_relative(102, 26)
                self.type_down()
                self.enter()
                if not self.find( "acrescentarficatecnicadoitem", matching=0.97, waiting_time=10000):
                    self.not_found("acrescentarficatecnicadoitem")
                self.click_relative(102, 26)
                self.type_down()
                self.enter()
                if not self.find( "localdeentregananotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("localdeentregananotafiscal")
                self.click_relative(430, 25)
                self.type_down()
                self.enter()
                if not self.find( "localdeentregananotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("localdeentregananotafiscal")
                self.click_relative(430, 25)
                self.type_down()
                self.enter()
                self.type_keys_with_interval(1,'t1!')

                                ####---FORMULARIO NF---####

                if not self.find( "formularionotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("formularionotafiscal")
                self.click_relative(147, 46)
                self.type_down()
                self.enter() 

                                ####---LEVANTA TELA---####
                
                if not self.find( "levantatelanf", matching=0.97, waiting_time=10000):
                    self.not_found("levantatelanf")
                self.click()
                x=0
                while x<7:
                    if not self.find( "levantatelanf2", matching=0.97, waiting_time=10000):
                        self.not_found("levantatelanf2")
                    self.double_click()
                    x=x+1

                                ####---FORMULARIO NF---####

                if not self.find( "formularionotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("formularionotafiscal")
                self.click_relative(147, 46)
                self.type_up()
                self.enter()

                                ####---NUMERACAO NOTA FISCAL---####
                    
                if not bot.find( "fatu_btn_adicionar_cad_param_8_param", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_adicionar_cad_param_8_param")
                bot.click()
                
                if not self.find( "oknumeronf", matching=0.97, waiting_time=10000):
                    self.not_found("oknumeronf")
                self.click()
                
                                ####---ABA9 CODIGOS PADROES---####
                                
                if not self.find( "aba9codigospadroes", matching=0.97, waiting_time=10000):
                    self.not_found("aba9codigospadroes")
                self.click()
                
                                    ####---A5 P1---####
                if not self.find( "aba5p1_parametrosEmpresa_garantia", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p1_parametrosEmpresa_garantia")
                self.click_relative(47, 140)
                                    
                if not self.find( "relacionadoaempresa", matching=0.97, waiting_time=10000):
                    self.not_found("relacionadoaempresa")
                self.click_relative(94, 25)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "cadastromodelo", matching=0.97, waiting_time=10000):
                    self.not_found("cadastromodelo")
                self.click_relative(96, 23)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                    self.not_found("achacod1")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "localestoquepadrao", matching=0.97, waiting_time=10000):
                    self.not_found("localestoquepadrao")
                self.click_relative(80, 27)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "volta", matching=0.97, waiting_time=10000):
                    self.not_found("volta")
                self.click()
                self.wait(1000)
                                ####---OPERACAO DE ENTRADA---####
                                
                if not self.find( "b_transformacaodeitens_parametros", matching=0.97, waiting_time=10000):
                    self.not_found("b_transformacaodeitens_parametros")
                self.click_relative(79, 25)                                               
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "inventarioentrada", matching=0.97, waiting_time=10000):
                    self.not_found("inventarioentrada")
                self.click_relative(483, 45)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "producaoeosm", matching=0.97, waiting_time=10000):
                    self.not_found("producaoeosm")
                self.click_relative(882, 44)                                    
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "itemkit", matching=0.97, waiting_time=10000):
                    self.not_found("itemkit")
                self.click_relative(-13, 87)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "itemmestreentrada", matching=0.97, waiting_time=10000):
                    self.not_found("itemmestreentrada")
                self.click_relative(483, 88)
                                    
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "almoxarifadoentrada", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifadoentrada")
                self.click_relative(885, 88)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "desmembramentoitens", matching=0.97, waiting_time=10000):
                    self.not_found("desmembramentoitens")
                self.click_relative(-11, 127)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "devolucaoitens", matching=0.97, waiting_time=10000):
                    self.not_found("devolucaoitens")
                self.click_relative(388, 127)
                if not self.find( "achacod01menordif", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menordif")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---OPERACOES DE SAIDA---####
                                
                if not self.find( "transformacaoitenssaida", matching=0.97, waiting_time=10000):
                    self.not_found("transformacaoitenssaida")
                self.click_relative(84, 46)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()           
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "inventariosaida", matching=0.97, waiting_time=10000):
                    self.not_found("inventariosaida")
                self.click_relative(483, 48)
                            
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "producaoeosm2", matching=0.97, waiting_time=10000):
                    self.not_found("producaoeosm2")
                self.click_relative(787, 43)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacoesdesaidaitemkit", matching=0.97, waiting_time=10000):
                    self.not_found("operacoesdesaidaitemkit")
                self.click_relative(83, 86)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "itemmestresaida", matching=0.97, waiting_time=10000):
                    self.not_found("itemmestresaida")
                self.click_relative(485, 86)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "almoxarifadosaida", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifadosaida")
                self.click_relative(884, 88)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "desmembramentosaida", matching=0.97, waiting_time=10000):
                    self.not_found("desmembramentosaida")
                self.click_relative(84, 129)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "centraldepecas", matching=0.97, waiting_time=10000):
                    self.not_found("centraldepecas")
                self.click_relative(388, 129)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---ABA5 P2---####

                if not self.find( "aba5p2pa", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p2pa")
                self.click()
                if not self.find( "clientepadraovendas", matching=0.97, waiting_time=10000):
                    self.not_found("clientepadraovendas")
                self.click_relative(97, 26)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                    self.not_found("achacod1")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "vendedorpadraovendas", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorpadraovendas")
                self.click_relative(83, 26)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                #if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
                #    self.not_found("cod101teste")
                #self.click()           
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "condicaodepagamentopadraovendas", matching=0.97, waiting_time=10000):
                    self.not_found("condicaodepagamentopadraovendas")
                self.click_relative(81, 26)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                    self.not_found("achacod01menor")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---PADROES OPERACOES FISCAIS---####

                if not self.find( "cfoppadraonfvendas", matching=0.97, waiting_time=10000):
                    self.not_found("cfoppadraonfvendas")
                self.click_relative(83, 45)         
                self.backspace()
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                    self.not_found("cod1101")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaosaidapadraovendas", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosaidapadraovendas")
                self.click_relative(81, 24)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaoparanfedecupomfiscal", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoparanfedecupomfiscal")
                self.click_relative(880, 41)                       
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaoparanfedopaf", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoparanfedopaf")
                self.click_relative(78, 23)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaosaidapadraordemdeservico", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosaidapadraordemdeservico")
                self.click_relative(77, 22)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                self.type_keys_with_interval(1,'consig')
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---PADROES ADICIONAIS---####
                                
                if not self.find( "pagamentoaddconsultitens", matching=0.97, waiting_time=10000):
                    self.not_found("pagamentoaddconsultitens")
                self.click_relative(84, 46)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "vendedordeclientesdisponivel", matching=0.97, waiting_time=10000):
                    self.not_found("vendedordeclientesdisponivel")
                self.click_relative(482, 46)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                #if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
                #    self.not_found("cod101teste")
                #self.click()           
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "planoprecominimo", matching=0.97, waiting_time=10000):
                    self.not_found("planoprecominimo")
                self.click_relative(79, 25)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                    self.not_found("codnulo")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.backspace()
                self.wait(1000)
                if not self.find( "planoprecomaximo", matching=0.97, waiting_time=10000):
                    self.not_found("planoprecomaximo")
                self.click_relative(-13, 25)                       
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                    self.not_found("codnulo")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.backspace()
                
                                ####---MAPA FISCAL---####
                                
                if not self.find( "mapafiscalcliente", matching=0.97, waiting_time=10000):
                    self.not_found("mapafiscalcliente")
                self.click_relative(84, 45)
                
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                    self.not_found("achacod1")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaosaidamapafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosaidamapafiscal")
                self.click_relative(481, 44)            
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "cfopmapafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("cfopmapafiscal")
                self.click_relative(80, 26)
                self.backspace()
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                    self.not_found("cod1101")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "cfopsubstituicaotributaria", matching=0.97, waiting_time=10000):
                    self.not_found("cfopsubstituicaotributaria")
                self.click_relative(81, 24)
                self.backspace()
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                    self.not_found("cod1101")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "cfopiss", matching=0.97, waiting_time=10000):
                    self.not_found("cfopiss")
                self.click_relative(80, 27)
                self.backspace()
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                    self.not_found("cod1101")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaosaidaiss", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosaidaiss")
                self.click_relative(81, 26)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                    self.not_found("achacod02")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "indiceiss", matching=0.97, waiting_time=10000):
                    self.not_found("indiceiss")
                self.click_relative(21, 27)
                self.type_keys_with_interval(1,'t1')
                self.enter()
                if not self.find( "indiceiss", matching=0.97, waiting_time=10000):
                    self.not_found("indiceiss")
                self.click_relative(21, 27)
                self.backspace()
                self.type_keys_with_interval(1,'!')
                
                                ####---ABA5 P3---####
                                
                if not self.find( "aba5p3pa", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p3pa")
                self.click()
                if not self.find( "classificacaocodpadrao", matching=0.97, waiting_time=10000):
                    self.not_found("classificacaocodpadrao")
                self.click_relative(83, 43)
                self.wait(2000)
                
                self.wait(2000)
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "moedapadrao", matching=0.97, waiting_time=10000):
                    self.not_found("moedapadrao")
                self.click_relative(82, 26)
                if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                    self.not_found("cod001real")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "adiantamentoosa9p3", matching=0.97, waiting_time=10000):
                    self.not_found("adiantamentoosa9p3")
                self.click_relative(-24, 25)
                if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                    self.not_found("cod002dinheiro")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "tptrocoa9p3", matching=0.97, waiting_time=10000):
                    self.not_found("tptrocoa9p3")
                self.click_relative(-22, 25)
                if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                    self.not_found("cod002dinheiro")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "tpentradasa9p3", matching=0.97, waiting_time=10000):
                    self.not_found("tpentradasa9p3")
                self.click_relative(-22, 24)
                if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                    self.not_found("cod001real")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "tpsaidasa9p3", matching=0.97, waiting_time=10000):
                    self.not_found("tpsaidasa9p3")
                self.click_relative(-22, 26)
                if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                    self.not_found("cod002dinheiro")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "tpbaixaadiantamentosa9p3", matching=0.97, waiting_time=10000):
                    self.not_found("tpbaixaadiantamentosa9p3")
                self.click_relative(-24, 28)
                if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                    self.not_found("cod001real")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---CHEQUES RECEBIDOS---####
                                
                if not self.find( "contachequerecebido", matching=0.97, waiting_time=10000):
                    self.not_found("contachequerecebido")
                self.click_relative(84, 44)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod001contacheque", matching=0.97, waiting_time=10000):
                    self.not_found("cod001contacheque")
                self.click()           
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "tipopagamentochequerecebido", matching=0.97, waiting_time=10000):
                    self.not_found("tipopagamentochequerecebido")
                self.click_relative(483, 46)
                if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                    self.not_found("cod001real")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "chequesrecebidosoperacao", matching=0.97, waiting_time=10000):
                    self.not_found("chequesrecebidosoperacao")
                self.click_relative(883, 44)
                if not bot.find( "fatu_cad_param_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_btn_localizar_2411")
                bot.click()
                if not self.find( "cod0024pagamentos", matching=0.97, waiting_time=10000):
                    self.not_found("cod0024pagamentos")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                
                                ####---ABA9 P4---####
                                
                if not self.find( "aba9p4", matching=0.97, waiting_time=10000):
                    self.not_found("aba9p4")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                
                                ####---ABA10 ECOMMERCE---####
                                
                if not self.find( "aba10ecommerce", matching=0.97, waiting_time=10000):
                    self.not_found("aba10ecommerce")
                self.click()                                         
                if not self.find( "empresacomecommerce", matching=0.97, waiting_time=10000):
                    self.not_found("empresacomecommerce")
                self.click_relative(163, 27)
                self.type_up()
                self.enter()
                if not self.find( "empresacomecommerce", matching=0.97, waiting_time=10000):
                    self.not_found("empresacomecommerce")
                self.click_relative(163, 27)
                self.type_down()
                self.enter()
                
                if not self.find( "vendedorpadrao", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorpadrao")
                self.click_relative(79, 25)
                #if not self.find( "cod00101testevendedorpadrao", matching=0.97, waiting_time=10000):
                #    self.not_found("cod00101testevendedorpadrao")
                #self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "operacaopadraoecommerce", matching=0.97, waiting_time=10000):
                    self.not_found("operacaopadraoecommerce")
                self.click_relative(80, 24)
                self.type_keys_with_interval(1,'consig')
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "condicaodepagamentopadraoecommerce", matching=0.97, waiting_time=10000):
                    self.not_found("condicaodepagamentopadraoecommerce")
                self.click_relative(80, 25)
                if not self.find( "cod0002vendassaida", matching=0.97, waiting_time=10000):
                    self.not_found("cod0002vendassaida")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.wait(1000)
                if not self.find( "planoprecopadrao", matching=0.97, waiting_time=10000):
                    self.not_found("planoprecopadrao")
                self.click_relative(80, 23)
                if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                    self.not_found("codnulo")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                self.backspace()
                
                                ####---FINALIZACAO---####
                                
                if not self.find( "salvarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("salvarfimpa")
                self.click()
                if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfimpa")
                self.click()
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                if not bot.find( "fatu_cad_param_achar_ictus_simples", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_achar_ictus_simples")
                bot.click()
                
                if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("editarfimpa")
                self.click()
                if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfimpa")
                self.click()
                #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
                #    self.not_found("botaosimexcluirfimpa")
                #self.click()
                self.enter()
                if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfimpa")
                self.click()
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfimpa")
                self.click()
                                
                
                self.wait(2000)

                                        #####---RECEITUARIO---#####
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not bot.find( "fatu_cad_parametros_btn_menu", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_parametros_btn_menu")
                bot.click()
                if not self.find( "receituario", matching=0.97, waiting_time=10000):
                    self.not_found("receituario")
                self.click()
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "empresareceituario", matching=0.97, waiting_time=10000):
                    self.not_found("empresareceituario")
                self.click_relative(97, 4)
                #if not self.find( "cod0101comnometeste", matching=0.97, waiting_time=10000):
                #    self.not_found("cod0101comnometeste")
                #self.click()            
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                if not self.find( "usuarioreceituario", matching=0.97, waiting_time=10000):
                    self.not_found("usuarioreceituario")
                self.click_relative(61, 5)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "senhareceituario", matching=0.97, waiting_time=10000):
                    self.not_found("senhareceituario")
                self.click_relative(70, 4)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "chavereceituario", matching=0.97, waiting_time=10000):
                    self.not_found("chavereceituario")
                self.click_relative(76, 4)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "agronomoreceituario", matching=0.97, waiting_time=10000):
                    self.not_found("agronomoreceituario")
                self.click_relative(116, 4)
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                if not self.find( "cod0081260agroreceituario", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260agroreceituario")
                self.click()
                if not bot.find( "fatu_cad_btn_selecionar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_btn_selecionar_2411")
                bot.click()
                if not self.find( "agronomoreceituario2", matching=0.97, waiting_time=10000):
                    self.not_found("agronomoreceituario2")
                self.click_relative(76, 5)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "aplicacaoreceituario1", matching=0.97, waiting_time=10000):
                    self.not_found("aplicacaoreceituario1")
                self.click_relative(9, 26)
                if not self.find( "aplicacaoreceituario2", matching=0.97, waiting_time=10000):
                    self.not_found("aplicacaoreceituario2")
                self.click_relative(92, 27)
                if not self.find( "dosereceituario1", matching=0.97, waiting_time=10000):
                    self.not_found("dosereceituario1")
                self.click_relative(8, 26)
                if not self.find( "dosereceituario2", matching=0.97, waiting_time=10000):
                    self.not_found("dosereceituario2")
                self.click_relative(92, 26)
                if not self.find( "salvarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("salvarfimpa")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                
                #if not self.find( "cod0101Aprteste", matching=0.97, waiting_time=10000):
                #    self.not_found("cod0101Aprteste")
                #self.click()            
                if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("editarfimpa")
                self.click()
                if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfimpa")
                self.click()
                #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
                #    self.not_found("botaosimexcluirfimpa")
                #self.click()
                self.enter()
                if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfimpa")
                self.click()
                if not self.find( "localizape", matching=0.97, waiting_time=10000):
                    self.not_found("localizape")
                self.click()
                
                if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfimpa")
                self.click()
                
                
                ###################################################################
                                        ####---PAISES---#### 
                ###################################################################

                self.wait(1500)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                self.wait(1500)
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.double_click()
                #if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                #    self.not_found("parametrosfiscais")
                #self.double_click()
                self.wait(1500)
                if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                    self.not_found("regionalizacao")
                self.click()
                if not self.find( "paises", matching=0.97, waiting_time=10000):
                    self.not_found("paises")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()           
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12')
                self.enter()
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("salvarpaises")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()            
                if not self.find( "acharpaises", matching=0.97, waiting_time=10000):
                    self.not_found("acharpaises")
                self.click()            
                if not self.find( "paisteste", matching=0.97, waiting_time=10000):
                    self.not_found("paisteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                self.enter()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---REGIOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                    self.not_found("regionalizacao")
                self.click()
                if not self.find( "regioes", matching=0.97, waiting_time=10000):
                    self.not_found("regioes")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "buscarpais", matching=0.97, waiting_time=10000):
                    self.not_found("buscarpais")
                self.click_relative(68, 6)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                
                if not bot.find( "fatu_cad_param_paises_btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("fatu_ca_param_paises_btn_selecionar")
                bot.click()
                if not self.find( "entradaestadual", matching=0.97, waiting_time=10000):
                    self.not_found("entradaestadual")
                self.click()
                if not self.find( "entradainterestadual", matching=0.97, waiting_time=10000):
                    self.not_found("entradainterestadual")
                self.click()
                if not self.find( "entradaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("entradaimportacao")
                self.click()
                if not self.find( "saidaestadual", matching=0.97, waiting_time=10000):
                    self.not_found("saidaestadual")
                self.click()
                if not self.find( "saidainterestadual", matching=0.97, waiting_time=10000):
                    self.not_found("saidainterestadual")
                self.click()
                if not self.find( "saidaimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("saidaimportacao")
                self.click()
                if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("salvarpaises")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "paisteste", matching=0.97, waiting_time=10000):
                    self.not_found("paisteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                self.enter()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---ESTADOS---####
                                            
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                    self.not_found("regionalizacao")
                self.click()
                if not self.find( "estados", matching=0.97, waiting_time=10000):
                    self.not_found("estados")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                
                x=0
                while x<27:
                    if not self.find( "sigla", matching=0.97, waiting_time=10000):
                        self.not_found("sigla")
                    self.click_relative(174, 4)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "regiaobuscar", matching=0.97, waiting_time=10000):
                    self.not_found("regiaobuscar")
                self.click_relative(81, 6)
                if not self.find( "cod001bpararegiao", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bpararegiao")
                self.click()
                if not bot.find( "fatu_cad_param_paises_btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_paises_btn_selecionar")
                bot.click()
                
                x=0
                while x<28:
                    if not self.find( "codigoibge", matching=0.97, waiting_time=10000):
                        self.not_found("codigoibge")
                    self.click_relative(210, 8)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("salvarpaises")
                self.click()
                
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                    self.not_found("digiteparalocalizar")
                self.click_relative(36, 31)
                self.type_keys_with_interval(1,'te')
                self.enter()
                if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                    self.not_found("codtesteestados")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                self.enter()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---MUNICIPIOS---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                    self.not_found("regionalizacao")
                self.click()
                if not self.find( "municipios", matching=0.97, waiting_time=10000):
                    self.not_found("municipios")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "buscarestado", matching=0.97, waiting_time=10000):
                    self.not_found("buscarestado")
                self.click_relative(79, 4)
                if not self.find( "cod001pestado", matching=0.97, waiting_time=10000):
                    self.not_found("cod001pestado")
                self.click()
                if not bot.find( "fatu_cad_param_paises_btn_selecionar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_paises_btn_selecionar")
                bot.click()
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
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'1')
                if not self.find( "feriadosmunicipais", matching=0.97, waiting_time=10000):
                    self.not_found("feriadosmunicipais")
                self.click()
                if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("salvarpaises")
                self.click()
                if not self.find( "incluirregistroferiado", matching=0.97, waiting_time=10000):
                    self.not_found("incluirregistroferiado")
                self.click()
                
                x=0
                while x<31:
                    if not self.find( "dia", matching=0.97, waiting_time=10000):
                        self.not_found("dia")
                    self.click_relative(84, 7)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<12:
                    if not self.find( "mes", matching=0.97, waiting_time=10000):
                        self.not_found("mes")
                    self.click_relative(160, 6)
                    self.type_down()
                    self.enter()
                    x=x+1
            
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                if not self.find( "savecommit", matching=0.97, waiting_time=10000):
                    self.not_found("savecommit")
                self.click()
                if not self.find( "excluirferiado", matching=0.97, waiting_time=10000):
                    self.not_found("excluirferiado")
                self.click()
                self.enter()
                #if not self.find( "simexcluirferiado", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirferiado")
                #self.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()

                                ####---GRUPO FISCAL DE ITENS---####
                self.wait(2000)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "grupofiscaldeitens", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscaldeitens")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'99')
                self.enter()
                if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("salvarpaises")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                    self.not_found("codtesteestados")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---CODIGOS DE OPERACAO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "codigosdeoperacao", matching=0.97, waiting_time=10000):
                    self.not_found("codigosdeoperacao")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                self.wait(500)
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()           
                #if not self.find( "naoimportarcodigooperacao", matching=0.97, waiting_time=10000):
                #    self.not_found("naoimportarcodigooperacao")
                #self.click()
                self.type_right()
                self.enter()
                if not self.find( "descricao", matching=0.97, waiting_time=10000):
                    self.not_found("descricao")
                self.click_relative(20, 30)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "tipo", matching=0.97, waiting_time=10000):
                    self.not_found("tipo")
                self.click_relative(108, 25)
                self.type_up()
                self.enter()    
                if not self.find( "tipo", matching=0.97, waiting_time=10000):
                    self.not_found("tipo")
                self.click_relative(108, 25)
                self.type_down()
                self.enter() 
                if not self.find( "tipo", matching=0.97, waiting_time=10000):
                    self.not_found("tipo")
                self.click_relative(108, 25)
                self.type_down()
                self.enter()
                if not self.find( "tipo", matching=0.97, waiting_time=10000):
                    self.not_found("tipo")
                self.click_relative(108, 25)
                self.type_up()
                self.enter()
                if not self.find( "dadosdaoperacao", matching=0.97, waiting_time=10000):
                    self.not_found("dadosdaoperacao")
                self.click()
                if not self.find( "dadosdaoperacao", matching=0.97, waiting_time=10000):
                    self.not_found("dadosdaoperacao")
                self.click()
                if not self.find( "subir_tela_gamb", matching=0.97, waiting_time=10000):
                    self.not_found("subir_tela_gamb")
                self.click()
                x=0
                while x<10:
                    if not self.find( "subir_tela_escuro_gamb", matching=0.97, waiting_time=10000):
                        self.not_found("subir_tela_escuro_gamb")
                    self.double_click()
                    x=x+1
                if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoestoque")
                self.click_relative(99, 27)
                self.type_up()
                self.enter()
                if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoestoque")
                self.click_relative(99, 27)
                self.type_down()
                self.enter()
                if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoestoque")
                self.click_relative(99, 27)
                self.type_down()
                self.enter()
                if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                    self.not_found("operacaoestoque")
                self.click_relative(99, 27)
                
                self.type_up()
                self.enter()
                if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaocomissao")
                self.click_relative(99, 28)
                self.type_down()
                self.enter()
                if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaocomissao")
                self.click_relative(99, 28)
                self.type_down()
                self.enter()
                if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaocomissao")
                self.click_relative(99, 28)
                self.type_up()
                self.enter()
                if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaocomissao")
                self.click_relative(99, 28)
                self.type_up()
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "tipodofinanceiro", matching=0.97, waiting_time=10000):
                        self.not_found("tipodofinanceiro")
                    self.click_relative(120, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
            
                x=0
                while x<3:
                    if not self.find( "tipodofinanceiro", matching=0.97, waiting_time=10000):
                        self.not_found("tipodofinanceiro")
                    self.click_relative(120, 26)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                x=0
                while x<32:
                    if not bot.find( "fatu_cad_cod_operacao_tipo_movimentacao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_cod_operacao_tipo_movimentacao")
                    bot.click_relative(210, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not bot.find( "fatu_cad_cod_operacao_valor_movimentacao", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cod_operacao_valor_movimentacao")
                bot.click_relative(104, 25)
                self.type_down()
                self.enter()
                
                x=0
                while x<7:
                    if not bot.find( "fatu_cad_cod_operacao_valor_movimentacao", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_cod_operacao_valor_movimentacao")
                    bot.click_relative(104, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:         
                    if not self.find( "subtotalizacaonota", matching=0.97, waiting_time=10000):
                        self.not_found("subtotalizacaonota")
                    self.click_relative(89, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "tipodoemitente", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoemitente")
                self.click_relative(144, 28)
                self.type_down()
                self.enter()
                if not self.find( "tipodoemitente", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoemitente")
                self.click_relative(144, 28)
                self.type_down()
                self.enter()
                
                if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                    self.not_found("tipolanctodmed")
                self.click_relative(105, 25)
                self.type_down()
                self.enter()
                if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                    self.not_found("tipolanctodmed")
                self.click_relative(105, 25)
                self.type_down()
                self.enter()
                
                x=0
                while x<2:
                    if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                        self.not_found("tipolanctodmed")
                    self.click_relative(105, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "tipodocumentoefdreinf", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocumentoefdreinf")
                    self.click_relative(108, 23)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<3:
                    if not self.find( "tipodocumentoefdreinf", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocumentoefdreinf")
                    self.click_relative(108, 23)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "tipodocontroledesaldo", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocontroledesaldo")
                    self.click_relative(147, 28)
                    self.type_up()
                    self.enter()
                    x=x+1
                x=0
                while x<2:
                    if not self.find( "tipodocontroledesaldo", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocontroledesaldo")
                    self.click_relative(147, 28)
                    self.type_down()
                    self.enter()
                    x=x+1 
                    
                x=0
                while x<6:
                    if not self.find( "naturezaoperaacomunicipal", matching=0.97, waiting_time=10000):
                        self.not_found("naturezaoperaacomunicipal")
                    self.click_relative(163, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<7:
                    if not self.find( "indicadordanaturezadofretecontratado", matching=0.97, waiting_time=10000):
                        self.not_found("indicadordanaturezadofretecontratado")
                    self.click_relative(210, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "indicadordepresenca", matching=0.97, waiting_time=10000):
                    self.not_found("indicadordepresenca")
                self.click_relative(210, 25)
                self.type_up()
                self.enter()
                
                x=0
                while x<6:
                    if not self.find( "indicadordepresenca", matching=0.97, waiting_time=10000):
                        self.not_found("indicadordepresenca")
                    self.click_relative(210, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                
                x=0
                while x<6:
                    if not self.find( "custopedidocompranota", matching=0.97, waiting_time=10000):
                        self.not_found("custopedidocompranota")
                    self.click_relative(120, 27)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                                ####---INDICADORES E ALIQUOTAS---####
                                
                if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                    self.not_found("tipofunrural")
                self.click_relative(107, 28)
                self.type_down()
                self.enter()
                if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                    self.not_found("tipofunrural")
                self.click_relative(107, 28)
                self.type_up()
                self.enter()
                if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                    self.not_found("tipofunrural")
                self.click_relative(107, 28)
                self.type_up()
                self.enter()
                if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                    self.not_found("tipofunrural")
                self.click_relative(107, 28)
                self.type_down()
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<3:
                    if not self.find( "tiposenar", matching=0.97, waiting_time=10000):
                        self.not_found("tiposenar")
                    self.click_relative(111, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "tiposenar", matching=0.97, waiting_time=10000):
                    self.not_found("tiposenar")
                self.click_relative(111, 25)
                self.type_up()
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                
                if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                    self.not_found("quotacapitalfethab")
                self.click_relative(109, 27)
                self.type_up()
                self.enter()
                if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                    self.not_found("quotacapitalfethab")
                self.click_relative(109, 27)
                self.type_down()
                self.enter()
                if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                    self.not_found("quotacapitalfethab")
                self.click_relative(109, 27)
                self.type_down()
                self.enter()
                if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                    self.not_found("quotacapitalfethab")
                self.click_relative(109, 27)
                self.type_up()
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                    self.not_found("tipodespadmfacs")
                self.click_relative(112, 24)
                self.type_up()
                self.enter()
                if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                    self.not_found("tipodespadmfacs")
                self.click_relative(112, 24)
                self.type_down()
                self.enter()
                if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                    self.not_found("tipodespadmfacs")
                self.click_relative(112, 24)
                self.type_down()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<3:
                    if not self.find( "calcularicmssimples", matching=0.97, waiting_time=10000):
                        self.not_found("calcularicmssimples")
                    self.click_relative(100, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<6:
                    if not bot.find( "fatu_cad_cod_operacao_pis_cofins_natureza", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_cod_operacao_pis_cofins_natureza")
                    bot.click_relative(256, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<2:
                    if not self.find( "piscofinsnaturezadareceita", matching=0.97, waiting_time=10000):
                        self.not_found("piscofinsnaturezadareceita")
                    self.click_relative(192, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---BASES ADICIONAIS ICMS E ICMS ST---####
                
                x=0
                while x<4:                 
                    if not self.find( "basesadicionaisicmseicmsst", matching=0.97, waiting_time=10000):
                        self.not_found("basesadicionaisicmseicmsst")
                    self.click_relative(147, 46)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "baiist", matching=0.97, waiting_time=10000):
                        self.not_found("baiist")
                    self.click_relative(309, 46)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                x=0
                while x<4:    
                    if not self.find( "baiist", matching=0.97, waiting_time=10000):
                        self.not_found("baiist")
                    self.click_relative(469, 45)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                x=0
                while x<4:   
                    if not self.find( "bapc", matching=0.97, waiting_time=10000):
                        self.not_found("bapc")
                    self.click_relative(139, 45)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "bapc", matching=0.97, waiting_time=10000):
                        self.not_found("bapc")
                    self.click_relative(299, 44)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "bapc", matching=0.97, waiting_time=10000):
                        self.not_found("bapc")
                    self.click_relative(462, 46)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                                ####---CONTABILIZACAO---####
                                
                x=0
                while x<3:
                    if not self.find( "contabilizacaoporitemservico", matching=0.97, waiting_time=10000):
                        self.not_found("contabilizacaoporitemservico")
                    self.click_relative(229, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "contabilizacaoporitemservico", matching=0.97, waiting_time=10000):
                        self.not_found("contabilizacaoporitemservico")
                    self.click_relative(229, 25)
                    self.type_up()
                    self.enter()
                    x=x+1
                    
                if not self.find( "contabilizacaoliquido", matching=0.97, waiting_time=10000):
                    self.not_found("contabilizacaoliquido")
                self.click()           
                           
                if not self.find( "contabilizacaoporrcm", matching=0.97, waiting_time=10000):
                    self.not_found("contabilizacaoporrcm")
                self.click()
                
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABAIXANDO TELA---####
                
                if not self.find( "abaixartelaco", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelaco")
                self.click()
                
                x=0
                while x<5:                 
                    if not self.find( "abaixartelacomarcado", matching=0.97, waiting_time=10000):
                        self.not_found("abaixartelacomarcado")
                    self.double_click()
                    x=x+1       
                
                                ####---MARCADORES---####
                self.wait(2000)
                if not self.find( "nfdeimpostos", matching=0.97, waiting_time=10000):
                    self.not_found("nfdeimpostos")
                self.click()
                self.space()

                if not self.find( "nfpermitealterarimpostos", matching=0.97, waiting_time=10000):
                    self.not_found("nfpermitealterarimpostos")
                self.click()
                self.space()         
                if not bot.find( "fatu_cad_cod_movimentacao_ativo_imobilizado", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cod_movimentacao_ativo_imobilizado")
                bot.click()
                self.space()
                if not self.find( "nfdecupomfiscal", matching=0.97, waiting_time=10000):
                    self.not_found("nfdecupomfiscal")
                self.click()
                self.space()
                if not self.find( "nfdeaquisicaofpm", matching=0.97, waiting_time=10000):
                    self.not_found("nfdeaquisicaofpm")
                self.click()
                self.space()
                if not bot.find( "fatu_cad_descontar_gestao_leite", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_descontar_gestao_leite")
                bot.click()
                self.space()
                if not self.find( "gerareceituario", matching=0.97, waiting_time=10000):
                    self.not_found("gerareceituario")
                self.click()
                self.space()
                if not bot.find( "fatu_cad_cod_gera_receituario", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cod_gera_receituario")
                bot.click()
                if not self.find( "geracontacorrente", matching=0.97, waiting_time=10000):
                    self.not_found("geracontacorrente")
                self.click()
                self.space()
                if not self.find( "gerademandasaida", matching=0.97, waiting_time=10000):
                    self.not_found("gerademandasaida")
                self.click()
                self.space()
                if not bot.find( "fatu_cad_operacao_venda_compra", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_operacao_venda_compra")
                bot.click()
                self.space()
                if not self.find( "movimentosomentecompedido", matching=0.97, waiting_time=10000):
                    self.not_found("movimentosomentecompedido")
                self.click()
                self.space()
                if not self.find( "calcularcustomedio", matching=0.97, waiting_time=10000):
                    self.not_found("calcularcustomedio")
                self.click()
                self.space()
                if not self.find( "atualizarmargem", matching=0.97, waiting_time=10000):
                    self.not_found("atualizarmargem")
                self.click()
                self.space()
                if not bot.find( "fatu_cad_cod_valida_unit_desconto", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cod_valida_unit_desconto")
                bot.click()
                self.space()
                
                if not self.find( "descontarvaloricmsdototalnf", matching=0.97, waiting_time=10000):
                    self.not_found("descontarvaloricmsdototalnf")
                self.click()
                self.space()
                if not self.find( "retencaoiss1", matching=0.97, waiting_time=10000):
                    self.not_found("retencaoiss1")
                self.click()
                self.space()
                if not self.find( "atualizarprecodevenda", matching=0.97, waiting_time=10000):
                    self.not_found("atualizarprecodevenda")
                self.click()
                self.space()
                if not self.find( "atualizartabeladepreco", matching=0.97, waiting_time=10000):
                    self.not_found("atualizartabeladepreco")
                self.click()
                self.space()
                if not self.find( "geralivrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("geralivrosfiscais")
                self.click()
                self.space()
   
                if not self.find( "atualizarcustos", matching=0.97, waiting_time=10000):
                    self.not_found("atualizarcustos")
                self.click()
                self.space()
                if not self.find( "exigeliberacaosupervisor", matching=0.97, waiting_time=10000):
                    self.not_found("exigeliberacaosupervisor")
                self.click()
                self.space()
                if not self.find( "baseliquidaipi1", matching=0.97, waiting_time=10000):
                    self.not_found("baseliquidaipi1")
                self.click()
                self.space()
                
                if not self.find( "valoripioutras1", matching=0.97, waiting_time=10000):
                    self.not_found("valoripioutras1")
                self.click()
                self.space()
                if not bot.find( "fatu_cad_cod_valor_do_ipi", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cod_valor_do_ipi")
                bot.click()
                if not self.find( "exigeveiculoautocenter", matching=0.97, waiting_time=10000):
                    self.not_found("exigeveiculoautocenter")
                self.click()
                self.space()
                if not self.find( "exigedref1", matching=0.97, waiting_time=10000):
                    self.not_found("exigedref1")
                self.click()
                self.space()
                
                
                                ####---DADOS ADICIONAIS---####
                                
                if not self.find( "dadosadicionais", matching=0.97, waiting_time=10000):
                    self.not_found("dadosadicionais")
                self.click()
                if not self.find( "cfoppadraomovimento", matching=0.97, waiting_time=10000):
                    self.not_found("cfoppadraomovimento")
                self.click_relative(65, 27)
                if not self.find( "cod1352b", matching=0.97, waiting_time=10000):
                    self.not_found("cod1352b")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                if not self.find( "tabeladeprecositens", matching=0.97, waiting_time=10000):
                    self.not_found("tabeladeprecositens")
                self.click_relative(69, 30)
                if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                    self.not_found("cod00000tabela")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                self.backspace()
                self.backspace()
                if not self.find( "tabeladeprecosservicos", matching=0.97, waiting_time=10000):
                    self.not_found("tabeladeprecosservicos")
                self.click_relative(61, 25)
                if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                    self.not_found("cod00000tabela")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                self.backspace()
                self.backspace()
                if not self.find( "macrosparaobservacao", matching=0.97, waiting_time=10000):
                    self.not_found("macrosparaobservacao")
                self.click_relative(28, 30)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                    self.not_found("camposdisponiveis")
                self.click_relative(-13, 33)
                if not self.find( "clientesefornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("clientesefornecedores")
                self.click()
                if not self.find( "empresacodigo", matching=0.97, waiting_time=10000):
                    self.not_found("empresacodigo")
                self.click()
                if not self.find( "inserir", matching=0.97, waiting_time=10000):
                    self.not_found("inserir")
                self.click()
                if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                    self.not_found("camposdisponiveis")
                self.click_relative(-13, 33)
                if not self.find( "camposdevendedores", matching=0.97, waiting_time=10000):
                    self.not_found("camposdevendedores")
                self.click()
                if not self.find( "empresacodigo", matching=0.97, waiting_time=10000):
                    self.not_found("empresacodigo")
                self.click()
                if not self.find( "inserir", matching=0.97, waiting_time=10000):
                    self.not_found("inserir")
                self.click()
                if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                    self.not_found("camposdisponiveis")
                self.click_relative(-13, 33)
                if not self.find( "condicaopagamento", matching=0.97, waiting_time=10000):
                    self.not_found("condicaopagamento")
                self.click()
                if not self.find( "condicaocodigo", matching=0.97, waiting_time=10000):
                    self.not_found("condicaocodigo")
                self.click()
                if not self.find( "inserir", matching=0.97, waiting_time=10000):
                    self.not_found("inserir")
                self.click()
                
                                ####---FINALIZANDO CO---####
                
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                    self.not_found("digiteparalocalizar")
                self.click_relative(36, 31)
                
                
                
                #if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                #    self.not_found("codtesteestados")
                #self.click()
                # Aqui esta dando erro para excluir pois esta sendo utilizado em outro processo

                # if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_fiscal_paises_editar")
                # bot.click()
                # if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_fiscal_excluir_2411")
                # bot.click()
                # if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #     self.not_found("simexcluirteste")
                # self.click()
                
                # if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_receituario_retornar")
                # bot.click()
                # if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                #     not_found("fatu_cad_param_fiscal_localizar")
                # bot.click()
                
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---CODIGOS FISCAIS---####
                self.wait(2000)

                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "codigosfiscaiscfop", matching=0.97, waiting_time=10000):
                    self.not_found("codigosfiscaiscfop")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()
                self.type_keys_with_interval(1,'8748')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "operacaobuscacfop", matching=0.97, waiting_time=10000):
                    self.not_found("operacaobuscacfop")
                self.click_relative(66, 48)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "cod0001cfop", matching=0.97, waiting_time=10000):
                    self.not_found("cod0001cfop")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                if not self.find( "informacoesdagia", matching=0.97, waiting_time=10000):
                    self.not_found("informacoesdagia")
                self.click_relative(21, 44)
                self.type_keys_with_interval(1,'t1')
                self.enter()
                self.type_keys_with_interval(1,'t!')
                self.enter()
                if not self.find( "valorcontabilincidenabasenagia", matching=0.97, waiting_time=10000):
                    self.not_found("valorcontabilincidenabasenagia")
                self.click()
                
                if not self.find( "valorcontabilincidenabasenagiamarcado", matching=0.97, waiting_time=10000):
                    self.not_found("valorcontabilincidenabasenagiamarcado")
                self.click()
                if not self.find( "seentradadeduzir", matching=0.97, waiting_time=10000):
                    self.not_found("seentradadeduzir")
                self.click()
                if not self.find( "seentradadeduzirmarcado2", matching=0.97, waiting_time=10000):
                    self.not_found("seentradadeduzirmarcado2")
                self.click()            
                if not self.find( "seentradadeduzirmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("seentradadeduzirmarcado")
                self.click()
                if not self.find( "ativoimobilizado", matching=0.97, waiting_time=10000):
                    self.not_found("ativoimobilizado")
                self.click()
                self.space()
                self.space()
                #if not self.find( "ativoimobilizadomarcado2", matching=0.97, waiting_time=10000):
                #    self.not_found("ativoimobilizadomarcado2")
                #self.click()            
                #if not self.find( "ativoimobilizadomarcado", matching=0.97, waiting_time=10000):
                #    self.not_found("ativoimobilizadomarcado")
                #self.click()
                if not self.find( "materialdeusoeconsumolimpo", matching=0.97, waiting_time=10000):
                    self.not_found("materialdeusoeconsumolimpo")
                self.click()            
                if not self.find( "materialdeusoeconsumo", matching=0.97, waiting_time=10000):
                    self.not_found("materialdeusoeconsumo")
                self.click()
                self.space()           
                #if not self.find( "materialdeusoeconsumomarcado", matching=0.97, waiting_time=10000):
                #    self.not_found("materialdeusoeconsumomarcado")
                #self.click()
                if not self.find( "geraretencao", matching=0.97, waiting_time=10000):
                    self.not_found("geraretencao")
                self.click()
                self.space()
                self.space()
                #if not self.find( "geraretencaomarcado2", matching=0.97, waiting_time=10000):
                #    self.not_found("geraretencaomarcado2")
                #self.click()           
                #if not self.find( "geraretencaomarcado", matching=0.97, waiting_time=10000):
                #    self.not_found("geraretencaomarcado")
                #self.click()
                if not self.find( "coddfc", matching=0.97, waiting_time=10000):
                    self.not_found("coddfc")
                self.click_relative(12, 27)
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                if not self.find( "ignorarnomovimentoerelatorio", matching=0.97, waiting_time=10000):
                    self.not_found("ignorarnomovimentoerelatorio")
                self.click()
                if not self.find( "ignorarnomovimentoerelatoriomarcado", matching=0.97, waiting_time=10000):
                    self.not_found("ignorarnomovimentoerelatoriomarcado")
                self.click()
                if not self.find( "industrializacao", matching=0.97, waiting_time=10000):
                    self.not_found("industrializacao")
                self.click()
                
                if not self.find( "transporte", matching=0.97, waiting_time=10000):
                    self.not_found("transporte")
                self.click()
                if not self.find( "externo", matching=0.97, waiting_time=10000):
                    self.not_found("externo")
                self.click()
                if not self.find( "interno", matching=0.97, waiting_time=10000):
                    self.not_found("interno")
                self.click()
                if not self.find( "insumos", matching=0.97, waiting_time=10000):
                    self.not_found("insumos")
                self.click()
                if not self.find( "outros", matching=0.97, waiting_time=10000):
                    self.not_found("outros")
                self.click()
                if not self.find( "mercadorias", matching=0.97, waiting_time=10000):
                    self.not_found("mercadorias")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                    self.not_found("digiteparalocalizar")
                self.click_relative(36, 31)
                self.type_keys_with_interval(1,'te')
                self.enter()
                if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                    self.not_found("codtesteestados")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---CODIGOS FISCAIS IMP---####
                self.wait(1500)     
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "codigosfiscaisimportacao", matching=0.97, waiting_time=10000):
                    self.not_found("codigosfiscaisimportacao")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()
                if not self.find( "origem", matching=0.97, waiting_time=10000):
                    self.not_found("origem")
                self.click_relative(102, 6)
                self.backspace()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                    self.not_found("cod1911")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                self.wait(500)
                if not self.find( "destino", matching=0.97, waiting_time=10000):
                    self.not_found("destino")
                self.click_relative(102, 5)
                self.backspace()
                self.wait(1000)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                    self.not_found("cod1911")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                
                #if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                #   self.not_found("salvarco")
                #self.click()
                #if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                #    self.not_found("salvarco")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                    self.not_found("cod1911")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.wait(1000)
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---DECRETOS E OBSERVACOES---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "decretoseobservacoes", matching=0.97, waiting_time=10000):
                    self.not_found("decretoseobservacoes")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "tipos", matching=0.97, waiting_time=10000):
                    self.not_found("tipos")
                self.click_relative(372, 28)
                if not self.find( "tipos", matching=0.97, waiting_time=10000):
                    self.not_found("tipos")
                self.click_relative(719, 27)
                if not self.find( "tipos", matching=0.97, waiting_time=10000):
                    self.not_found("tipos")
                self.click_relative(1055, 26)
                if not self.find( "tipos", matching=0.97, waiting_time=10000):
                    self.not_found("tipos")
                self.click_relative(30, 28)
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                    self.not_found("camposdecretos")
                self.click_relative(59, -2)
                if not self.find( "camposdeclintes", matching=0.97, waiting_time=10000):
                    self.not_found("camposdeclintes")
                self.click()
                if not self.find( "bancocodigodecreto", matching=0.97, waiting_time=10000):
                    self.not_found("bancocodigodecreto")
                self.click()
                if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("inserirdecreto")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                    self.not_found("camposdecretos")
                self.click_relative(59, -2)
                if not self.find( "camposnfdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("camposnfdecreto")
                self.click()
                if not self.find( "bancocodigodecreto", matching=0.97, waiting_time=10000):
                    self.not_found("bancocodigodecreto")
                self.click()
                if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("inserirdecreto")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                    self.not_found("camposdecretos")
                self.click_relative(59, -2)
                if not self.find( "camposdepedidosdevendadecreto", matching=0.97, waiting_time=10000):
                    self.not_found("camposdepedidosdevendadecreto")
                self.click()
                if not self.find( "autenticodecreto", matching=0.97, waiting_time=10000):
                    self.not_found("autenticodecreto")
                self.click()
                if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("inserirdecreto")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                    self.not_found("camposdecretos")
                self.click_relative(59, -2)
                if not self.find( "camposdeconhecimentosdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("camposdeconhecimentosdecreto")
                self.click()
                if not self.find( "anttconsigdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("anttconsigdecreto")
                self.click()
                if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                    self.not_found("inserirdecreto")
                self.click()
                if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                    self.not_found("salvarco")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "descricaodecretoteste", matching=0.97, waiting_time=10000):
                    self.not_found("descricaodecretoteste")
                self.click()
                
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---SITUACOES---####
                
                self.wait(1500)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                    self.not_found("parametrosfiscais")
                self.click()
                if not self.find( "situacoes", matching=0.97, waiting_time=10000):
                    self.not_found("situacoes")
                self.click()           
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(500)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()
                if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                    self.not_found("incluirco")
                self.click()
                if not self.find( "operacaosituacao", matching=0.97, waiting_time=10000):
                    self.not_found("operacaosituacao")
                self.click_relative(50, 27)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "buscarcoddeop", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcoddeop")
                self.click_relative(43, 29)
                self.type_keys_with_interval(1,'0048')
                self.enter()
                
                if not self.find( "codop0048", matching=0.97, waiting_time=10000):
                    self.not_found("codop0048")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                self.wait(500)
                if not self.find( "regiaosituacao", matching=0.97, waiting_time=10000):
                    self.not_found("regiaosituacao")
                self.click_relative(47, 26)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_nordeste_situacoes_achar_btn", matching=0.97, waiting_time=10000):
                    not_found("fatu_nordeste_situacoes_achar_btn")
                bot.click()                                 
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                self.wait(500)
                if not self.find( "grupofiscalsituacao", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscalsituacao")
                self.click_relative(51, 30)
                if not self.find( "cod001btributado", matching=0.97, waiting_time=10000):
                    self.not_found("cod001btributado")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                
                                ####---ICMS---####
                                
                if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("icmsbasecalculo")
                self.click_relative(146, 50)            
                self.type_keys_with_interval(1,'123')
                if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("icmsbasecalculo")
                self.click_relative(140, 29)
                self.type_keys_with_interval(1,'123')
                x=0
                while x<5:
                    if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                        self.not_found("icmstipo")
                    self.click_relative(621, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<5:
                    if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                        self.not_found("icmstipo")
                    self.click_relative(621, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not self.find( "redutoraliquotabase", matching=0.97, waiting_time=10000):
                    self.not_found("redutoraliquotabase")
                self.click_relative(140, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                    self.not_found("saldobasereduzicms")
                self.click_relative(142, 31)
                self.type_down()
                self.enter()
                x=0
                while x<4:
                    if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                        self.not_found("icmsmodalidade")
                    self.click_relative(1261, 45)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<3:
                    if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                        self.not_found("icmsmodalidade")
                    self.click_relative(1261, 45)
                    self.type_up()
                    self.enter()
                    x=x+1
                x=0
                while x<20:
                    if not self.find( "situacaotributariaicms", matching=0.97, waiting_time=10000):
                        self.not_found("situacaotributariaicms")
                    self.click_relative(300, 96)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "baseicmsdiferencaliquota", matching=0.97, waiting_time=10000):
                    self.not_found("baseicmsdiferencaliquota")
                self.click_relative(141, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotadiferencialicms", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotadiferencialicms")
                self.click_relative(142, 27)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotaicmsdesoneracao", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotaicmsdesoneracao")
                self.click_relative(141, 30)           
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                x=0
                while x<12:
                    if not self.find( "motivodesoneracaoicms", matching=0.97, waiting_time=10000):
                        self.not_found("motivodesoneracaoicms")
                    self.click_relative(296, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.enter()    
                if not self.find( "descontadovalortotalicms", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotalicms")
                self.click()
                if not self.find( "descontadovalortotalmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotalmarcado")
                self.click()
                if not self.find( "descontadovalortotal1", matching=0.97, waiting_time=10000):
                    self.not_found("descontadovalortotal1")
                self.click()
                if not self.find( "calculardiferimentoicms", matching=0.97, waiting_time=10000):
                    self.not_found("calculardiferimentoicms")
                self.click()
                
                if not self.find( "cteemoutrasuf", matching=0.97, waiting_time=10000):
                    self.not_found("cteemoutrasuf")
                self.click()
                
                
                if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                    self.not_found("icmsstdifinterno")
                self.click_relative(197, 25)
                self.type_down()
                self.enter()
                if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                    self.not_found("icmsstdifinterno")
                self.click_relative(197, 25)
                self.type_down()
                self.enter()
                
                self.wait(1000)
                                ####---ICMS SUBS TRIBU---####  
                
                if not self.find( "icmssubstrib", matching=0.97, waiting_time=10000):
                    self.not_found("icmssubstrib")
                self.click_relative(143, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "icmssubstibaliq", matching=0.97, waiting_time=10000):
                    self.not_found("icmssubstibaliq")
                self.click_relative(305, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_up()
                self.enter()
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_down()
                self.enter()
                if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                    self.not_found("stnototaldodocumento")
                self.click_relative(140, 28)
                self.type_down()
                self.enter()
                self.enter()
                if not self.find( "reduzirvalordoicms", matching=0.97, waiting_time=10000):
                    self.not_found("reduzirvalordoicms")
                self.click()
                if not self.find( "reduzirvalordoicmsmarcado", matching=0.97, waiting_time=10000):
                    self.not_found("reduzirvalordoicmsmarcado")
                self.click()
                x=0
                while x<5:
                    if not self.find( "tipoantecipacaovalida", matching=0.97, waiting_time=10000):
                        self.not_found("tipoantecipacaovalida")
                    self.click_relative(295, 27)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<7:
                    if not bot.find( "fatu_modalidade_rel_cad_situacoes", matching=0.97, waiting_time=10000):
                        not_found("fatu_modalidade_rel_cad_situacoes")
                    bot.click_relative(343, 92)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "percentualreducaobaseicmsst", matching=0.97, waiting_time=10000):
                    self.not_found("percentualreducaobaseicmsst")
                self.click_relative(175, 23)
                self.type_keys_with_interval(1,'123')
                self.wait(1000)
                if not bot.find( "fatu_cad_situacoes_flecha_esquerda", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_flecha_esquerda")
                bot.click()
                x = 0
                while x < 31:
                    self.click()
                    x += 1
                
                if not self.find( "baseicmsdifst", matching=0.97, waiting_time=10000):
                    self.not_found("baseicmsdifst")
                self.click_relative(140, 30)
                self.type_keys_with_interval(1,'123')
                if not self.find( "aliquotadiferencialst", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotadiferencialst")
                self.click_relative(142, 30)
                self.type_keys_with_interval(1,'123') 
                self.wait(500)
                self.enter()             
                
                                ####---ICMS SUB TRIB RETIDA---####   
                
                if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                    self.not_found("icmsretida")
                self.click_relative(144, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()            
                if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                    self.not_found("icmsretida")
                self.click_relative(303, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                x=0
                while x<7:
                    if not self.find( "valororigembasedecalculo", matching=0.97, waiting_time=10000):
                        self.not_found("valororigembasedecalculo")
                    self.click_relative(297, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "aliquotafcpretida", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotafcpretida")
                self.click_relative(140, 32)
                self.type_keys_with_interval(1,'123')
                
                                ####---IPI---####
                
                if not self.find( "IPIbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("IPIbasecalculo")
                self.click_relative(143, 47)
                self.type_keys_with_interval(1,'123')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                
                if not self.find( "ipialiquota", matching=0.97, waiting_time=10000):
                    self.not_found("ipialiquota")
                self.click_relative(303, 46)
                self.type_keys_with_interval(1,'1')
                self.backspace()
                self.type_keys_with_interval(1,'0')
                if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                    self.not_found("fecharcalculadorasituacao")
                self.click()
                
                x=0
                while x<6:
                    if not self.find( "ipitipo", matching=0.97, waiting_time=10000):
                        self.not_found("ipitipo")
                    self.click_relative(624, 46)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "enquadramentoipi", matching=0.97, waiting_time=10000):
                    self.not_found("enquadramentoipi")
                self.click_relative(40, 27)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "ipirsquantidade", matching=0.97, waiting_time=10000):
                    self.not_found("ipirsquantidade")
                self.click_relative(141, 27)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<14:
                    if not bot.find( "fatu_cad_situacoes_situacao_tributaria", matching=0.97, waiting_time=10000):
                        not_found("fatu_cad_situacoes_situacao_tributaria")
                    bot.click_relative(297, 27)
                    self.type_down()
                    self.enter()
                    x=x+1

                self.wait(500)
                self.enter()
                self.space()
                self.enter()
                self.space()
                

                if not bot.find( "fatu_cad_situacoes_flecha_esquerda", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_flecha_esquerda")
                bot.click()
                x = 0
                while x < 31:
                    self.click()
                    x += 1
                

                if not bot.find( "fatu_cad_situacoes_frete_base_ipi", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_frete_base_ipi")
                bot.click()
                if not bot.find( "fatu_cad_situacoes_frete_base_marcado", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_frete_base_marcado")
                bot.click()
                if not bot.find( "fatu_cad_situacoes_ipi_base_sub", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_ipi_base_sub")
                bot.click()
                self.wait(1000)
                self.space()
                
                self.enter()
                if not self.find( "indicevariacaopreco", matching=0.97, waiting_time=10000):
                    self.not_found("indicevariacaopreco")
                self.click_relative(140, 30)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                    self.not_found("cancelacalculadoraipi")
                self.click()
                
                if not self.find( "basepresumidomapafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("basepresumidomapafiscal")
                self.click_relative(140, 26)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                    self.not_found("cancelacalculadoraipi")
                self.click()
                
                x=0
                while x<8:
                    if not self.find( "atividadepresumido", matching=0.97, waiting_time=10000):
                        self.not_found("atividadepresumido")
                    self.click_relative(300, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "aliquotaecf", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotaecf")
                self.click_relative(40, 27)
                self.type_keys_with_interval(1,'t1')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "datadevalidadeipi", matching=0.97, waiting_time=10000):
                    self.not_found("datadevalidadeipi")
                self.click_relative(140, 25)
                if not self.find( "diadatavalidade", matching=0.97, waiting_time=10000):
                    self.not_found("diadatavalidade")
                self.click_relative(97, 74)
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixandotelasituacao1", matching=0.97, waiting_time=10000):
                    self.not_found("abaixandotelasituacao1")
                self.click()
                x=0
                while x<11:
                    if not self.find( "abaixandotelasituacao2", matching=0.97, waiting_time=10000):
                        self.not_found("abaixandotelasituacao2")
                    self.click()
                    x=x+1
                
                                ####---AJUSTE SPED ICMS C197---####
                                
                if not self.find( "codigo", matching=0.97, waiting_time=10000):
                    self.not_found("codigo")
                self.click_relative(22, 28)
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "descricaoajuste", matching=0.97, waiting_time=10000):
                    self.not_found("descricaoajuste")
                self.click_relative(188, 44)
                self.type_keys_with_interval(1,'te12!@')    
                
                                ####---PIS, COFINS, ISS---####
                self.wait(1000)       
                if not self.find( "aba2piscofinsiss", matching=0.97, waiting_time=10000):
                    self.not_found("aba2piscofinsiss")
                self.click()
                if not self.find( "pisbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("pisbasecalculo")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "pisaliquota", matching=0.97, waiting_time=10000):
                    self.not_found("pisaliquota")
                self.click_relative(304, 47)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<5:
                    if not self.find( "tipopis", matching=0.97, waiting_time=10000):
                        self.not_found("tipopis")
                    self.click_relative(625, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                
                if not self.find( "pisvalordeunidade", matching=0.97, waiting_time=10000):
                    self.not_found("pisvalordeunidade")
                self.click_relative(786, 46)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<33:
                    if not self.find( "pissituacaotributaria", matching=0.97, waiting_time=10000):
                        self.not_found("pissituacaotributaria")
                    self.click_relative(1101, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<4:
                    if not self.find( "pisrateiocreditocomuns", matching=0.97, waiting_time=10000):
                        self.not_found("pisrateiocreditocomuns")
                    self.click_relative(304, 94)
                    self.type_down()
                    self.enter()
                    x=x+1
                

                if not bot.find( "fatu_cad_situacoes_descontar_valor_icms", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_descontar_valor_icms")
                bot.click()
                if not bot.find( "fatu_cad_situacoes_descontar_valor_icms_marcado", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_descontar_valor_icms_marcado")
                bot.click()
                self.wait(500)
                self.enter()
                self.space()
                    
                                ####---COFINS---####
                                
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(304, 47)
                self.type_keys_with_interval(1,'123')
                x=0
                while x<5:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(625, 47)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                self.click_relative(786, 46)
                self.type_keys_with_interval(1,'123')
                
                x=0
                while x<33:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(1101, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
            
                x=0
                while x<19:
                    if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                        self.not_found("cofinsbase")
                    self.click_relative(304, 94)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---ISS---####
                                
                if not self.find( "issbasecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("issbasecalculo")
                self.click_relative(145, 48)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'t1!')
                
                x=0
                while x<8:
                    if not self.find( "issexigiblidade", matching=0.97, waiting_time=10000):
                        self.not_found("issexigiblidade")
                    self.click_relative(787, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---OUTROS IMPOSTOS---####
                                
                if not self.find( "outrosimpostossuframa", matching=0.97, waiting_time=10000):
                    self.not_found("outrosimpostossuframa")
                self.click_relative(145, 46)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                
                                ####---RETENCOES---####
                                
                if not self.find( "retencoesaliquotairrf", matching=0.97, waiting_time=10000):
                    self.not_found("retencoesaliquotairrf")
                self.click_relative(144, 49)
                self.type_keys_with_interval(1,'123')
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
                
                self.type_keys_with_interval(1,'123')
                self.enter()
                
                
                                ####---DECRETOS E OBSERVACOES---####
                                
                if not self.find( "decretoseobservacoesemsituacao", matching=0.97, waiting_time=10000):
                    self.not_found("decretoseobservacoesemsituacao")
                self.click()
                if not self.find( "decretonf1", matching=0.97, waiting_time=10000):
                    self.not_found("decretonf1")
                self.click_relative(43, 28)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                if not self.find( "decretonf2", matching=0.97, waiting_time=10000):
                    self.not_found("decretonf2")
                self.click_relative(43, 25)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                
                if not self.find( "observacaonf1", matching=0.97, waiting_time=10000):
                    self.not_found("observacaonf1")
                self.click_relative(43, 26)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                if not self.find( "observacaonf2", matching=0.97, waiting_time=10000):
                    self.not_found("observacaonf2")
                self.click_relative(44, 29)
                if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                    self.not_found("cod001bdecretonf")
                self.click()
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                
                if not self.find( "cfopsituacao1", matching=0.97, waiting_time=10000):
                    self.not_found("cfopsituacao1")
                self.click_relative(58, 25)
                self.backspace()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "buscarcfop", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcfop")
                self.click_relative(59, 30)
                self.type_keys_with_interval(1,'9.999')
                self.enter()
                if not self.find( "cod9999cfop", matching=0.97, waiting_time=10000):
                    self.not_found("cod9999cfop")
                self.click()            
                if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcfoppadrao")
                self.click()
                
                if not self.find( "observacaocfop", matching=0.97, waiting_time=10000):
                    self.not_found("observacaocfop")
                self.click_relative(24, 50)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---GNRE---####
                                
                if not self.find( "gnresituacao", matching=0.97, waiting_time=10000):
                    self.not_found("gnresituacao")
                self.click()
                if not self.find( "incluirnovoregistrognresituacao", matching=0.97, waiting_time=10000):
                    self.not_found("incluirnovoregistrognresituacao")
                self.click()
                if not self.find( "cancelargnre", matching=0.97, waiting_time=10000):
                    self.not_found("cancelargnre")
                self.click()
                
                self.wait(1500)
                                ####---FINALIZACAO SITUACAO---###
                                
                if not self.find( "salvarsituacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvarsituacao")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "buscarcfop", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcfop")
                self.click_relative(59, 30)
                self.type_keys_with_interval(1,'0048')
                self.enter()
                if not bot.find( "fatu_cad_situacoes_achar_nordeste", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_situacoes_achar_nordeste")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                
                if not bot.find( "fatu_cad_param_fiscal_excluir_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_excluir_2411")
                bot.click()
                self.enter()
                #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirteste")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                ######################################################################
                ############# clientes,fornecedoresetransportadores ##################
                ######################################################################

                self.wait(1500)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                self.wait(1500)
                if not self.find( "clientes,fornecedoresetransportadores", matching=0.97, waiting_time=10000):
                    self.not_found("clientes,fornecedoresetransportadores")
                self.click()            
                self.wait(2000)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(2000)
                
                
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(100,'11517192935')
                #self.type_right()
                #self.type_right()
                self.tab()
                #if not self.find( "cpfcadastrocliente", matching=0.97, waiting_time=10000):
                #    self.not_found("cpfcadastrocliente")
                #self.click_relative(3, 25)
                #self.type_keys_with_interval(100,'086.580.33902')
                #self.enter()
                self.type_keys_with_interval(1,'14.734.534-8')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                #self.type_keys_with_interval(100,'te12!@')
                #self.tab()
                self.type_keys_with_interval(100,'01012022')
                self.tab()
                self.tab()
                
                
                
                                ####---ABA1 CADASTRO---####
                                
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(10,'8505 5370')
                if not self.find( "procurarcep", matching=0.97, waiting_time=10000):
                    self.not_found("procurarcep")
                self.click()
                if not self.find( "endprinproximo", matching=0.97, waiting_time=10000):
                    self.not_found("endprinproximo")
                self.click_relative(12, 88)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "municipioendprin", matching=0.97, waiting_time=10000):
                    self.not_found("municipioendprin")
                self.click_relative(403, 86)
                self.wait(1000)
                self.backspace()
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                self.wait(2000)
                
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.wait(500)
                if not self.find( "telefoneendprin", matching=0.97, waiting_time=10000):
                    self.not_found("telefoneendprin")
                self.click_relative(829, 88)
                self.type_keys_with_interval(1,'984119244')
                self.enter()
                
                x=0
                while x<7:
                    if not self.find( "operadoraendprin", matching=0.97, waiting_time=10000):
                        self.not_found("operadoraendprin")
                    self.click_relative(1068, 86)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "telempendprin", matching=0.97, waiting_time=10000):
                    self.not_found("telempendprin")
                self.click_relative(9, 129)
                self.type_keys_with_interval(1,'984119244')
                
                x=0
                while x<7:
                    if not self.find( "operadorateleemp", matching=0.97, waiting_time=10000):
                        self.not_found("operadorateleemp")
                    self.click_relative(260, 129)               
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "telcelendprin", matching=0.97, waiting_time=10000):
                    self.not_found("telcelendprin")
                self.click_relative(293, 130)
                self.type_keys_with_interval(1,'984119244')
                
                x=0
                while x<8:
                    if not self.find( "operadoratelcel", matching=0.97, waiting_time=10000):
                        self.not_found("operadoratelcel")
                    self.click_relative(533, 131)                              
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "longaltgoogle", matching=0.97, waiting_time=10000):
                    self.not_found("longaltgoogle")
                self.click()
                self.wait(5000)
                
                                ####---PESSOA FISICA---####
                                
                if not self.find( "nomefantasiapessoafisica", matching=0.97, waiting_time=10000):
                    self.not_found("nomefantasiapessoafisica")
                self.click_relative(13, 45)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<3:
                    if not self.find( "indicadorie", matching=0.97, waiting_time=10000):
                        self.not_found("indicadorie")
                    self.click_relative(124, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "sexopessoafisica", matching=0.97, waiting_time=10000):
                    self.not_found("sexopessoafisica")
                self.click_relative(74, 26)
                self.type_down()
                self.enter()
                if not self.find( "sexopessoafisica", matching=0.97, waiting_time=10000):
                    self.not_found("sexopessoafisica")
                self.click_relative(74, 26)
                self.type_down()
                self.enter()
                
                x=0
                while x<5:
                    if not self.find( "estadocivilpessoafisica", matching=0.97, waiting_time=10000):
                        self.not_found("estadocivilpessoafisica")
                    self.click_relative(92, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "pessoafisicaresponsavel", matching=0.97, waiting_time=10000):
                    self.not_found("pessoafisicaresponsavel")
                self.click_relative(13, 32)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---DATAS---####
                                
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(1,'t')
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.backspace()
                self.type_keys_with_interval(1,'!')
                self.backspace()
                self.type_keys_with_interval(1,'a')
                if not self.find( "controledatas", matching=0.97, waiting_time=10000):
                    self.not_found("controledatas")
                self.click_relative(6, 25)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "integracaodatas", matching=0.97, waiting_time=10000):
                    self.not_found("integracaodatas")
                self.click_relative(95, 27)
                self.type_down()
                self.enter()
                if not self.find( "integracaodatas", matching=0.97, waiting_time=10000):
                    self.not_found("integracaodatas")
                self.click_relative(95, 27)
                self.type_up()
                self.enter()
                
                if not self.find( "conveniodiadovencimento", matching=0.97, waiting_time=10000):
                    self.not_found("conveniodiadovencimento")
                self.double_click_relative(60, 20)
                if not self.find( "conveniodiadovencimento2", matching=0.97, waiting_time=10000):
                    self.not_found("conveniodiadovencimento2")
                self.click_relative(60, 32)
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'874')
                
                                ####---ENDERECO DE COBRANCA ALTERNATIVO---####
                                
                if not self.find( "enderecocomnumeroca", matching=0.97, waiting_time=10000):
                    self.not_found("enderecocomnumeroca")
                self.click_relative(7, 27)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "enderecodecobrancaalternativo", matching=0.97, waiting_time=10000):
                    self.not_found("enderecodecobrancaalternativo")
                self.click_relative(54, 87)
                self.type_keys_with_interval(1,'Guarapuava')
                if not self.find( "cod0001guarapuavab", matching=0.97, waiting_time=10000):
                    self.not_found("cod0001guarapuavab")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixartelacft1", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelacft1")
                self.click()
                
                x=0
                while x<10:
                    if not self.find( "abaixandotelacft2", matching=0.97, waiting_time=10000):
                        self.not_found("abaixandotelacft2")
                    self.double_click()
                    x=x+1
                
                                ####---DADOS DE CONTATO---####
                                
                if not self.find( "emailcft", matching=0.97, waiting_time=10000):
                    self.not_found("emailcft")
                self.click_relative(10, 28)
                self.type_keys_with_interval(1,'emailtesteteorema123@gmail.com')
                
                
                if not self.find( "emaildocecft", matching=0.97, waiting_time=10000):
                    self.not_found("emaildocecft")
                self.click_relative(9, 27)
                self.type_keys_with_interval(1,'emailtesteteorema123@gmail.com')

                if not self.find( "skypecft", matching=0.97, waiting_time=10000):
                    self.not_found("skypecft")
                self.click_relative(21, 25)           
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                
                self.type_keys_with_interval(1,'www.google.com.br')
                # if not self.find( "abrirsiteinternetexp", matching=0.97, waiting_time=10000):
                #     self.not_found("abrirsiteinternetexp")
                # self.click()
                # if not self.find( "fechargooglecerto", matching=0.97, waiting_time=10000):
                #     self.not_found("fechargooglecerto")
                # self.click_relative(1260, 6            
                if not self.find( "idmarketplace", matching=0.97, waiting_time=10000):
                    self.not_found("idmarketplace")
                self.click_relative(10, 28)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "contatodadosdecontato", matching=0.97, waiting_time=10000):
                    self.not_found("contatodadosdecontato")
                self.click_relative(925, 89)
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---MARCADORES---####
                                
                self.tab()                 
                #if not self.find( "clientemarcadores", matching=0.97, waiting_time=10000):
                #    self.not_found("clientemarcadores")
                #self.click()
                #self.space()
                
                # if not self.find( "clientemarcadocft", matching=0.97, waiting_time=10000):
                #     self.not_found("clientemarcadocft")
                # self.click()
                # if not self.find( "fornecedorcft", matching=0.97, waiting_time=10000):
                #     self.not_found("fornecedorcft")
                # self.click()
                # if not self.find( "fornecedorcft1", matching=0.97, waiting_time=10000):
                #     self.not_found("fornecedorcft1")
                # self.click()            
                # if not self.find( "fornecedorcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("fornecedorcftmarcado")
                # self.click()
                # if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                #     self.not_found("transportadorcfta1")
                # self.click_relative(163, 30)
                # if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                #     self.not_found("transportadorcfta1")
                # self.click_relative(163, 30)
                # if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                #     self.not_found("transportadorcfta1")
                # self.click_relative(163, 30)
                # if not self.find( "prospectcft", matching=0.97, waiting_time=10000):
                #     self.not_found("prospectcft")
                # self.click()
                # if not self.find( "prospectcft1", matching=0.97, waiting_time=10000):
                #     self.not_found("prospectcft1")
                # self.click()       
                # if not self.find( "prospectmarcadocft", matching=0.97, waiting_time=10000):
                #     self.not_found("prospectmarcadocft")
                # self.click()
                # if not self.find( "prestadorservicocft", matching=0.97, waiting_time=10000):
                #     self.not_found("prestadorservicocft")
                # self.click()
                        
                # if not self.find( "prestadorservicocftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("prestadorservicocftmarcado")
                # self.click()
                # if not self.find( "clienteinternocft", matching=0.97, waiting_time=10000):
                #     self.not_found("clienteinternocft")
                # self.click_relative(286, 51)
                # if not self.find( "clienteinternocft", matching=0.97, waiting_time=10000):
                #     self.not_found("clienteinternocft")
                # self.click_relative(286, 51)
                
                # if not self.find( "concorrentecft", matching=0.97, waiting_time=10000):
                #     self.not_found("concorrentecft")
                # self.click()
                # if not self.find( "concorrentecft1", matching=0.97, waiting_time=10000):
                #     self.not_found("concorrentecft1")
                # self.click()            
                # if not self.find( "concorrentecftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("concorrentecftmarcado")
                # self.click()
                # if not self.find( "consumidorfinalcft1", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorfinalcft1")
                # self.click()
                # if not self.find( "consumidorfinalcft2", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorfinalcft2")
                # self.click()           
                # if not self.find( "consumidorfinalcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorfinalcftmarcado")
                # self.click()
                # if not self.find( "consumidorfinalcft", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorfinalcft")
                # self.click()
                # if not self.find( "calculofunrural", matching=0.97, waiting_time=10000):
                #     self.not_found("calculofunrural")
                # self.click()
                            
                # if not self.find( "calculofunruralcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("calculofunruralcftmarcado")
                # self.click()
                # if not self.find( "calculosenarcft1", matching=0.97, waiting_time=10000):
                #     self.not_found("calculosenarcft1")
                # self.click()
                # if not self.find( "calculosenarcft2", matching=0.97, waiting_time=10000):
                #     self.not_found("calculosenarcft2")
                # self.click()                       
                # if not self.find( "calculosenarcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("calculosenarcftmarcado")
                # self.click()
                # if not self.find( "calculosenarcft", matching=0.97, waiting_time=10000):
                #     self.not_found("calculosenarcft")
                # self.click()
                # if not self.find( "quotacapitalcft", matching=0.97, waiting_time=10000):
                #     self.not_found("quotacapitalcft")
                # self.click()
                # if not self.find( "quotacapitalcft2", matching=0.97, waiting_time=10000):
                #     self.not_found("quotacapitalcft2")
                # self.click()
                
                # if not self.find( "quotacapitalcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("quotacapitalcftmarcado")
                # self.click()
                # if not self.find( "consumidorcrmcft", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorcrmcft")
                # self.click_relative(649, 51)
                # if not self.find( "consumidorcrmcft", matching=0.97, waiting_time=10000):
                #     self.not_found("consumidorcrmcft")
                # self.click_relative(649, 51)
                        
                
                # if not self.find( "itemcontroladocft1", matching=0.97, waiting_time=10000):
                #     self.not_found("itemcontroladocft1")
                # self.click()
                # if not self.find( "itemcontroladocftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("itemcontroladocftmarcado")
                # self.click()
                # if not self.find( "itemcontroladocft", matching=0.97, waiting_time=10000):
                #     self.not_found("itemcontroladocft")
                # self.click()
                # if not self.find( "art19cft", matching=0.97, waiting_time=10000):
                #     self.not_found("art19cft")
                # self.click()
                # if not self.find( "art19cftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("art19cftmarcado")
                # self.click()
                # if not self.find( "simplesnacionalcft", matching=0.97, waiting_time=10000):
                #     self.not_found("simplesnacionalcft")
                # self.click()
                # if not self.find( "simplesnacionalcftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("simplesnacionalcftmarcado")
                # self.click()
                # if not self.find( "integrarconcreteiracft", matching=0.97, waiting_time=10000):
                #     self.not_found("integrarconcreteiracft")
                # self.click()
                # if not self.find( "integrarconcreteiracftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("integrarconcreteiracftmarcado")
                # self.click()
                # if not self.find( "seguradorasiglacft1", matching=0.97, waiting_time=10000):
                #     self.not_found("seguradorasiglacft1")
                # self.click()
                # if not self.find( "seguradorasiglacftmarcado", matching=0.97, waiting_time=10000):
                #     self.not_found("seguradorasiglacftmarcado")
                # self.click()
                # if not self.find( "seguradorasiglacft", matching=0.97, waiting_time=10000):
                #     self.not_found("seguradorasiglacft")
                # self.click()
                # if not self.find( "siglaseguradora", matching=0.97, waiting_time=10000):
                #     self.not_found("siglaseguradora")
                # self.click_relative(6, 26)
                # self.type_keys_with_interval(1,'t1!')
                
                x=0
                while x<16:
                        self.tab()
                        self.space()
                        self.space()
                        x=x+1
                        
                                ####---ABA2 AGRUPAMENTO---####
                    
                self.wait(1500)
                if not self.find( "aba2agrupamentocft", matching=0.97, waiting_time=10000):
                    self.not_found("aba2agrupamentocft")
                self.click()
                if not self.find( "localdecobrancacft", matching=0.97, waiting_time=10000):
                    self.not_found("localdecobrancacft")
                self.click_relative(67, 25)
                if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod00001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "vendedorcompradorcft", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorcompradorcft")
                self.click_relative(64, 26)
                #if not self.find( "cod00101cft", matching=0.97, waiting_time=10000):
                #    self.not_found("cod00101cft")
                #self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "classificacaocft", matching=0.97, waiting_time=10000):
                    self.not_found("classificacaocft")
                self.click_relative(69, 25)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "codcontabilfixocft", matching=0.97, waiting_time=10000):
                    self.not_found("codcontabilfixocft")
                self.click_relative(65, 25)
                self.wait(1000)
                self.type_keys_with_interval(100,"00001")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "tabeladeprecositenscft", matching=0.97, waiting_time=10000):
                    self.not_found("tabeladeprecositenscft")
                self.click_relative(66, 25)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.backspace()
                if not self.find( "transportadoragrupamentocft", matching=0.97, waiting_time=10000):
                    self.not_found("transportadoragrupamentocft")
                self.click_relative(86, 256)            
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "ramodeatividadecft", matching=0.97, waiting_time=10000):
                    self.not_found("ramodeatividadecft")
                self.click_relative(68, 24)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "planofinanceirocft", matching=0.97, waiting_time=10000):
                    self.not_found("planofinanceirocft")
                self.click_relative(83, 26)
                self.wait(500)
                self.type_keys_with_interval(100,"001001001")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()

                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "contacorrentecft", matching=0.97, waiting_time=10000):
                    self.not_found("contacorrentecft")
                self.click_relative(68, 26)
                if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "segmentocft", matching=0.97, waiting_time=10000):
                    self.not_found("segmentocft")
                self.click_relative(66, 24)
                if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod00001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "tabeladeprecosservicoscft", matching=0.97, waiting_time=10000):
                    self.not_found("tabeladeprecosservicoscft")
                self.click_relative(66, 31)
                if not self.find( "cod00000cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod00000cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.backspace()
                if not self.find( "condicaodepagamento", matching=0.97, waiting_time=10000):
                    self.not_found("condicaodepagamento")
                self.click_relative(67, 26)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "comissaocft", matching=0.97, waiting_time=10000):
                    self.not_found("comissaocft")
                self.click_relative(68, 27)
                if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "centrodecustocft", matching=0.97, waiting_time=10000):
                    self.not_found("centrodecustocft")
                self.click_relative(85, 27)
                if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.backspace()
                if not self.find( "codigocontabilfixocft", matching=0.97, waiting_time=10000):
                    self.not_found("codigocontabilfixocft")
                self.click_relative(66, 26)
                self.wait(500)
                self.type_keys_with_interval(100,"00051")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "linhacft", matching=0.97, waiting_time=10000):
                    self.not_found("linhacft")
                self.click_relative(67, 26)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "operacaopdvbalcaocft", matching=0.97, waiting_time=10000):
                    self.not_found("operacaopdvbalcaocft")
                self.click_relative(67, 26)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "cod0002cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod0002cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                
                                ####---ABA2 P2 CFT---####
                    
                if not self.find( "aba2p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba2p2cft")
                self.click()
                if not self.find( "codigocontabilclientescft", matching=0.97, waiting_time=10000):
                    self.not_found("codigocontabilclientescft")
                self.click_relative(63, 27)
                self.type_keys_with_interval(100,"00051")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "codigocontabilfornecedorescft", matching=0.97, waiting_time=10000):
                    self.not_found("codigocontabilfornecedorescft")
                self.click_relative(65, 25)
                self.type_keys_with_interval(100,"00051")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                
                                ####---CODIGOS CONTABEIS MULTIEMPRESA---####
                                
                if not self.find( "aba2p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba2p3cft")
                self.click()
                if not self.find( "aba4cft", matching=0.97, waiting_time=10000):
                        self.not_found("aba4cft")
                self.click()
                x=0
                while x<7:
                    if not self.find( "situacaoespecialtipoassinantecft", matching=0.97, waiting_time=10000):
                        self.not_found("situacaoespecialtipoassinantecft")
                    self.click_relative(290, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                #if not self.find( "aba8transportadoresconfig", matching=0.97, waiting_time=10000):
                #    self.not_found("aba8transportadoresconfig")
                #self.click()
                #if not self.find( "codidentinsstransportadoresa8", matching=0.97, waiting_time=10000):
                #    self.not_found("codidentinsstransportadoresa8")
                #self.click_relative(139, 87)
                #self.type_keys_with_interval(1,'12312312312')
                if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                    self.not_found("aba2cftparte2")
                self.click()          
                if not self.find( "addnovoregistroa2p3_CFT", matching=0.97, waiting_time=10000):
                    self.not_found("addnovoregistroa2p3_CFT")
                self.click_relative(11, 162)
                self.enter()
                if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                    self.not_found("aba2cftparte2")
                self.click()
                self.enter()
                if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                    self.not_found("aba2cftparte2")
                self.click()           
                if not self.find( "codcontabilclientecft", matching=0.97, waiting_time=10000):
                    self.not_found("codcontabilclientecft")
                self.click_relative(-110, 50)
                self.enter()
                        
                self.type_keys_with_interval(100,"00051")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.wait(500)
                self.enter()
                self.wait(500)
                self.enter()
                if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                    self.not_found("aba2cftparte2")
                self.click()
                if not self.find( "codigocontabilfornecedor", matching=0.97, waiting_time=10000):
                    self.not_found("codigocontabilfornecedor")
                self.click_relative(60, 26)
                self.enter()
                self.type_keys_with_interval(100,"00051")
                if not bot.find( "fatu_cad_municipios_btn_localizar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_municipios_btn_localizar_2411")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.enter()
                self.wait(500)
                self.enter()
                if not self.find( "commitcodcontabilcft", matching=0.97, waiting_time=10000):
                    self.not_found("commitcodcontabilcft")
                self.click_relative(9, 7)            
                if not self.find( "excluir_a2p2_cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluir_a2p2_cft")
                self.click_relative(12, 188)
                self.enter()                                               
                #if not self.find( "simexcluircommit", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircommit")
                #self.click()
                self.wait(500)
                self.enter()
                
                                ####---ABA3 PESSOA FISICA---####
                                
                self.wait(1500)
                if not self.find( "aba3cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba3cft")
                self.click()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(100,'te12!@')
                self.enter()                 
                self.wait(500)
                self.type_keys_with_interval(100,'01012022')
                self.tab()
                self.wait(500)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'99147252547')
                
                x=0
                while x<6:
                    if not self.find( "telefoneaba3cft", matching=0.97, waiting_time=10000):
                        self.not_found("telefoneaba3cft")
                    self.click_relative(262, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                                ####---MORADIA E OUTRAS RENDAS---####
                                
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'874')
                if not self.find( "casapropriacft", matching=0.97, waiting_time=10000):
                    self.not_found("casapropriacft")
                self.click()
                
                if not self.find( "possuiautomovela3cft", matching=0.97, waiting_time=10000):
                    self.not_found("possuiautomovela3cft")
                self.click_relative(710, 49)
                
                
                
                
                                ####---INFORMACOES SOBRE PAI/MAE---####
                                
                if not self.find( "infopaimaecft", matching=0.97, waiting_time=10000):
                    self.not_found("infopaimaecft")
                self.click_relative(13, 43)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---INFORMACOES SOBRE CONJUGE---####
                                
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(100,'01012000')
                self.enter()
                self.type_keys_with_interval(100,'08658033902')
                self.enter()
                self.type_keys_with_interval(100,'147345348')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(100,'984119244')
                x=0
                while x<5:
                    if not self.find( "telefoneservicocft", matching=0.97, waiting_time=10000):
                        self.not_found("telefoneservicocft")
                    self.click_relative(201, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.type_keys_with_interval(1,'874')
                self.enter()
                
                                ####---ABAIXANDO TELA---####
                                
                if not self.find( "abaixartelacft1", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelacft1")
                self.click()
                
                x=0
                while x<5:
                    if not self.find( "abaixandotelacft2", matching=0.97, waiting_time=10000):
                        self.not_found("abaixandotelacft2")
                    self.double_click()
                    x=x+1
                
                                ####---FOTO---####
                                
                #if not self.find( "inserirfotocft", matching=0.97, waiting_time=10000):
                #    self.not_found("inserirfotocft")
                #self.click()
                #self.key_esc()
                #if not self.find( "fotocft", matching=0.97, waiting_time=10000):
                #    self.not_found("fotocft")
                #self.click()
                #if not self.find( "abrirfotocft", matching=0.97, waiting_time=10000):
                #    self.not_found("abrirfotocft")
                #self.click()
                #if not self.find( "excluirfotocft", matching=0.97, waiting_time=10000):
                #    self.not_found("excluirfotocft")
                #self.click()
                
                
                                ####---ABA4 CFT---####
                                
                if not self.find( "aba4cft2", matching=0.97, waiting_time=10000):
                    self.not_found("aba4cft2")
                self.click()
                if not self.find( "rotadeentregacft", matching=0.97, waiting_time=10000):
                    self.not_found("rotadeentregacft")
                self.click_relative(66, 46)
                if not self.find( "cod00002cftrota", matching=0.97, waiting_time=10000):
                    self.not_found("cod00002cftrota")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                
                x=0
                while x<6:
                    if not self.find( "tipofretecft", matching=0.97, waiting_time=10000):
                        self.not_found("tipofretecft")
                    self.click_relative(619, 47)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                                ####---ROTA DIAS DA SEMANA---####    
                    
                if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana")
                self.click_relative(14, 29)
                if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana")
                self.click_relative(14, 29)
                if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana")
                self.click_relative(14, 29)
                if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana2")
                self.click_relative(16, 48)
                if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana2")
                self.click_relative(16, 48)
                if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana2")
                self.click_relative(16, 48)
                if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana2")
                self.click_relative(16, 48)
                if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana3")
                self.click_relative(97, 29)
                if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana3")
                self.click_relative(97, 29)
                if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana3")
                self.click_relative(97, 29)
                if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana3")
                self.click_relative(97, 29)
                if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana4")
                self.click_relative(96, 48)
                if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana4")
                self.click_relative(96, 48)
                if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana4")
                self.click_relative(96, 48)
                if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana4")
                self.click_relative(96, 48)
                if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana5")
                self.click_relative(176, 30)
                if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana5")
                self.click_relative(176, 30)
                if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana5")
                self.click_relative(176, 30)
                if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana5")
                self.click_relative(176, 30)
                if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana6")
                self.click_relative(177, 45)
                if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana6")
                self.click_relative(177, 45)
                if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana6")
                self.click_relative(177, 45)
                if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana6")
                self.click_relative(177, 45)
                if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana7")
                self.click_relative(257, 30)
                if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana7")
                self.click_relative(257, 30)
                if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana7")
                self.click_relative(257, 30)
                if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                    self.not_found("rotadiasdasemana7")
                self.click_relative(257, 30)
                if not self.find( "diasdociclocft", matching=0.97, waiting_time=10000):
                    self.not_found("diasdociclocft")
                self.click_relative(57, 28)
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
                
                                ####---INFORMACOES ADICIONAIS---####
                
                x=0
                while x<7:                 
                    if not self.find( "indicadorpaacft", matching=0.97, waiting_time=10000):
                        self.not_found("indicadorpaacft")
                    self.click_relative(159, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                x=0
                while x<5:
                    if not self.find( "indicadorcomcft", matching=0.97, waiting_time=10000):
                        self.not_found("indicadorcomcft")
                    self.click_relative(157, 26)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'te12!')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---DADOS DO CONTABILISTA---####
                                
                if not self.find( "crccontabilistacft", matching=0.97, waiting_time=10000):
                    self.not_found("crccontabilistacft")
                self.click_relative(9, 28)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'12312312313212')
                
                                ####---DADOS DO COOPERADO---####
                                
                if not self.find( "cooperadocft", matching=0.97, waiting_time=10000):
                    self.not_found("cooperadocft")
                self.click_relative(11, 35)
                if not self.find( "cooperadocft", matching=0.97, waiting_time=10000):
                    self.not_found("cooperadocft")
                self.click_relative(11, 35)
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                
                                ####---OBSERVACAO---####
                                
                if not self.find( "observacaocft", matching=0.97, waiting_time=10000):
                    self.not_found("observacaocft")
                self.click_relative(20, 50)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA5 CFT---####
                                
                if not self.find( "aba5cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba5cft")
                self.click()
                if not self.find( "limiteultrapassadocft", matching=0.97, waiting_time=10000):
                    self.not_found("limiteultrapassadocft")
                self.click()
                if not self.find( "ultrapassouprazocft", matching=0.97, waiting_time=10000):
                    self.not_found("ultrapassouprazocft")
                self.click()
                if not self.find( "chequedevolvidocft", matching=0.97, waiting_time=10000):
                    self.not_found("chequedevolvidocft")
                self.click()
                if not self.find( "chequeroubadocft", matching=0.97, waiting_time=10000):
                    self.not_found("chequeroubadocft")
                self.click()
                if not self.find( "vendasomenteavistacft", matching=0.97, waiting_time=10000):
                    self.not_found("vendasomenteavistacft")
                self.click()
                if not self.find( "spcpempresacft", matching=0.97, waiting_time=10000):
                    self.not_found("spcpempresacft")
                self.click()
                if not self.find( "bloqueadocft", matching=0.97, waiting_time=10000):
                    self.not_found("bloqueadocft")
                self.click()
                if not self.find( "clientevipcft", matching=0.97, waiting_time=10000):
                    self.not_found("clientevipcft")
                self.click()
                
                                ####---LIMITE DE CRÉDITO---###
                
                if not self.find( "limitecrédito", matching=0.97, waiting_time=10000):
                    self.not_found("limitecrédito")
                self.click_relative(103, 44)
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.enter()
                
                                ####---VMP---####
                                
                self.enter()
                self.type_keys_with_interval(1,'123')
                
                                ####---VENCIMENTOS DIAS DA SEMANA---####
                                
                if not self.find( "vencimentossegundacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentossegundacft")
                self.click_relative(12, 26)
                if not self.find( "vencimentossegundacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentossegundacft")
                self.click_relative(12, 26)
                if not self.find( "vencimentostercacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentostercacft")
                self.click_relative(13, 48)
                if not self.find( "vencimentostercacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentostercacft")
                self.click_relative(13, 48)
                if not self.find( "vencimentosquartacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentosquartacft")
                self.click_relative(134, 28)
                if not self.find( "vencimentosquartacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentosquartacft")
                self.click_relative(134, 28)
                if not self.find( "vencimentosquintacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentosquintacft")
                self.click_relative(130, 46)
                if not self.find( "vencimentosquintacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentosquintacft")
                self.click_relative(130, 46)
                if not self.find( "vencimentossextacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentossextacft")
                self.click_relative(252, 26)
                if not self.find( "vencimentossextacft", matching=0.97, waiting_time=10000):
                    self.not_found("vencimentossextacft")
                self.click_relative(252, 26)
                
                x=0
                while x<3:
                    if not self.find( "gerarvencimentos", matching=0.97, waiting_time=10000):
                        self.not_found("gerarvencimentos")
                    self.click_relative(478, 43)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "descontoporcentagemboletocft", matching=0.97, waiting_time=10000):
                    self.not_found("descontoporcentagemboletocft")
                self.click_relative(100, 43)
                self.type_keys_with_interval(1,'123')
                if not self.find( "descontovalorcft", matching=0.97, waiting_time=10000):
                    self.not_found("descontovalorcft")
                self.click_relative(303, 46)
                self.type_keys_with_interval(1,'123')
                
                                ####---ABA5 P2 CFT---####
                                
                if not self.find( "aba5p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p2cft")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA5 P3 CFT---####
                                
                if not self.find( "aba5p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p3cft")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA5 P4 CFT---####
                                
                if not self.find( "aba5p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba5p4cft")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                
                                ####---ABA6 P1 CFT---####
                                
                if not self.find( "aba6cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba6cft")
                self.click()
                if not self.find( "commitspccft", matching=0.97, waiting_time=10000):
                    self.not_found("commitspccft")
                self.click_relative(-17, 8)          
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarcommitspccft", matching=0.97, waiting_time=10000):
                    self.not_found("salvarcommitspccft")
                self.click()            
                if not self.find( "excluirspccft", matching=0.97, waiting_time=10000):
                    self.not_found("excluirspccft")
                self.click_relative(-20, 32)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()
                
                                ####---ABA6 P2---####
                self.wait(1500)
                if not self.find( "aba6p2", matching=0.97, waiting_time=10000):
                    self.not_found("aba6p2")
                self.click()
                if not self.find( "addregisrepresentantesa6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("addregisrepresentantesa6p2cft")
                self.click_relative(-47, 10)            
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'08658033902')
                self.enter()
                self.type_keys_with_interval(1,'147345348')
                if not self.find( "municipioa6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("municipioa6p2cft")
                self.click_relative(99, 4)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(100,'85055370')
                if not bot.find( "fatu_cad_clientes_achar_cep", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_clientes_achar_cep")
                bot.click()
                if not self.find( "complementoa6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("complementoa6p2cft")
                self.click_relative(82, 4)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'123123123123')
                self.enter()
                self.type_keys_with_interval(1,'123123123123')
                x=0
                while x<7:
                    if not self.find( "celulara6p2cft", matching=0.97, waiting_time=10000):
                        self.not_found("celulara6p2cft")
                    self.click_relative(290, 5)
                    self.type_down()
                    self.enter()
                    x=x+1
                if not self.find( "faxa6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("faxa6p2cft")
                self.click_relative(38, 4)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvara6p2", matching=0.97, waiting_time=10000):
                    self.not_found("salvara6p2")
                self.click_relative(-50, 53)
                if not self.find( "exxcluira6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("exxcluira6p2cft")
                self.click_relative(-50, 34)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P3---####
                                
                if not self.find( "a6p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p3cft")
                self.click()
                
                if not self.find( "novoregistroa6p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("novoregistroa6p3cft")
                self.click_relative(-133, 9)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()
                if not self.find( "salvara6p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("salvara6p3cft")
                self.click_relative(-136, 52)
                if not self.find( "excluira6p3cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p3cft")
                self.click_relative(-137, 35)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()
                
                                ####---ABA6 P4---####
                self.wait(1500)

                if not self.find( "aba6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba6p4cft")
                self.click()
                if not self.find( "novoregistroa6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("novoregistroa6p4cft")
                self.click_relative(-226, 9)
                if not self.find( "tipodocontatocft", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocontatocft")
                self.click_relative(79, 56)
                x=0
                while x<6:
                    if not self.find( "tipodocontatocfta6p4", matching=0.97, waiting_time=10000):
                        self.not_found("tipodocontatocfta6p4")
                    self.click_relative(232, 61)
                    self.type_down()
                    self.enter()
                    x=x+1

                self.tab()
                self.type_keys_with_interval(100,'08658033902')
                self.tab()
                self.type_keys_with_interval(100,'147345348')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(100,'01012000')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(100,'85055370')
                if not bot.find( "fatu_cad_cliente_achar_cep_buscar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_cliente_achar_cep_buscar")
                bot.click()
                self.tab()
                if not self.find( "crca6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("crca6p4cft")
                self.click_relative(60, 3)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "botaobuscarmunicipioa6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("botaobuscarmunicipioa6p4cft")
                self.click_relative(106, 6)
                
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123123123123')
                x=0
                while x<8:
                    if not self.find( "operadoracelular1a6p4cft", matching=0.97, waiting_time=10000):
                        self.not_found("operadoracelular1a6p4cft")
                    self.click_relative(236, 190)
                    self.type_down()
                    self.enter()
                    x=x+1

                self.tab()
                self.type_keys_with_interval(1,'123123123123')
                x=0
                while x<7:
                    if not self.find( "operadora2a6p4cft", matching=0.97, waiting_time=10000):
                        self.not_found("operadora2a6p4cft")
                    self.click_relative(633, 189)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123123123123')
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.wait(1000)
                if not self.find( "recebeemaila6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("recebeemaila6p4cft")
                self.click_relative(564, 6)
                self.wait(1000)
                #if not self.find( "recebemaildocecfta6p4", matching=0.97, waiting_time=10000):
                #    self.not_found("recebemaildocecfta6p4")
                #self.click()
                # if not self.find( "recebemailvendascfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailvendascfta6p4")
                # self.click()
                # if not self.find( "recebemailcomprascfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailcomprascfta6p4")
                # self.click()
                # if not self.find( "recebemailfinana6p4cft", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailfinana6p4cft")
                # self.click()
                # if not self.find( "recebemailrhcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailrhcfta6p4")
                # self.click()
                # if not self.find( "recebemailfiscalcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailfiscalcfta6p4")
                # self.click()
                # if not self.find( "recebemailcontabilcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailcontabilcfta6p4")
                # self.click()
                # self.type_down()
                # if not self.find( "recebemailcontratoa6p4cft", matching=0.97, waiting_time=10000):
                #     self.not_found("recebemailcontratoa6p4cft")
                # self.click()
                # if not self.find( "recontratocfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recontratocfta6p4")
                # self.click()
                # if not self.find( "recontabilcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("recontabilcfta6p4")
                # self.click()
                # if not self.find( "refiscalcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("refiscalcfta6p4")
                # self.click()
                # if not self.find( "rerhcfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("rerhcfta6p4")
                # self.click()
                # if not self.find( "refinanceirocft2", matching=0.97, waiting_time=10000):
                #     self.not_found("refinanceirocft2")
                # self.click()            
                # if not self.find( "recomprascft2", matching=0.97, waiting_time=10000):
                #     self.not_found("recomprascft2")
                # self.click()           
                # if not self.find( "revendascfta6p4", matching=0.97, waiting_time=10000):
                #     self.not_found("revendascfta6p4")
                # self.click()
                #if not self.find( "redocecfta6p4", matching=0.97, waiting_time=10000):
                #    self.not_found("redocecfta6p4")
                #self.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvara6p4", matching=0.97, waiting_time=10000):
                    self.not_found("salvara6p4")
                self.click_relative(-224, 55)
                if not self.find( "excluira6p4", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p4")
                self.click_relative(-226, 32)
                if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluircft1")
                self.click()
                self.tab()

                                ####---ABA6 P5---####
                                
                if not self.find( "a6p5cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p5cft")
                self.click()
                if not self.find( "addregistroa6p5", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroa6p5")
                self.click_relative(-328, 9)
                if not self.find( "procuraavaliacaoa6p5", matching=0.97, waiting_time=10000):
                    self.not_found("procuraavaliacaoa6p5")
                self.click_relative(113, 45)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "dataa6p5", matching=0.97, waiting_time=10000):
                    self.not_found("dataa6p5")
                self.click_relative(466, 44)
                self.type_keys_with_interval(100,'01012022')
                if not self.find( "commita6p5", matching=0.97, waiting_time=10000):
                    self.not_found("commita6p5")
                self.click_relative(-17, 31)
                if not self.find( "oka6p5cft", matching=0.97, waiting_time=10000):
                    self.not_found("oka6p5cft")
                self.click()
                if not self.find( "cancelarcfta6p5", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarcfta6p5")
                self.click_relative(-17, 52)
                
                                ####---ABA6 P6---####
                                
                if not self.find( "a6p6cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p6cft")
                self.click()
                if not self.find( "adda6p6cft", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p6cft")
                self.click_relative(-387, 9)
                #if not self.find( "codtestecfta6p6", matching=0.97, waiting_time=10000):
                #    self.not_found("codtestecfta6p6")
                #self.click_relative(-98, 7)
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "excluira6p6", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p6")
                self.click_relative(-389, 32)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P7---####
                                
                if not self.find( "a6p7cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p7cft")
                self.click()
                if not self.find( "adda6p7cft", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p7cft")
                self.click_relative(-501, 9)
                if not self.find( "procurarquivoacfta6", matching=0.97, waiting_time=10000):
                    self.not_found("procurarquivoacfta6")
                self.click() 
                self.wait(500)           
                #if not self.find( "selecionararquivoa6p7cft", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionararquivoa6p7cft")
                #self.click_relative(145, 120)
                #if not self.find( "abrirarquivocfta6", matching=0.97, waiting_time=10000):
                #    self.not_found("abrirarquivocfta6")
                #self.click()
                self.key_esc()
                self.wait(500)          
                if not self.find( "tipoa6p7cft", matching=0.97, waiting_time=10000):
                    self.not_found("tipoa6p7cft")
                self.click_relative(709, 31)
                self.enter()
                if not self.find( "obsa6p7cft", matching=0.97, waiting_time=10000):
                    self.not_found("obsa6p7cft")
                self.click_relative(9, 31)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "anexoarquivocfta6p7", matching=0.97, waiting_time=10000):
                    self.not_found("anexoarquivocfta6p7")
                self.click_relative(7, 142)
                self.enter()
                self.key_esc()
                self.key_esc()
                #if not self.find( "cancelaarqteste1", matching=0.97, waiting_time=10000):
                #    self.not_found("cancelaarqteste1")
                #self.click_relative(5, 184)
                #if not self.find( "retornaanexoarqteste1", matching=0.97, waiting_time=10000):
                #    self.not_found("retornaanexoarqteste1")
                #self.click_relative(25, 41)          
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not self.find( "excluira6p7cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p7cft")
                self.click_relative(-502, 32)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P8---####
                                
                if not self.find( "a6p8cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p8cft")
                self.click()
                if not self.find( "addcfta6p8", matching=0.97, waiting_time=10000):
                    self.not_found("addcfta6p8")
                self.click_relative(-572, 9)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(1,'123')
                self.enter()
                self.type_keys_with_interval(1,'12')
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(100,'01012022')
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "gerarfinanceironfcfta6", matching=0.97, waiting_time=10000):
                    self.not_found("gerarfinanceironfcfta6")
                self.click_relative(1125, 45)
                if not self.find( "gerarfinanceironfcfta6", matching=0.97, waiting_time=10000):
                    self.not_found("gerarfinanceironfcfta6")
                self.click_relative(1125, 45)
                self.enter()
                self.type_keys_with_interval(1,'123')
                if not self.find( "tipovalorimplantacao", matching=0.97, waiting_time=10000):
                    self.not_found("tipovalorimplantacao")
                self.click_relative(115, 87)
                self.type_down()
                self.enter()
                if not self.find( "tipovalorimplantacao", matching=0.97, waiting_time=10000):
                    self.not_found("tipovalorimplantacao")
                self.click_relative(115, 87)
                self.type_up()
                self.enter()
                if not self.find( "tipodocontrato", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocontrato")
                self.click_relative(62, 44)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "comissaocfta6p8", matching=0.97, waiting_time=10000):
                    self.not_found("comissaocfta6p8")
                self.click_relative(462, 45)
                if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                    self.not_found("cod001cft")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                if not self.find( "obscontratuaisa6p8", matching=0.97, waiting_time=10000):
                    self.not_found("obscontratuaisa6p8")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "commita6p8cft", matching=0.97, waiting_time=10000):
                    self.not_found("commita6p8cft")
                self.click_relative(-571, 53)
                if not self.find( "excluira6p8cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p8cft")
                self.click_relative(-570, 30)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P9---####
                                
                if not self.find( "a6p9cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p9cft")
                self.click()
                if not self.find( "adda6p9", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p9")
                self.click_relative(-627, 8)
                if not self.find( "procuraclientea6p9", matching=0.97, waiting_time=10000):
                    self.not_found("procuraclientea6p9")
                self.click_relative(-442, 41)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                self.wait(1500)
                if not self.find( "cod0081260a6p9", matching=0.97, waiting_time=10000):
                    self.not_found("cod0081260a6p9")
                self.click()
                if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarcft")
                self.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "commita6p9cft", matching=0.97, waiting_time=10000):
                    self.not_found("commita6p9cft")
                self.click_relative(-627, 52)
                if not self.find( "excluira6p9cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p9cft")
                self.click_relative(-627, 32)
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P10---####
                                
                if not self.find( "a6p10cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p10cft")
                self.click()
                if not self.find( "adda6p10cft", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p10cft")
                self.click_relative(-730, 9)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---ABA6 P11---####
                                
                if not self.find( "a6p11rateiocft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p11rateiocft")
                self.click()
                
                if not self.find( "addrateioa6p11cft", matching=0.97, waiting_time=10000):
                    self.not_found("addrateioa6p11cft")
                self.click_relative(-842, 9)            
                if not self.find( "buscacfta6p11", matching=0.97, waiting_time=10000):
                    self.not_found("buscacfta6p11")
                self.click_relative(-646, 44)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'90')
                #if not self.find( "commitcfta6p11", matching=0.97, waiting_time=10000):
                #    self.not_found("commitcfta6p11")
                #self.click_relative(-844, 53)
                if not self.find( "cancelara6p11cft", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara6p11cft")
                self.click_relative(-843, 72)
                
                                ####---ABA6 P12---####
                                
                if not self.find( "a6p12", matching=0.97, waiting_time=10000):
                    self.not_found("a6p12")
                self.click()
                
                if not self.find( "adda6p12cft", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p12cft")
                self.click_relative(-964, 11)
                                    
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                if not self.find( "commita6p12cft", matching=0.97, waiting_time=10000):
                    self.not_found("commita6p12cft")
                self.click_relative(-965, 56)
                
                if not self.find( "excluira6p12cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p12cft")
                self.click_relative(-965, 32)
                
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()

                                ####---ABA6 P13---####
                                
                if not self.find( "a6p12cft", matching=0.97, waiting_time=10000):
                    self.not_found("a6p12cft")
                self.click()
                if not self.find( "adda6p13cft", matching=0.97, waiting_time=10000):
                    self.not_found("adda6p13cft")
                self.click_relative(-1018, 34)            
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                if not self.find( "commita6p13cft", matching=0.97, waiting_time=10000):
                    self.not_found("commita6p13cft")
                self.click_relative(-1016, 101)
                
                if not self.find( "excluira6p13cft", matching=0.97, waiting_time=10000):
                    self.not_found("excluira6p13cft")
                self.click_relative(-1017, 77)
                
                self.enter()
                
                
                                ####---ABA7---####
                                
                if not self.find( "aba7cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba7cft")
                self.click()
                if not self.find( "periodoaba7cft", matching=0.97, waiting_time=10000):
                    self.not_found("periodoaba7cft")
                self.click_relative(220, 27)
                if not self.find( "carregardiaaba7", matching=0.97, waiting_time=10000):
                    self.not_found("carregardiaaba7")
                self.click()
                if not self.find( "carregardiaatualaba7", matching=0.97, waiting_time=10000):
                    self.not_found("carregardiaatualaba7")
                self.click()
                if not self.find( "visualizarmovimentoevetivo1", matching=0.97, waiting_time=10000):
                    self.not_found("visualizarmovimentoevetivo1")
                self.click_relative(89, 35)
                if not self.find( "visualizarmovimentoefetivo2", matching=0.97, waiting_time=10000):
                    self.not_found("visualizarmovimentoefetivo2")
                self.click_relative(170, 31)
                if not self.find( "visualizarmovimentoefetivo3", matching=0.97, waiting_time=10000):
                    self.not_found("visualizarmovimentoefetivo3")
                self.click_relative(8, 33)
                if not self.find( "movagrupadoitensaba7", matching=0.97, waiting_time=10000):
                    self.not_found("movagrupadoitensaba7")
                self.click()
                if not self.find( "consultarmvtfinanceiroaba7", matching=0.97, waiting_time=10000):
                    self.not_found("consultarmvtfinanceiroaba7")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---FINALIZAR CFT---####
                                
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "procurarcft", matching=0.97, waiting_time=10000):
                    self.not_found("procurarcft")
                self.click_relative(20, 32)
                self.type_keys_with_interval(1,'te12')
                self.enter()
                if not self.find( "achoucftteste", matching=0.97, waiting_time=10000):
                    self.not_found("achoucftteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(5000)
                if not self.find( "excluircft1", matching=0.97, waiting_time=10000):
                    self.not_found("excluircft1")
                self.click()
                #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluircft1")
                #self.click()
                self.enter()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                self.enter()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "fecharsistemacft", matching=0.97, waiting_time=10000):
                    self.not_found("fecharsistemacft")
                self.click()
                if not self.find( "fecharsistemacft", matching=0.97, waiting_time=10000):
                    self.not_found("fecharsistemacft")
                self.click()
                if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluircft1")
                self.click()
                #self.enter()

                        #SESSÃO PÁGINA 5(Parte 2 Cadastros 10608 - 14282)
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
                
                                ####---REDES SOCIAIS---#### 
                
                self.wait(1500)
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=100000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                self.wait(1500)
                if not self.find( "redessociais", matching=0.97, waiting_time=10000):
                    self.not_found("redessociais")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                self.wait(1000)            
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                self.wait(3000)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                self.wait(1000)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                
                x=0
                while x<13:
                    if not self.find( "iconers", matching=0.97, waiting_time=10000):
                        self.not_found("iconers")
                    self.click_relative(184, 8)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---AVALIACOES ISO---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "avaliacoesiso", matching=0.97, waiting_time=10000):
                    self.not_found("avaliacoesiso")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()
                if not self.find( "addnovaenquete", matching=0.97, waiting_time=10000):
                    self.not_found("addnovaenquete")
                self.click_relative(8, 33)
                if not self.find( "buscarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("buscarenquete")
                self.click_relative(134, 157)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "selecionarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarenquete")
                self.click()
                if not self.find( "ordemcima", matching=0.97, waiting_time=10000):
                    self.not_found("ordemcima")
                self.double_click_relative(67, 0)
                if not self.find( "ordembaixo", matching=0.97, waiting_time=10000):
                    self.not_found("ordembaixo")
                self.click_relative(69, 11)
                if not self.find( "cancelarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarenquete")
                self.click_relative(-598, 66)
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---LINHAS, RAMOS, ATIVIDADES ETC---####
                                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                    self.not_found("linhasramosetc")
                self.click()
                if not self.find( "linha", matching=0.97, waiting_time=10000):
                    self.not_found("linha")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                
                
                            
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                    self.not_found("linhasramosetc")
                self.click()
                if not self.find( "ramodeatividade", matching=0.97, waiting_time=10000):
                    self.not_found("ramodeatividade")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()            
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
                    self.not_found("localizaramo")
                self.click_relative(17, 26)
                self.type_keys_with_interval(1,'te12')
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                
                
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                    self.not_found("linhasramosetc")
                self.click()
                if not self.find( "rotasdeentrega", matching=0.97, waiting_time=10000):
                    self.not_found("rotasdeentrega")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()            
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
                    self.not_found("localizaramo")
                self.click_relative(17, 26)
                self.type_keys_with_interval(1,'te12')
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                
                
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                    self.not_found("linhasramosetc")
                self.click()
                if not self.find( "segmento", matching=0.97, waiting_time=10000):
                    self.not_found("segmento")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()  
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()                    
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                
                
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                    self.not_found("linhasramosetc")
                self.click()
                if not self.find( "tiposdecontratos", matching=0.97, waiting_time=10000):
                    self.not_found("tiposdecontratos")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                    self.not_found("salvaravaliacao")
                self.click()  
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()                    
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---VENDEDORES, COMPRADORES---####
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "vendedorescompradores", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorescompradores")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(100,'08658033902')
                self.enter()
                self.type_keys_with_interval(100,'147345348')
                if not self.find( "vcrjuridica", matching=0.97, waiting_time=10000):
                    self.not_found("vcrjuridica")
                self.click()
                if not self.find( "vcrfisica", matching=0.97, waiting_time=10000):
                    self.not_found("vcrfisica")
                self.click()
                if not self.find( "vcrinativo", matching=0.97, waiting_time=10000):
                    self.not_found("vcrinativo")
                self.click()
                if not self.find( "vcrativo", matching=0.97, waiting_time=10000):
                    self.not_found("vcrativo")
                self.click()
                if not self.find( "vendedorvcr", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorvcr")
                self.click()
                if not self.find( "vendedorvcr2", matching=0.97, waiting_time=10000):
                    self.not_found("vendedorvcr2")
                self.click()
                if not self.find( "compradorvcr", matching=0.97, waiting_time=10000):
                    self.not_found("compradorvcr")
                self.click_relative(746, -23)
                if not self.find( "compradorvcr", matching=0.97, waiting_time=10000):
                    self.not_found("compradorvcr")
                self.click_relative(746, -23)
                if not self.find( "enderecovcr", matching=0.97, waiting_time=10000):
                    self.not_found("enderecovcr")
                self.click_relative(9, 43)
                self.type_keys_with_interval(100,'85055370')
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'874')
                self.enter()
                self.type_keys_with_interval(1,'casa')
                if not self.find( "municipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("municipiovcr")
                self.click_relative(59, 25)
                self.backspace()
                self.enter()
                self.wait(2000)
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=100000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "telefonevcr", matching=0.97, waiting_time=10000):
                    self.not_found("telefonevcr")
                self.click_relative(553, 90)
                self.type_keys_with_interval(1,'123123123123')
                self.enter()
                self.type_keys_with_interval(1,'123123123123')
                self.enter()
                self.type_keys_with_interval(1,'testeteorema@testeteorema.com.br')
                if not self.find( "botaoemailvcr", matching=0.97, waiting_time=10000):
                    self.not_found("botaoemailvcr")
                self.click_relative(344, 22)
                if not self.find( "fecharaddcontavcr", matching=0.97, waiting_time=10000):
                    self.not_found("fecharaddcontavcr")
                self.click_relative(428, 7)
                if not self.find( "fecharaddemailvcr2", matching=0.97, waiting_time=10000):
                    self.not_found("fecharaddemailvcr2")
                self.click_relative(493, -236)
                
                if not self.find( "familiacomprasvcr", matching=0.97, waiting_time=10000):
                    self.not_found("familiacomprasvcr")
                self.click_relative(63, 42)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "datacadastrovcr", matching=0.97, waiting_time=10000):
                    self.not_found("datacadastrovcr")
                self.click_relative(545, 44)
                if not self.find( "diadatavcr", matching=0.97, waiting_time=10000):
                    self.not_found("diadatavcr")
                self.click_relative(100, 60)
                self.enter()
                
                x=0
                while x<3:
                    if not self.find( "ratioosvcr", matching=0.97, waiting_time=10000):
                        self.not_found("ratioosvcr")
                    self.click_relative(92, 28)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                if not self.find( "bancovcr", matching=0.97, waiting_time=10000):
                    self.not_found("bancovcr")
                self.click_relative(65, 46)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.enter()
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                self.enter()
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "clientevcr", matching=0.97, waiting_time=10000):
                    self.not_found("clientevcr")
                self.click_relative(843, 43)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "nivelcomissaovcr", matching=0.97, waiting_time=10000):
                    self.not_found("nivelcomissaovcr")
                self.click_relative(60, 47)
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
                if not self.find( "fatovcr", matching=0.97, waiting_time=10000):
                    self.not_found("fatovcr")
                self.click_relative(670, 42)
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not self.find( "obsvcr", matching=0.97, waiting_time=10000):
                    self.not_found("obsvcr")
                self.click_relative(14, 42)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarvcr", matching=0.97, waiting_time=10000):
                    self.not_found("salvarvcr")
                self.click()
                if not self.find( "aba2gerenciavsr", matching=0.97, waiting_time=10000):
                    self.not_found("aba2gerenciavsr")
                self.click()
                if not self.find( "addregistroaba2vcr", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2vcr")
                self.click_relative(-50, 35)
                if not self.find( "buscargerenciavcr", matching=0.97, waiting_time=10000):
                    self.not_found("buscargerenciavcr")
                self.click_relative(116, 4)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                
                x=0
                while x<2:
                    if not self.find( "tipovcr", matching=0.97, waiting_time=10000):
                        self.not_found("tipovcr")
                    self.click_relative(127, 6)
                    self.type_down()
                    self.enter()
                    x=x+1
                    
                self.type_keys_with_interval(1,'10')
                self.enter()
                if not self.find( "salvaraba2vcr", matching=0.97, waiting_time=10000):
                    self.not_found("salvaraba2vcr")
                self.click()
                if not self.find( "apagaraba2gerenciavcr", matching=0.97, waiting_time=10000):
                    self.not_found("apagaraba2gerenciavcr")
                self.click_relative(-54, 57)
                self.enter()
                #if not self.find( "confirmaexcluiraba2vcr", matching=0.97, waiting_time=10000):
                #    self.not_found("confirmaexcluiraba2vcr")
                #self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                
                                ####---ENQUETES---####
                
                if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
                self.click()
                if not self.find( "enquetes", matching=0.97, waiting_time=10000):
                    self.not_found("enquetes")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                
                x=0
                while x<5:
                    if not self.find( "tipodeutilizacao1", matching=0.97, waiting_time=10000):
                        self.not_found("tipodeutilizacao1")
                    self.click_relative(276, 51)
                    self.type_down()
                    self.enter()
                    x=x+1
                
                if not self.find( "tiporesposta", matching=0.97, waiting_time=10000):
                    self.not_found("tiporesposta")
                self.click_relative(271, 31)
                self.type_up()
                self.enter()
                
                if not self.find( "buscarempresaenquete", matching=0.97, waiting_time=10000):
                    self.not_found("buscarempresaenquete")
                self.click_relative(53, 32)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "periodoenquete", matching=0.97, waiting_time=10000):
                    self.not_found("periodoenquete")
                self.click_relative(73, 31)
                if not self.find( "diaperiodoenquete1", matching=0.97, waiting_time=10000):
                    self.not_found("diaperiodoenquete1")
                self.click_relative(94, 58)
                if not self.find( "periodoenquete2", matching=0.97, waiting_time=10000):
                    self.not_found("periodoenquete2")
                self.click_relative(180, 30)
                if not self.find( "dataenquete2", matching=0.97, waiting_time=10000):
                    self.not_found("dataenquete2")
                self.click_relative(59, 91)
                if not self.find( "questoesenquete", matching=0.97, waiting_time=10000):
                    self.not_found("questoesenquete")
                self.click_relative(15, 46)
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("salvarenquete")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                    self.not_found("redesocialteste")
                self.click()
                if not bot.find( "fatu_cad_param_fiscal_paises_editar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_paises_editar")
                bot.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()
                if not bot.find( "fatu_cad_param_fiscal_localizar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_fiscal_localizar")
                bot.click()
                if not bot.find( "fatu_cad_param_receituario_retornar", matching=0.97, waiting_time=10000):
                    not_found("fatu_cad_param_receituario_retornar")
                bot.click()

def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  