# locale_translation_filter_form_validate()

- **Type:** Function
- **File:** [`modules/locale/locale.admin.inc`](_file.md), lines 897–901 · [local source](../../../../source/modules/locale/locale.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc#L897-L901)
- **Module/theme:** locale
- **Topics:** [locale-translate-administration-screens](../../../topics/locale-translate-administration-screens.md)

## Signature

```php
function locale_translation_filter_form_validate($form, &$form_state)
```

## Documentation

```text
Validate result from locale translation filter form.
```

## Code

```php
function locale_translation_filter_form_validate($form, &$form_state) {
  if ($form_state['values']['op'] == t('Filter') && empty($form_state['values']['language']) && empty($form_state['values']['group'])) {
    form_set_error('type', t('You must select something to filter by.'));
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
