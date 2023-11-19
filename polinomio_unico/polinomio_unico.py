"""Método de Polinomio Único"""
import tkinter as tk
from tkinter import messagebox
import numpy as np
from sympy import Poly, symbols, pretty
import matplotlib.pyplot as plt


class ResultadosVentana:
    """Clase para generar la interfaz que muestra los resultados"""

    def __init__(self, polinomio, puntos):
        self.ventana_resultados = tk.Toplevel()
        self.ventana_resultados.title("Resultados")
        self.ventana_resultados.geometry("800x250")
        self.ventana_resultados["background"] = "#0A6FB1"
        self.label_polinomio = tk.Label(
            self.ventana_resultados,
            text="Polinomio resultante:",
            font=("Arial", 20),
            bg="#FFE001",
        )
        self.label_polinomio.pack(pady=10)
        x = symbols("x", real=True)
        polinomio_sym = Poly(polinomio, x)
        pretty_p = pretty(polinomio_sym.as_expr(), use_unicode=True)
        label_polinomio_texto = tk.Label(
            self.ventana_resultados, text=pretty_p, font=("Arial", 14)
        )
        label_polinomio_texto.pack(pady=20)
        self.realizar_grafico(polinomio, puntos)

    def realizar_grafico(self, polinomio, puntos):
        """Generar gráfica de la función obtenida y los puntos pn(xk,yk)"""
        x_vals = np.linspace(min(puntos[:, 0]) - 1, max(puntos[:, 0]) + 1, 100)
        y_vals = np.polyval(polinomio, x_vals)
        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label="Polinomio obtenido", color="blue")
        plt.scatter(
            puntos[:, 0], puntos[:, 1], label="Puntos introducidos", color="red"
        )
        plt.title("Gráfico del polinomio y puntos introducidos")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.show()


class GUI:
    """Clase para generar la interfaz principal"""

    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("Polinomio Único")
        self.raiz.geometry("650x350")
        self.raiz["background"] = "#B01482"
        self.titulo = tk.Label(
            self.raiz,
            text="Método de Polinomio Único",
            font=("Arial", 18),
            bg="#FFE001",
        )
        self.titulo.pack(pady=10)
        self.autor_label = tk.Label(
            self.raiz, text="^_~ Arland Barrera ;)", font=("Arial", 16), bg="#A8F75F"
        )
        self.autor_label.pack(pady=10)
        self.caja_puntos = tk.Frame(self.raiz)
        self.texto_puntos = tk.Label(
            self.caja_puntos, text="Número de puntos", font=("Arial", 16), bg="#FFA962"
        )
        self.texto_puntos.grid(row=0, column=0)
        self.n_puntos = tk.StringVar()
        self.input_puntos = tk.Entry(
            self.caja_puntos,
            font=("Arial", 16),
            textvariable=self.n_puntos,
            cursor="heart",
            width=5,
            justify="center",
        )
        self.input_puntos.grid(row=0, column=1, padx=5)
        self.generar_puntos = tk.Button(
            self.caja_puntos,
            text="Generar tabla de valores",
            font=("Arial", 16),
            bg="#F70B60",
            command=self.verificar_valor_numerico,
        )
        self.generar_puntos.grid(row=0, column=2)
        self.caja_puntos.pack(pady=10)
        self.caja_valores = tk.Frame(self.raiz)
        self.caja_variables = tk.Frame(self.caja_valores, background="black")
        self.valores_x = tk.Label(
            self.caja_variables, text="X", font=("Arial", 16), bg="#FF660E"
        )
        self.valores_x.grid(row=0, column=0, pady=1, padx=1)
        self.valores_y = tk.Label(
            self.caja_variables, text="Y", font=("Arial", 16), bg="#00DFB2"
        )
        self.valores_y.grid(row=1, column=0, pady=1, padx=1)
        self.caja_variables.grid(row=0, column=0, padx=5)
        self.tabla_valores = tk.Frame(self.caja_valores)
        self.tabla_valores.grid(row=0, column=1)
        self.caja_valores.pack(pady=20)
        self.boton_resolver = tk.Button(
            self.raiz,
            text="Solucionar",
            font=("Arial", 16),
            bg="#47B7E1",
            command=self.obtener_valores,
        )
        self.boton_resolver.pack(pady=20)
        self.valores_entries = []
        self.raiz.mainloop()

    def generar_entries_valores(self, num_puntos):
        """Crear tabla de valores para los puntos pn(xk,yk)"""
        for widget in self.tabla_valores.winfo_children():
            widget.destroy()
        self.valores_entries = []
        for i in range(num_puntos):
            entry_x = tk.Entry(
                self.tabla_valores, font=("Arial", 14), width=5, justify="center"
            )
            entry_x.grid(row=0, column=i, pady=1)
            entry_y = tk.Entry(
                self.tabla_valores, font=("Arial", 14), width=5, justify="center"
            )
            entry_y.grid(row=1, column=i, pady=1)

            self.valores_entries.append((entry_x, entry_y))

    def verificar_valor_numerico(self):
        """Comprobar que la cantidad de puntos sea entera. f(string(n)) = int(n)"""
        string = self.n_puntos.get()
        try:
            num_puntos = int(float(string))
            self.generar_entries_valores(num_puntos)
        except ValueError:
            messagebox.showinfo(
                title="Error de Entrada", message="El dato introducido no es numérico"
            )

    def obtener_valores(self):
        """Determinar la matriz de los resultados. a0, a1x^1, a2x^2, ..., anx^n"""
        valores = []
        for entry_x, entry_y in self.valores_entries:
            valor_x = entry_x.get()
            valor_y = entry_y.get()
            try:
                valor_x = float(valor_x)
                valor_y = float(valor_y)
                valores.append((valor_x, valor_y))
            except ValueError:
                messagebox.showinfo(
                    title="Error de Entrada",
                    message="Los valores deben ser numéricos",
                )
        num_puntos = len(valores)
        matriz_x = []
        for i in range(num_puntos):
            fila = [1]
            fila.append(valores[i][0])
            for potencia in range(2, num_puntos):
                fila.append(valores[i][0] ** potencia)
            matriz_x.append(fila)
        matriz_y = np.array([[valores[i][1]] for i in range(num_puntos)])
        try:
            _ = np.linalg.det(matriz_x)
        except np.linalg.LinAlgError:
            messagebox.showinfo(
                title="Error de Determinante",
                message="La matriz de coeficientes x es singular",
            )
        try:
            matriz_inversa_x = np.linalg.inv(matriz_x)
        except np.linalg.LinAlgError:
            messagebox.showinfo(
                title="Error de Matriz Inversa",
                message="La matriz de coeficientes x es singular",
            )
        try:
            producto = np.dot(matriz_inversa_x, matriz_y)
            producto = np.round(producto, 6)
            for i in range(num_puntos):
                if producto[i] == int(producto[i]):
                    producto[i] = int(producto[i])
            self.mostrar_resultados(producto)
        except ValueError as e:
            print(f"Error al multiplicar matrices: {e}")
            messagebox.showinfo(
                title="Error de Cálculo", message="Error al multiplicar matrices"
            )

    def mostrar_resultados(self, producto):
        """Formatear y enviar los resultados a la ventana de resultados"""
        producto = np.asarray(producto).flatten()
        polinomio = np.poly1d(producto[::-1])
        valores = np.array(
            [
                (float(entry_x.get()), float(entry_y.get()))
                for entry_x, entry_y in self.valores_entries
            ]
        )
        ResultadosVentana(polinomio, valores)


GUI()
