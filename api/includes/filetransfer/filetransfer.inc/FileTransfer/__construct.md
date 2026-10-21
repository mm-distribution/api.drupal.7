# FileTransfer::__construct()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 24–26 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L24-L26)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
function __construct($jail)
```

## Documentation

```text
The constructor for the UpdateConnection class. This method is also called
from the classes that extend this class and override this method.
```

## Code

```php
  function __construct($jail) {
    $this->jail = $jail;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
