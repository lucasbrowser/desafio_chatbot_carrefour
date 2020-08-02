import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, name):
        try:
            memory = open(name+'.json','r')
        except FileNotFoundError:
            memory = open(name+'.json','w')
            memory.write('[["Lucas","João"], {"oi": "Seja Bem vindo ao Banco Carrefour,\nQual é o seu nome?"}]')
            memory.close()
            memory = open(name+'.json','r')
        self.name = name
        self.knowns, self.phrases = json.load(memory)
        memory.close()
        self.history = [None]
        

    def listen(self, phrase=None):
        if phrase == None:
            phrase = input('>: ')
        phrase = str(phrase)
        if 'executa' in phrase:
            return phrase
        phrase = phrase.lower()
        phrase = phrase.replace('é','eh')
        return phrase

    def analyze(self,phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        lastphrase = self.history[-1]
        if lastphrase == 'Seja Bem vindo ao Banco Carrefour,\nQual é o seu nome?':
            name = self.catchName(phrase)
            phrase = self.answerName(name)
            return phrase
        try:
            resp = str(eval(phrase))
            return resp
        except:
            pass
        return 'Não entendi a sua resposta.\nPor favor repita a resposta ou digite /menu para opções.'
            
    def catchName(self,name):
        if 'o meu nome eh ' in name:
            name = name[14:]

        name = name.title()
        return name
    
    def recordMemory(self):
        memory = open(self.name+'.json','w')
        json.dump([self.knowns, self.phrases],memory)
        memory.close()

    def answerName(self,name):
        if name in self.knowns:
            phrase = 'Olá {}, em que podemos lhe ajudar? \nDigite /menu para opções '.format(name)
        else:
            phrase = 'Olá {}, em que podemos lhe ajudar? \nDigite /menu para opções '.format(name)
            self.knowns.append(name)
            self.recordMemory()

        return phrase

    def talk(self,phrase):
        if 'executa ' in phrase:
            plataf = sys.platform
            command = phrase.replace('executa ','')
            if 'win' in plataf:
                os.startfile(command)
            if 'linux' in plataf:
                try:
                    s.Popen(command)
                except FileNotFoundError:
                    s.Popen(['xdg-open',command])
        else:
            print(phrase)
        self.history.append(phrase)
