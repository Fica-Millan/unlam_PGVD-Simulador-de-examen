import streamlit as st
import random
import time

# ------------------------------------------------------------
# Banco de preguntas (6 clases – 120 preguntas)
# ------------------------------------------------------------

questions = {
    "Clase 01 – Introducción a Big Data": [
        ("¿Cuál es una razón clave del surgimiento del Big Data?",
        ["Eliminación de redes sociales","Decrecimiento del e-commerce","Reducción de costos en almacenamiento y cómputo","Falta de datos disponibles"], 2),
        
        ("¿Cuál de las siguientes NO es una V del Big Data?",
        ["Velocidad","Validación","Variedad","Volumen"], 1),
        
        ("El tipo de dato que representa el 80% del total es:",
        ["Datos estructurados","Datos semiestructurados","Datos no estructurados","Datos relacionales"], 2),
        
        ("¿Qué tipo de problema requiere baja latencia?",
        ["Batch","Offline","Online / tiempo real","Archivo histórico"], 2),
        
        ("¿Qué tecnología permite conectar varias computadoras para escalar tareas?",
        ["HDFS","Computación distribuida","Blockchain","FTP"], 1),
        
        ("¿Qué tipo de base de datos incluye MongoDB y HBase?",
        ["Relacionales","Columnar-relacional","NoSQL","SQL tradicionales"], 2),
        
        ("¿Cuál es un caso de uso típico del Big Data?",
        ["Ordenar carpetas en un disco local","Análisis de redes sociales","Creación de documentos PDF","Instalación de sistemas operativos"], 1),
        
        ("¿Qué describe mejor el valor en Big Data?",
        ["Cantidad de datos procesados","Utilidad obtenida de los datos","Número de servidores","Tamaño de la red"], 1),
        
        ("La computación en la nube aporta principalmente:",
        ["Mayor complejidad","Escalabilidad elástica","Menor latencia garantizada","Eliminación de bases de datos"], 1),
        
        ("Los datos semiestructurados…",
        ["Tienen esquema fijo","No poseen ningún tipo de estructura","Poseen estructura parcial","Solo existen en RDBMS"], 2),
        
        ("'Escriba una vez, lea muchas veces' se refiere a:",
        ["RDBMS","Redes TCP","Big Data","HDFS"], 3),
        
        ("¿Cuál es un ejemplo de dato no estructurado?",
        ["Fecha","Número entero","Imagen","ID de usuario"], 2),
        
        ("¿Qué V se relaciona con sensores en tiempo real?",
        ["Volumen","Valor","Variedad","Velocidad"], 3),
        
        ("El contenido multimedia pertenece a:",
        ["Datos estructurados","Datos no estructurados","Datos tabulares","Datos binarios únicamente"], 1),
        
        ("Batch se usa principalmente para:",
        ["Detección de fraude en milisegundos","Procesar datos históricos masivos","Juegos en línea","Procesos embebidos"], 1),
        
        ("La pila tecnológica de Big Data comienza por:",
        ["Capa de seguridad","Infraestructura física redundante","Capa de análisis","Interfaces de usuario"], 1),
        
        ("En las capas de la pila, la capa 3 incluye:",
        ["SQL","Integraciones móviles","MapReduce y Hadoop","GPUs"], 2),
        
        ("Las bases de datos operativas se encuentran en:",
        ["Capa 0","Capa 1","Capa 2","Capa 4"], 2),
        
        ("¿Qué requiere la integración para que Big Data sea posible?",
        ["Interfaces entre capas","Instalación de drivers","Computadoras de alta gama","Conexión 5G"], 0),
        
        ("Big Data NO es…",
        ["Una sola tecnología","Una combinación de tecnologías","Utilizado para extraer valor","El resultado de la convergencia tecnológica"], 0),
    ],


    "Clase 02 – Hadoop, HDFS, MapReduce": [
        ("¿Quién desarrolló originalmente Hadoop?",
        ["IBM", "Microsoft", "Yahoo!", "Google"], 2),

        ("Hadoop está diseñado para:",
        ["Procesamiento online", "Procesamiento batch", "Lectura aleatoria rápida", "Bases SQL tradicionales"], 1),

        ("¿Qué componente gestiona recursos en Hadoop?",
        ["Hive", "YARN", "HBase", "Sqoop"], 1),

        ("¿Qué tamaño de bloque tiene HDFS por defecto?",
        ["1 MB", "16 MB", "64 MB", "1 GB"], 2),

        ("En HDFS, ¿dónde se almacenan los metadatos?",
        ["DataNode", "NameNode", "Sqoop", "Hive"], 1),

        ("¿Qué componente permite acceso aleatorio en tiempo real?",
        ["HDFS", "MapReduce", "HBase", "Pig"], 2),

        ("MapReduce utiliza como entrada:",
        ["Datos JSON", "Pares clave-valor", "Imágenes", "SQL"], 1),

        ("¿Qué fase de MapReduce ordena la salida intermedia?",
        ["Map", "Reduce", "Sort", "Combine"], 2),

        ("¿Qué fase mueve los datos intermedios a los reducers?",
        ["Map", "Shuffle", "Sort", "Almacenamiento"], 1),

        ("¿Qué proyecto permite scripts simples para Hadoop?",
        ["Hive", "Pig", "Zookeeper", "Flume"], 1),

        ("¿Cuál es una ventaja de MapReduce?",
        ["No es escalable", "No tolera fallos", "Oculta la complejidad del cluster", "Permite lectura aleatoria"], 2),

        ("En MapReduce, la función map es:",
        ["Mutable", "No conmutativa", "Inmutable y conmutativa", "No paralelizable"], 2),

        ("La replicación típica en HDFS es:",
        ["1", "2", "3", "10"], 2),

        ("¿Qué componente coordina sincronización en sistemas distribuidos?",
        ["HDFS", "Pig", "Zookeeper", "Sqoop"], 2),

        ("Hadoop funciona mejor sobre:",
        ["Hardware caro", "Hardware commodity", "Procesadores GPU", "Mainframes"], 1),

        ("Hive utiliza un lenguaje similar a SQL llamado:",
        ["MySQL", "SparkSQL", "HiveQL", "PigLatin"], 2),

        ("Sqoop sirve para:",
        ["Streaming", "Importar/exportar datos entre SQL y Hadoop", "Crear clusters", "Procesar logs"], 1),

        ("La filosofía 'mover el código al dato' pertenece a:",
        ["SQL", "HDFS", "Hadoop", "Kafka"], 2),

        ("MapReduce fue creado por:",
        ["Google", "Facebook", "Microsoft", "Netflix"], 0),

        ("¿Qué componente envía heartbeats al NameNode?",
        ["Hive", "DataNode", "Zookeeper", "Client"], 1)
    ],


    "Clase 03 – Spark, RDD, DataFrames, SQL": [
        ("Spark fue creado en:",
        ["Yahoo!", "MIT", "UC Berkeley", "IBM"], 2),

        ("Spark es aproximadamente _____ veces más rápido que Hadoop MapReduce.",
        ["2", "10", "50", "100"], 3),

        ("La pieza central de conexión al cluster es:",
        ["SparkDriver", "SparkShell", "SparkContext", "SparkCore"], 2),

        ("¿Cómo se llama el módulo para datos estructurados?",
        ["Spark Stream", "Spark SQL", "GraphX", "MLlib"], 1),

        ("Un RDD es…",
        ["Mutable", "Inmutable", "Un archivo físico", "Una base SQL"], 1),

        ("Los DataFrames se definen como:",
        ["RDDs con esquema", "RDDs sin particiones", "Tablas SQL normales", "Conjuntos binarios crudos"], 0),

        ("Spark Streaming trabaja mediante:",
        ["Streaming puro", "Micro-batches", "Hilos paralelos", "SQL iterativo"], 1),

        ("¿Qué módulo se usa para machine learning?",
        ["GraphX", "Spark SQL", "MLlib", "Flume"], 2),

        ("GraphX permite trabajar con:",
        ["Archivos CSV", "Grafos", "Imágenes", "Streams financieros"], 1),

        ("Los shells interactivos de Spark incluyen:",
        ["Python y C++", "Python y Scala", "R y Go", "Java y C"], 1),

        ("Para scripts se utiliza:",
        ["spark-run", "spark-init", "spark-submit", "spark-exec"], 2),

        ("Los RDDs son tolerantes a fallos mediante:",
        ["Replicación", "DAG de operaciones", "Hashing", "Integridad binaria"], 1),

        ("¿Qué lenguaje se usa en HiveQL?",
        ["SQL extendido", "Python", "Scala nativo", "Bash"], 0),

        ("En Spark Streaming, un DStream es:",
        ["Una tabla", "Un RDD distribuido único", "Una secuencia de RDDs", "Un archivo en HDFS"], 2),

        ("Spark Core se encarga de:",
        ["Machine learning", "Grafos", "Scheduling y funciones básicas", "Manejo de imágenes"], 2),

        ("¿Qué formato NO se menciona como compatible con Spark SQL?",
        ["JSON", "JDBC", "ODBC", "XML"], 3),

        ("Spark integra por defecto con:",
        ["HDFS", "Docker", "Prometheus", "Airflow"], 0),

        ("Un DataFrame está compuesto por:",
        ["Archivos", "Tuplas con nombre y tipo", "Bytes sin procesar", "Listas sin esquema"], 1),

        ("¿Qué lenguaje incluye spark-shell?",
        ["Python", "Scala", "Java", "SQL"], 1),

        ("El driver en Spark:",
        ["Ejecuta operaciones en los nodos",
        "Maneja la lógica y envía tareas",
        "Es un DataFrame",
        "Es el sistema de archivos"], 
        1),
    ],


    "Clase 04 – Spark Streaming, MLlib, GraphX": [
        ("Spark Streaming funciona mediante:", 
        ["Streaming 100% continuo", "Micro-batches", "Lectura por lotes diarios", "SQL en tiempo real"], 
        1),

        ("Un DStream está compuesto por:", 
        ["Una sola RDD", "Un archivo JSON", "Una secuencia de RDDs", "Un DataFrame temporal"], 
        2),

        ("Spark Streaming NO es 100% streaming debido a:", 
        ["Su arquitectura", "La latencia de Kafka", "El uso de micro-batches", "Limitaciones de HDFS"], 
        2),

        ("Una ventana que conserva los últimos n datos se llama:", 
        ["Landmark", "Sliding", "Fading", "Growing"], 
        1),

        ("¿Cuál es una fuente típica de streaming?", 
        ["CSV", "Amazon S3", "Twitter", "Parquet"], 
        2),

        ("Un algoritmo de streaming debe priorizar:", 
        ["Precisión sin límite", "Velocidad, memoria y eficacia", "Tamaño del cluster", "Número de particiones"], 
        1),

        ("Un DStream representa:", 
        ["Un RDD continuo", "Datos estructurados", "Flujos discretizados", "Tablas SQL"], 
        2),

        ("¿Qué fuente NO es mencionada para Spark Streaming?", 
        ["Kafka", "Twitter", "Flume", "Google Drive"], 
        3),

        ("La ventana Sliding Window:", 
        ["Mantiene todos los datos históricos", "Se mueve en intervalos fijos", "Aumenta infinitamente", "Solo sirve para MLlib"], 
        1),

        ("En MLlib, los algoritmos son:", 
        ["No distribuidos", "Diseñados para RAM local", "Iterativos y distribuidos", "Basados en GPUs"], 
        2),

        ("¿Qué algoritmo NO pertenece a MLlib?", 
        ["K-Means", "Random Forest", "Árboles impulsados por gradiente", "Algoritmos de ordenamiento"], 
        3),

        ("MLlib puede realizar:", 
        ["Clustering", "Procesamiento de imágenes", "Renderizado 3D", "Compilación de código"], 
        0),

        ("¿Cuál NO es un algoritmo de clustering?", 
        ["Gaussian Mixtures", "LDA", "K-means", "Random Forest"], 
        3),

        ("GraphX se usa para trabajar con:", 
        ["HDFS", "Grafos", "Bases relacionales", "Archivos XML"], 
        1),

        ("PageRank sirve para:", 
        ["Clasificación", "Detección de duplicados", "Medir importancia de nodos", "Hacer compresión de grafos"], 
        2),

        ("Strongly Connected Components identifica:", 
        ["Una única comunidad", "Componentes conectados por fuerza", "Componentes fuertemente conectados", "Solo nodos sin relaciones"], 
        2),

        ("Triangle Count se usa para:", 
        ["Contar nodos", "Contar triángulos", "Medir latencia", "Detectar outliers"], 
        1),

        ("GraphX es parte de:", 
        ["Hadoop", "Kubernetes", "Spark", "Hive"], 
        2),

        ("Un uso típico de GraphX es:", 
        ["Limpieza de datos tabulares", "Detección de fraudes", "Exportar CSV", "Entrenar modelos NLP"], 
        1),

        ("Un modelo de streaming puede:", 
        ["Entrenarse dinámicamente", "No actualizarse nunca", "Trabajar solo offline", "Depender solo de HDFS"], 
        0)
    ],


    "Clase 05 – Containers y Docker": [
        ("¿Cuál es el problema que motivó el uso de containers?",
        ["Falta de RAM", "“En mi máquina funciona…”", "Incompatibilidad de redes", "Escasez de CPUs"],
        1),

        ("Un contenedor incluye:",
        ["Un OS completo", "Todos los paquetes del host", "Solo lo necesario para la aplicación", "Un kernel propio"],
        2),

        ("¿Qué característica NO es propia de un contenedor?",
        ["Ligero", "Portable", "Aislado", "Arranque lento"],
        3),

        ("Las imágenes son:",
        ["Contenedores en ejecución", "Archivos sin estado", "Binarios del procesador", "Bases de datos"],
        1),

        ("Los contenedores se crean a partir de:",
        ["Repositorios", "Imágenes", "Kernels", "Procesos del SO"],
        1),

        ("¿Qué diferencia a una VM de un contenedor?",
        ["La VM incluye un OS completo", "La VM arranca más rápido", "Los contenedores pesan GB", "Los contenedores no se aíslan"],
        0),

        ("Docker Engine consiste en:",
        ["Cliente, servidor y API", "Driver y shell", "Kernel y red", "Daemon y GPU"],
        0),

        ("El daemon de Docker se llama:",
        ["docker-engine", "docker-daemon", "dockerd", "docker-run"],
        2),

        ("El cliente Docker se comunica con el daemon mediante:",
        ["API REST", "SSH", "FTP", "SQL"],
        0),

        ("¿Qué mide el tamaño de un contenedor típicamente?",
        ["KB", "MB", "GB", "TB"],
        1),

        ("Un contenedor es:",
        ["Un proceso", "Un archivo", "Una VM", "Un hypervisor"],
        0),

        ("Las imágenes pueden:",
        ["Tener estado", "Iniciar procesos", "Moverse entre máquinas", "Modificar el kernel"],
        2),

        ("Las VMs se caracterizan por:",
        ["Arranques muy rápidos", "Aislamiento ligero", "Uso de un OS completo", "Reutilizar kernel del host"],
        2),

        ("Un caso típico de uso de containers es:",
        ["Correr sistemas operativos completos", "Empaquetar microservicios", "Administrar hardware", "Montar redes físicas"],
        1),

        ("Los containers comparten:",
        ["El kernel del host", "El filesystem del host", "Usuarios del host", "Drivers del host"],
        0),

        ("¿Qué afirma la metáfora del “remolque”?",
        ["Los contenedores incluyen motor", "Las VMs son más ligeras", "Los contenedores usan el kernel del host", "Las VMs comparten kernel"],
        2),

        ("Una imagen incluye:",
        ["El kernel", "Archivos necesarios para ejecutar una app", "El scheduler del sistema", "Un servidor web siempre"],
        1),

        ("La portabilidad se debe a:",
        ["Imágenes siempre idénticas", "Uso de redes privadas", "Uso de drivers comunes", "Falta de dependencias"],
        0),

        ("¿Qué comando/lista corresponde a una VM?",
        ["GB de tamaño", "MB de tamaño", "Kernel compartido", "Inicio casi instantáneo"],
        0),

        ("Los contenedores permiten resolver:",
        ["Altos costos", "Conflictos de dependencias", "Falta de datos", "Problemas de visualización"],
        1),
    ],


    "Clase 06 – Kafka": [
        ("Kafka es principalmente un:", 
        ["Sistema de archivos", "Sistema de mensajería distribuida", "Motor SQL", "Renderizador"], 
        1),

        ("Los servidores que almacenan mensajes se llaman:", 
        ["DataNodes", "Brokers", "Producers", "Agents"], 
        1),

        ("Kafka utiliza para coordinación:", 
        ["HDFS", "Zookeeper", "MLlib", "JDBC"], 
        1),

        ("Un producer se encarga de:", 
        ["Leer mensajes", "Crear y publicar mensajes", "Controlar particiones", "Ordenar offsets"], 
        1),

        ("Un consumer se encarga de:", 
        ["Publicar mensajes", "Eliminar particiones", "Leer mensajes", "Replicar brokers"], 
        2),

        ("Los mensajes se agrupan en:", 
        ["Streams", "Tópicos", "Jobs", "Hilos"], 
        1),

        ("El orden de Kafka está garantizado:", 
        ["En todo el cluster", "Entre particiones únicamente", "Solo dentro de una partición", "No está garantizado"], 
        2),

        ("La política de retención define:", 
        ["El orden de los mensajes", "Cuándo se borran mensajes", "Qué consumer los recibe", "La prioridad en redes"], 
        1),

        ("Una partición contiene:", 
        ["Mensajes en paralelo", "Mensajes con timestamp", "Offset y mensajes", "Solo claves"], 
        2),

        ("El offset representa:", 
        ["La hora del servidor", "La posición del mensaje", "El tamaño del tópico", "La clave del mensaje"], 
        1),

        ("La ventaja de la retención es:", 
        ["Más capacidad de borrado", "Lectura repetida de mensajes", "Seguridad", "Evita duplicados"], 
        1),

        ("¿Qué algoritmo se usa para elegir partición por defecto?", 
        ["Hash por clave", "Round robin", "Prioridad", "Tiempo de llegada"], 
        1),

        ("Kafka garantiza tolerancia a fallos mediante:", 
        ["Redundancia de offsets", "Replicación de particiones", "Zookeeper distribuido", "Duplicación de producers"], 
        1),

        ("Kafka NO elimina mensajes automáticamente porque:", 
        ["Es un sistema batch", "Requiere política de retención", "No soporta borrado", "Usa solo RAM"], 
        1),

        ("Streams API permite:", 
        ["Crear tópicos", "Crear pipelines de procesamiento", "Configurar offsets", "Administrar Zookeeper"], 
        1),

        ("Connect API permite:", 
        ["Enviar datos a sistemas externos", "Manejar particiones", "Ajustar retención", "Replicar brokers"], 
        0),

        ("Kafka es ideal para:", 
        ["Procesamiento offline", "Flujo continuo de datos", "SQL intensivo", "Sistemas monolíticos"], 
        1),

        ("Kafka mantiene orden dentro de una partición porque:", 
        ["Usa índices invertidos", "Los mensajes se agregan secuencialmente", "Se ordenan por timestamp", "Usa árboles B+"], 
        1),

        ("¿Qué NO pertenece al ecosistema de Kafka?", 
        ["Brokers", "Producers", "Consumers", "DataNodes"], 
        3),

        ("El timestamp del mensaje incluye:", 
        ["Offset", "Hora en 64 bits", "Partición", "Hash de clave"], 
        1),
    ]

}

