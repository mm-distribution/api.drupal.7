# theme_system_powered_by()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3469–3471 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3469-L3471)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_powered_by()
```

## Documentation

```text
Returns HTML for the Powered by Drupal text.

@ingroup themeable
```

## Code

```php
function theme_system_powered_by() {
  return '<span>' . t('Powered by <a href="@poweredby">Drupal</a>', array('@poweredby' => 'https://www.drupal.org')) . '</span>';
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
