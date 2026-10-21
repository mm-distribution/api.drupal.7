# FileTransferSSH::isDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 67–79 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L67-L79)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
public function isDirectory($path)
```

## Documentation

```text
WARNING: This is untested.  It is not currently used, but should do the trick.
```

## Code

```php
  public function isDirectory($path) {
    $directory = escapeshellarg($path);
    $cmd = "[ -d {$directory} ] && echo 'yes'";
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
