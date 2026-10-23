
tamanho_mb = float(input(" o tamanho do arquivo para download (em MB): "))


velocidade_mbps = float(input(" a velocidade da sua internet (em Mbps): "))


velocidade_mb_por_segundo = velocidade_mbps / 8


tempo_segundos = tamanho_mb / velocidad_mb_por_segundo


tempo_minutos = tempo_segundos / 60


print(f"\nO tempo aproximado de download é de: {tempo_minutos:.2f} minutos.")
