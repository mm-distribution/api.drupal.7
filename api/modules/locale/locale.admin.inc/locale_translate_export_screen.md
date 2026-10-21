# locale_translate_export_screen()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 1018–1032 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L1018-L1032)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translate_export_screen()
```

## Documentation

```text
User interface for the translation export screen.
```

## Code

```php
function locale_translate_export_screen() {
  // Get all languages, except English
  drupal_static_reset('language_list');
  $names = locale_language_list('name');
  unset($names['en']);
  $output = '';
  // Offer translation export if any language is set up.
  if (count($names)) {
    $elements = drupal_get_form('locale_translate_export_po_form', $names);
    $output = drupal_render($elements);
  }
  $elements = drupal_get_form('locale_translate_export_pot_form');
  $output .= drupal_render($elements);
  return $output;
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
