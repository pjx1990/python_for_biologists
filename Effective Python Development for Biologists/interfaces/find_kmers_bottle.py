from __future__ import division
import collections
from bottle import route, run, post, request

@route('/input')
def kmers_form():
    return '''
        <form action="/output" method="post">
            DNA: <input name="dna" type="text" /><br/>
            kmer length: <input name="kmer_length" type="text" /><br/>
            threshold: <input name="threshold" type="text" /><br/>
            <input value="Analyse" type="submit" />
        </form>
    '''

@post('/output') 
def count_kmers():
    # get the form parameters
    dna = request.forms.get('dna')
    kmer_length = int(request.forms.get('kmer_length'))
    threshold = float(request.forms.get('threshold'))

    # construct the result
    result = ""
    all_kmers = []

    for start in range(len(dna) - kmer_length + 1):
        kmer = dna[start:start+kmer_length]
        all_kmers.append(kmer)

    kmer_counts = collections.Counter(all_kmers)
    total_count = len(all_kmers)


    for kmer, count in kmer_counts.items():
        fraction = count / total_count
        if fraction > threshold:
            line = kmer + "," + str(count) + "," + str(fraction) + "<br/>"
            result = result + line
    return result

run(host='localhost', port=8080, debug=True)
