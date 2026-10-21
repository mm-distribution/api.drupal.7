# node_type_page_title()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2184–2186 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2184-L2186)
- **Module/theme:** node

## Signature

```php
function node_type_page_title($type)
```

## Documentation

```text
Title callback: Returns the unsanitized title of the node type edit form.

@param $type
  The node type object.

@return string
  An unsanitized string that is the title of the node type edit form.

@see node_menu()
```

## Code

```php
function node_type_page_title($type) {
  return $type->name;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
