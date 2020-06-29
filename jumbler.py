import random

def make_paragraphs(num):
	with open("transcript.txt") as transcript:
		data = transcript.readlines()
		hot_mess = []
		for x in range(num):
			lines = []
			while len(lines) < 6:
				line = random.choice(data).rstrip()
				lines.append(line)
			paragraph = " ".join(lines)
			hot_mess.append(paragraph)
		return "\n".join(hot_mess)