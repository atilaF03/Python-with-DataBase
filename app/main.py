from services.usuario_services import UsuarioService
from repositories.usuario_repository import  UsuarioRepository
from config.connection import Session


def main():
    session=Session()
    repository = UsuarioRepository
    service = UsuarioService

    service.criar_usuario("marta","marta@gmai.com","123")

    print("\nListando todos os usuarios")
    usuarios = service.listar_todos_usurarios

    for usuario in usuarios:
        print(f"{usuario.nome}-{usuario.email}")

if __name__ == "__main__":
    main()