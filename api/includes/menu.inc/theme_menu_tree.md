# theme_menu_tree()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1636–1638 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1636-L1638)
- **Topics:** [menu](../../topics/menu.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_menu_tree($variables)
```

## Documentation

```text
Returns HTML for a wrapper for a menu sub-tree.

@param $variables
  An associative array containing:
  - tree: An HTML string containing the tree's items.

@see template_preprocess_menu_tree()
@ingroup themeable
```

## Code

```php
function theme_menu_tree($variables) {
  return '<ul class="menu">' . $variables['tree'] . '</ul>';
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
