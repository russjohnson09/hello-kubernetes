# perl ./graphql-3.pl daemon -l http://*:9000
use Mojolicious::Lite -signatures;

use GraphQL::Schema;
use GraphQL::Type::Object;
use GraphQL::Type::Scalar qw($String);
use GraphQL::Execution qw(execute);

# my $schema = GraphQL::Schema->from_doc(<<'EOF');
# type Query {
#   helloWorld: String
# }
# EOF

#https://blogs.perl.org/users/ed_j/2017/10/graphql-perl---graphql-js-tutorial-translation-to-graphql-perl-and-mojoliciousplugingraphql.html
my $schema = GraphQL::Schema->from_doc(<<'EOF');
type Query { helloWorld: String }
EOF
say Dumper execute($schema, "{ helloWorld }",
  { helloWorld=>"Hello world!" });

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
    my $queryJson = execute(
        $schema,
        $body_parameters->{query},
        { helloWorld => 'Hello world!' },
        undef,
        $body_parameters->{variables},
        $body_parameters->{operationName},
        undef,
    );
    $c->render(json =>  $queryJson);

#   send_as JSON => 
};



#Can't use bareword ("body_parameters") as a HASH ref while "strict refs" in use at ./graphql-3.pl line 48.
post '/graphql' => sub ($c) {
    $c->res->headers->from_hash( {'Access-Control-Allow-Headers' => '*',  'Access-Control-Allow-Origin' => '*'});

    my $body_parameters = $c->req->json;
    # $hash->{message} = reverse $hash->{message};
    # $c->render(json => $hash);
    my $queryJson = execute(
        $schema,
        $body_parameters->{query},
        { helloWorld => 'Hello world!' },
        undef,
        $body_parameters->{variables},
        $body_parameters->{operationName},
        undef,
    );
    $c->render(json => $queryJson);

#   send_as JSON => 
};


# Route leading to an action that renders some text
get '/foo' => sub ($c) {
  $c->render(text => 'foo!');
};

get '/bar' => sub ($c) {
  $c->render(text => 'bar!');
};

#https://docs.mojolicious.org/Mojo/Headers
#https://docs.mojolicious.org/Mojolicious/Routes/Route
#https://docs.mojolicious.org/Mojolicious/Guides/Tutorial
options '/graphql' => sub ($c) {

  #say "test"

  #my $res = Mojo::Message::Response->new;

  #my $headers = Mojo::Headers->new;

  # $c->res->headers->header('X-Bender' => 'Bite my shiny metal ass!');

#  $c->res->headers->header( 'Access-Control-Allow-Origin' => '*');
 # $c->res->headers->header( 'Access-Control-Allow-Headers' => '*');
  $c->res->headers->from_hash( {'Access-Control-Allow-Headers' => '*',  'Access-Control-Allow-Origin' => '*'});

  $c->render(text => '', status => 200);

  # $res->code(200);
  # $headers->content_length(42);
  # $headers->content_type('text/plain');
  # $headers->add(Vary => 'Accept')->add(Vary => 'Accept-Encoding')->to_string;
  # $headers = $headers->from_hash({'Cookie' => 'a=b'});

# say $headers->to_string;
#   $c->render(text => 'bar!');

  #say $req->method;
  #say $req->headers->content_type;
  #say $req->body;
};

# app.addContextHook('router:before', async ctx => {
#  ctx.res.set('Access-Control-Allow-Origin', '*');
# });

app->start;

