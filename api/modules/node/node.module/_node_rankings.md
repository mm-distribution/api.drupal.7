# _node_rankings()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1617–1631 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1617-L1631)
- **Module/theme:** node

## Signature

```php
function _node_rankings(SelectQueryExtender $query)
```

## Documentation

```text
Gathers the rankings from the hook_ranking() implementations.

@param $query
  A query object that has been extended with the Search DB Extender.
```

## Code

```php
function _node_rankings(SelectQueryExtender $query) {
  if ($ranking = module_invoke_all('ranking')) {
    $tables = &$query->getTables();
    foreach ($ranking as $rank => $values) {
      if ($node_rank = variable_get('node_rank_' . $rank, 0)) {
        // If the table defined in the ranking isn't already joined, then add it.
        if (isset($values['join']) && !isset($tables[$values['join']['alias']])) {
          $query->addJoin($values['join']['type'], $values['join']['table'], $values['join']['alias'], $values['join']['on']);
        }
        $arguments = isset($values['arguments']) ? $values['arguments'] : array();
        $query->addScore($values['score'], $arguments, $node_rank);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
