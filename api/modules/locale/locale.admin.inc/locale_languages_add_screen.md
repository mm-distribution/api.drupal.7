# locale_languages_add_screen()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 181–185 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L181-L185)
- **Module/theme:** locale
- **Topics:** [locale-language-administration](../../../topics/locale-language-administration.md)

## Signature

```php
function locale_languages_add_screen()
```

## Documentation

```text
User interface for the language addition screen.
```

## Code

```php
function locale_languages_add_screen() {
  $build['predefined'] = drupal_get_form('locale_languages_predefined_form');
  $build['custom'] = drupal_get_form('locale_languages_custom_form');
  return $build;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
