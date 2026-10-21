# FileTransferSSH::isFile()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 81–93 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L81-L93)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
public function isFile($path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isFile($path) {
    $file = escapeshellarg($path);
    $cmd = "[ -f {$file} ] && echo 'yes'";
    if ($output = @ssh2_exec($this->connection, $cmd)) {
      if ($output == 'yes') {
        return TRUE;
      }
      return FALSE;
    }
    else {
      throw new FileTransferException('Cannot check @path.', NULL, array('@path' => $path));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
