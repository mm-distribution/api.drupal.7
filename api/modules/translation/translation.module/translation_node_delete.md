# translation_node_delete()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 417–422 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L417-L422)
- **Module/theme:** translation
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function translation_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function translation_node_delete($node) {
  // Only act if we are dealing with a content type supporting translations.
  if (translation_supported_type($node->type)) {
    translation_remove_from_set($node);
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
