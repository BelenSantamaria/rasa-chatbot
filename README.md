# rasa-chatbot

## Creación del entorno

Para poder utilizar el chatbot es necesario tener instalado Python con Anaconda o Miniconda. 
Con el siguiente comando se puede crear un entorno con las dependencias del proyecto
```
conda env create -n rasa-chatbot -f requierements.txt
```

## Entrenamiento del modelo
Para poder utilizarlo es necesario entrenar antes un modelo. Para ello ejecutamos el sieguiente comando
```
rasa train
```

## Despliegue
En primer lugar desplegamos el servidor de acciones
```
rasa run actions
```

En otro terminal, ejecutamos lo siguiente para levantar el servidor del agente
```
rasa run --enable-api --cors="*"
```

En otro terminal ejecutamos:
```
python -m http.server
```

Por último, abrimos desde el navegador http://localhost:8000/ para poder interactuar con el chatbot