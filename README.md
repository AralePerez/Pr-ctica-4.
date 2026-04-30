# Practica-4.
Extensiones agregadas al simulador

1. Soporte mejorado para AFND y AFN-λ
- Simulación general para AFND y AFN-λ.
- Manejo de múltiples estados activos.
- Manejo de ramificaciones por símbolo.
- Aplicación de λ-clausura durante la simulación.
- Visualización textual paso a paso del conjunto activo de estados.

2. Conversión entre autómatas
- AFND / AFN-λ -> AFD con algoritmo de subconjuntos.
- AFN-λ -> AFND eliminando transiciones lambda.
- Registro textual del proceso de conversión.

3. Minimización de AFD
- Eliminación de estados inaccesibles.
- Detección de pares distinguibles.
- Fusión de estados equivalentes.
- Construcción del AFD mínimo.
- Comparación con 5 cadenas representativas.

4. Interfaz gráfica ampliada
- Selector de tipo: dfa, nfa, nfae.
- Tabla de transición con columna λ para AFN-λ.
- Botón para mostrar λ-clausura de un estado.
- Pestaña de Conversión / Minimización.
- Pestaña de Pruebas múltiples con carga de TXT.

5. Pruebas múltiples
- Carga de archivo TXT con cadenas.
- Validación de todas las cadenas.
- Reporte textual exportable.

Nota:
La visualización gráfica fue mejorada para resaltar estados activos y dibujar las transiciones lambda con estilo diferenciado.

MODIFICACIONES NUEVAS: EJERCICIO 2 Y EJERCICIO 3


EJERCICIO 2: Conversión de AFD a Expresión Regular

Se agregó la opción AFD → ER al software.

Funcionalidades incluidas:
- Conversión de un AFD a una expresión regular equivalente.
- Algoritmo implementado: eliminación de estados.
- Visualización del AFD original en la interfaz.
- Proceso paso a paso con botón "Siguiente eliminación".
- Muestra las conexiones nuevas que se generan al eliminar cada estado.
- Al finalizar, muestra claramente la expresión regular resultante.

Cómo usarlo:
1. Abre el programa.
2. Crea un AFD manualmente o carga un archivo.
3. Si el AFD está incompleto, presiona "Completar AFD".
4. Presiona "AFD → ER" o entra a la pestaña "Conversión / Minimización".
5. Presiona "Preparar AFD → ER".
6. Presiona "Siguiente eliminación" para ver el proceso paso por paso.
7. Al finalizar aparecerá la ER resultante.

Importación desde JFLAP:
- Se agregó el botón "Importar .jff AFD".
- Permite importar archivos .jff creados en JFLAP.
- Verifica que el archivo importado sea un AFD válido.
- Si tiene transiciones lambda, múltiples destinos, o le faltan transiciones, muestra un error.
- Si es válido, el AFD se visualiza en la interfaz y puede convertirse a ER.

Carga y guardado:
- El software conserva la carga de archivos .jff, .json y .xml.
- El formato propio puede usarse con .json o .xml.
- También se puede guardar en .jff para abrirlo en JFLAP.

EJERCICIO 3: Validadores con Expresiones Regulares

Se agregó una pestaña llamada "Validadores ER".

Casos de uso implementados:
1. Validador de correo electrónico.
2. Validador de teléfono nacional de México.
3. Validador de URL.
4. Validador de fechas.
5. Validador de contraseña segura.

Para cada caso se incluye:
- La expresión regular utilizada.
- Entrada de texto para validar.
- Resultado claro: VÁLIDO o NO VÁLIDO.
- Sugerencias de corrección cuando el texto no cumple el patrón.
- Visualización de un AFD equivalente simplificado para entender el patrón.

Cómo usar los validadores:
1. Ve a la pestaña "Validadores ER".
2. Selecciona el caso de uso.
3. Escribe el texto a validar.
4. Presiona "Validar".
5. Presiona "Ver AFD equivalente" si quieres visualizar el autómata del patrón.

Comando para ejecutar el programa:
------------------------------------------------------------
Desde la carpeta del proyecto:

cd afd_simulator_project
python src/main.py

Codigo fuente del programa se ecnucentra en el siguiente drive listo para ejecutar:
https://drive.google.com/file/d/1tHDN9sEbnY0BygSqTHaFvOpzPaJtrTPo/view?usp=sharing

<img width="1600" height="825" alt="image" src="https://github.com/user-attachments/assets/24fccd84-32ba-49d3-92f6-257cef76a3e6" />



Si usas Visual Studio Code:
1. Abre la carpeta afd_simulator_project.
2. Abre una terminal nueva.
3. Ejecuta:
   python src/main.py

Documentacion 
Todas las listas, investigaciones nuevas y pasadas se encuentran aqui, respecto a la practica 4 se encuentra en el siguiente overlife: 
https://www.overleaf.com/project/69f17b6ee438f16b9ad5150b
