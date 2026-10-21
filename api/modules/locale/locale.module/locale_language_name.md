# locale_language_name()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 829–835 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L829-L835)
- **Module/theme:** locale

## Signature

```php
function locale_language_name($lang)
```

## Documentation

```text
Returns a language name
```

## Code

```php
function locale_language_name($lang) {
  $list = &drupal_static(__FUNCTION__);
  if (!isset($list)) {
    $list = locale_language_list();
  }
  return ($lang && isset($list[$lang])) ? $list[$lang] : t('All');
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
