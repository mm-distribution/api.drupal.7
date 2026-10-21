# _translation_tab_access()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 86–91 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L86-L91)
- **Module/theme:** translation

## Signature

```php
function _translation_tab_access($node)
```

## Documentation

```text
Access callback: Checks that the user has permission to 'translate content'.

Only displays the translation tab for nodes that are not language-neutral
of types that have translation enabled.

@param $node
  A node object.

@return
  TRUE if the translation tab should be displayed, FALSE otherwise.

@see translation_menu()
```

## Code

```php
function _translation_tab_access($node) {
  if (entity_language('node', $node) != LANGUAGE_NONE && translation_supported_type($node->type) && node_access('view', $node)) {
    return user_access('translate content');
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
