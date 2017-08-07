### eliza.py, ELIZA in Python

This is a little version of ELIZA, a famous natural-language AI demo from the 1960s,
packaged up as a Python module.  It's all smoke and mirrors; the program doesn't
have a clue what it is saying and it's not difficult to catch it out, but it's amusing
and it means your chatbot always has something to say.

The eliza.py module includes an interactive mode, so you can get a feel for how it performs. Just grab the code
and `python eliza.py`.  To use the it from with in your own script do something like

``` python
import eliza

therapist = eliza.eliza()
while some_condition:
  #get input from somewhere
  reply = therapist.respond(input)
  #send reply somewhere
```

## References
J. Weizenbaum, [ELIZA - A Computer Program For the Study of Natural Language Communication Between Man And Machine](http://www.cse.buffalo.edu/~rapaport/572/S02/weizenbaum.eliza.1966.pdf) _Communications of the ACM, Vol 9, No 1, January 1966_

## License

Original code written by Joe Strout, with some updates by Jeff Epler.  Converted to a module and updated for Python 3 by Jez Higgins.

Copyright (c) 2002-2017 [JezUK Ltd](http://www.jezuk.co.uk), Joe Strout, Jeff Epler

Licensed under the terms of the MIT License.
