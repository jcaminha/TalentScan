# TalentScan - Guia de Instalação

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Chave da API OpenAI
- Sistema operacional: Linux, macOS ou Windows

## 🚀 Instalação Passo a Passo

### 1. Verificar Python
```bash
python3 --version
# Deve mostrar Python 3.7 ou superior
```

### 2. Clonar/Baixar o Projeto
```bash
# Se usando git:
git clone <url-do-repositorio>
cd TalentScan

# Ou baixe e extraia os arquivos
```

### 3. Criar Ambiente Virtual
```bash
python3 -m venv venv
```

### 4. Ativar Ambiente Virtual
```bash
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 5. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 6. Configurar API OpenAI
```bash
# Copiar arquivo de exemplo
cp config.env.example .env

# Editar arquivo .env
nano .env  # ou use seu editor preferido
```

Adicione sua chave da API:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

### 7. Testar Instalação
```bash
python test_talentscan.py
```

Se todos os testes passarem, a instalação foi bem-sucedida!

## 🔧 Configuração Rápida

### Script de Ativação
```bash
# Tornar executável (apenas uma vez)
chmod +x activate_env.sh

# Ativar ambiente
source activate_env.sh
```

### Configuração Automática
```bash
python setup.py
```

## 📁 Estrutura Após Instalação

```
TalentScan/
├── venv/                 # Ambiente virtual
├── .env                  # Configurações (criar)
├── curriculos_exemplo/   # Diretório para testes
├── talent_scan.py        # Aplicação principal
├── requirements.txt      # Dependências
└── ... (outros arquivos)
```

## 🧪 Verificação da Instalação

### Teste Básico
```bash
source venv/bin/activate
python talent_scan.py --help
```

### Teste Completo
```bash
source venv/bin/activate
python test_talentscan.py
```

### Teste com Exemplo
```bash
source venv/bin/activate
python exemplo_uso.py
```

## 🚨 Solução de Problemas

### Erro: "python: comando não encontrado"
```bash
# Use python3 em vez de python
python3 --version
python3 -m venv venv
```

### Erro: "externally-managed-environment"
```bash
# Use ambiente virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "No module named 'PyPDF2'"
```bash
# Reinstalar dependências
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "OPENAI_API_KEY não encontrada"
```bash
# Verificar arquivo .env
cat .env
# Deve conter: OPENAI_API_KEY=sua_chave_aqui
```

## 🔑 Obter Chave da API OpenAI

1. Acesse: https://platform.openai.com/
2. Faça login ou crie uma conta
3. Vá para "API Keys"
4. Clique em "Create new secret key"
5. Copie a chave e adicione no arquivo `.env`

## 📞 Suporte

Se encontrar problemas:

1. Verifique se seguiu todos os passos
2. Execute os testes: `python test_talentscan.py`
3. Consulte o `README.md` para mais detalhes
4. Verifique os logs em `talent_scan.log`

## ✅ Instalação Concluída

Após a instalação bem-sucedida, você pode:

1. **Usar a aplicação principal:**
   ```bash
   python talent_scan.py -c curriculos/ -p perfil_vaga.txt
   ```

2. **Executar exemplos:**
   ```bash
   python exemplo_uso.py
   ```

3. **Consultar documentação:**
   - `README.md` - Documentação completa
   - `INSTRUCOES_RAPIDAS.md` - Guia rápido
   - `RESUMO_PROJETO.md` - Resumo do projeto
