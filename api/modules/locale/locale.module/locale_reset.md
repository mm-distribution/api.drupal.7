# locale_reset()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 765–767 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L765-L767)
- **Module/theme:** locale

## Signature

```php
function locale_reset()
```

## Documentation

```text
Reset static variables used by locale().
```

## Code

```php
function locale_reset() {
  drupal_static_reset('locale');
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
