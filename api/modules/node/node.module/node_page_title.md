# node_page_title()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2199–2201 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2199-L2201)
- **Module/theme:** node

## Signature

```php
function node_page_title($node)
```

## Documentation

```text
Title callback: Returns the title of the node.

@param $node
  The node object.

@return
  An unsanitized string that is the title of the node.

@see node_menu()
```

## Code

```php
function node_page_title($node) {
  return $node->title;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
