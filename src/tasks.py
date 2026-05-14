tarefas = [

    {
        "nome": "classificacao_sentimento",

        "tipo": "classificacao",

        "instrucao": (
            "Classifique o sentimento do cliente "
            "como POSITIVO, NEGATIVO, NEUTRO ou MISTO."
        ),

        "formato_output": (
            "Responda APENAS com a classificação."
        ),

        "exemplos_fewshot": [
            {
                "input": "Produto excelente e entrega rápida.",
                "output": "POSITIVO"
            },
            {
                "input": "Veio quebrado e atrasado.",
                "output": "NEGATIVO"
            }
        ],

        "passos_cot": [
            "Identifique pontos positivos.",
            "Identifique pontos negativos.",
            "Compare os aspectos encontrados.",
            "Defina a classificação final."
        ],

        "persona": "analista_cx"
    },

    {
        "nome": "extracao_dados",

        "tipo": "extracao",

        "instrucao": (
            "Extraia produto, preço e problema "
            "mencionados pelo cliente."
        ),

        "formato_output": (
            "Responda em formato JSON."
        ),

        "exemplos_fewshot": [
            {
                "input": (
                    "Notebook Dell de R$3500 "
                    "com tela quebrada."
                ),
                "output": (
                    '{"produto":"Notebook Dell",'
                    '"preco":"R$3500",'
                    '"problema":"tela quebrada"}'
                )
            }
        ],

        "passos_cot": [
            "Identifique o produto.",
            "Identifique o preço.",
            "Identifique o problema relatado.",
            "Monte o JSON final."
        ],

        "persona": "especialista_suporte"
    },

    {
        "nome": "resumo_reclamacao",

        "tipo": "sumarizacao",

        "instrucao": (
            "Crie um resumo executivo da reclamação "
            "do cliente."
        ),

        "formato_output": (
            "Responda em até 3 linhas."
        ),

        "exemplos_fewshot": [
            {
                "input": (
                    "Cliente relata atraso na entrega "
                    "e dificuldade no suporte."
                ),
                "output": (
                    "Cliente insatisfeito com atraso "
                    "e baixa eficiência do suporte."
                )
            }
        ],

        "passos_cot": [
            "Identifique o principal problema.",
            "Remova informações repetidas.",
            "Crie um resumo curto e claro."
        ],

        "persona": "gerente_operacoes"
    }
]