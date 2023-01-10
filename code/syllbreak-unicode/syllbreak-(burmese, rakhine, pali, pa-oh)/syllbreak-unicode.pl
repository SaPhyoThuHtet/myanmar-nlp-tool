#!usr/bin/perl
# Syllable Segmenter for unicode
# Usage: perl syllbreak-unicode.pl input > output

# Phyo Thu Htet, Information Science Student, UTYCC
# @SoftwareLab, UTYCC
# 4 Oct 2019, Last Modified : 29 Dec 2019
use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";


my $count = 0;
while (!eof($inputFILE)) {
   
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {
        chomp($line);
    $line = uc $line;
    
    # word segmentation for english, syllable for burmese, character for other language
    
    # Pa-Oh
    # ꩻ for pa-oh  ါꩻ
    # ꩻ for pa-oh ကꩻ
    # ႏ pa-oh

    $line =~ s/([\t\n\r]*)//g;
    $line =~ s/(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)/$1 /g;
    print "$line";
    print "\n";
   }
   
   
}

close ($inputFILE);



