import openai  # pip install openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table
import PyPDF2

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""

pdf_file_obj=open("Listas por Comprension.pdf", "rb") 
pdf_reader=PyPDF2.PdfReader(pdf_file_obj)
    #print(pdf_reader.document Info) 
number_of_pages = len(pdf_reader.pages)
print(len(pdf_reader.pages))
alltext=""
for page in range(len(pdf_reader.pages)): 
    page_obj=pdf_reader.pages[page]
    text=page_obj.extract_text() 
    alltext+=text
    print(text.strip())
def main():

    openai.api_key = "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"

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt+alltext


if __name__ == "__main__":
    typer.run(main)