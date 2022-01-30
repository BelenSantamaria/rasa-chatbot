# Flujos conversacionales

* [ ] Intent bienvenida 
  * Respuesta: 'Hola, Soy el Bot de la Universitat de València ¿En qué te puedo ayudar?'

## 1. Grado

* [ ] Añadir intent `grado` para dar unformación sobre oferta formativa y webs específicas de cada grado
    * [ ] Parsear [página de grados](https://www.uv.es/uvweb/universidad/es/estudios-grado/oferta-grados/oferta-grados-1285846094474.html) para obtener correspondencia entre grados y páginas web.
    * [ ] Preguntar si quiere información general o sobre algún grado en concreto
  * Respuesta: 'Nuestros grados se imparten de manera presencial. Puedes consultar la oferta formativa en ir.uv.es/Na09Pog'
  * Respuesta: 'Puedes consultar los grados que ofrece la Universitat de València en el siguiente enlace: links.uv.es/xw5us9N'
  * Respuesta: 'Toda la información que planteas la podrás encontrar en la siguiente página web de la UV: uv.es/uvweb/grado-matematicas/es/grado-matematicas-1285929208365.html'

* [ ] Añadir intent `admision`. Parece que tiene una respuesta general sobre admisiones y también responde a las preguntas frecuentes sobre inscripciones añadiendo después 'Más información: Web específica'. En mi caso pondré el enlace a la página de prenscripciones en todas las respuestas para no tener que anotar manualmente el enlace de cada respuesta.
    * [ ] Parsear 'Preguntas frecuentes' sobre [inscripción](https://www.uv.es/uvweb/universidad/es/estudios-grado/admision/preguntas-frecuentes-1286095200713.html)
  * Respuesta: 'La admisión a las titulaciones oficiales de la Universidad de Valencia es un proceso a través del cual se distribuyen las plazas ofertadas cada curso entre las personas que solicitan la plaza y cumplen alguno de los requisitos de acceso. Este procedimiento incluye tanto las pruebas y acreditaciones para el acceso como la solicitud y asignación de las plazas.
Según sea la situación académica de partida de cada candidato, en primer lugar hay que:
1.- Superar las pruebas de acceso correspondientes (PAU Bachillerato, PAU Mayores de 25 años, PAU Mayores de 45 años o Selectivo del bachillerato extranjero no comunitario), o bien
2.- Obtener la acreditación de acceso (Mayores de 40 años, bachillerato de sistemas educativos de la UE), o bien
3.- Tener la titulación necesaria para el acceso (Ciclos Formativos o titulación universitaria).
Realizar la Preinscripción
Una vez que se tiene el requisito académico para poder acceder a la universidad es necesario realizar la preinscripción. Este procedimientos sirve para ordenar por nota de acceso a los estudiantes que piden plaza en un grado. Las universidades públicas valencianas y sus centros adscritos hacen la preinscripción conjuntamente, por ello, cada estudiante solo puede presentar una única preinscripción al distrito universitario valenciano.
Más información: links.uv.es/ceR60tM'
  * Respuesta: 'El porcentaje de plazas reservado para los diferentes cupos es:
- Titulados universitarios 3%
- Discapacitados 5%
- Alumnos mayores 25 años 3%
- Alumnos mayores 40 años 1%
- Alumnos mayores 45 años 1%
- Deportistas de alto nivel, deportista de élite A y B o de alta competición y deportistas de alto rendimiento: 5% (Para las enseñanzas de Maestro en Educación Primaria, Fisioterapia y Ciencias de la Actividad Física y del Deporte, un 10%)
Más información: ir.uv.es/APXVmV4'

* [ ] Matrícula

* [ ] Becas



