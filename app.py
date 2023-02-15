# Passos manuais em sequência, depois tornar cada passo em código python.
# Quais são os passos manuais.
# 1. Navegar até a pagina https://www.tiktok.com/?lang=pt-BR
import webbrowser, pyautogui
from time import sleep

webbrowser.open('https://www.tiktok.com/')
sleep(10)
# 2. Clicar em login
pyautogui.click(1807,142,duration=2)
sleep(5)
# 3. Clicar em logar com e-mail
pyautogui.click(1404,430,duration=2)
sleep(3)
# 4. Clicar em logar com e-mail/username
pyautogui.click(1553,366,duration=2)
sleep(5)
# 5. Digitar E-mail/username e senha

# 6. Clicar em login
pyautogui.click(1483,553,duration=2)
sleep(10)
# 7. Navegar até a pagina https://www.tiktok.com/@leozitorocha1?lang=pt-BR
webbrowser.open('https://www.tiktok.com/@leozitorocha1')
sleep(10)
# 8. Clicar na postagem mais recente
pyautogui.click(1293,587,duration=2)
sleep(5)
# 9. Verificar se video já foi curtido
for video in range(15):
    imagem = pyautogui.locateOnScreen('curtida.png')
    if imagem:
        #Se foi curtido, passar para próximo video
        pyautogui.press('down')
        sleep(5)
    else:
        # Se não foi curtido, curtir este video e passar para próxima video
        sleep(5)
        pyautogui.click(1678,344,duration=2)
        sleep(2)
        pyautogui.press('down')
    # 10. Repetir por quantas vezes quizer.
