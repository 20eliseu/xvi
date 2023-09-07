
from app import Ebay
from time import sleep
from pyfiglet import figlet_format
from colorama import init, Fore
import os





#show on screen
if __name__ == '__main__':
	nun_page = 1
	init(autoreset=True)
	while True:
		print(Fore.BLUE + figlet_format('Ebay Prices', font='slant'))
		opc = int(input('[0]- ENTRAR\n[1]- SAIR\nSUA OPÇÂO: '))
		
		if opc is 1:
			print('SAINDO...')
			sleep(2)
			try:
				os.system('clear')
			except:
				os.system('cls')
			break

		elif opc is 0:
			try:
				os.system('clear')
			except:
				os.system('cls')

			print(Fore.BLUE + figlet_format('Ebay Prices', font='slant'))
			produto = input('Nome do produto: ')
			ebay = Ebay(produto)
			pages = ebay.get_pages()
			ebay.show_price_n_product(pages[0])

			change_page = input('IR PARA À PÁGINA SEGUINTE [S/N]: ').lower()

			if change_page == 's':
				try:
					os.system('clear')
				except:
					os.system('cls')

				pages = ebay.get_pages()
				print('O site tem {} páginas'.format(len(pages)))

				ebay.show_price_n_product(pages[int(input(f'DIGITE O Nº DA PÁGINA DE 0 À {len(pages)-1}: '))])

			elif change_page == 'n':
				print('SAINDO...')
				sleep(2)
				try:
					os.system('clear')
				except:
					os.system('cls')

				break

			else:
				print('OPÇÃO INVÁLIDA!')


		elif opc is not 0 or opc is not 2:
			print('OPÇÃO INCORRETA!')
			sleep(2)
			try:
				os.system('clear')
			except:
				os.system('cls')
