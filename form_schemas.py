from typing import Any, Dict, Optional


def build_full_sample_form_payload(
	name: str = "Exemplo CRUD - Fulcrum (Completo)",
	classification_set_id: Optional[str] = None,
	linked_form_id: Optional[str] = None,
) -> Dict[str, Any]:
	"""
	Monta um payload de formulário contendo todos os campos solicitados.
	Alguns campos exigem recursos externos:
	- ClassificationField: requer 'classification_set_id'.
	- RecordLinkField: requer 'form_id' do formulário vinculado.
	"""
	# Campos base
	elements = [
		{
			"type": "TextField",
			"key": "campo_texto",
			"label": "Texto",
		},
		{
			"type": "NumberField",
			"key": "campo_numerico",
			"label": "Numérico",
		},
		{
			"type": "YesNoField",
			"key": "campo_sim_nao",
			"label": "Sim/Não",
		},
		{
			"type": "DateField",
			"key": "campo_data",
			"label": "Data",
		},
		{
			"type": "TimeField",
			"key": "campo_hora",
			"label": "Hora",
		},
		# Single choice
		{
			"type": "ChoiceField",
			"key": "campo_escolha_unica",
			"label": "Escolha Única",
			"choices": [
				{"label": "Opção A", "value": "a"},
				{"label": "Opção B", "value": "b"},
				{"label": "Opção C", "value": "c"},
			],
			"allow_multiple": False,
		},
		# Multiple choice
		{
			"type": "ChoiceField",
			"key": "campo_escolha_multipla",
			"label": "Escolha Múltipla",
			"choices": [
				{"label": "X", "value": "x"},
				{"label": "Y", "value": "y"},
				{"label": "Z", "value": "z"},
			],
			"allow_multiple": True,
		},
		# Mídia e anexos
		{"type": "SignatureField", "key": "campo_assinatura", "label": "Assinatura"},
		{"type": "PhotoField", "key": "campo_foto", "label": "Foto"},
		{"type": "VideoField", "key": "campo_video", "label": "Vídeo"},
		{"type": "AudioField", "key": "campo_audio", "label": "Áudio"},
		{"type": "AttachmentField", "key": "campo_anexo", "label": "Anexo"},
		# Outros campos
		{"type": "AddressField", "key": "campo_endereco", "label": "Endereço"},
		{"type": "HyperlinkField", "key": "campo_link", "label": "Hyperlink"},
		{"type": "BarcodeField", "key": "campo_codigo_barras", "label": "Código de Barras"},
	]

	# Classification
	if classification_set_id:
		elements.append(
			{
				"type": "ClassificationField",
				"key": "campo_classificacao",
				"label": "Classificação",
				"classification_set_id": classification_set_id,
			}
		)

	# Record link
	if linked_form_id:
		elements.append(
			{
				"type": "RecordLinkField",
				"key": "campo_vinculo_registro",
				"label": "Vínculo de Registro",
				"form_id": linked_form_id,
				"allow_multiple": False,
			}
		)

	# Calculation - usa expressão simples baseada em outros campos
	elements.append(
		{
			"type": "CalculatedField",
			"key": "campo_calculado",
			"label": "Calculado",
			# A sintaxe de expressão pode variar; ajuste conforme sua necessidade
			"expression": "FIELD('campo_texto') + ' - ' + TO_TEXT(FIELD('campo_numerico'))",
		}
	)

	return {
		"form": {
			"name": name,
			"elements": elements,
		}
	}

