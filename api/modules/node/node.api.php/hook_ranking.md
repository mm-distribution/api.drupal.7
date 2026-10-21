# hook_ranking()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 969–991 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L969-L991)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_ranking()
```

## Documentation

```text
Provide additional methods of scoring for core search results for nodes.

A node's search score is used to rank it among other nodes matched by the
search, with the highest-ranked nodes appearing first in the search listing.

For example, a module allowing users to vote on content could expose an
option to allow search results' rankings to be influenced by the average
voting score of a node.

All scoring mechanisms are provided as options to site administrators, and
may be tweaked based on individual sites or disabled altogether if they do
not make sense. Individual scoring mechanisms, if enabled, are assigned a
weight from 1 to 10. The weight represents the factor of magnification of
the ranking mechanism, with higher-weighted ranking mechanisms having more
influence. In order for the weight system to work, each scoring mechanism
must return a value between 0 and 1 for every node. That value is then
multiplied by the administrator-assigned weight for the ranking mechanism,
and then the weighted scores from all ranking mechanisms are added, which
brings about the same result as a weighted average.

@return
  An associative array of ranking data. The keys should be strings,
  corresponding to the internal name of the ranking mechanism, such as
  'recent', or 'comments'. The values should be arrays themselves, with the
  following keys available:
  - title: (required) The human readable name of the ranking mechanism.
  - join: (optional) An array with information to join any additional
    necessary table. This is not necessary if the table required is already
    joined to by the base query, such as for the {node} table. Other tables
    should use the full table name as an alias to avoid naming collisions.
  - score: (required) The part of a query string to calculate the score for
    the ranking mechanism based on values in the database. This does not need
    to be wrapped in parentheses, as it will be done automatically; it also
    does not need to take the weighted system into account, as it will be
    done automatically. It does, however, need to calculate a decimal between
    0 and 1; be careful not to cast the entire score to an integer by
    inadvertently introducing a variable argument.
  - arguments: (optional) If any arguments are required for the score, they
    can be specified in an array here.

@ingroup node_api_hooks
```

## Code

```php
function hook_ranking() {
  // If voting is disabled, we can avoid returning the array, no hard feelings.
  if (variable_get('vote_node_enabled', TRUE)) {
    return array(
      'vote_average' => array(
        'title' => t('Average vote'),
        // Note that we use i.sid, the search index's search item id, rather than
        // n.nid.
        'join' => array(
          'type' => 'LEFT',
          'table' => 'vote_node_data',
          'alias' => 'vote_node_data',
          'on' => 'vote_node_data.nid = i.sid',
        ),
        // The highest possible score should be 1, and the lowest possible score,
        // always 0, should be 0.
        'score' => 'vote_node_data.average / CAST(%f AS DECIMAL)',
        // Pass in the highest possible voting score as a decimal argument.
        'arguments' => array(variable_get('vote_score_max', 5)),
      ),
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_ranking()".

- [comment_ranking()](../../comment/comment.module/comment_ranking.md) — `modules/comment/comment.module`
- [node_ranking()](../node.module/node_ranking.md) — `modules/node/node.module`
- [statistics_ranking()](../../statistics/statistics.module/statistics_ranking.md) — `modules/statistics/statistics.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
