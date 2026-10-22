"""Aula 1 — Exercício 1: o bom-dia da padaria.

Objetivo: montar a lista de mensagens (system + user) e chamar a porta LLMPort.

Rodar e verificar:
    uv run python aulas/aula_01_fundamentos/exercicios/ex01_bom_dia_padaria.py
"""

from assistente_ia.adapters.llm.fake_llm import FakeLLM
from assistente_ia.domain.modelos import Mensagem
from assistente_ia.exercicios import verificar
from assistente_ia.ports import LLMPort

PAO_DO_DIA = "pão de queijo"


def montar_mensagens(nome_cliente: str, pao_do_dia: str) -> list[Mensagem]:
    """Devolva DUAS mensagens:
    1) system: diga ao modelo que ele é o atendente da Padaria Peter Pão;
    2) user: um pedido de bom-dia que contenha o nome do cliente E o pão do dia.
    """
    return [
        Mensagem(
            "system",
            "Você é o atendente da Padaria Peter Pão."
        ),
        Mensagem(
            "user",
            f"Dê bom-dia ao cliente {nome_cliente} e informe que o pão do dia é {pao_do_dia}."
        )
    ]

def dar_bom_dia(llm: LLMPort, nome_cliente: str) -> str:
    """Chame o llm com as mensagens e devolva só o texto da resposta."""
    mensagens = montar_mensagens(nome_cliente, "Pão francês")
    return llm.responder(mensagens).texto


def checar_mensagens():
    mensagens = montar_mensagens("Joana", PAO_DO_DIA)
    assert len(mensagens) == 2, "Devolva exatamente 2 mensagens."
    assert mensagens[0].papel == "system", "A primeira mensagem deve ser 'system'."
    assert mensagens[1].papel == "user", "A segunda mensagem deve ser 'user'."
    assert "Joana" in mensagens[1].conteudo, "O nome do cliente deve aparecer na mensagem do usuário."
    assert PAO_DO_DIA in mensagens[1].conteudo, "O pão do dia deve aparecer na mensagem do usuário."


def checar_chamada():
    llm = FakeLLM()
    texto = dar_bom_dia(llm, "Joana")
    assert isinstance(texto, str) and texto, "dar_bom_dia deve devolver um texto."
    assert len(llm.chamadas) == 1, "O llm deve ser chamado exatamente uma vez."


if __name__ == "__main__":
    verificar("Aula 1 — Exercício 1", checar_mensagens, checar_chamada)
