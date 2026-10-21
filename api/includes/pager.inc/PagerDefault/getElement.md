# PagerDefault::getElement()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 178–181 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L178-L181)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function getElement()
```

## Documentation

```text
Gets the element ID for this pager query.

The element is used to differentiate different pager queries on the same
page so that they may be operated independently.

@return
  Element ID that is used to differentiate between different pager
  queries.
```

## Code

```php
  public function getElement() {
    $this->ensureElement();
    return $this->element;
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
