# toolbar_toggle_page()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 70–81 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L70-L81)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_toggle_page()
```

## Documentation

```text
Menu callback; toggles the visibility of the toolbar drawer.
```

## Code

```php
function toolbar_toggle_page() {
  global $base_path;
  // Toggle the value in the cookie.
  drupal_setcookie('Drupal.toolbar.collapsed', !_toolbar_is_collapsed(),
    array(
      'samesite' => 'Lax',
      'path' => $base_path,
    )
  );
  // Redirect the user from where he used the toggle element.
  drupal_goto();
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
