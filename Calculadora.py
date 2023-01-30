import tkinter
from tkinter import messagebox


class Calculadora(tkinter.Tk):
  def __init__(self):
    super().__init__()
    self.geometry('310x340')
    self.resizable(0,0)
    self.title('Calculadora')
    
    # Atributos de clase
    self.expresion = ''
    self.entrada = None
    self.entrada_texto = tkinter.StringVar()
    self._creacion_componentes()

    # Primer Frame
  def _creacion_componentes(self):
    entrada_frame = tkinter.Frame(self, width=400, height=50, bg='grey')
    entrada_frame.pack(side=tkinter.TOP)
    
    # Caja de texto
    entrada = tkinter.Entry(entrada_frame, font=('arial', 18, 'bold'),
                            textvariable=self.entrada_texto, width=22, justify=tkinter.RIGHT)
    entrada.grid(row=0, column=0, ipady=10)

    # Segundo Frame
    botones_frame = tkinter.Frame(self, width=310, height=340, bg='grey')
    botones_frame.pack()

    # Boton Limpiar
    boton_limpiar = tkinter.Button(botones_frame, text='C', width='32', height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
    boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    # Boton Dividir
    boton_dividir = tkinter.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                    command=lambda: self._evento_click('/'))
    boton_dividir.grid(row=0, column=3, padx=1, pady=1)

    # Boton 7
    boton_7 = tkinter.Button(botones_frame, text='7', width=10, height=3, bd=0, bg='#fff',
                              cursor='hand2', command=lambda: self._evento_click(7))
    boton_7.grid(row=1, column=0, padx=1, pady=1)

    # Boton 8
    boton_8 = tkinter.Button(botones_frame, text='8', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click(8))
    boton_8.grid(row=1, column=1, padx=1, pady=1)

    # Boton 9
    boton_9 = tkinter.Button(botones_frame, text='9', width=10, height=3, bd=0, bg='#fff',
                              cursor='hand2', command=lambda: self._evento_click(9))
    boton_9.grid(row=1, column=2)

    # Boton Multiplicar
    boton_x=tkinter.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#eee',
                          cursor='hand2', command=lambda: self._evento_click('*'))
    boton_x.grid(row=1, column=3, padx=1, pady=1)

    # Boton 4
    boton_4 = tkinter.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click(4))
    boton_4.grid(row=2, column=0, padx=1, pady=1)

    # Boton 5
    boton_5 = tkinter.Button(botones_frame, text='5', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click(5))
    boton_5.grid(row=2, column=1, padx=1, pady=1)

    # Boton 6
    boton_6 = tkinter.Button(botones_frame, text='6', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click(6))
    boton_6.grid(row=2, column=2, padx=1, pady=1)

    # Boton Restar
    boton_restar = tkinter.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee',
                            cursor='hand2', command=lambda: self._evento_click('-'))
    boton_restar.grid(row=2, column=3, padx=1, pady=1)

    # Boton 1
    boton_1 = tkinter.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click('1'))
    boton_1.grid(row=3, column=0, padx=1, pady=1)

    # Boton 2
    boton_2 = tkinter.Button(botones_frame, text='2', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click('2'))
    boton_2.grid(row=3, column=1, padx=1, pady=1)

    # Boton 3
    boton_3 = tkinter.Button(botones_frame, text='3', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click('3'))
    boton_3.grid(row=3, column=2, padx=1, pady=1)

    # Boton Suma
    boton_suma = tkinter.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee',
                            cursor='hand2', command=lambda: self._evento_click('+'))
    boton_suma.grid(row=3, column=3, padx=1, pady=1)

    # Boton 0
    boton_0 = tkinter.Button(botones_frame, text='0', width=21, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click(0))
    boton_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    # Boton Punto
    boton_punto = tkinter.Button(botones_frame, text='.', width=10, height=3, bd=0, bg='#fff',
                            cursor='hand2', command=lambda: self._evento_click('.'))
    boton_punto.grid(row=4, column=2, padx=1, pady=1)

    # Boton Resultado
    boton_resultado = tkinter.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee',
                            cursor='hand2', command=self._evento_resultado)
    boton_resultado.grid(row=4, column=3, padx=1, pady=1)

    


  # Funciones
  def _evento_limpiar(self):
    self.expresion=''
    self.entrada_texto.set(self.expresion)

  def _evento_click(self, elemento):
    self.expresion = f'{self.expresion}{elemento}'
    self.entrada_texto.set(self.expresion)

  def _evento_resultado(self):
    try:
      resultado = str(eval(self.expresion))
      self.entrada_texto.set(resultado)
    except Exception as e:
      messagebox.showerror('Error', f'Ocurrio un Error: {e}')
      self.entrada_texto.set('')
    finally:
      self.expresion = ''

if __name__ == '__main__':
  calculadora = Calculadora()
  calculadora.mainloop()  


