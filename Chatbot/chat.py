#### Importamos librerias
import random
import json

import torch

from model import NeuralNet
from NLP import bag_of_words, tokenize

#### Declaramos el uso de placa de video si existiese una placa CUDA o similar (Agiliza el trabajo al pasar el procecamiento a la GPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#### Traemos la data y el modelo entrenado
with open('datajotason.json', 'r', encoding = 'utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#### Damos algunas caracteristicas y condiciones al Chatbot
bot_name = "JC"
print("Bienvenidx! Soy tu asistente virtual, dejame tu consulta (escribi 'salir' para salir)")
while True:
    sentence = input("Tu ")
    if sentence == "salir":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

#### Desde este punto trabajamos las probabilidades de cada input para dar la mejor respuesta posible
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: No entiendo...")