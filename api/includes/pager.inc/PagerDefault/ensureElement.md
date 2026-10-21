# PagerDefault::ensureElement()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 90–94 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L90-L94)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
protected function ensureElement()
```

## Documentation

```text
Ensure that there is an element associated with this query.
If an element was not specified previously, then the value of the
$maxElement counter is taken, after which the counter is incremented.

After running this method, access $this->element to get the element for this
query.
```

## Code

```php
  protected function ensureElement() {
    if (!isset($this->element)) {
      $this->element = self::$maxElement++;
    }
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
