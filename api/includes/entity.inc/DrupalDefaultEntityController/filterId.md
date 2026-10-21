# DrupalDefaultEntityController::filterId()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 256–261 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L256-L261)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function filterId($id)
```

## Documentation

```text
Callback for array_filter that removes non-integer IDs.
```

## Code

```php
  protected function filterId($id) {
    // ctype_digit() is used here instead of a strict comparison as sometimes
    // the id is passed as a string containing '0' which may represent a bug
    // elsewhere but would fail with a strict comparison.
    return is_numeric($id) && $id == (int) $id && ctype_digit((string) $id);
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
