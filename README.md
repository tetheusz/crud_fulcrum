# CRUD Fulcrum - Flask

Aplicação Flask em Python que expõe endpoints CRUD usando a API do Fulcrum, com exemplo de formulário contendo campos de vários tipos (texto, numérico, sim/não, etc.).

## Requisitos

- Python 3.10+
- Chave de API do Fulcrum (token)

## Instalação

```bash
pip install -r requirements.txt
```

Ou use um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` baseado em `.env.example`:

```env
FULCRUM_API_TOKEN=coloque_sua_chave_aqui
# Opcional: defina um formulário padrão para criar/consultar registros
# FULCRUM_FORM_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
PORT=8000
```

## Executando a API

```bash
python app.py
# Servidor em http://localhost:8000
```

Abra no navegador `http://localhost:8000/` para usar a UI simples.

## Endpoints

- GET /health — verificação simples
- GET /forms — lista formulários
- POST /bootstrap-form — cria um formulário de exemplo completo com campos: texto, numérico, sim/não, data, hora, escolha única, múltiplas escolhas, classificação, assinatura, foto, vídeo, áudio, anexo de arquivo, endereço, hyperlink, cálculo, código de barras, vínculo de registro
- GET /records?form_id=<id> — busca registros (pode usar `FULCRUM_FORM_ID` do `.env`)
- GET /records/<record_id> — obtém um registro
- POST /records — cria registro
- PUT /records/<record_id> — atualiza registro (apenas `form_values`)
- DELETE /records/<record_id> — remove registro

## Exemplos de uso

### 1) Criar formulário de exemplo

```bash
curl -X POST http://localhost:8000/bootstrap-form \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Exemplo CRUD - Fulcrum (Completo)",
    "create_linked_form": true
    # opcional: "classification_set_id": "<CLASSIFICATION_SET_ID>"
    # opcional: "linked_form_id": "<FORM_ID>"
  }'
```

Resposta (trecho):

```json
{
  "form": {
    "id": "<FORM_ID>",
    "name": "Exemplo CRUD - Fulcrum",
    "elements": [ ... ]
  }
}
```

Copie o `form.form.id` retornado e defina como `FULCRUM_FORM_ID` no `.env` (ou use diretamente nos requests abaixo).

### 2) Criar registro

```bash
curl -X POST http://localhost:8000/records \
  -H 'Content-Type: application/json' \
  -d '{
    "record": {
      "form_id": "<FORM_ID>",
      "form_values": {
        "campo_texto": "Exemplo de texto",
        "campo_numerico": 123,
        "campo_sim_nao": "yes",
        "campo_data": "2025-08-28",
        "campo_hora": "13:45",
        "campo_email": "exemplo@dominio.com",
        "campo_telefone": "+55 11 99999-9999",
        "campo_escolha_unica": "a"
      }
    }
  }'
```

Observações:
- Para `YesNoField` use `"yes"` ou `"no"`.
- Para `ChoiceField` use o `value` da opção (ex.: `"a"`, `"b"`, `"c"`).

### 3) Listar registros

```bash
curl 'http://localhost:8000/records?form_id=<FORM_ID>'
```

### 4) Atualizar registro

```bash
curl -X PUT http://localhost:8000/records/<RECORD_ID> \
  -H 'Content-Type: application/json' \
  -d '{
    "record": {
      "form_values": {
        "campo_texto": "Valor atualizado",
        "campo_sim_nao": "no"
      }
    }
  }'
```

### 5) Remover registro

```bash
curl -X DELETE http://localhost:8000/records/<RECORD_ID>
```

## Notas sobre tipos de campo

Os tipos seguem a nomenclatura da API do Fulcrum: `TextField`, `NumberField`, `YesNoField`, `DateField`, `TimeField`, `ChoiceField` (com `allow_multiple` para múltipla), `ClassificationField` (requer `classification_set_id`), `SignatureField`, `PhotoField`, `VideoField`, `AudioField`, `AttachmentField`, `AddressField`, `HyperlinkField`, `CalculatedField` (com `expression`), `BarcodeField`, `RecordLinkField` (requer `form_id`). Veja `form_schemas.py`.