# ---------------------------
# Agregar la opción integradora
# ---------------------------
clases_existentes = list(questions.keys())
opcion_integradora = "🔀 Integrador (todas las clases)"
clases_mostradas = clases_existentes + [opcion_integradora]

# ---------------------------
# Cronómetro
# ---------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None

def iniciar_cronometro():
    st.session_state.start_time = time.time()

def obtener_tiempo_transcurrido():
    if st.session_state.start_time is None:
        return "00:00"
    t = int(time.time() - st.session_state.start_time)
    mins = t // 60
    secs = t % 60
    return f"{mins:02d}:{secs:02d}"

# ------------------------------------------------------------
# Configuración de la página
# ------------------------------------------------------------
st.title("Simulador de Examen")
st.markdown("Selecciona una clase para comenzar el examen.")

# ------------------------------------------------------------
# Selección de clase
# ------------------------------------------------------------
clase = st.selectbox("📘 Selecciona la clase:", clases_mostradas)

# ------------------------------------------------------------
# Inicialización de sesión
# ------------------------------------------------------------
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ------------------------------------------------------------
# Generar examen
# ------------------------------------------------------------
if st.button("🎯 Generar examen de la clase"):
    st.session_state.submitted = False
    st.session_state.answers = {}

    # activar cronometro
    iniciar_cronometro()

    # Cargar preguntas según la opción
    if clase == opcion_integradora:
        todas = []
        for c in clases_existentes:
            todas.extend(questions[c])
        num_questions = min(20, len(todas))  # integrador con 20 preguntas
        st.session_state.selected_questions = random.sample(todas, k=num_questions)
    else:
        num_questions = min(10, len(questions[clase]))
        st.session_state.selected_questions = random.sample(questions[clase], k=num_questions)

    st.success("Preguntas generadas. ¡Podés comenzar!")

