#!c:/Python27/python.exe
""" Importing python interpreter to parse python script on the browser"""

class HtmlTemplate:
    """ Class HtmlTemplate has got Header(),Body(), Form(), Footer() and CloseHtml() functions. """

    def Header(self):
        """ Definition of Header() and self argument pointing to itself."""

        print '''
        <html><head>

        <title>Multiple Sequence alignment</title>
        <link rel="SHORTCUT ICON" href="images/bookmark.ico">
        </head>
        '''
    def Body(self):
        """ Definition of Body() and self argument pointing to itself."""

        print '''
        <body>
        <p align="center"><img src='images/header.jpg'></img></p>
        <p align="right"><a href="Documentation/_build/html/index.html" class="link"> <b>Documentation </b></a></p>
        '''
    def Form(self):
        """ Definition of Form() and self argument pointing to itself."""

        print '''
        <script language=\"javascript\" type=\"text/javascript\">

        function validate(form)
        {
        if ((form.dfile.value.length==0) && (form.sequence.value.length==0))
        {
        alert("Upload fasta file or paste sequence");
        return false;
        }
        else if ((form.dfile.value.length>0) && (form.sequence.value.length>0))
        {
        alert("Only one option is available");
        return false;
        }

        else
        {
        return true;
        }
        }

        </script>
        <table width="823" height="302" border="1" align="center" cellpadding="0" cellspacing="0" bordercolor="#a1a1a1" bgcolor="#f3f3f3">
         <tr>
        <td width="819" height="300" valign="top">
        <form method="post" action="display.py" enctype="multipart/form-data" onSubmit="return validate(this);">
          <table width="811" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td width="556"><table width="544" border="0" cellspacing="0" cellpadding="0">
                <tr>
                  <td colspan="3">&nbsp;</td>
                </tr>
                <tr>
                  <td width="156"><div align="center"><u>Upload fasta file</u></div></td>
                  <td colspan="2"><input name="dfile" type="file" class="style1" size="45" />
                    &nbsp;</td>
                </tr>
                <tr>
                  <td colspan="3"><div align="center"></div></td>
                </tr>
                <tr>
                  <td colspan="3"><div align="center">******OR******</div></td>
                </tr>
                <tr>
                  <td valign="top"><div align="center"><u>Paste your sequence</u></div></td>
                  <td colspan="2"><textarea name="sequence" cols="45" rows="10" class="style2" id="sequence"></textarea>
                    &nbsp;</td>
                </tr>
                <tr>
                  <td height="39">&nbsp;</td>
                  <td width="309" height="39">&nbsp;</td>
                  <td width="79"><INPUT TYPE = hidden NAME = "action" VALUE ="display">
                      <INPUT TYPE = submit class="style2" VALUE = "Execute">                  </td>
                </tr>
              </table></td>
              <td width="4">&nbsp;</td>
              <td width="247" valign="top"><table width="259" height="298" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#F3F3F3">
                <tr>
                  <td colspan="3" bgcolor="#F3F3F3">&nbsp;</td>
                </tr>
                <tr>
                  <td>&nbsp;</td>
                  <td><span class="style1"><u>General Instructions</u></span></td>
                  <td width="12">&nbsp;</td>
                </tr>
                <tr>
                  <td width="12" height="246" valign="top">&nbsp;</td>
                  <td width="235" valign="top"><div align="left" class="texta1">
                    <p>As project is going through enhancement and still struggling to minimize errors, so its wise to follow the given instructions. </p>
                    <p># Include a fasta file with correct format</p>
                    <p># Dont paste fasta sequences in a random order.</p>

                    <p># Output will be generated according to the weightage of a dataset, so please be patient untill the page will redirect</p>
                    <p># <a href="http://en.wikipedia.org/wiki/FASTA_format" target=_new>About Fasta </a></p>
                  </div></td>
                  <td height="246" valign="top">&nbsp;</td>
                </tr>
              </table></td>
            </tr>
          </table>
        </form>
        </td>
        </tr>
        </table>
        '''

    def Footer(self):
        """ Definition of Footer() and self argument pointing to itself."""

        print '''
        <p align="center">
        <br><br>
        <table width="931" border="0" cellpadding="0" cellspacing="0" bgcolor="#cccccc">
        <tr>
        <td><div align="center">Thaman Chand @ 2010, University of Turku</div></td>
        </tr>
        </table>
        </p>
        '''

    def CloseHtml(self):
        """ Definition of CloseHtml() and self argument pointing to itself."""

        print "</body>"
        print "</html>"


## Calling all the functions of the class template with object (objx)
if __name__ == '__main__':
    """ Checking for the __main__ from where python interpreter starts to interpret."""

    import cgi, cgitb
    cgitb.enable()
    """ cgitb.enable() catch the errors in the python cgi mode. """

    print 'Content-type: text/html\n\n'
    print "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/msa.css\" >"
    objx=HtmlTemplate()
    """ Defining object (objx) for the class HtmlTemplate()"""
    objx.Header()
    objx.Body()
    objx.Form()
    objx.Footer()
    objx.CloseHtml()