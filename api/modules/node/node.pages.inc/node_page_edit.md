# node_page_edit()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 11–15 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L11-L15)
- **Module/theme:** node

## Signature

```php
function node_page_edit($node)
```

## Documentation

```text
Menu callback; presents the node editing form.
```

## Code

```php
function node_page_edit($node) {
  $type_name = node_type_get_name($node);
  drupal_set_title(t('<em>Edit @type</em> @title', array('@type' => $type_name, '@title' => $node->title)), PASS_THROUGH);
  return drupal_get_form($node->type . '_node_form', $node);
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
