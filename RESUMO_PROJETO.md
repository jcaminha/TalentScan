# TalentScan - Resumo do Projeto

## 🎯 Objetivo
Sistema automatizado para análise de currículos em PDF e DOCX usando inteligência artificial da OpenAI, comparando com perfis de vaga e gerando relatórios Excel com pontuações e resumos.

## ✅ Funcionalidades Implementadas

### 1. Leitura de Documentos
- ✅ Suporte a arquivos PDF e DOCX
- ✅ Extração automática de texto
- ✅ Identificação de informações de contato (nome, email, telefone)
- ✅ Processamento em lote de diretórios

### 2. Análise com IA
- ✅ Integração com API OpenAI (GPT-3.5-turbo)
- ✅ Análise automática de currículos
- ✅ Pontuação de 1 a 5 para cada atributo
- ✅ Geração de resumos personalizados
- ✅ Sistema de pesos (atributos requeridos vs desejáveis)

### 3. Geração de Relatórios
- ✅ Planilha Excel com dados completos
- ✅ Planilha de resumo com estatísticas
- ✅ Formatação colorida baseada em pontuações
- ✅ Ranking de candidatos
- ✅ Filtros e congelamento de linhas

### 4. Interface e Usabilidade
- ✅ Interface de linha de comando intuitiva
- ✅ Modo verboso para debugging
- ✅ Logs detalhados
- ✅ Tratamento de erros robusto
- ✅ Validação de configurações

## 📁 Estrutura do Projeto

```
TalentScan/
├── talent_scan.py          # Aplicação principal
├── document_reader.py      # Leitura de PDF/DOCX
├── openai_analyzer.py      # Análise com IA
├── excel_generator.py      # Geração de relatórios
├── config.py              # Configurações
├── requirements.txt       # Dependências Python
├── perfil_vaga_exemplo.txt # Exemplo de perfil
├── activate_env.sh        # Script de ativação
├── setup.py              # Configuração inicial
├── exemplo_uso.py        # Exemplo de uso
├── test_talentscan.py    # Testes automatizados
├── README.md             # Documentação completa
├── INSTRUCOES_RAPIDAS.md # Guia rápido
├── config.env.example    # Exemplo de configuração
└── venv/                 # Ambiente virtual Python
```

## 🚀 Como Usar

### Configuração Inicial
```bash
# 1. Ativar ambiente virtual
source activate_env.sh

# 2. Configurar API OpenAI
cp config.env.example .env
# Editar .env e adicionar OPENAI_API_KEY=sua_chave

# 3. Executar análise
python talent_scan.py -c curriculos/ -p perfil_vaga.txt
```

### Exemplo de Perfil de Vaga
```
PERFIL DA VAGA - DESENVOLVEDOR PYTHON SENIOR

ATRIBUTOS REQUERIDOS:
- Experiência em Python (3+ anos)
- Conhecimento em frameworks web (Django/Flask)
- Experiência com bancos de dados (PostgreSQL, MySQL)
- Conhecimento em Git e controle de versão
- Experiência com APIs REST
- Conhecimento em Docker
- Experiência com testes automatizados
- Conhecimento em cloud (AWS, Azure, GCP)
- Inglês técnico (leitura e escrita)
- Experiência em metodologias ágeis

ATRIBUTOS DESEJÁVEIS:
- Conhecimento em machine learning
- Experiência com microserviços
- Conhecimento em Kubernetes
- Experiência com CI/CD
- Certificações em cloud
```

## 📊 Resultado Final

O sistema gera um arquivo Excel com:

### Planilha "Análise de Currículos"
- Nome do candidato
- E-mail
- Telefone
- Arquivo original
- Pontuação total
- Nota individual para cada atributo (1-5)
- Resumo das qualidades

### Planilha "Resumo"
- Estatísticas gerais
- Top 5 candidatos
- Média de pontuação por atributo

## 🔧 Tecnologias Utilizadas

- **Python 3.7+**: Linguagem principal
- **OpenAI API**: Análise de currículos com IA
- **PyPDF2**: Leitura de arquivos PDF
- **python-docx**: Leitura de arquivos DOCX
- **pandas**: Manipulação de dados
- **openpyxl**: Geração de planilhas Excel
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 🧪 Testes

O projeto inclui testes automatizados que verificam:
- ✅ Importação de todos os módulos
- ✅ Funcionamento do leitor de documentos
- ✅ Geração de planilhas Excel
- ✅ Configurações do sistema
- ✅ Estrutura de arquivos

Execute os testes com:
```bash
source venv/bin/activate
python test_talentscan.py
```

## 📈 Melhorias Futuras

- [ ] Interface web com Flask/Django
- [ ] Suporte a mais formatos de arquivo
- [ ] Análise de compatibilidade com diferentes modelos de IA
- [ ] Sistema de templates para perfis de vaga
- [ ] Integração com sistemas de RH
- [ ] Análise de sentimento nos currículos
- [ ] Exportação para outros formatos (PDF, CSV)

## 🎉 Conclusão

O TalentScan é um sistema completo e funcional para análise automatizada de currículos, oferecendo:

- **Automação**: Processamento em lote de currículos
- **Inteligência**: Análise com IA para pontuação objetiva
- **Usabilidade**: Interface simples e documentação completa
- **Flexibilidade**: Configurável para diferentes perfis de vaga
- **Relatórios**: Saída em Excel com formatação profissional

O sistema está pronto para uso em produção e pode ser facilmente adaptado para diferentes necessidades de análise de currículos.
