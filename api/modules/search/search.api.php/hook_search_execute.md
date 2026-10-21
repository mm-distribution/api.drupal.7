# hook_search_execute()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 171–225 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L171-L225)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_execute($keys = NULL, $conditions = NULL)
```

## Documentation

```text
Execute a search for a set of key words.

Use database API with the 'PagerDefault' query extension to perform your
search.

If your module uses hook_update_index() and search_index() to index its
items, use table 'search_index' aliased to 'i' as the main table in your
query, with the 'SearchQuery' extension. You can join to your module's table
using the 'i.sid' field, which will contain the $sid values you provided to
search_index(). Add the main keywords to the query by using method
searchExpression(). The functions search_expression_extract() and
search_expression_insert() may also be helpful for adding custom search
parameters to the search expression.

See node_search_execute() for an example of a module that uses the search
index, and user_search_execute() for an example that doesn't use the search
index.

@param $keys
  The search keywords as entered by the user.
@param $conditions
  An optional array of additional conditions, such as filters.

@return
  An array of search results. To use the default search result
  display, each item should have the following keys':
  - 'link': Required. The URL of the found item.
  - 'type': The type of item (such as the content type).
  - 'title': Required. The name of the item.
  - 'user': The author of the item.
  - 'date': A timestamp when the item was last modified.
  - 'extra': An array of optional extra information items.
  - 'snippet': An excerpt or preview to show with the result (can be
    generated with search_excerpt()).
  - 'language': Language code for the item (usually two characters).

@ingroup search
```

## Code

```php
function hook_search_execute($keys = NULL, $conditions = NULL) {
  // Build matching conditions
  $query = db_select('search_index', 'i', array('target' => 'slave'))->extend('SearchQuery')->extend('PagerDefault');
  $query->join('node', 'n', 'n.nid = i.sid');
  $query
    ->condition('n.status', 1)
    ->addTag('node_access')
    ->searchExpression($keys, 'node');

  // Insert special keywords.
  $query->setOption('type', 'n.type');
  $query->setOption('language', 'n.language');
  if ($query->setOption('term', 'ti.tid')) {
    $query->join('taxonomy_index', 'ti', 'n.nid = ti.nid');
  }
  // Only continue if the first pass query matches.
  if (!$query->executeFirstPass()) {
    return array();
  }

  // Add the ranking expressions.
  _node_rankings($query);

  // Load results.
  $find = $query
    ->limit(10)
    ->execute();
  $results = array();
  foreach ($find as $item) {
    // Build the node body.
    $node = node_load($item->sid);
    node_build_content($node, 'search_result');
    $node->body = drupal_render($node->content);

    // Fetch comments for snippet.
    $node->rendered .= ' ' . module_invoke('comment', 'node_update_index', $node);
    // Fetch terms for snippet.
    $node->rendered .= ' ' . module_invoke('taxonomy', 'node_update_index', $node);

    $extra = module_invoke_all('node_search_result', $node);

    $results[] = array(
      'link' => url('node/' . $item->sid, array('absolute' => TRUE)),
      'type' => check_plain(node_type_get_name($node)),
      'title' => $node->title,
      'user' => theme('username', array('account' => $node)),
      'date' => $node->changed,
      'node' => $node,
      'extra' => $extra,
      'score' => $item->calculated_score,
      'snippet' => search_excerpt($keys, $node->body),
    );
  }
  return $results;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_execute()".

- [node_search_execute()](../../node/node.module/node_search_execute.md) — `modules/node/node.module`
- [search_extra_type_search_execute()](../tests/search_extra_type.module/search_extra_type_search_execute.md) — `modules/search/tests/search_extra_type.module`
- [user_search_execute()](../../user/user.module/user_search_execute.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
