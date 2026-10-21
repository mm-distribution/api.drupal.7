# FileTransfer::__get()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 53–63 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L53-L63)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
function __get($name)
```

## Documentation

```text
Implementation of the magic __get() method.

If the connection isn't set to anything, this will call the connect() method
and set it to and return the result; afterwards, the connection will be
returned directly without using this method.
```

## Code

```php
  function __get($name) {
    if ($name == 'connection') {
      $this->connect();
      return $this->connection;
    }

    if ($name == 'chroot') {
      $this->setChroot();
      return $this->chroot;
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
