#!/usr/bin/env python3
"""
Script de configuração inicial do TalentScan
"""
import os
import sys
import subprocess

def install_requirements():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_env_file():
    """Cria arquivo .env se não existir"""
    env_file = ".env"
    if not os.path.exists(env_file):
        print("🔧 Criando arquivo de configuração...")
        with open(env_file, 'w') as f:
            f.write("OPENAI_API_KEY=sua_chave_api_aqui\n")
        print(f"✅ Arquivo {env_file} criado!")
        print("   ⚠️  IMPORTANTE: Edite o arquivo .env e adicione sua chave da API OpenAI")
    else:
        print(f"✅ Arquivo {env_file} já existe")

def create_directories():
    """Cria diretórios necessários"""
    directories = ["curriculos_exemplo", "relatorios"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Diretório criado: {directory}")
        else:
            print(f"📁 Diretório já existe: {directory}")

def check_python_version():
    """Verifica a versão do Python"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 ou superior é necessário")
        print(f"   Versão atual: {sys.version}")
        return False
    else:
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
        return True

def main():
    """Função principal de configuração"""
    print("🚀 TALENTSCAN - CONFIGURAÇÃO INICIAL")
    print("=" * 50)
    
    # Verificar versão do Python
    if not check_python_version():
        sys.exit(1)
    
    # Instalar dependências
    if not install_requirements():
        sys.exit(1)
    
    # Criar arquivo de configuração
    create_env_file()
    
    # Criar diretórios
    create_directories()
    
    print("\n" + "=" * 50)
    print("✅ Configuração concluída!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Edite o arquivo .env e adicione sua chave da API OpenAI")
    print("2. Coloque seus currículos (PDF/DOCX) no diretório 'curriculos_exemplo'")
    print("3. Execute: python talent_scan.py -c curriculos_exemplo/ -p perfil_vaga_exemplo.txt")
    print("\n📚 Para mais informações, consulte o README.md")

if __name__ == "__main__":
    main()
