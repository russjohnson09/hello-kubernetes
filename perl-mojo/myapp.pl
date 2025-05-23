# TODO ./myapp.pl daemon -l http://*:9000
#perl ./myapp.pl daemon -l http://*:9000
use Mojolicious::Lite -signatures;

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


# Route leading to an action that renders some text
get '/foo' => sub ($c) {
  $c->render(text => 'foo!');
};

get '/bar' => sub ($c) {
  $c->render(text => 'bar!');
};

app->start;