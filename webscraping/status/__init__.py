def start(n=''):
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.common.keys import Keys
   from time import sleep
   import json

   driver = webdriver.Chrome()

   url = 'https://www.stats.brawlhalla.fr/'
   driver.get(url)
   sleep(1)

   driver.maximize_window()
   sleep(1)

   cookies = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
   cookies.click()
   sleep(1)

   elemento = driver.find_element(By.XPATH, '//html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/vex-toolbar/div/div/input')
   elemento.click()
   elemento.send_keys(n)
   sleep(1)

   buttonsearch = driver.find_elements(By.CLASS_NAME, 'mat-button-wrapper')[3]
   buttonsearch.click()
   sleep(5)

   buscar_nome = driver.find_elements(By.XPATH, '//html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/main/vex-search/div/div/vex-search-player/div/div/mat-card-content/div/div/div/h2')[0].text
   conferidor = False
   for l in range(0, 101):
      if buscar_nome == f'{n} ({l})':
         conferidor = True
   print(conferidor)
   if conferidor == True:
      player = driver.find_elements(By.XPATH, '//html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/main/vex-search/div/div/vex-search-player/div/div/mat-card-content/div/div/div/h2')[0]
      player.click()
      sleep(2)
   else:
      buscar_nome = driver.find_elements(By.XPATH, '//html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/main/vex-search/div/div/vex-search-player/div/div/mat-card-content/div/div/div/h2')[1].text
      player = driver.find_elements(By.XPATH, '//html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/main/vex-search/div/div/vex-search-player/div/div/mat-card-content/div/div/div/h2')[1]
      player.click()
      sleep(2)

   updateplayer = driver.find_elements(By.CLASS_NAME, 'mat-button-wrapper')[5]
   updateplayer.click()
   sleep(2)

# INFORMAÇÕES COLETADAS:
   
   sleep(2)
   worldranking = driver.find_elements(By.CLASS_NAME, 'mat-line')[1].text

   winrateranked = driver.find_elements(By.CLASS_NAME, 'mat-line')[3].text

   winrateunranked = driver.find_elements(By.CLASS_NAME, 'mat-line')[5].text

   xp = driver.find_elements(By.CLASS_NAME, 'mat-line')[7].text

   clan = driver.find_elements(By.CLASS_NAME, 'mat-line')[9].text
   
   tier = driver.find_elements(By.CLASS_NAME, 'mat-line')[11].text
   
   rating = driver.find_elements(By.CLASS_NAME, 'mat-line')[13].text

   peakrating = driver.find_elements(By.CLASS_NAME, 'mat-line')[15].text

   level = driver.find_elements(By.CLASS_NAME, 'mat-line')[17].text

   region = driver.find_elements(By.CLASS_NAME, 'mat-line')[19].text

   for c in range(1, 6): # Organizar variáveis quando o jogador não tiver "clan".
      if clan == 'Valhallan' or clan == 'Diamond' or clan == f'Platinum {c}' or clan == f'Gold {c}' or clan == f'Silver {c}' or clan == f'Bronze {c}' or clan == f'Tin {c}' or clan == 'Unranked':
         region = level
         level = peakrating
         peakrating = rating
         rating = tier
         tier = clan
         clan = ''
   
   nome = ''
   for c in buscar_nome.split(): # Organizar o nome do jogador.
      if c != f'({level})' and c != 'Diamond' and c != 'Platinum 1' and c != 'Platinum 2' and c != 'Platinum 3' and c != 'Platinum 4' and c != 'Platinum 5' and c != 'Gold 1' and c != 'Gold 2' and c != 'Gold 3' and c != 'Gold 4' and c != 'Gold 5' and c != 'Silver 1' and c != 'Silver 2' and c != 'Silver 3' and c != 'Silver 4' and c != 'Silver 5' and c != 'Bronze 1' and c != 'Bronze 2' and c != 'Bronze 3' and c != 'Bronze 4' and c != 'Bronze 5' and c != 'Tin 1' and c != 'Tin 2' and c != 'Tin 3' and c != 'Tin 4' and c != 'Tin 5' and c != 'Unranked':
         nome += c

   driver.quit()

# DICIONÁRIO TO JSON:

   dicstatus = {
      "Name": nome,
      "World Ranking": worldranking,
      "Winrate Ranked": winrateranked,
      "Winrate Unranked": winrateunranked,
      "XP": xp,
      "Clan": clan,
      "Tier": tier,
      "Rating": rating,
      "Peak Rating": peakrating,
      "Level": level,
      "Region": region
      }
   
   dicstatus_json = json.dumps(dicstatus, indent=4)
   with open('./data/zdata.json', 'w') as arquivo:
      arquivo.write(dicstatus_json)