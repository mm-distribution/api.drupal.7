# node_title_list()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 288–297 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L288-L297)
- **Module/theme:** node

## Signature

```php
function node_title_list($result, $title = NULL)
```

## Documentation

```text
Gathers a listing of links to nodes.

@param $result
  A database result object from a query to fetch node entities. If your
  query joins the {node_comment_statistics} table so that the comment_count
  field is available, a title attribute will be added to show the number of
  comments.
@param $title
  A heading for the resulting list.

@return
  A renderable array containing a list of linked node titles fetched from
  $result, or FALSE if there are no rows in $result.
```

## Code

```php
function node_title_list($result, $title = NULL) {
  $items = array();
  $num_rows = FALSE;
  foreach ($result as $node) {
    $items[] = l($node->title, 'node/' . $node->nid, !empty($node->comment_count) ? array('attributes' => array('title' => format_plural($node->comment_count, '1 comment', '@count comments'))) : array());
    $num_rows = TRUE;
  }

  return $num_rows ? array('#theme' => 'item_list__node', '#items' => $items, '#title' => $title) : FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
