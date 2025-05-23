#perl ./graphql.pl daemon -l http://*:9000
use Mojolicious::Lite -signatures;

my $schema = GraphQL::Schema->from_doc(<<'EOF');
schema {
  query: QueryRoot
}
type QueryRoot {
  helloWorld: String
}
EOF

#syntax error at ./graphql.pl line 14, near "plugin GraphQL"
#cpanm Mojolicious::Plugin::GraphQL


# for Mojolicious substitute "plugin" with $app->plugin(...
# Mojolicious::Lite (with endpoint under "/graphql")
plugin GraphQL => {
  schema => $schema, root_value => { helloWorld => 'Hello, world!' }
};
# OR, equivalently:
plugin GraphQL => {schema => $schema, handler => sub {
  my ($c, $body, $execute, $subscribe_fn) = @_;
  # returns JSON-able Perl data
  $execute->(
    $schema,
    $body->{query},
    { helloWorld => 'Hello, world!' }, # $root_value
    $c->req->headers,
    $body->{variables},
    $body->{operationName},
    undef, # $field_resolver
    $subscribe_fn ? (undef, $subscribe_fn) : (), # only passed for subs
  );
}};
# OR, with bespoke user-lookup and caching:
plugin GraphQL => {schema => $schema, handler => sub {
  my ($c, $body, $execute, $subscribe_fn) = @_;
  my $user = MyStuff::User->lookup($app->request->headers->header('X-Token'));
  die "Invalid user\n" if !$user; # turned into GraphQL { errors => [ ... ] }
  my $cached_result = MyStuff::RequestCache->lookup($user, $body->{query});
  return $cached_result if $cached_result;
  MyStuff::RequestCache->cache_and_return($execute->(
    $schema,
    $body->{query},
    undef, # $root_value
    $user, # per-request info
    $body->{variables},
    $body->{operationName},
    undef, # $field_resolver
    $subscribe_fn ? (undef, $subscribe_fn) : (), # only passed for subs
  ));
};
# With GraphiQL, on /graphql
plugin GraphQL => {schema => $schema, graphiql => 1};