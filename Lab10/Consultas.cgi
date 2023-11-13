#!"C:/xampp/perl/bin/perl.exe"

use strict;
use CGI;

my $cgi = new CGI;
my $criterio1 = $cgi->param('criterio1');
my $criterio2 = $cgi->param('criterio2');
my $criterio3 = $cgi->param('criterio3');
my $criterio4 = $cgi->param('criterio4');

print $cgi->header("text/html");

my $archivo_csv = 'Programas de Universidades.csv';


open my $data, '<', $archivo_csv or die "No se pudo abrir el archivo CSV";

my $contador = 0;

print "<table border = '2'><br>";

while (my $line = <$data>) {
	chomp $line;
	my @text = split /\|/, $line;
	if ($contador == 0) {
		print "<tr><td>$text[1]</td><td>$text[4]</td><td>$text[10]</td><td>$text[16]</td></tr><br>";
	}
	if (
    (!$criterio1 || $text[1] =~ /$criterio1/) && (!$criterio2 || $text[4] =~ /$criterio2/) && (!$criterio3 || $text[10] =~ /$criterio3/) && (!$criterio4 || $text[16] =~ /$criterio4/))	{
		print "<tr><td>$text[1]</td><td>$text[4]</td><td>$text[10]</td><td>$text[16]</td></tr><br>";
	}
	$contador ++;	
}

print "</table>";

close $data;