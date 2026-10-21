# options_theme()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 24–30 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L24-L30)
- **Module/theme:** options
- **Implements:** [hook_theme()](../../../../system/system.api.php/hook_theme.md)

## Signature

```php
function options_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function options_theme() {
  return array(
    'options_none' => array(
      'variables' => array('instance' => NULL, 'option' => NULL),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
