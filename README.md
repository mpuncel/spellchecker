spellchecker
============

This project was inspired by http://www.twitch.tv/problems/spellcheck.

Running spellchecker.py will prompt the user for an input string on each iteration of 
an infinite loop.  It will attempt to correct the spelling of the input string to
an english word in the 'words' file (borrowed from /usr/share/dict/words on Unix based
machines).  The rules it applies to correct spelling are detailed in the url above,
but in brief: they are
	1: Case (upper/lower) errors:
	2: Repeated letters: i.e. "jjoobbb" => "job"
	3: Incorrect vowels: "weke" => "wake"

If no word can be found using a combination of these rules, it will print "NO SUGGESTION".

This is most certainly not an optimized autocorrection algorithm, as there is no guarantee
regarding the "error distance" between the input word and the output word. One example of
the lack of such a guarantee is that the word "sheeeeep" gets corrected to "shop" by this
implementation. This is due to the fact that the algorithm works by stripping out duplicate
letters, and ignores vowels.  Technically the word "shop" can turn into "sheeeeep" by 
mistyping the "o" as an "e", and then repeating it many times, i.e. using rule 3 followed
by multiple instances of rule 2.

wordgenerator.py uses the list of words in 'words' and probabilistically makes errors to it
following the three rules above and prints them while running off of an infinite loop.  
This can be used as a sort of test for spellchecker.py by running:
	python wordgenerator.py | python spellchecker.py.

No instances of "NO SUGGESTION" should occur, because the error rules were followed in
generating each word input to spellchecker.py.
