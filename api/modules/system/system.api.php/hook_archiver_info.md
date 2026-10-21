# hook_archiver_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4088–4095 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4088-L4095)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_archiver_info()
```

## Documentation

```text
Declare archivers to the system.

An archiver is a class that is able to package and unpackage one or more files
into a single possibly compressed file.  Common examples of such files are
zip files and tar.gz files.  All archiver classes must implement
ArchiverInterface.

Each entry should be keyed on a unique value, and specify three
additional keys:
- class: The name of the PHP class for this archiver.
- extensions: An array of file extensions that this archiver supports.
- weight: This optional key specifies the weight of this archiver.
  When mapping file extensions to archivers, the first archiver by
  weight found that supports the requested extension will be used.

@see hook_archiver_info_alter()
```

## Code

```php
function hook_archiver_info() {
  return array(
    'tar' => array(
      'class' => 'ArchiverTar',
      'extensions' => array('tar', 'tar.gz', 'tar.bz2'),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_archiver_info()".

- [update_test_archiver_info()](../../update/tests/update_test.module/update_test_archiver_info.md) — `modules/update/tests/update_test.module`
- [system_archiver_info()](../system.module/system_archiver_info.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
