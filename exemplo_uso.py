#!/usr/bin/env python3
"""
Exemplo de uso do TalentScan
Este script demonstra como usar a aplicação programaticamente
"""
import os
import sys
from talent_scan import TalentScan

def exemplo_basico():
    """Exemplo básico de uso"""
    print("=== EXEMPLO BÁSICO DE USO DO TALENTSCAN ===")
    
    # Criar instância da aplicação
    app = TalentScan()
    
    # Caminhos dos arquivos (ajuste conforme necessário)
    curriculos_dir = "curriculos_exemplo"
    perfil_file = "perfil_vaga_exemplo.txt"
    output_file = "relatorio_exemplo.xlsx"
    
    # Verificar se os diretórios/arquivos existem
    if not os.path.exists(curriculos_dir):
        print(f"❌ Diretório de currículos não encontrado: {curriculos_dir}")
        print("   Crie o diretório e adicione alguns currículos PDF/DOCX")
        return
    
    if not os.path.exists(perfil_file):
        print(f"❌ Arquivo de perfil não encontrado: {perfil_file}")
        print("   Use o arquivo perfil_vaga_exemplo.txt como modelo")
        return
    
    try:
        # Executar análise
        print(f"📁 Processando currículos em: {curriculos_dir}")
        print(f"📋 Usando perfil: {perfil_file}")
        print(f"📊 Gerando relatório: {output_file}")
        print()
        
        app.run(curriculos_dir, perfil_file, output_file)
        
        print()
        print("✅ Análise concluída com sucesso!")
        print(f"📄 Relatório salvo em: {output_file}")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

def exemplo_avancado():
    """Exemplo avançado com controle individual dos passos"""
    print("\n=== EXEMPLO AVANÇADO DE USO ===")
    
    try:
        # Criar instância da aplicação
        app = TalentScan()
        
        # Carregar perfil da vaga
        perfil_file = "perfil_vaga_exemplo.txt"
        if not os.path.exists(perfil_file):
            print(f"❌ Arquivo de perfil não encontrado: {perfil_file}")
            return
        
        print("📋 Carregando perfil da vaga...")
        job_profile = app.load_job_profile(perfil_file)
        
        print(f"   ✅ {len(job_profile['requeridos'])} atributos requeridos")
        print(f"   ✅ {len(job_profile['desejaveis'])} atributos desejáveis")
        
        # Processar candidatos
        curriculos_dir = "curriculos_exemplo"
        if not os.path.exists(curriculos_dir):
            print(f"❌ Diretório de currículos não encontrado: {curriculos_dir}")
            return
        
        print(f"\n📁 Processando currículos em: {curriculos_dir}")
        candidates_data = app.process_candidates(curriculos_dir, job_profile)
        
        if not candidates_data:
            print("❌ Nenhum candidato foi processado")
            return
        
        print(f"   ✅ {len(candidates_data)} candidatos processados")
        
        # Mostrar estatísticas
        total_score = sum(c.get('pontuacao_total', 0) for c in candidates_data)
        avg_score = total_score / len(candidates_data)
        best_candidate = max(candidates_data, key=lambda x: x.get('pontuacao_total', 0))
        
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   Pontuação média: {avg_score:.2f}")
        print(f"   Melhor candidato: {best_candidate.get('contato', {}).get('nome', 'N/A')} - {best_candidate.get('pontuacao_total', 0)} pontos")
        
        # Gerar relatório
        print(f"\n📄 Gerando relatório Excel...")
        excel_file = app.generate_report(candidates_data, job_profile, "relatorio_avancado.xlsx")
        
        print(f"   ✅ Relatório salvo em: {excel_file}")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

def criar_estrutura_exemplo():
    """Cria estrutura de exemplo para teste"""
    print("\n=== CRIANDO ESTRUTURA DE EXEMPLO ===")
    
    # Criar diretório de exemplo
    curriculos_dir = "curriculos_exemplo"
    if not os.path.exists(curriculos_dir):
        os.makedirs(curriculos_dir)
        print(f"📁 Diretório criado: {curriculos_dir}")
    else:
        print(f"📁 Diretório já existe: {curriculos_dir}")
    
    # Criar arquivo de exemplo de currículo
    exemplo_cv = os.path.join(curriculos_dir, "exemplo_curriculo.txt")
    if not os.path.exists(exemplo_cv):
        with open(exemplo_cv, 'w', encoding='utf-8') as f:
            f.write("""JOÃO SILVA
joao.silva@email.com
(11) 99999-9999

EXPERIÊNCIA PROFISSIONAL
Desenvolvedor Python Senior - Empresa XYZ (2020-2023)
- Desenvolvimento de aplicações web com Django e Flask
- Experiência com PostgreSQL e MySQL
- Implementação de APIs REST
- Uso de Docker para containerização
- Testes automatizados com pytest
- Experiência com AWS (EC2, S3, RDS)
- Inglês fluente (leitura e escrita)
- Trabalho em metodologias ágeis (Scrum)

Desenvolvedor Python - Empresa ABC (2018-2020)
- Desenvolvimento de scripts Python
- Trabalho com Git e controle de versão
- Conhecimento em machine learning básico

FORMAÇÃO
Bacharelado em Ciência da Computação - Universidade XYZ (2014-2018)

CERTIFICAÇÕES
- AWS Certified Developer
- Docker Certified Associate
""")
        print(f"📄 Arquivo de exemplo criado: {exemplo_cv}")
    
    print("\n💡 Para testar com arquivos reais:")
    print(f"   1. Coloque currículos PDF/DOCX em: {curriculos_dir}")
    print("   2. Execute: python exemplo_uso.py")

def main():
    """Função principal do exemplo"""
    print("🚀 TALENTSCAN - EXEMPLO DE USO")
    print("=" * 50)
    
    # Verificar se a API key está configurada
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OPENAI_API_KEY não configurada!")
        print("   Configure a variável de ambiente ou crie um arquivo .env")
        print("   Exemplo: OPENAI_API_KEY=sua_chave_aqui")
        return
    
    # Criar estrutura de exemplo
    criar_estrutura_exemplo()
    
    # Executar exemplos
    exemplo_basico()
    exemplo_avancado()
    
    print("\n" + "=" * 50)
    print("✅ Exemplos concluídos!")
    print("\n📚 Para mais informações, consulte o README.md")

if __name__ == "__main__":
    main()
