# Sistema de Gerenciamento de Alunos
# CRUD completo com menu interativo

# Lista para armazenar os alunos
alunos = []

def calcular_situacao(nota):
    """Calcula a situação do aluno baseado na nota"""
    if nota >= 7.0:
        return "Aprovado"
    elif nota >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_aluno():
    """Cadastra um novo aluno no sistema"""
    print("\n=== CADASTRO DE ALUNO ===")
    
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("❌ Nome não pode estar vazio!")
        return
    
    # Verifica se matrícula já existe
    matricula = input("Matrícula: ").strip()
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print("❌ Matrícula já cadastrada!")
            return
    
    if not matricula:
        print("❌ Matrícula não pode estar vazia!")
        return
    
    try:
        nota = float(input("Nota (0.0 a 10.0): "))
        if nota < 0 or nota > 10:
            print("❌ Nota deve estar entre 0.0 e 10.0!")
            return
    except ValueError:
        print("❌ Nota inválida! Use números.")
        return
    
    situacao = calcular_situacao(nota)
    
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'nota': nota,
        'situacao': situacao
    }
    
    alunos.append(aluno)
    print(f"✅ Aluno {nome} cadastrado com sucesso!")

def listar_alunos():
    """Lista todos os alunos cadastrados"""
    print("\n=== LISTA DE ALUNOS ===")
    
    if not alunos:
        print("📭 Nenhum aluno cadastrado ainda.")
        return
    
    # Estrutura avançada: sorted() com lambda para ordenar por nota (maior para menor)
    alunos_ordenados = sorted(alunos, key=lambda x: x['nota'], reverse=True)
    
    for i, aluno in enumerate(alunos_ordenados, 1):
        print(f"\n{i}. {aluno['nome']}")
        print(f"   Matrícula: {aluno['matricula']}")
        print(f"   Nota: {aluno['nota']:.1f}")
        print(f"   Situação: {aluno['situacao']}")

def atualizar_aluno():
    """Atualiza os dados de um aluno existente"""
    print("\n=== ATUALIZAR ALUNO ===")
    
    if not alunos:
        print("📭 Nenhum aluno cadastrado ainda.")
        return
    
    matricula = input("Digite a matrícula do aluno: ").strip()
    
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f"\nAluno encontrado: {aluno['nome']}")
            print(f"Nota atual: {aluno['nota']:.1f}")
            
            novo_nome = input("Novo nome (ou Enter para manter): ").strip()
            if novo_nome:
                aluno['nome'] = novo_nome
            
            try:
                nova_nota = input("Nova nota (ou Enter para manter): ").strip()
                if nova_nota:
                    nota = float(nova_nota)
                    if nota < 0 or nota > 10:
                        print("❌ Nota deve estar entre 0.0 e 10.0!")
                        return
                    aluno['nota'] = nota
                    aluno['situacao'] = calcular_situacao(nota)
            except ValueError:
                print("❌ Nota inválida!")
                return
            
            print(f"✅ Aluno atualizado com sucesso!")
            return
    
    print("❌ Aluno não encontrado!")

def remover_aluno():
    """Remove um aluno do sistema"""
    print("\n=== REMOVER ALUNO ===")
    
    if not alunos:
        print("📭 Nenhum aluno cadastrado ainda.")
        return
    
    matricula = input("Digite a matrícula do aluno a remover: ").strip()
    
    for i, aluno in enumerate(alunos):
        if aluno['matricula'] == matricula:
            confirmacao = input(f"Tem certeza que deseja remover {aluno['nome']}? (s/n): ").lower()
            if confirmacao == 's':
                alunos.pop(i)
                print(f"✅ Aluno removido com sucesso!")
            else:
                print("Operação cancelada.")
            return
    
    print("❌ Aluno não encontrado!")

def gerar_relatorio():
    """Gera um relatório estatístico dos alunos"""
    print("\n=== RELATÓRIO DE ALUNOS ===")
    
    if not alunos:
        print("📭 Nenhum aluno cadastrado ainda.")
        return
    
    total = len(alunos)
    
    # Estrutura avançada: list comprehension para filtrar alunos por situação
    aprovados = [a for a in alunos if a['situacao'] == 'Aprovado']
    recuperacao = [a for a in alunos if a['situacao'] == 'Recuperação']
    reprovados = [a for a in alunos if a['situacao'] == 'Reprovado']
    
    # Calcula média geral
    soma_notas = sum(aluno['nota'] for aluno in alunos)
    media_geral = soma_notas / total if total > 0 else 0
    
    print(f"\n📊 Estatísticas:")
    print(f"   Total de alunos: {total}")
    print(f"   Aprovados: {len(aprovados)}")
    print(f"   Em recuperação: {len(recuperacao)}")
    print(f"   Reprovados: {len(reprovados)}")
    print(f"   Média geral: {media_geral:.2f}")
    
    if aprovados:
        print(f"\n🏆 Melhor nota: {max(alunos, key=lambda x: x['nota'])['nota']:.1f}")

def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n" + "="*40)
    print("   SISTEMA DE GERENCIAMENTO DE ALUNOS")
    print("="*40)
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Atualizar aluno")
    print("4. Remover aluno")
    print("5. Gerar relatório")
    print("0. Sair")
    print("="*40)

def main():
    """Função principal que executa o menu interativo"""
    print("🎓 Bem-vindo ao Sistema de Alunos!")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            gerar_relatorio()
        elif opcao == '0':
            print("\n👋 Obrigado por usar o sistema! Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

