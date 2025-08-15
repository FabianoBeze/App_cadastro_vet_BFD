class Animal:            #testando o PEP 8
    def __init__(self, nome, especie, idade,contato, id, procedimento=None):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.contato = contato
        self.id = id
        self.procedimento = procedimento

    def __str__(self):
        proc = self.procedimento if self.procedimento else "N/A"
        return (
            f"Nome: {self.nome}\n"
            f"Espécie: {self.especie}\n"
            f"Idade: {self.idade} anos\n"
            f"Telefone para contato: {self.contato}\n"
            f"Identificação: {self.id}\n"
            f"Procedimento: {proc}\n"
            "----------------------"
        )


class CadastroAnimal:
    def __init__(self):
        self.lista_animais = []
        self.proximo_id = 1

    def adicionar_animal(self, nome, especie, idade, contato, procedimento=None):
        # atenção: id vem antes de procedimento conforme __init__ de Animal
        animal = Animal(nome, especie, idade, contato, self.proximo_id, procedimento)
        self.lista_animais.append(animal)
        self.proximo_id += 1
        print("✅ Animal cadastrado com sucesso!")

    def listar_animais(self):
        if not self.lista_animais:
            print("⚠ Nenhum animal cadastrado.")
        else:
            print("\nAnimais cadastrados:")
            for animal in self.lista_animais:
                print(animal)


def menu():
    cadastro = CadastroAnimal()

    while True:
        print("\n--- Menu de Cadastro de Animais ---")
        print("1 - Cadastrar animal")
        print("2 - Listar animais")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do animal: ")
            especie = input("Espécie do animal: ")
            contato = input("Telefone de contato: ")

            while True:
                try:
                    idade = int(input("Idade do animal: "))
                    break
                except ValueError:
                    print("⚠ Digite um número válido para a idade.")

            procedimento = input("Procedimento (opcional): ").strip() or None

            cadastro.adicionar_animal(nome, especie, idade, contato, procedimento)

        elif opcao == "2":
            cadastro.listar_animais()

        elif opcao == "0":
            print("👋 Encerrando programa...")
            break

        else:
            print("⚠ Opção inválida.")


if __name__ == "__main__":
    menu()
