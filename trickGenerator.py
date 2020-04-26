import tracery
from tracery.modifiers import base_english

tricks = {
    "origin":[
		"#output#"
	],

	"output":[
		"#desc1.capitalize# #desc2# #desc3# #trick#",
		"#desc3.capitalize# #trick# in to #desc1.a# #desc2# #trick#",
		"#desc1.capitalize# #trick# #trick#",
		"#desc1.capitalize# #desc2# #desc3# #trick# #suffix#",
		"#starter.capitalize# off the #ramp# and do #desc1.a# #trick# #starter#ing on to a nearby #obstacle# to do #desc3.a# #trick#"
	],


	"desc1":[
		"gnarly","radical","tubular","fabulous","sweet","sick","dope","eXtreme","fakie","reverse","cRaZy"
	],

	"trick":[
		"kickflip","McTwist","revert","shuvit","tre-flip","wyrmride","flamingo","funk flip","christ-air","ollie","boneless","hardflip","bonerflip","timewarp"
	],

	"desc2":[
	"1080°","900°","720°","360°","180°","railgrind","69°","420°"
	],

	"desc3":[
		"pro-bono","double","triple","quadruple","octuple","big dick","extreme","upside-down"
	],

	"suffix":[
		"with a li'l sauce","deluxe supreme","with fries","trainwreck","with a SWEEET landing"
	],

	"ramp":[
		"vert","mini ramp","child’s ramp","half-pipe"
	],

	"obstacle":[
		"rock","kiddie pool","fence","trampoline","snowbank","golf car"
	],

	"starter": [
		"pop","hop","jump","launch","swivel","bomb"
	]
}

def generate():
    grammar = tracery.Grammar(tricks)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")