#perl ./graphql-2.pl daemon -l http://*:9000

#cpanm GraphQL

#https://metacpan.org/dist/App-cpanminus/view/bin/cpanm


# cpanm Test::Needs --force
# cpanm JSON::MaybeXS

# cpanm Try::Tiny --force

# cpanm Test::Fatal


# cpanm Test2
# cpanm IPC::Run3 --force
# cpanm Test2::Plugin::NoWarnings
# cpanm Params::ValidationCompiler
# cpanm DateTime

# cpanm GraphQL::Schema

#! Installing the dependencies failed: Module 'Dist::CheckConflicts' is not installed

use GraphQL::Schema;
use GraphQL::Type::Object;
use GraphQL::Type::Scalar qw($String);
use GraphQL::Execution qw(execute);

my $schema = GraphQL::Schema->from_doc(<<'EOF');
type Query {
  helloWorld: String
}
EOF
post '/graphql' => sub {
  send_as JSON => execute(
    $schema,
    body_parameters->{query},
    { helloWorld => 'Hello world!' },
    undef,
    body_parameters->{variables},
    body_parameters->{operationName},
    undef,
  );
};