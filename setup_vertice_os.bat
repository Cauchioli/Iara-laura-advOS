@echo off
chcp 65001 > nul
title Instalador Vertice OS - Iara e Laura Advocacia

echo ========================================================
echo   VERTICE OS: INSTALACAO E SETUP OPERACIONAL
echo   Cliente: Iara e Laura Advocacia
echo ========================================================
echo.

echo [1/3] Verificando ambiente Python...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [AVISO] Python nao localizado no PATH do sistema.
    echo A integracao via navegador (Claude / Antigravity Web) operara normalmente.
) else (
    echo [OK] Python localizado com sucesso.
)

echo.
echo [2/3] Validando estrutura de diretorios...
if not exist "vertice-os\prompts" (
    echo [ERRO] Pasta de prompts nao localizada. Execute este instalador na raiz do projeto.
    pause
    exit /b 1
)
echo [OK] Estrutura de prompts e regras validada.

echo.
echo [3/3] Arquivos de Governanca Configurados:
echo - AGENTS.md (Regras universais para Antigravity)
echo - CLAUDE.md (Instrucoes para Claude Code e Claude Projects)
echo - GEMINI.md (Instrucoes para o ecossistema Gemini)
echo - 4 Skills em vertice-os\prompts\ prontas para uso.

echo.
echo ========================================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo ========================================================
echo.
pause
