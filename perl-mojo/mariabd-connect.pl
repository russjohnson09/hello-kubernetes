# perl ./mariabd-connect.pl

use DBI;

my $database = "test";
my $hostname = "db";
my $port = "3306";
my $user = "root";
my $password = "example";

my $dsn = "DBI:MariaDB:database=$database;host=$hostname;port=$port";

$dsn = "DBI:MariaDB:host=$hostname;port=$port;database=sys";

my $dbh = DBI->connect($dsn, $user, $password);
my $sth = $dbh->prepare(
    'SELECT id, first_name, last_name FROM authors WHERE last_name = ?'
) or die 'prepare statement failed: ' . $dbh->errstr();

my $sth = $dbh->prepare(
    'SELECT 1'
) or die 'prepare statement failed: ' . $dbh->errstr();
#$sth->execute('Eggers') or die 'execution failed: ' . $dbh->errstr();
$sth->execute() or die 'execution failed: ' . $dbh->errstr();
print $sth->rows() . " rows found.\n";
while (my $ref = $sth->fetchrow_hashref()) {
    print "Found a row: id = $ref->{'id'}, fn = $ref->{'first_name'}\n";
}

# print 'hello' . "\n";


# print "\n";


