# FileTransferException::__construct()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 368–371 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L368-L371)
- **Class:** [FileTransferException](../FileTransferException.md)

## Signature

```php
function __construct($message, $code = 0, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  function __construct($message, $code = 0, $arguments = array()) {
    parent::__construct($message, (int) $code);
    $this->arguments = $arguments;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
