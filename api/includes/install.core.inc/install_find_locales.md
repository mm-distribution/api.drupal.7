# install_find_locales()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1203–1216 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1203-L1216)

## Signature

```php
function install_find_locales($profilename)
```

## Documentation

```text
Find all .po files for the current profile.
```

## Code

```php
function install_find_locales($profilename) {
  $locales = file_scan_directory('./profiles/' . $profilename . '/translations', '/\.po$/', array('recurse' => FALSE));
  array_unshift($locales, (object) array('name' => 'en'));
  foreach ($locales as $key => $locale) {
    // The locale (file name) might be drupal-7.2.cs.po instead of cs.po.
    $locales[$key]->langcode = preg_replace('!^(.+\.)?([^\.]+)$!', '\2', $locale->name);
    // Language codes cannot exceed 12 characters to fit into the {languages}
    // table.
    if (strlen($locales[$key]->langcode) > 12) {
      unset($locales[$key]);
    }
  }
  return $locales;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
