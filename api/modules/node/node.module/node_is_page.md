# node_is_page()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1483–1486 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1483-L1486)
- **Module/theme:** node

## Signature

```php
function node_is_page($node)
```

## Documentation

```text
Returns whether the current page is the full page view of the passed-in node.

@param $node
  A node object.

@return
  The ID of the node if this is a full page view, otherwise FALSE.
```

## Code

```php
function node_is_page($node) {
  $page_node = menu_get_object();
  return (!empty($page_node) ? $page_node->nid == $node->nid : FALSE);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
