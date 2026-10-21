# hook_filetransfer_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4811–4818 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4811-L4818)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_filetransfer_info_alter(&$filetransfer_info)
```

## Documentation

```text
Alter the FileTransfer class registry.

@param array $filetransfer_info
  Reference to a nested array containing information about the FileTransfer
  class registry.

@see hook_filetransfer_info()
```

## Code

```php
function hook_filetransfer_info_alter(&$filetransfer_info) {
  if (variable_get('paranoia', FALSE)) {
    // Remove the FTP option entirely.
    unset($filetransfer_info['ftp']);
    // Make sure the SSH option is listed first.
    $filetransfer_info['ssh']['weight'] = -10;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_filetransfer_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
