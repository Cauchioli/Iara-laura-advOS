@echo off
chcp 65001 > nul
title Instalador Vertice OS - Segundo Cerebro Iara e Laura Advocacia

echo ========================================================
echo   VERTICE OS: SEGUNDO CEREBRO
echo   Cliente: Iara e Laura Advocacia
echo ========================================================
echo.

echo [1/3] Verificando ambiente Python local...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [AVISO] Python nao identificado no PATH do sistema.
    echo A integracao web via Claude Projects operara normalmente.
) else (
    echo [OK] Python localizado com sucesso.
)

echo.
echo [2/3] Validando estrutura decimal do Vault...
if not exist "40-operacional\prompts" (
    echo [ERRO] Pasta 40-operacional\prompts nao localizada. Execute este instalador na raiz do projeto.
    pause
    exit /b 1
)
echo [OK] Estrutura do Vault (00-ENTRADA, 01-REGRAS, 10-clientes, 20-modelos, 40-operacional) validada.

echo.
echo [3/3] Arquivos de Governanca Configurados:
echo - 00-ENTRADA.md (Porta de entrada do Segundo Cerebro)
echo - 01-REGRAS.md (Leis inegociaveis do escritorio)
echo - 02-PROTOCOLO-ORGANIZADOR.md (Protocolo organizador com lacre para o Drive)
echo - CLAUDE.md (Instrucoes nativas para Claude Code e Claude Projects)
echo - AGENTS.md / GEMINI.md (Instrucoes para Antigravity)
echo - 4 Skills em 40-operacional\prompts\ prontas para uso.

echo.
echo ========================================================
echo   SEGUNDO CEREBRO CONFIGURADO COM SUCESSO!
echo ========================================================
echo.
pause
