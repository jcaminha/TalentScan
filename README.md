# TalentScan - Sistema de Análise de Currículos

Sistema automatizado para análise de currículos em PDF e DOCX usando inteligência artificial da OpenAI. O sistema compara os currículos com um perfil de vaga e gera uma planilha Excel com pontuações e resumos.

## Funcionalidades

- ✅ Leitura de currículos em PDF e DOCX
- ✅ Análise automática usando API OpenAI
- ✅ Pontuação de 1 a 5 para cada atributo da vaga
- ✅ Geração de planilha Excel com resumos
- ✅ Extração automática de informações de contato
- ✅ Relatório de resumo com estatísticas

## Instalação

1. Clone ou baixe os arquivos do projeto
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure sua chave da API OpenAI:

```bash
cp config.env.example .env
```

Edite o arquivo `.env` e adicione sua chave da API:

```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como Usar

### 1. Preparar o Perfil da Vaga

Crie um arquivo de texto com o perfil da vaga. Use o arquivo `perfil_vaga_exemplo.txt` como modelo:

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

### 2. Organizar os Currículos

Coloque todos os currículos (PDF e DOCX) em um diretório. Exemplo:

```
curriculos/
├── joao_silva.pdf
├── maria_santos.docx
├── pedro_oliveira.pdf
└── ana_costa.docx
```

### 3. Executar a Análise

Execute o comando principal:

```bash
python talent_scan.py -c curriculos/ -p perfil_vaga.txt
```

Ou com nome personalizado para o arquivo de saída:

```bash
python talent_scan.py -c curriculos/ -p perfil_vaga.txt -o relatorio_analise.xlsx
```

### 4. Visualizar Resultados

O sistema gerará um arquivo Excel com:

- **Planilha "Análise de Currículos"**: Dados completos de cada candidato
- **Planilha "Resumo"**: Estatísticas gerais e ranking

## Estrutura do Relatório Excel

### Planilha Principal
- Nome do candidato
- E-mail
- Telefone
- Arquivo original
- Pontuação total
- Nota individual para cada atributo (1-5)
- Resumo das qualidades

### Planilha de Resumo
- Estatísticas gerais
- Top 5 candidatos
- Média de pontuação por atributo

## Formato de Pontuação

- **5 pontos**: Muito aderente ao perfil
- **4 pontos**: Aderente ao perfil
- **3 pontos**: Parcialmente aderente
- **2 pontos**: Pouco aderente
- **1 ponto**: Não aderente

## Exemplos de Uso

### Análise Básica
```bash
python talent_scan.py -c curriculos/ -p perfil_vaga.txt
```

### Análise com Arquivo Personalizado
```bash
python talent_scan.py -c curriculos/ -p perfil_vaga.txt -o relatorio_final.xlsx
```

### Modo Verboso (mais detalhes)
```bash
python talent_scan.py -c curriculos/ -p perfil_vaga.txt --verbose
```

## Arquivos do Projeto

- `talent_scan.py` - Aplicação principal
- `document_reader.py` - Leitura de PDF e DOCX
- `openai_analyzer.py` - Análise com IA
- `excel_generator.py` - Geração de relatórios
- `requirements.txt` - Dependências
- `perfil_vaga_exemplo.txt` - Exemplo de perfil

## Logs

O sistema gera logs em `talent_scan.log` para acompanhar o processamento e identificar possíveis problemas.

## Limitações

- Requer conexão com internet para usar a API OpenAI
- Limite de tokens da API OpenAI (texto do currículo é truncado se muito longo)
- Suporta apenas PDF e DOCX
- Extração de informações de contato pode não ser 100% precisa

## Solução de Problemas

### Erro de API Key
```
Erro ao inicializar analisador OpenAI: OPENAI_API_KEY não encontrada
```
**Solução**: Configure a variável de ambiente `OPENAI_API_KEY` no arquivo `.env`

### Nenhum documento encontrado
```
Nenhum documento encontrado no diretório
```
**Solução**: Verifique se o diretório contém arquivos PDF ou DOCX

### Erro de análise
```
Erro na análise do currículo
```
**Solução**: Verifique a conexão com internet e se a API key está válida

## Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
