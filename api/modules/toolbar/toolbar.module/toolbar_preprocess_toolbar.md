# toolbar_preprocess_toolbar()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 163–165 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L163-L165)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_preprocess_toolbar(&$variables)
```

## Documentation

```text
Implements hook_preprocess_toolbar().

Adding the 'overlay-displace-top' class to the toolbar pushes the overlay
down, so it appears below the toolbar.
```

## Code

```php
function toolbar_preprocess_toolbar(&$variables) {
  $variables['classes_array'][] = "overlay-displace-top";
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
