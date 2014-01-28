#!c:/Python27/python.exe
class MainDisplay:
    def execute(self):
        cline = ClustalwCommandline("clustalw4", infile=filename, seqnos="ON")
        child = subprocess.call(str(cline), shell=(sys.platform!="win32"))


    def display(self):
        alignment =AlignIO.read(alignfile, "clustal")
        print "<b> Result Analysis</b>"
        print "<hr width='80%' align='left'><br>"
        print "Input file name : "+filename + "<br>"
        print "Total Number of Records: %i" % len(alignment)
        handle=open(alignfile,'rU')
        for seql in SeqIO.parse(handle, "clustal"):
            seq_length = len(seql.seq)
        print "<br>"
        print "Total number of Sequences: %i" % seq_length
        print "<br><br><br>"
        print "<b>Alignment Result</b><hr width='80%' align='left'></br>"
        print "<pre>"
        f = open(alignfile)
        for line in f.readlines():
            print line
        print "</pre><br>"
        print "<b>Guide Tree Result</b><hr width='80%' align='left'></br>"
        print "<pre>"
        f = open(name + '.dnd')
        for line in f.readlines():
            print line
        print "</pre>"


    def tree(self):
        infile=name+'.dnd'
        outfile=name+'.xml'
        treexml=name+'.xml'
        Phylo.convert(infile, "newick", outfile, "phyloxml")
        tree=Phylo.read(treexml,"phyloxml")
        print "<b>Phylogram Tree </b><hr width='80%' align='left'></br>"
        print "<pre>"
        Phylo.draw_ascii(tree)
        print "</pre>"

if __name__ == '__main__':
    """ This is inline function from where script starts to run """
    """ Importing all the Python & Biophython modules for the application"""
    import sys, subprocess, os, tempfile
    from Bio import Phylo
    from Bio import AlignIO
    from Bio import SeqIO
    from Bio.Align.Applications import ClustalwCommandline
    import cgi, cgitb
    cgitb.enable()
    print 'Content-type: text/html\n\n'
    from index import HtmlTemplate
    form=cgi.FieldStorage()
    i=(form["dfile"].value)
    j=(form["sequence"].value)

    if (i!="" and j=="" ):
        filename=(form["dfile"].filename)
        (name, ext) = os.path.splitext(filename)
        alignfile=name + '.aln'


    elif(j!="" and i==""):
        def unique_file(file_name):
            dirname, filename = os.path.split(file_name)
            prefix, suffix = os.path.splitext(filename)
            fd, filename = tempfile.mkstemp(suffix, prefix+"_", dirname)
            return os.fdopen(fd), filename

        f, filename=unique_file('input.fasta')
        file = open(filename, 'w')
        value=str(j)
        file.write(value)
        file.close()
        (name, ext) = os.path.splitext(filename)
        alignfile=name + '.aln'

    t = HtmlTemplate()
    t.Header()
    t.Body()
    print "<br>"
    print "Go To : "
    print "<a href='index.py'>"
    print "Home</a><br><br>"
    o=MainDisplay()
    o.execute()
    o.display()
    o.tree()
    t.Footer()