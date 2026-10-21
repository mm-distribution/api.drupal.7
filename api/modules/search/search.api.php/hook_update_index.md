# hook_update_index()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 312–339 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L312-L339)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_update_index()
```

## Documentation

```text
Update the search index for this module.

This hook is called every cron run if search.module is enabled, your
module has implemented hook_search_info(), and your module has been set as
an active search module on the Search settings page
(admin/config/search/settings). It allows your module to add items to the
built-in search index using search_index(), or to add them to your module's
own indexing mechanism.

When implementing this hook, your module should index content items that
were modified or added since the last run. PHP has a time limit
for cron, though, so it is advisable to limit how many items you index
per run using variable_get('search_cron_limit') (see example below). Also,
since the cron run could time out and abort in the middle of your run, you
should update your module's internal bookkeeping on when items have last
been indexed as you go rather than waiting to the end of indexing.

@ingroup search
```

## Code

```php
function hook_update_index() {
  $limit = (int)variable_get('search_cron_limit', 100);

  $result = db_query_range("SELECT n.nid FROM {node} n LEFT JOIN {search_dataset} d ON d.type = 'node' AND d.sid = n.nid WHERE d.sid IS NULL OR d.reindex <> 0 ORDER BY d.reindex ASC, n.nid ASC", 0, $limit);

  foreach ($result as $node) {
    $node = node_load($node->nid);

    // Save the changed time of the most recent indexed node, for the search
    // results half-life calculation.
    variable_set('node_cron_last', $node->changed);

    // Render the node.
    node_build_content($node, 'search_index');
    $node->rendered = drupal_render($node->content);

    $text = '<h1>' . check_plain($node->title) . '</h1>' . $node->rendered;

    // Fetch extra data normally not visible
    $extra = module_invoke_all('node_update_index', $node);
    foreach ($extra as $t) {
      $text .= $t;
    }

    // Update index
    search_index($node->nid, 'node', $text);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update_index()".

- [comment_update_index()](../../comment/comment.module/comment_update_index.md) — `modules/comment/comment.module`
- [node_update_index()](../../node/node.module/node_update_index.md) — `modules/node/node.module`
- [statistics_update_index()](../../statistics/statistics.module/statistics_update_index.md) — `modules/statistics/statistics.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
