# node_add_page()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 24–33 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L24-L33)
- **Module/theme:** node

## Signature

```php
function node_add_page()
```

## Documentation

```text
Page callback: Displays add content links for available content types.

Redirects to node/add/[type] if only one content type is available.

@see node_menu()
```

## Code

```php
function node_add_page() {
  $item = menu_get_item();
  $content = system_admin_menu_block($item);
  // Bypass the node/add listing if only one content type is available.
  if (count($content) == 1) {
    $item = array_shift($content);
    drupal_goto($item['href']);
  }
  return theme('node_add_list', array('content' => $content));
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
