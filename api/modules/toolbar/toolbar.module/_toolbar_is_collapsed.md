# _toolbar_is_collapsed()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 113–117 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L113-L117)
- **Module/theme:** toolbar

## Signature

```php
function _toolbar_is_collapsed()
```

## Documentation

```text
Determines the current state of the toolbar drawer's visibility.

@return
  TRUE when drawer is collapsed, FALSE when it is expanded.
```

## Code

```php
function _toolbar_is_collapsed() {
  // PHP converts dots into underscores in cookie names to avoid problems with
  // its parser, so we use a converted cookie name.
  return isset($_COOKIE['Drupal_toolbar_collapsed']) ? $_COOKIE['Drupal_toolbar_collapsed'] : 0;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
