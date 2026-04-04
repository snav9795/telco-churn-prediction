# Publish only churn-prediction/ to the "public" remote (grading repo).
# Prereqs: run from capstone workspace root; remote "public" must exist (see docs/setup/Two_Repos_Git.md).
# Usage: .\scripts\Publish-PublicChurnRepo.ps1

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

git rev-parse --git-dir *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Not a git repository. Run git init at: $root"
}

$branch = "churn-public"
git subtree split --prefix=churn-prediction -b $branch
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

git push public "${branch}:main" --force
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

git branch -d $branch

Write-Host "Public repo updated: churn-prediction/ is now at remote 'public' branch main."
