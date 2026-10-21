# system_archiver_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4016–4028 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4016-L4028)
- **Module/theme:** system
- **Implements:** [hook_archiver_info()](../system.api.php/hook_archiver_info.md)

## Signature

```php
function system_archiver_info()
```

## Documentation

```text
Implements hook_archiver_info().
```

## Code

```php
function system_archiver_info() {
  $archivers['tar'] = array(
    'class' => 'ArchiverTar',
    'extensions' => array('tar', 'tgz', 'tar.gz', 'tar.bz2'),
  );
  if (function_exists('zip_open')) {
    $archivers['zip'] = array(
      'class' => 'ArchiverZip',
      'extensions' => array('zip'),
    );
  }
  return $archivers;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
