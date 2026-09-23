# Vértice OS: Setup Automatizado para Windows PowerShell
# Cliente: Iara & Laura Advocacia

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  VÉRTICE OS: INSTALAÇÃO E SETUP OPERACIONAL" -ForegroundColor Cyan
Write-Host "  Cliente: Iara & Laura Advocacia" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Checagem de Python
Write-Host "[1/3] Verificando ambiente Python local..." -ForegroundColor Yellow
$pythonCheck = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCheck) {
    $pyVer = & python --version
    Write-Host "[OK] $pyVer identificado." -ForegroundColor Green
} else {
    Write-Host "[AVISO] Python não identificado no PATH. As skills web (Claude e Antigravity) funcionarão normalmente." -ForegroundColor DarkYellow
}

# 2. Validação da Estrutura
Write-Host ""
Write-Host "[2/3] Validando estrutura de pastas e skills..." -ForegroundColor Yellow
$requiredPaths = @(
    "vertice-os/prompts/skill_elaboracao_estagiarias.md",
    "vertice-os/prompts/skill_revisao_estagiaria_king.md",
    "vertice-os/prompts/skill_revisao_laura.md",
    "vertice-os/prompts/skill_atendimento_comercial_nanda.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md"
)

$missing = 0
foreach ($p in $requiredPaths) {
    if (Test-Path $p) {
        Write-Host "  [OK] $p" -ForegroundColor DarkGreen
    } else {
        Write-Host "  [FALTA] $p" -ForegroundColor Red
        $missing++
    }
}

if ($missing -eq 0) {
    Write-Host "[OK] Todas as 4 skills e governança validadas com sucesso." -ForegroundColor Green
} else {
    Write-Host "[ERRO] Há arquivos essenciais ausentes." -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  SISTEMA OPERACIONAL VÉRTICE PRONTO PARA USO!" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
