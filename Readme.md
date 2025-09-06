# 🔥 ChatBot n8n workflow.

<!-- Badges -->
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Downloads](https://img.shields.io/badge/downloads-100%2B-blue.svg)](#)
![Project Status](https://img.shields.io/badge/status-beta-yellow)
![Language](https://img.shields.io/github/languages/top/potlitel/n8n_chatbot)
![Last Commit](https://img.shields.io/github/last-commit/potlitel/n8n_chatbot)
![GPT-4.1-mini](https://img.shields.io/badge/Model-GPT--4.1--mini-blue)

<!-- ![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-blue) -->
<!-- ![Build Status](https://img.shields.io/github/actions/workflow/status/usuario/repositorio/ci.yml?branch=main) -->



## ✍️ Descripción

Este es un proyecto de chatbot diseñado para actuar como un experto en el béisbol cubano. Utiliza la lógica de un agente de IA para responder preguntas de los usuarios de forma interactiva y con un conocimiento contextualizado, basándose en una base de datos específica sobre el tema.
Además muestra utilizar la API de n8n con python scripts. n8n tiene una API que permite a los desarrolladores interactuar con el sistema de automatización de procesos. Permite realizar diversas operaciones, como crear, actualizar y eliminar flujos de trabajo (workflows), así como gestionar credenciales y ejecutar flujos de trabajo de manera programática.

## ✨Características Principales 

- **Experto en Béisbol Cubano 🧠:** El chatbot está entrenado con datos sobre ligas, equipos, jugadores, estadios y eventos históricos del béisbol en Cuba.
- **Conversacional 💬:** Utiliza un modelo de lenguaje de IA para mantener conversaciones fluidas y coherentes.
- **Memoria de Búfer 📜:** Mantiene el contexto de la conversación para ofrecer respuestas más precisas y relevantes.
- **Fácil de Expandir 📈:** La base de conocimientos es un archivo de texto (`baseball_prompt.md`) que puede ser fácilmente modificado y expandido con más información.

## ⚙️Tecnologías Utilizadas 

- **n8n 🤖:** Plataforma de automatización que gestiona el flujo del chatbot, desde la recepción del mensaje hasta el envío de la respuesta.
- **Agente de IA 🧠:** Implementado en n8n para procesar el lenguaje natural.
- **Modelo de Chat de IA 🗨️:** Un modelo de lenguaje (como OpenAI GPT, Llama, etc.) que actúa como el cerebro del chatbot.
- **Windows Buffer Memory (n8n-nodes-langchain.memorybufferwindow)📝:** Componente de n8n que mantiene un historial de la conversación para que el agente de IA tenga memoria de los diálogos previos.

## 📝 Requisitos Previos

- Asegúrate de tener n8n en funcionamiento y accesible. Puedes utilizar como referencia la siguiente [guía](https://github.com/potlitel/n8n_ELK). 
- Crear una Cuenta de Usuario
  - #### Completar el formulario de configuración inicial:
      ##### 1. Nombre de usuario (administrador)
      ##### 2. Contraseña segura (mínimo 8 caracteres, incluyendo al menos un número y una letra mayúscula)
      ##### 3. Correo electrónico válido para recuperación
- Necesitarás un token de la API de n8n para autenticarte. (**Necesario solo si creas el workflow usando el script createChatboty**)
  - #### Crear una clave API

    ##### 1. Inicia sesión en n8n.
    ##### 2. Ve a **Configuración > API de n8n**.
    ##### 3. Selecciona **Crear una clave API**.
    ##### 4. Elige una **Etiqueta** y establece un **Tiempo de expiración** para la clave.
    ##### 5. Si estás en un plan empresarial, elige los **Ámbitos** para otorgar a la clave.
    ##### 6. Copia **Mi clave API** y utiliza esta clave para autenticar tus llamadas.


## 📝 Requisitos de Software

### 1. Python
- **Versión**: Python 3.7 o superior

#### Instalación de Python en Windows

##### 1. Descargar el instalador de Python

Visita el sitio web oficial de Python: python.org.
Descarga la última versión de Python 3.x para Windows (asegúrate de elegir entre la versión de 32 bits o 64 bits según tu sistema).

##### 2. Ejecutar el instalador

Abre el archivo descargado (por ejemplo, python-3.x.x-amd64.exe).
Asegúrate de marcar la opción "Add Python to PATH" antes de hacer clic en "Install Now".

##### 3. Personalizar la instalación (opcional)

Si deseas personalizar la instalación, selecciona "Customize installation" y elige las características que deseas incluir, como pip, documentación, etc.

##### 4. Verificar la instalación

Abre el símbolo del sistema (cmd) y ejecuta el siguiente comando para verificar que Python se haya instalado correctamente:

  ```bash
  python --version
  ```

#### Instalación de Python en linux

##### 1: Usar el gestor de paquetes

Abre la terminal y ejecuta el siguiente comando según tu distribución:

  * Ubuntu/Debian:

      ```bash
      sudo apt-get install python3
      ```

  * Fedora:

      ```bash
      sudo dnf install python3
      ```

##### 2: Verificar la instalación

Ejecuta el siguiente comando en la terminal:

   ```bash
  python3 --version
  ```

#### Instalación de Python en Mac

##### 1. Descargar el instalador de Python

Ve a python.org y descarga la versión más reciente de Python para macOS.

##### 2. Ejecutar el instalador

Localiza el archivo descargado en tu carpeta de Descargas y haz doble clic en él para iniciar la instalación.
Sigue las instrucciones en pantalla para completar la instalación.

##### 3. Verificar la instalación

Abre la Terminal y ejecuta:

  ```bash
  python3 --version
  ```

#### Instalación de pip 

##### 1. Verificar si pip está instalado

Después de instalar Python, pip generalmente se instala automáticamente. Verifica su instalación ejecutando:

  ```bash
  pip --version
  ```

##### 2. Instalar pip (si no está instalado)

Si pip no está instalado, puedes instalarlo usando el script get-pip.py. Sigue estos pasos:

###### 1. Descarga el script

  ```bash
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  ```

###### 2. Ejecuta el script

  ```bash
  python get-pip.py
  ```

## 🛠️ Para instalar el proyecto, sigue estos pasos:

1. Clona el repositorio:
   
   ```bash
   git clone https://github.com/potlitel/???.git
   ```

2. Navega al directorio del proyecto:
   
   ```bash
   cd tu_repositorio
   ```

3. Crear un Entorno Virtual (**opcional pero recomendado**): Esto ayuda a manejar las dependencias sin afectar tu instalación global de Python.

   ```bash
   python -m venv venv
   ```

4. Activar el Entorno Virtual:

    * En Windows:

        ```bash
        venv\Scripts\activate
        ```

    * En Linux/Mac

        ```bash
        source venv/bin/activate
        ```
5. Instalar las Dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 📥 Uso del proyecto

### 3. Levantar servicios con Docker Compose

Para iniciar los servicios de **n8n** y **PostgreSQL** como soporte de base de datos, es necesario ejecutar el fichero `docker-compose.yml`. 

Esto se hace con el siguiente comando:

```bash
    docker-compose up -d
```

Este comando levantará los contenedores configurados en el archivo, asegurando que ambos servicios estén operativos y correctamente conectados.

### 4. Asegúrate de tener listos todos los [requisitos previos](#requisitos-previos) antes de continuar.

### 5. Ejecución del script **createChatbot.py** (automatiza la creación del flujo)

1. Desde una terminal, diríjase hacia la ubicación del proyecto.

2. Especifique el valor del API key creado previamente en la variable **N8N_API_KEY**

3. Use el siguiente comando para ejecutar el fichero createChatbot.py

    ```bash
    python createChatbot.py
    ```

4. Configurar las credenciales para tu clave de API de OpenAI o el modelo de lenguaje de tu elección. 🔑

#### Estructura para el Prompt del Agente de IA de Béisbol  

```bash
  **Instrucción de Sistema:**  
Actúa como un chatbot experto en béisbol cubano. Tu propósito es responder preguntas de los usuarios de forma concisa y amigable, utilizando únicamente la base de datos de conocimiento que se te proporciona a continuación. Si la información solicitada no está en tu base de datos, debes indicarlo claramente y ofrecer tu ayuda con otra pregunta.

**Base de Datos de Conocimiento:**

**Ligas:**

- **Serie Nacional de Béisbol:** Principal liga de Cuba fundada en 1961 tras la reestructuración del deporte.

**Equipos Emblemáticos:**

- **Industriales (La Habana):**  
  - **Estadio:** Estadio Latinoamericano, La Habana.  
  - **Fundación:** 1962.  
  - **Títulos:** 12 campeonatos de la Serie Nacional.  
  - **Jugadores Clave:** Antonio Muñoz, Javier Méndez, Frederich Cepeda.

- **Santiago de Cuba (Santiago de Cuba):**  
  - **Estadio:** Estadio Guillermón Moncada, Santiago de Cuba.  
  - **Fundación:** 1962.  
  - **Títulos:** 8 campeonatos de la Serie Nacional.  
  - **Jugadores Clave:** Orestes Kindelán, Antonio Pacheco, Norge Luis Vera.

- **Pinar del Río (Pinar del Río):**  
  - **Estadio:** Estadio Capitán San Luis, Pinar del Río.  
  - **Fundación:** 1962.  
  - **Títulos:** 10 campeonatos de la Serie Nacional.  
  - **Jugadores Clave:** Omar Linares, Pedro Luis Lazo, Yovani Gallardo.

**Grandes Figuras (1960-Actualidad):**

- **Omar Linares:**  
  - **Posición:** Tercera Base.  
  - **Apodo:** El Niño.  
  - **Estadísticas:** Bateador de alto promedio, con gran capacidad de embasarse. Considerado uno de los mejores de todos los tiempos.

- **Orestes Kindelán:**  
  - **Posición:** Bateador Designado, Primera Base.  
  - **Apodo:** El Tambor Mayor.  
  - **Estadísticas:** Líder histórico en jonrones y carreras impulsadas en las Series Nacionales de Cuba.

- **Pedro Luis Lazo:**  
  - **Posición:** Lanzador.  
  - **Apodo:** El Rascacielos.  
  - **Logros:** Récord de victorias y ponches en la Serie Nacional. Conquistó la medalla de oro en dos Juegos Olímpicos.

- **Antonio Pacheco:**  
  - **Posición:** Segunda Base.  
  - **Apodo:** El Capitán de la Armada.  
  - **Logros:** Excelente a la defensiva y líder de su equipo en múltiples campeonatos.

- **Frederich Cepeda:**  
  - **Posición:** Jardinero y Bateador Designado.  
  - **Apodo:** El Cepeda.  
  - **Logros:** Miembro del equipo Cuba en eventos internacionales por más de dos décadas, conocido por su versatilidad y consistencia.

- **Yuli Gurriel:**  
  - **Posición:** Primera Base, Tercera Base.  
  - **Logros:** Medalla de oro en los Juegos Olímpicos de 2004. Ganador de la Serie Mundial con los Houston Astros.

- **Adolis García:**  
  - **Posición:** Jardinero.  
  - **Logros:** Jugador de la MLB con los Texas Rangers, MVP de la Serie de Campeonato de la Liga Americana de 2023.

- **Yasmany Tomás:**  
  - **Posición:** Jardinero.  
  - **Logros:** Jugó en la MLB y ha sido un bateador poderoso en la Serie Nacional.

- **Alfredo Despaigne:**  
  - **Posición:** Bateador Designado, Jardinero.  
  - **Logros:** Líder en jonrones en Series Nacionales y conocido por su paso por la liga de Japón.

- **Norge Luis Vera:**  
  - **Posición:** Lanzador.  
  - **Logros:** Uno de los lanzadores más dominantes de la década de 2000 en Cuba.

- **Kendrys Morales:**  
  - **Posición:** Primera Base, Bateador Designado.  
  - **Logros:** Bateador de poder que ha jugado en múltiples equipos de la MLB.

- **Ariel Pestano:**  
  - **Posición:** Receptor.  
  - **Logros:** Considerado uno de los mejores receptores defensivos en la historia de Cuba.

**Árbitros Notables:**

- **Jorge Luis Hernández:** Conocido por su larga trayectoria y profesionalismo en la Serie Nacional.
- **Luis César Valdés:** Uno de los árbitros más respetados y de mayor experiencia en el béisbol cubano.

**Eventos Internacionales:**

- **Juegos Olímpicos:** Cuba ha ganado 3 medallas de oro y 2 de plata en béisbol.
- **Clásico Mundial de Béisbol:** Cuba fue finalista en la edición de 2023.
- **Copas del Mundo:** Históricamente, Cuba fue la fuerza dominante en este evento.
```

### 6. Creación manual del workflow, usando la UI de n8n

Para poner en funcionamiento este chatbot, necesitarás:

1. Crear un flujo en n8n. ✅  
2. Configurar las credenciales para tu clave de API de OpenAI o el modelo de lenguaje de tu elección. 🔑  
3. Configurar un Workflow Trigger para recibir los mensajes del usuario (por ejemplo, un Webhook). 🌐  
4. Añadir un nodo de AI Agent y vincularlo con tu modelo de chat de IA preferido. 🤖  
5. Cargar el siguiente contenido en la configuración del agente de IA para que sirva como su base de conocimiento. 📝  

O simplemente, 

1. Crear un flujo en n8n. ✅  
2. Importar el fichero openAI.json.

Una vez finalizada la creación del workflow, usando cualquiera de las variantes antes mencionado, puedes verificar desde la UI de n8n, y debes tener un workflow similar a la siguiente imagen:

<!-- ![ChatBot-Workflow](images/2025-09-06%2017%2004%2034.png) -->
<div align="center">
  <img src="images/2025-09-06%2017%2004%2034.png" alt="ChatBot-Workflow" width="600" />
</div>


> [!Important]
> Este proyecto está diseñado para ser una **plantilla flexible**. Puedes modificar la base de datos de conocimiento y el flujo para **adaptarlo a cualquier otro tema**.


## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas ayudar a mejorar este proyecto, puedes hacerlo siguiendo estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu feature o corrección: `git checkout -b nombre-de-tu-rama`
3. Realiza tus cambios y realiza commits claros y descriptivos.
4. Envía un pull request describiendo detalladamente tus modificaciones.

Por favor, asegúrate de que tu código sigue las buenas prácticas, y si haces mejoras significativas, considera incluir pruebas o documentación adicional.

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 🙏 Agradecimiento y contacto

¡Gracias por visitar y usar este proyecto! ✨  
Si tienes dudas, sugerencias o quieres contribuir, no dudes en abrir un issue 📥 o contactarme directamente:  

- GitHub: [potlitel](https://github.com/potlitel) 👨‍💻  
- Email: potlitel@gmail.com ✉️  

¡Espero tus aportes y comentarios! 💬😊