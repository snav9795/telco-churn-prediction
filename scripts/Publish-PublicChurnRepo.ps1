# Publish only churn-prediction/ to the "public" remote (grading repo).
#
# Usage (from capstone workspace root):
#   .\scripts\Publish-PublicChurnRepo.ps1
#   .\scripts\Publish-PublicChurnRepo.ps1 -CreatePublicRepo   # runs gh repo create first (needs gh + gh auth login)
#
# Prereqs: git remote "public" points at the empty public GitHub repo (see docs/setup/Two_Repos_Git.md).

param(
    [switch] $CreatePublicRepo
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

function Resolve-Gh {
    $cmd = Get-Command gh -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $candidates = @(
        "${env:ProgramFiles}\GitHub CLI\gh.exe",
        "${env:LocalAppData}\Programs\GitHub CLI\gh.exe"
    )
    foreach ($p in $candidates) {
        if (Test-Path $p) { return $p }
    }
    return $null
}

git rev-parse --git-dir *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Not a git repository. Run git init at: $root"
}

if ($CreatePublicRepo) {
    $ghExe = Resolve-Gh
    if (-not $ghExe) {
        Write-Error "GitHub CLI (gh) not found. Install it, restart the terminal, run 'gh auth login', then retry."
    }
    Write-Host "Creating public repo on GitHub (if the name is taken, choose another and: git remote set-url public <url>)..."
    & $ghExe repo create telco-churn-prediction --public --description "CS5998 capstone: telco churn (public grading repo)"
    if ($LASTEXITCODE -ne 0) {
        Write-Error "gh repo create failed. Create an empty public repo manually, set 'public' remote, then rerun without -CreatePublicRepo."
    }
}

$branch = "churn-public"
git branch -D $branch 2>$null | Out-Null
git subtree split --prefix=churn-prediction -b $branch
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

git push public "${branch}:main" --force
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Push failed. If the error is 'Repository not found', create the public repo first:"
    Write-Host "  gh repo create telco-churn-prediction --public --description ""CS5998 grading"""
    Write-Host "Or create it on github.com/new, then: git remote set-url public https://github.com/YOUR_USER/REPO.git"
    exit $LASTEXITCODE
}

git branch -d $branch

Write-Host "Public repo updated: churn-prediction/ is now at remote 'public' branch main."
