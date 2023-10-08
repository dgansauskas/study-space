# Extração de Anúncios de Veículos

Este projeto teve como objetivo criar uma rotina de raspagem de dados dos site `OLX` e `Mercado Livre` para fazer extração dos anúncios de veículos filtrados para as regiões de **São Paulo-SP** e **Campo Grande-MS** e baseados por critérios como: valor mínimo, valor máximo, quilometragem mínima e modelos para incluir/excluir da análise. Também há uma tratativa para minimizar a possibilidade de anúncios duplicados.

Foi adicionado o móulo `timer_tasks` com finalidade de ajudar na contabilização do tempo de processamento e quais funções dos códigos que estão sendo processados durante a execução.


### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Python 3.11 ou superior
```

### 🔧 Instalação

Criar uma pasta

```bash
mkdir nome_projeto
```
Entrar na pasta do projeto criada
```bash
cd nome_projeto/
```
Para criar o ambiente virtual, abra o terminal dentro da pasta criada e faça:
```bash
python3 -m venv venv
```
Ativar o ambiente virtual, abrindo o terminal dentro da pasta criada e digite:
```bash
source venv/bin/activate
```
Caso utilize o windows, para ativar o ambiente o comando se difere:
```bash
venv\Scripts\Activate
```
Ainda com o ambiente virtual ativo, solicitar a instalação de todas as bibliotecas necessárias
```bash
pip install -r requirements.txt
```

## 📌 Versão

Este projeto foi desenvolvido baseado nos links dos sites em `Outubro de 2023`.`

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Danilo Gansauskas** - [dgansauskas](https://github.com/dgansauskas)

## 📄 Licença

Este projeto está sob a licença (MIT) - veja o arquivo [LICENSE.md](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) para detalhes.
