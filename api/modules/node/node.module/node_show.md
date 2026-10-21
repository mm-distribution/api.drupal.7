# node_show()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1460–1472 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1460-L1472)
- **Module/theme:** node

## Signature

```php
function node_show($node, $message = FALSE)
```

## Documentation

```text
Generates an array which displays a node detail page.

@param $node
  A node object.
@param $message
  A flag which sets a page title relevant to the revision being viewed.

@return
  A $page element suitable for use by drupal_render().
```

## Code

```php
function node_show($node, $message = FALSE) {
  if ($message) {
    drupal_set_title(t('Revision of %title from %date', array('%title' => $node->title, '%date' => format_date($node->revision_timestamp))), PASS_THROUGH);
  }

  // For markup consistency with other pages, use node_view_multiple() rather than node_view().
  $nodes = node_view_multiple(array($node->nid => $node), 'full');

  // Update the history table, stating that this user viewed this node.
  node_tag_new($node);

  return $nodes;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
