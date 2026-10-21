# FileTransferSSH::factory()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 26–32 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L26-L32)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
static function factory($jail, $settings)
```

## Documentation

_No docblock in source._

## Code

```php
  static function factory($jail, $settings) {
    $username = empty($settings['username']) ? '' : $settings['username'];
    $password = empty($settings['password']) ? '' : $settings['password'];
    $hostname = empty($settings['advanced']['hostname']) ? 'localhost' : $settings['advanced']['hostname'];
    $port = empty($settings['advanced']['port']) ? 22 : $settings['advanced']['port'];
    return new FileTransferSSH($jail, $username, $password, $hostname, $port);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
