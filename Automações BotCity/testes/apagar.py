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

        x = 0
        while x < 25:
            self.wait(1000)
            if not self.find( "btn_localizar_teste_apagar_qa12", matching=0.97, waiting_time=10000):
                not_found("btn_localizar_teste_apagar_qa12")
            self.click()
            
            self.wait(1000)
            if not self.find( "btn_clicar_teste_qa_12_apagar", matching=0.97, waiting_time=10000):
                not_found("btn_clicar_teste_qa_12_apagar")
            self.click()
            self.wait(1000)
            if not self.find( "editar_teste_24_apagar_qa12", matching=0.97, waiting_time=10000):
                not_found("editar_teste_24_apagar_qa12")
            self.click()
            self.wait(1000)
            if not self.find( "excluir_btn_teste_apagar_qa12", matching=0.97, waiting_time=10000):
                not_found("excluir_btn_teste_apagar_qa12")
            self.click()
            self.wait(1000)
            self.enter()
            self.wait(1000)
            if not self.find( "btn_retornar_excluir_teste_apagar", matching=0.97, waiting_time=10000):
                not_found("btn_retornar_excluir_teste_apagar")
            self.click()

            x +=1 
        



def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()


