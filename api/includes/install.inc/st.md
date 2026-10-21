# st()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1125–1168 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1125-L1168)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function st($string, array $args = array(), array $options = array())
```

## Documentation

```text
Translates a string when some systems are not available.

Used during the install process, when database, theme, and localization
system is possibly not yet available.

Use t() if your code will never run during the Drupal installation phase.
Use st() if your code will only run during installation and never any other
time. Use get_t() if your code could run in either circumstance.

@see t()
@see get_t()
@ingroup sanitization
```

## Code

```php
function st($string, array $args = array(), array $options = array()) {
  static $locale_strings = NULL;
  global $install_state;

  if (empty($options['context'])) {
    $options['context'] = '';
  }

  if (!isset($locale_strings)) {
    $locale_strings = array();
    if (isset($install_state['parameters']['profile']) && isset($install_state['parameters']['locale'])) {
      // If the given locale was selected, there should be at least one .po file
      // with its name ending in {$install_state['parameters']['locale']}.po
      // This might or might not be the entire filename. It is also possible
      // that multiple files end with the same extension, even if unlikely.
      $po_files = file_scan_directory('./profiles/' . $install_state['parameters']['profile'] . '/translations', '/'. $install_state['parameters']['locale'] .'\.po$/', array('recurse' => FALSE));
      if (count($po_files)) {
        require_once DRUPAL_ROOT . '/includes/locale.inc';
        foreach ($po_files as $po_file) {
          _locale_import_read_po('mem-store', $po_file);
        }
        $locale_strings = _locale_import_one_string('mem-report');
      }
    }
  }

  // Transform arguments before inserting them
  foreach ($args as $key => $value) {
    switch ($key[0]) {
      // Escaped only
      case '@':
        $args[$key] = check_plain($value);
        break;
      // Escaped and placeholder
      case '%':
      default:
        $args[$key] = '<em>' . check_plain($value) . '</em>';
        break;
      // Pass-through
      case '!':
    }
  }
  return strtr((!empty($locale_strings[$options['context']][$string]) ? $locale_strings[$options['context']][$string] : $string), $args);
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
