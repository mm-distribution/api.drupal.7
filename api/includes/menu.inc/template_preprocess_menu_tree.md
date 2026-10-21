# template_preprocess_menu_tree()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1621–1624 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1621-L1624)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function template_preprocess_menu_tree(&$variables)
```

## Documentation

```text
Implements template_preprocess_HOOK() for theme_menu_tree().
```

## Code

```php
function template_preprocess_menu_tree(&$variables) {
  $variables['#tree'] = $variables['tree'];
  $variables['tree'] = $variables['tree']['#children'];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
