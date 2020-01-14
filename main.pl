use 5.30.1;

use experimental 'switch';

my @tree = (
    {name => 'root', children => [1, 4]},
        {name => 'tree1', children => [2, 3]},      #1
            {name => 'branch1', children => []},    #2
            {name => 'branch2', children => []},    #3
        {name => 'tree2', children => [5, 6]},      #4
            {name => 'branch1', children => []},    #5
            {name => 'branch2', children => []}     #6
);

sub print_node {
    my $node = $tree[$_[0]];
    my $offset = defined $_[1] ? $_[1] : "    ";
    
    say "[$_[0]]:$node->{name}";
    foreach my $child (@{$node->{children}}) {
        print $offset;
        print_node($child, $offset . "    ");
    }
}

while (print '$ ' and my $command = <>) {
    my @args = $command =~ /\b(\w+)\b/g;
    unless ($args[0] =~ s/^([a-z])$//) {
        say 'Invalid syntax';
        next;
    }
    given ($1) {
        when ('p') {
            unless (@args > 1) {
                print_node 0;
                next;
            }
            unless ($args[1] ~~ [0 .. $#tree]) {
                say 'Invalid index';
                next;
            }
            print_node $args[1];
        }
        when ('r') {
            unless (@args > 2) {
                say q('q' requires two arguments);
                next;
            }
            unless ($args[1] ~~ [0 .. $#tree]) {
                say 'Invalid index';
                next;
            }
            $tree[$args[1]]->{name} = $args[2];
        }
        when ('h') {
            say q('p $index': print node);
            say q('q': exit);
        }
        when ('q') {
            say 'Good bye';
            last;
        }
        default {
            say 'Unknown command';
        }
    }
}