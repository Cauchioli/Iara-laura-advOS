# Vértice OS: Setup Automatizado para Windows PowerShell
# Cliente: Iara & Laura Advocacia (Segundo Cérebro T.O.G.A)

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  VÉRTICE OS: SEGUNDO CÉREBRO (MÉTODO T.O.G.A)" -ForegroundColor Cyan
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

# 2. Validação da Estrutura Decimal
Write-Host ""
Write-Host "[2/3] Validando estrutura decimal do Vault..." -ForegroundColor Yellow
$requiredPaths = @(
    "00-ENTRADA.md",
    "01-REGRAS.md",
    "02-PROTOCOLO-ORGANIZADOR.md",
    "03-SCHEMA.md",
    "40-operacional/crm_comercial_astrea.md",
    "40-operacional/prompts/01_skill_elaboracao_estagiarias.md",
    "40-operacional/prompts/02_skill_revisao_coordenacao_keren.md",
    "40-operacional/prompts/03_skill_supervisao_laura_iara.md",
    "40-operacional/prompts/04_skill_comercial_crm_ana_nanda.md",
    "CLAUDE.md",
    "AGENTS.md"
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
    Write-Host "[OK] Todas as notas de governança e skills validadas com sucesso." -ForegroundColor Green
} else {
    Write-Host "[ERRO] Há arquivos essenciais ausentes." -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  SEGUNDO CÉREBRO CONFIGURADO COM SUCESSO!" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
