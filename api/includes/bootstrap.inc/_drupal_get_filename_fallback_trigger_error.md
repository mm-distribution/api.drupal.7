# _drupal_get_filename_fallback_trigger_error()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1129–1151 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1129-L1151)

## Signature

```php
function _drupal_get_filename_fallback_trigger_error($type, $name, $error_type)
```

## Documentation

```text
Triggers a user-level warning for missing or unexpectedly moved files.

@param $type
  The type of the item (theme, theme_engine, module, profile).
@param $name
  The name of the item for which the filename is requested.
@param $error_type
  The type of the error ('missing' or 'moved').

@see drupal_get_filename()
@see _drupal_get_filename_fallback()
```

## Code

```php
function _drupal_get_filename_fallback_trigger_error($type, $name, $error_type) {
  // Hide messages due to known bugs that will appear on a lot of sites.
  // @todo Remove this in https://www.drupal.org/node/2383823
  if (empty($name)) {
    return;
  }

  // Make sure we only show any missing or moved file errors only once per
  // request.
  static $errors_triggered = array();
  if (empty($errors_triggered[$type][$name][$error_type])) {
    // Use _drupal_trigger_error_with_delayed_logging() here since these are
    // triggered during low-level operations that cannot necessarily be
    // interrupted by a watchdog() call.
    if ($error_type == 'missing') {
      _drupal_trigger_error_with_delayed_logging(format_string('The following @type is missing from the file system: %name. For information about how to fix this, see <a href="@documentation">the documentation page</a>.', array('@type' => $type, '%name' => $name, '@documentation' => 'https://www.drupal.org/node/2487215')), E_USER_WARNING);
    }
    elseif ($error_type == 'moved') {
      _drupal_trigger_error_with_delayed_logging(format_string('The following @type has moved within the file system: %name. In order to fix this, clear caches or put the @type back in its original location. For more information, see <a href="@documentation">the documentation page</a>.', array('@type' => $type, '%name' => $name, '@documentation' => 'https://www.drupal.org/node/2487215')), E_USER_WARNING);
    }
    $errors_triggered[$type][$name][$error_type] = TRUE;
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
