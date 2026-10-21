# ArchiverInterface::__construct()

- **Type:** Method
- **File:** [`includes/archiver.inc`](../_file.md), lines 21–21 · [local source](../../../../source/includes/archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc#L21)
- **Class:** [ArchiverInterface](../ArchiverInterface.md)

## Signature

```php
public function __construct($file_path);
```

## Documentation

```text
Constructs a new archiver instance.

@param $file_path
  The full system path of the archive to manipulate. Only local files
  are supported. If the file does not yet exist, it will be created if
  appropriate.
```

## Code

```php
  public function __construct($file_path);
```

---
_Drupal 7.103 · [includes/archiver.inc](https://github.com/drupal/drupal/blob/7.103/includes/archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