# ------------------------------------------------------------
# Mostrar preguntas + Cronómetro
# ------------------------------------------------------------
if st.session_state.selected_questions and not st.session_state.submitted:

    # ⏱️ CRONÓMETRO (actualiza con cada interacción)
    st.markdown(f"### ⏱️ Tiempo transcurrido: **{obtener_tiempo_transcurrido()}**")

    st.header(f"📚 Examen – {clase}")
    st.markdown("Seleccioná una respuesta para cada pregunta.")

    for idx, (q, options, ans_index) in enumerate(st.session_state.selected_questions):
        st.session_state.answers[idx] = st.radio(
            f"{idx+1}. {q}",
            options,
            key=f"q_{idx}"
        )

    if st.button("📌 Enviar examen"):
        st.session_state.submitted = True

# ------------------------------------------------------------
# Corrección
# ------------------------------------------------------------
if st.session_state.submitted:
    st.header("📊 Resultados del examen")

    tiempo_final = obtener_tiempo_transcurrido()
    st.markdown(f"⏱️ **Tiempo total:** `{tiempo_final}`")

    score = 0
    for idx, (q, options, ans_index) in enumerate(st.session_state.selected_questions):
        user_answer = st.session_state.answers.get(idx, None)
        correct = options[ans_index]

        if user_answer == correct:
            score += 1
            st.success(f"✔️ {idx+1}. Correcta – {q}")
        else:
            st.error(f"❌ {idx+1}. Incorrecta – {q}\n**Respuesta correcta:** {correct}")

    st.markdown(f"### 🟦 Puntaje final: **{score} / {len(st.session_state.selected_questions)}**")

    if st.button("🔄 Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


# ------------------------------------------------------------
# FOOTER 
# ------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 15px; color: gray;'>
        <p><b>Especialización en Ciencia de Datos – UNLaM</b><br>
        Esto lo hice para estudiar para la materia de <b>Procesamiento de Grandes Volúmenes de Datos</b>.</p>
        <p>Desarrollado por <b>Yesica Fica Millán</b> – <a href="https://www.linkedin.com/in/yesica-fica-millan" target="_blank">LinkedIn</a></p>
        <p style='font-size:13px;'>© 2025 – Proyecto de estudio personal</p>
    </div>
    """,
    unsafe_allow_html=True
)
