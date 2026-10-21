# color_theme()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 28–34 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L28-L34)
- **Module/theme:** color
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function color_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function color_theme() {
  return array(
    'color_scheme_form' => array(
      'render element' => 'form',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
