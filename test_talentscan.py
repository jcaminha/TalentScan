#!/usr/bin/env python3
"""
Testes básicos para o TalentScan
"""
import os
import sys
import tempfile
import shutil
from pathlib import Path

# Adicionar o diretório atual ao path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🧪 Testando imports...")
    
    try:
        from document_reader import DocumentReader
        print("   ✅ DocumentReader importado")
    except ImportError as e:
        print(f"   ❌ Erro ao importar DocumentReader: {e}")
        return False
    
    try:
        from openai_analyzer import OpenAIAnalyzer
        print("   ✅ OpenAIAnalyzer importado")
    except ImportError as e:
        print(f"   ❌ Erro ao importar OpenAIAnalyzer: {e}")
        return False
    
    try:
        from excel_generator import ExcelGenerator
        print("   ✅ ExcelGenerator importado")
    except ImportError as e:
        print(f"   ❌ Erro ao importar ExcelGenerator: {e}")
        return False
    
    try:
        from talent_scan import TalentScan
        print("   ✅ TalentScan importado")
    except ImportError as e:
        print(f"   ❌ Erro ao importar TalentScan: {e}")
        return False
    
    return True

def test_document_reader():
    """Testa o leitor de documentos"""
    print("\n🧪 Testando DocumentReader...")
    
    try:
        from document_reader import DocumentReader
        reader = DocumentReader()
        
        # Testar extração de informações de contato
        test_text = """
        João Silva
        joao.silva@email.com
        (11) 99999-9999
        
        Desenvolvedor Python com 5 anos de experiência...
        """
        
        contact_info = reader.extract_contact_info(test_text)
        
        if contact_info['email'] == 'joao.silva@email.com':
            print("   ✅ Extração de email funcionando")
        else:
            print("   ❌ Erro na extração de email")
            return False
        
        if contact_info['telefone'] == '(11) 99999-9999':
            print("   ✅ Extração de telefone funcionando")
        else:
            print("   ❌ Erro na extração de telefone")
            return False
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erro no teste do DocumentReader: {e}")
        return False

def test_excel_generator():
    """Testa o gerador de Excel"""
    print("\n🧪 Testando ExcelGenerator...")
    
    try:
        from excel_generator import ExcelGenerator
        generator = ExcelGenerator()
        
        # Dados de teste
        test_candidates = [
            {
                'contato': {'nome': 'João Silva', 'email': 'joao@email.com'},
                'arquivo': 'joao.pdf',
                'analise': {
                    'pontuacoes': {'Python': 5, 'Django': 4},
                    'resumo': 'Excelente candidato'
                },
                'pontuacao_total': 4.5
            }
        ]
        
        test_profile = {
            'requeridos': ['Python', 'Django'],
            'desejaveis': ['Docker']
        }
        
        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
            output_file = tmp.name
        
        # Gerar relatório
        result_file = generator.create_analysis_report(test_candidates, test_profile, output_file)
        
        if os.path.exists(result_file):
            print("   ✅ Geração de Excel funcionando")
            os.unlink(result_file)  # Limpar arquivo temporário
            return True
        else:
            print("   ❌ Erro na geração de Excel")
            return False
        
    except Exception as e:
        print(f"   ❌ Erro no teste do ExcelGenerator: {e}")
        return False

def test_config():
    """Testa as configurações"""
    print("\n🧪 Testando configurações...")
    
    try:
        from config import Config
        
        # Verificar se as configurações padrão estão corretas
        if Config.OPENAI_MODEL == 'gpt-3.5-turbo':
            print("   ✅ Modelo OpenAI configurado")
        else:
            print("   ❌ Modelo OpenAI incorreto")
            return False
        
        if Config.OPENAI_MAX_TOKENS == 1000:
            print("   ✅ Max tokens configurado")
        else:
            print("   ❌ Max tokens incorreto")
            return False
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erro no teste de configurações: {e}")
        return False

def test_file_structure():
    """Testa se a estrutura de arquivos está correta"""
    print("\n🧪 Testando estrutura de arquivos...")
    
    required_files = [
        'talent_scan.py',
        'document_reader.py',
        'openai_analyzer.py',
        'excel_generator.py',
        'config.py',
        'requirements.txt',
        'perfil_vaga_exemplo.txt',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"   ❌ Arquivos faltando: {', '.join(missing_files)}")
        return False
    else:
        print("   ✅ Todos os arquivos necessários estão presentes")
        return True

def main():
    """Função principal de teste"""
    print("🧪 TALENTSCAN - TESTES BÁSICOS")
    print("=" * 50)
    
    tests = [
        test_file_structure,
        test_imports,
        test_config,
        test_document_reader,
        test_excel_generator
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} testes passaram")
    
    if passed == total:
        print("✅ Todos os testes passaram! O sistema está funcionando corretamente.")
        print("\n🚀 Próximos passos:")
        print("1. Configure sua chave da API OpenAI no arquivo .env")
        print("2. Execute: python setup.py")
        print("3. Teste com: python exemplo_uso.py")
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
