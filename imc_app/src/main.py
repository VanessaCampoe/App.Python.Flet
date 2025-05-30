import flet as ft


def main(page:ft.Page):
    def calcular_imc(e):
        if not peso.value:
            peso.error_text = " Peso não pode ficar vazio"
            page.update()
        else:
            peso.error_text = ""
            page.update()
        if not altura.value:
            altura.error_text = " "
            page.update()
        else:
            altura.error_text = ""
            
            peso.value = float(peso.value.replace(",", "."))
            altura.value = float(altura.value.replace(",", "."))
            
            if peso.value > 0 and altura.value > 0:
                imc = peso.value / altura.value **2
                peso.value = ""
                altura.value = "" 
                result.value = f"O valor do IMC é: {imc:.2f}"


                
                if imc < 18.5:
                    diagnostico.value = "Abaixo do peso"
                    diagnostico.color= ft.colors.Black
                elif imc < 25 :
                    diagnostico.value = "Peso normal"
                    diagnostico.color = ft.colors.GREEN
                elif imc < 30:
                    diagnostico.value = "Sobrepeso"
                    diagnostico.color= ft.colors.Blue
                elif imc < 35:
                    diagnostico.value = "Obesidade I"
                    diagnostico.color = ft.colors.orange
                elif imc < 40:
                    diagnostico.value = "Obesidade II"
                    diagnostico.color = ft.colors.rose
                else:
                    diagnostico.value = "Obesidade III"
                    diagnostico.color = ft.colors.RED
                diagnostico.update()
                page.update()
            elif peso.value < 0 and altura.value > 0:
                peso.error_text = " Valor invalido"
                page.update()
            elif peso.value > 0 and altura.value < 0:
                altura.error_text = " Valor invalido"
                page.update()
            else:
                peso.error_text = " Valor invalido"
                altura.error_text = " Valor invalido"
                page.update()

    page.title = "Imc - Indice de Massa Corporal"
    page.scroll = "Adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.title = "Imc - Indice de Massa Corporal"
    page.scroll = "Adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    peso =  ft.TextField(label="Peso ", suffix_text="kg",on_submit=calcular_imc)  # aqui a solução com enter para calcular o imc
                         
                         
    altura = ft.TextField(label="Altura", 
                          suffix_text="M" , on_submit=calcular_imc)  # aqui a solução com enter para calcular o imc 
    
    
    result = ft.Text(size=20, weight="bold")
    diagnostico = ft.Text() 
    
       
    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text("\n Índice de massa coporal",size=30, weight="bold"
                         )],
                
            )
        ),
    
    peso, altura,
    ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
    result 
        
    )

ft.app(main)
  