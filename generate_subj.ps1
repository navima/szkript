$n = Read-Host
$s = 'Python HF, Cs 10, ' + (Get-Date ((Get-Date '2021-02-17').AddDays(7 * $n)) -Format "yyyy-MM-dd")
Set-Clipboard $s