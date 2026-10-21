# install_import_locales_remaining()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1558–1567 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1558-L1567)

## Signature

```php
function install_import_locales_remaining(&$install_state)
```

## Documentation

```text
Installation task; import remaining languages via a batch process.

@param $install_state
  An array of information about the current installation state.

@return
  The batch definition, if there are language files to import.
```

## Code

```php
function install_import_locales_remaining(&$install_state) {
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  // Collect files to import for this language. Skip components already covered
  // in the initial batch set.
  $install_locale = $install_state['parameters']['locale'];
  $batch = locale_batch_by_language($install_locale, NULL, variable_get('install_locale_batch_components', array()));
  // Remove temporary variable.
  variable_del('install_locale_batch_components');
  return $batch;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
