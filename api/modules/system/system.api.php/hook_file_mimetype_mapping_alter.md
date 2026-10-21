# hook_file_mimetype_mapping_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3964–3971 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3964-L3971)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_mimetype_mapping_alter(&$mapping)
```

## Documentation

```text
Alter MIME type mappings used to determine MIME type from a file extension.

This hook is run when file_mimetype_mapping() is called. It is used to
allow modules to add to or modify the default mapping from
file_default_mimetype_mapping().

@param $mapping
  An array of mimetypes correlated to the extensions that relate to them.
  The array has 'mimetypes' and 'extensions' elements, each of which is an
  array.

@see file_default_mimetype_mapping()
```

## Code

```php
function hook_file_mimetype_mapping_alter(&$mapping) {
  // Add new MIME type 'drupal/info'.
  $mapping['mimetypes']['example_info'] = 'drupal/info';
  // Add new extension '.info' and map it to the 'drupal/info' MIME type.
  $mapping['extensions']['info'] = 'example_info';
  // Override existing extension mapping for '.ogg' files.
  $mapping['extensions']['ogg'] = 189;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_mimetype_mapping_alter()".

- [file_test_file_mimetype_mapping_alter()](../../simpletest/tests/file_test.module/file_test_file_mimetype_mapping_alter.md) — `modules/simpletest/tests/file_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
