# FileTransferFTP::factory()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 25–39 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L25-L39)
- **Class:** [FileTransferFTP](../FileTransferFTP.md)

## Signature

```php
static function factory($jail, $settings)
```

## Documentation

```text
Return an object which can implement the FTP protocol.

@param string $jail
@param array $settings
@return FileTransferFTP
  The appropriate FileTransferFTP subclass based on the available
  options. If the FTP PHP extension is available, use it.
```

## Code

```php
  static function factory($jail, $settings) {
    $username = empty($settings['username']) ? '' : $settings['username'];
    $password = empty($settings['password']) ? '' : $settings['password'];
    $hostname = empty($settings['advanced']['hostname']) ? 'localhost' : $settings['advanced']['hostname'];
    $port = empty($settings['advanced']['port']) ? 21 : $settings['advanced']['port'];

    if (function_exists('ftp_connect')) {
      $class = 'FileTransferFTPExtension';
    }
    else {
      throw new FileTransferException('No FTP backend available.');
    }

    return new $class($jail, $username, $password, $hostname, $port);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
