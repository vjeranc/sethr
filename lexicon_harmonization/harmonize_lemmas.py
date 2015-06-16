#!/usr/bin/python
import sys

def compare_msd(corpus,lexicon):
  if corpus.startswith('A'):
    return corpus[:6]+'y'+corpus[6:]==lexicon or corpus[:6]+'n'+corpus[6:]==lexicon
  else:
    return corpus==lexicon

lexicon={}
for line in sys.stdin: # lexicon
  token,lemma,msd=line.decode('utf8').strip().split('\t')
  token=token.lower()
  if token not in lexicon:
    lexicon[token]=set()
  lexicon[token].add((lemma,msd))
print 'lexicon loaded'
for line in open(sys.argv[1]):
  if line.strip()=='':
    pass#sys.stdout.write(line)
  else:
    els=line.decode('utf8').split('\t')
    #if els[4].startswith('Np') and els[2].lower()==els[2]:
    #  els[2]=els[2].title()
    #line='\t'.join(els).encode('utf8')
    token=els[1].lower()
    lemma,msd=els[2],els[4]
    if token not in lexicon:
      #print 'not covered by lexicon:',token.encode('utf8')
      #sys.stdout.write(line)
      continue
    lemmas=set([e[0] for e in lexicon[token]])
    if lemma not in lemmas:
      print 'lemma does not correspond:',lemma.encode('utf8'),lemmas
      potential_lemmas=set()
      for plemma,pmsd in lexicon[token]:
        #print pmsd,msd,compare_msd(pmsd,msd)
        if compare_msd(msd,pmsd):
          potential_lemmas.add(plemma)
      if len(potential_lemmas)>1:
        print repr(lemma),potential_lemmas
      if len(potential_lemmas)==1:
        els=line.split('\t')
      #  sys.stdout.write('\t'.join(els[:2]+[list(potential_lemmas)[0].encode('utf8')]+els[3:]))
      #else:
      #  sys.stdout.write(line)
    #elif (lemma,msd) not in lexicon[token] and (lemma,msd[:6]+'y'+msd[6:]) not in lexicon[token] and (lemma,msd[:6]+'n'+msd[6:]) not in lexicon[token]:
    #  print 'lemma or MSD do not correspond:',token.encode('utf8'),lemma.encode('utf8'),msd,lexicon[token]#(lemma,msd),lexicon[token]
    #else:
    #  sys.stdout.write(line)
    