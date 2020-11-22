# coding: utf-8
import argparse

from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client, gql
import rich

parser = argparse.ArgumentParser()
parser.add_argument(
    "PAT",
    help="""GitHub PAT, see
        https://docs.github.com/en/free-pro-team@latest/graphql/guides/forming-calls-with-graphql#authenticating-with-graphql
        (I've already one, named 'github_gql_api')""",
)
args = parser.parse_args()

transport = AIOHTTPTransport(
    url="https://api.github.com/graphql",
    headers={"Authorization": f"bearer {args.PAT}"},
)
client = Client(transport=transport, fetch_schema_from_transport=True)

slides_folders_gql = gql(
    """
{
  search(query: "AleCandido/slides", type: REPOSITORY, first: 10) {
    nodes {
      ... on Repository {
        nameWithOwner
        refs(refPrefix: "refs/heads/", first: 10) {
          nodes {
            name
            id
          }
        }
      }
    }
  }
}
"""
)

response = client.execute(slides_folders_gql)
repos = response["search"]["nodes"]
repo = list(filter(lambda x: x["nameWithOwner"] == "AleCandido/slides", repos))[0]
branches = repo["refs"]["nodes"]
branch = list(filter(lambda x: x["name"] == "gh-pages", branches))[0]


gh_pages_content_gql = gql(
    """
{
  node(id: "%s") {
    ... on Ref {
      target {
        ... on Commit {
          tree {
            entries {
              name
              type
              object {
                id
                ... on Tree {
                  entries {
                    name
                    object {
                      id
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
"""
    % (branch["id"])
)

result = client.execute(gh_pages_content_gql)
content = result["node"]["target"]["tree"]["entries"]
rich.print(content)
