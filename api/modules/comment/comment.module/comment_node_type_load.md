# comment_node_type_load()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 148–152 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L148-L152)
- **Module/theme:** comment

## Signature

```php
function comment_node_type_load($name)
```

## Documentation

```text
Menu loader callback for Field UI paths.

Return a comment bundle name from a node type in the URL.
```

## Code

```php
function comment_node_type_load($name) {
  if ($type = node_type_get_type(strtr($name, array('-' => '_')))) {
    return 'comment_node_' . $type->type;
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
