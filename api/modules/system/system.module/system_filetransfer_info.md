# system_filetransfer_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1897–1923 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1897-L1923)
- **Module/theme:** system
- **Implements:** [hook_filetransfer_info()](../system.api.php/hook_filetransfer_info.md)

## Signature

```php
function system_filetransfer_info()
```

## Documentation

```text
Implements hook_filetransfer_info().
```

## Code

```php
function system_filetransfer_info() {
  $backends = array();

  // This is the default, will be available on most systems.
  if (function_exists('ftp_connect')) {
    $backends['ftp'] = array(
      'title' => t('FTP'),
      'class' => 'FileTransferFTP',
      'file' => 'ftp.inc',
      'file path' => 'includes/filetransfer',
      'weight' => 0,
    );
  }

  // SSH2 lib connection is only available if the proper PHP extension is
  // installed.
  if (function_exists('ssh2_connect')) {
    $backends['ssh'] = array(
      'title' => t('SSH'),
      'class' => 'FileTransferSSH',
      'file' => 'ssh.inc',
      'file path' => 'includes/filetransfer',
      'weight' => 20,
    );
  }
  return $backends;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
