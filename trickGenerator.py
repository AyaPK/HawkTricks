import random
import tracery
from tracery.modifiers import base_english

starters = ["pop", "hop", "jump", "launch", "swivel", "bomb","leap","ride"]

def starter():
	return ing(random.choice(starters))

def ing(w):
	if w[-1] in "dgnpm" and w[-2] in "aeiou":
		if w[-3] in "aeiou":
			return w+"ing"
		else:
			return w+w[-1]+"ing"
	elif w[-1] == "e":
		return w[0:-1]+"ing"
	else:
		return w+"ing"

tricks = {
    "origin":[
		"#output#"
	],

	"output":[
		"#desc1.capitalize# #desc2# #desc3# #trick#",
		"#desc3.capitalize# #trick# in to #desc1.a# #desc2# #trick#",
		"#desc1.capitalize# #trick# #trick#",
		"#desc1.capitalize# #desc2# #desc3# #trick# #suffix#",
		"#starter.capitalize# off the #ramp# and do #desc1.a# #trick#, "+str(starter())+" on to a nearby #obstacle# to do #desc3.a# #trick#"
	],


	"desc1":[
		"gnarly","radical","tubular","fabulous","sweet","sick","dope","eXtreme","fakie","reverse","cRaZy","ridiculous","badass","nollie"
	],

	"trick":[
		"kickflip","McTwist","revert","shuvit","tre-flip","wyrmride","flamingo","funk flip","christ-air","ollie","boneless","hardflip","bonerflip","timewarp","heelflip"
	],

	"desc2":[
	"1080°","900°","720°","360°","180°","railgrind","69°","420°"
	],

	"desc3":[
		"pro-bono","double","triple","quadruple","octuple","big dick","extreme","upside-down","multiple","twisted","nollie"
	],

	"suffix":[
		"with a li'l sauce","deluxe supreme","with fries","trainwreck","with a SWEEET landing"
	],

	"ramp":[
		"vert","mini ramp","child’s ramp","half-pipe","quarter pipe","flat ramp","bowl","spine","stairway"
	],

	"obstacle":[
		"rock","kiddie pool","fence","trampoline","snowbank","golf cart"
	],

	"starter": starters
}

def generate():
    grammar = tracery.Grammar(tricks)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")