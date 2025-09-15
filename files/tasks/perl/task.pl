use strict;
use warnings;

my $count;

my $range = config()->{range};

my @lines;
for ($count = 0; $count < 10; $count++) {
  push @lines, rand($range) . ', ' . rand($range);
}

print join "\n", @lines;

update_state({ lines => \@lines });
