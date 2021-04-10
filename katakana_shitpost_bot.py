import urllib.request
from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"

MAX = 10
example = ['this','is','max','ten','words','in','one','url','call','max','this','is','max','ten','words','in','one','url','call','max']
example2 = ['this','is','max']

class katakana_meme_bot(object):


	def adjust_URL_call(self, ex):
		base_url = f'https://www.sljfaq.org/cgi/e2k.cgi?word='

		for words in ex:
			append_argument = words + '%' + '20'
			base_url = base_url + append_argument
			print(base_url)

		return base_url

	def make_URL_call(self, ex, current_list):

		if len(ex) != 10:
			URL = self.adjust_URL_call(ex)
		else:
			URL = f'https://www.sljfaq.org/cgi/e2k.cgi?word={ex[0]}%20{ex[1]}%20{ex[2]}%20{ex[3]}%20{ex[4]}%20{ex[5]}%20{ex[6]}%20{ex[7]}%20{ex[8]}%20{ex[9]}'

		opener = AppURLopener()
		response = opener.open(URL)

		soup = BeautifulSoup(response.read())

		tags = soup.find_all('td', {'class':'j_pron_spell'})

		for thats_cap in tags:
			current_list.append(', '.join(thats_cap.contents))

		return current_list


	def Activate_shitpost(self, provided_string):
		buffer_list = []
		all_words = []
		for traverse_string in provided_string:
			buffer_list.append(traverse_string)

			if len(buffer_list) == MAX:
				all_words = self.make_URL_call(buffer_list, all_words)

				buffer_list = []

		#if buffer list has any remaining words, we'll append the last of it
		if buffer_list:
			all_words = self.make_URL_call(buffer_list, all_words)

		return all_words


# def main():
# 	user_input = input(f'Enter The Shitpost:')
# 	final_string = ""

# 	li = list(user_input.split(" "))

# 	final_string = Activate_shitpost(li)

# 	print(' '.join(final_string))
# 	print(f'length of the final string is :{len(final_string)}')


# if __name__ == '__main__':
# 	main()



