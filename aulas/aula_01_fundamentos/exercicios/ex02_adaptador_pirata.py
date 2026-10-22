"""Aula 1 — Exercício 2: crie o seu próprio adaptador!

O PirataLLM deve "encaixar" na porta LLMPort e responder como um pirata.
Nenhuma linha do resto do sistema precisa mudar para usá-lo.

Rodar e verificar:
    uv run python aulas/aula_01_fundamentos/exercicios/ex02_adaptador_pirata.py
"""

from assistente_ia.domain.modelos import Mensagem, RespostaLLM
from assistente_ia.exercicios import verificar
from assistente_ia.ports import LLMPort


class PirataLLM:
    """Adaptador que responde: 'Arrr! <pergunta do usuário>, marujo!'"""

    def responder(self, mensagens: list[Mensagem], *, esforco: str | None = None) -> RespostaLLM:
        conteudo = mensagens[-1].conteudo
        texto = f"Arrr! {conteudo}, marujo!"
        return RespostaLLM(texto=texto, modelo="pirata")

    def transmitir(self, mensagens: list[Mensagem]):
        yield from self.responder(mensagens).texto.split()

    def responder_estruturado(self, mensagens, esquema):
        raise NotImplementedError("Pirata não preenche formulário!")


def checar_porta():
    assert isinstance(PirataLLM(), LLMPort), "PirataLLM precisa ter os 3 métodos da LLMPort."


def checar_resposta():
    resposta = PirataLLM().responder([Mensagem("user", "Tem sonho")])
    assert resposta.texto == "Arrr! Tem sonho, marujo!", f"Texto recebido: {resposta.texto!r}"
    assert resposta.modelo == "pirata"


def checar_streaming():
    pedacos = list(PirataLLM().transmitir([Mensagem("user", "Tem sonho")]))
    assert len(pedacos) == 4, f"Esperava 4 pedaços (palavras), recebi {len(pedacos)}."


if __name__ == "__main__":
    verificar("Aula 1 — Exercício 2", checar_porta, checar_resposta, checar_streaming)
