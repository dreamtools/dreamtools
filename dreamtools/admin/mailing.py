from BeautifulSoup import BeautifulSoup
import urllib2




class GetTeamMail(object):
    def __init__(self, lowercase=False, url=None, filename=None):
        """Manipulate the team/mail pairs from Dream challenge log file

        This function reads an URL from the Dream website (
        http://www.the-dream-project.org/file_downloads/1/feeds?attach=page_1) that
        returns a CSV document. This document is parsed to get pair of email/team names.

        This web page is a log that is not always up-to-date. A new and more
        complete page is available but cannot be accessed with scripting tools
        at the moment. So, you can also provide a file that
        contains two columns : team name and emails (see :meth:`read_mails_from_file`
        and the example below).

        The instance contains the team names, and values containing their emails.

        :param lowercase: if true (default) return the team names as lower case
        :param url: overwrite the default url
        :param filename: if provided, the url is replaced by the contents of this file

        :return: a dictionary of team names versus emails

        :Example:

        The following example retrieve team/mail pairs from the default url.

            >>> import dreamtools
            >>> from dreamtools import mailing
            >>> mails = mailing.GetTeamMail()
            >>> print mails

        You can read a list in a file instead:

            >>> import dreamtools
            >>> from dreamtools import mailing
            >>> mails = mailing.GetTeamMail(filename='share/data/list.txt')
            >>> print mails


        """
        if url == None:
            self.url = 'http://www.the-dream-project.org/file_downloads/1/feeds?attach=page_1'
        else:
            self.url = url


        if filename:
            self._read_mails_from_file(filename)
        else:
            # read the url page
            u = urllib2.urlopen(self.url)
            source = u.read()
            soup = BeautifulSoup(source)

            mails = {}

            data = str(soup).split('\n')
            # remove the header
            del(data[0])

            # scan all lines
            for line in data:
                fields = line.split(',')
                if len(fields) != 8:
                    pass
                else:
                    if lowercase:
                        team = str(fields[6].lower().replace('"', ''))
                    else:
                        team = str(fields[6].replace('"', ''))
                    mail = str(fields[5].replace('"', ''))
                    mails[team] = mail
            self.data = mails

    def getTeamsGivenMails(self, emails_list):
        """

        :Usage:

            >>> m = GetTeamMail(file='test')
            >>> teamNames = m.getTeamsGivenMails(['test@yahoo.fr'])

        """
        return [team for team, email in self.data.iteritems() if email in emails_list]

    def _read_mails_from_file(self, filename):
        """Fill the team/mail with a CSV file instead of url

        Expect a 2-columns file to contain team names in the first
        column and email in the second one

        """
        f = open(filename, 'r')
        data = f.readlines()
        f.close()
        self.data = {}
        for item in data:
            team, mail = item.split()
            self.data[team] =  mail.rstrip('\n')

    def __str__(self):

        str_ = "Found teamName / mails -------------------------------\n"
        for teamName in self.data.keys():
            try:
                str_ += '    ' + teamName +" "+ self.data[teamName] +'\n'
            except Exception,e:
                str_ += self.lookfor(teamName)
                print e

        str_ += "\n\nMailing list is ------------------------\n\n"
        for teamName in self.data.keys():
            try:
                str_ +=  self.data[teamName] + ', '
            except Exception,e:
                str_ += self.lookfor(teamName) + '\n'
                print e
        return str_

    def lookfor(self, team):
        """Look for a team name in the data attributes

        >>> m = mailing.GetTeamMail(filename='./share/data/list.txt')
        >>> m.lookfor('fly')

        If found, print the team name and emails and return the team name provided.
        If not found, try to find an equivalent name (comparing lower case only).

        """
        str_ = ''
        for this in self.data.keys():
            if this == team:
                print this, self.data[team]
                return this
            elif team.lower() in this.lower():
                str_ = team + ' Not found. Did you mean '+ this + '?'
                break
        if str_ == '':
            str_ = 'Team ' + team + ' not found.'
        return str_




