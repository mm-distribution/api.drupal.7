# install_import_locales()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1460–1483 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1460-L1483)

## Signature

```php
function install_import_locales(&$install_state)
```

## Documentation

```text
Imports languages via a batch process during installation.

@param $install_state
  An array of information about the current installation state.

@return
  The batch definition, if there are language files to import.
```

## Code

```php
function install_import_locales(&$install_state) {
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  $install_locale = $install_state['parameters']['locale'];

  include_once DRUPAL_ROOT . '/includes/iso.inc';
  $predefined = _locale_get_predefined_list();
  if (!isset($predefined[$install_locale])) {
    // Drupal does not know about this language, so we prefill its values with
    // our best guess. The user will be able to edit afterwards.
    locale_add_language($install_locale, $install_locale, $install_locale, LANGUAGE_LTR, '', '', TRUE, TRUE);
  }
  else {
    // A known predefined language, details will be filled in properly.
    locale_add_language($install_locale, NULL, NULL, NULL, '', '', TRUE, TRUE);
  }

  // Collect files to import for this language.
  $batch = locale_batch_by_language($install_locale, NULL);
  if (!empty($batch)) {
    // Remember components we cover in this batch set.
    variable_set('install_locale_batch_components', $batch['#components']);
    return $batch;
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
