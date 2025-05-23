# perl ./graphql-3.pl daemon -l http://*:9000
use Mojolicious::Lite -signatures;

use GraphQL::Schema;
use GraphQL::Type::Object;
use GraphQL::Type::Scalar qw($String);
use GraphQL::Execution qw(execute);

my $schema = GraphQL::Schema->from_doc(<<'EOF');
type Query {
  helloWorld: String
}
EOF

#!/usr/local/bin/perl perl
# perl: warning: Falling back to the standard locale ("C").
# ": No such file or directory


#http://localhost:9000/
get '/' => sub ($c) {
  $c->render(text => 'Hello World!');
};

# TODO connect to mariadb 
get '/test-data' => sub ($c) {
  my $foo = $c->app->config('foo');
  $c->render(json => {foo => $foo});
};

#TODO setup graphql
#https://metacpan.org/pod/Mojolicious::Plugin::GraphQL

#https://docs.mojolicious.org/Mojolicious/Guides/Tutorial#JSON
# Modify the received JSON document and return it
put '/reverse' => sub ($c) {
  my $hash = $c->req->json;
  $hash->{message} = reverse $hash->{message};
  $c->render(json => $hash);
};

get '/graphql' => sub ($c) {
    my $body_parameters = $c->req->json;
    # $hash->{message} = reverse $hash->{message};
    # $c->render(json => $hash);
    my $foo = execute(
        $schema,
        $body_parameters->{query},
        { helloWorld => 'Hello world!' },
        undef,
        $body_parameters->{variables},
        $body_parameters->{operationName},
        undef,
    );
    $c->render(json => {foo => $foo});

#   send_as JSON => 
};

#Can't use bareword ("body_parameters") as a HASH ref while "strict refs" in use at ./graphql-3.pl line 48.
post '/graphql' => sub ($c) {
    my $body_parameters = $c->req->json;
    # $hash->{message} = reverse $hash->{message};
    # $c->render(json => $hash);
    my $foo = execute(
        $schema,
        $body_parameters->{query},
        { helloWorld => 'Hello world!' },
        undef,
        $body_parameters->{variables},
        $body_parameters->{operationName},
        undef,
    );
    $c->render(json => {foo => $foo});

#   send_as JSON => 
};


# Route leading to an action that renders some text
get '/foo' => sub ($c) {
  $c->render(text => 'foo!');
};

get '/bar' => sub ($c) {
  $c->render(text => 'bar!');
};

app->start;