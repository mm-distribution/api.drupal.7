# Updater::__construct()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 87–91 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L87-L91)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function __construct($source)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($source) {
    $this->source = $source;
    $this->name = self::getProjectName($source);
    $this->title = self::getProjectTitle($source);
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
