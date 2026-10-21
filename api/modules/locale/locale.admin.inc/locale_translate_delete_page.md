# locale_translate_delete_page()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1241–1246 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1241-L1246)
- **Module/theme:** locale
- **Topics:** [locale-translate-edit-delete](../../../topics/locale-translate-edit-delete.md)

## Signature

```php
function locale_translate_delete_page($lid)
```

## Documentation

```text
String deletion confirmation page.
```

## Code

```php
function locale_translate_delete_page($lid) {
  if ($source = db_query('SELECT lid, source FROM {locales_source} WHERE lid = :lid', array(':lid' => $lid))->fetchObject()) {
    return drupal_get_form('locale_translate_delete_form', $source);
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
