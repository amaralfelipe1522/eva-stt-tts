# EVA - RPG Bot
EVA é o módulo principal de um bot para RPG, projetado para facilitar a interação entre jogadores e o ambiente do jogo, utilizando transcrição de voz para texto (gTTS), texto pra voz (AWS Polly) e integração com IA generativa (localmente com Ollama). O módulo se concentra na comunicação interativa e em melhorar a experiência de narrativa nos jogos de RPG.

![EVA Avatar](./assets/img/eva-avatar.webp)
## Recursos Principais
- Conversão de voz para texto e vice-versa.
- Integração com IA generativa para respostas em tempo real.
- Configurações avançadas para reconhecimento de diferentes personagens e jogadores.

## Executando o Bot com Docker
### Passo 1: Construir a Imagem
Para construir a imagem Docker localmente, execute:
```docker
docker build -t amaralfelipe1522/eva-stt-tts:2.0 .
```

### Passo 2: Executar o Container
Para iniciar o container com suporte para dispositivos de áudio e teclado, utilize o seguinte comando:
```docker
xhost +local:docker && docker run -it --rm --name eva\
    --device /dev/snd \
    --group-add audio \
    -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native \
    -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native \
    amaralfelipe1522/eva-stt-tts:2.0
```
Este comando configura o acesso aos dispositivos necessários para captura e reprodução de áudio, bem como a interação com o sistema de som.

## Executando Localmente (Sem Docker)
> Pré-requisitos: Instalação de algumas dependências essenciais.

### FFmpeg:
A instalação do FFmpeg pode variar conforme o sistema operacional. Abaixo estão os métodos de instalação em Windows e Ubuntu.

- Windows (Método 1):
    1. Baixe os binários do FFmpeg no site oficial: [ffmpeg.org/download.html](ffmpeg.org/download.html);
    2. Extraia o conteúdo para um diretório de sua escolha;
    3. Adicione o diretório ao PATH do sistema nas configurações de ambiente do Windows para acessá-lo de qualquer termina.

- Windows (Método 2):
    - Use o Windows Package Manager:
        ```bash
        winget install "FFmpeg (Essentials Build)"
        ```

- Ubuntu:
    ```bash
    sudo apt install ffmpeg
    sudo apt install portaudio19-dev python3-dev
    ```
Essas dependências são necessárias para que o EVA possa capturar e processar áudio, além de integrar recursos em Python que exigem compilação.

## Próximos passos: Multiagentes + MCP

1. Narrador Principal
- Responsável por descrever cenários, eventos e manter a história coerente.
- Pode interagir com outros agentes para enriquecer a narrativa.

2. Gerador de NPCs
- Cria personagens com personalidade, aparência e objetivos.
- Pode consultar um banco de dados via MCP para nomes, culturas, etc.

3. Agente de Regras
- Valida ações dos jogadores conforme o sistema (D&D, Tormenta, etc.).
- Usa MCP para acessar PDFs ou APIs com regras oficiais.

4. Agente de Clima e Ambiente
- Gera descrições dinâmicas do clima, sons, iluminação.
- Pode usar MCP para puxar dados reais (ex.: clima atual da cidade para inspiração).

5. Agente de Música e Sons
- Sugere trilhas sonoras ou efeitos sonoros.
- MCP pode integrar com Spotify ou bancos de áudio.
