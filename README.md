# Sistema de Reconhecimento Facial

## Descrição
Este projeto tem como objetivo implementar um sistema de detecção e reconhecimento facial utilizando o framework TensorFlow e outras bibliotecas complementares. O sistema deve ser capaz de detectar e reconhecer múltiplas faces simultaneamente.

## Requisitos
Para executar o projeto, certifique-se de ter as seguintes bibliotecas instaladas:
- Python 3.x
- TensorFlow
- OpenCV
- NumPy
- dlib
- face_recognition

Para instalar todas as dependências, utilize o seguinte comando:
```bash
pip install tensorflow opencv-python numpy dlib face-recognition
```

## Estrutura do Projeto
O projeto é composto pelos seguintes arquivos:
- `reconhecimento_facial.py`: Script principal para detecção e reconhecimento facial.
- `dataset/`: Pasta contendo as imagens utilizadas para treinamento e reconhecimento.
- `model/`: Pasta onde será armazenado o modelo treinado.
- `README.md`: Documento de referência sobre o projeto.

## Como Executar
1. Certifique-se de que todas as dependências estão instaladas.
2. Adicione imagens das faces a serem reconhecidas na pasta `dataset/`.
3. Execute o script principal:
   ```bash
   python reconhecimento_facial.py
   ```
4. O sistema abrirá a câmera e tentará detectar e reconhecer as faces com base nas imagens fornecidas.

## Funcionalidades
- **Detecção Facial:** Utiliza uma rede de detecção treinada para localizar rostos em tempo real.
- **Reconhecimento Facial:** Compara os rostos detectados com um banco de imagens previamente treinado.
- **Suporte a Múltiplas Faces:** Permite a identificação de diversas pessoas simultaneamente.


