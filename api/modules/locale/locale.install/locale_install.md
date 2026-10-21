# locale_install()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 11–27 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L11-L27)
- **Module/theme:** locale
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function locale_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function locale_install() {
  // locales_source.source and locales_target.target are not used as binary
  // fields; non-MySQL database servers need to ensure the field type is text
  // and that LIKE produces a case-sensitive comparison.

  db_insert('languages')
    ->fields(array(
      'language' => 'en',
      'name' => 'English',
      'native' => 'English',
      'direction' => 0,
      'enabled' => 1,
      'weight' => 0,
      'javascript' => '',
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
