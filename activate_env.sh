#!/bin/bash
# Script para ativar o ambiente virtual do TalentScan

echo "🚀 Ativando ambiente virtual do TalentScan..."

if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✅ Ambiente virtual ativado!"
    echo "💡 Para desativar, execute: deactivate"
    echo "💡 Para executar o TalentScan, use: python talent_scan.py --help"
else
    echo "❌ Ambiente virtual não encontrado!"
    echo "💡 Execute primeiro: python3 -m venv venv"
    echo "💡 Depois: pip install -r requirements.txt"
fi
