# PagerDefault::element()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 160–166 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L160-L166)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function element($element)
```

## Documentation

```text
Specify the element ID for this pager query.

The element is used to differentiate different pager queries on the same
page so that they may be operated independently.  If you do not specify an
element, every pager query on the page will get a unique element.  If for
whatever reason you want to explicitly define an element for a given query,
you may do so here.

Setting the element here also increments the static $maxElement counter,
which is used for determining the $element when there's none specified.

Note that no collision detection is done when setting an element ID
explicitly, so it is possible for two pagers to end up using the same ID
if both are set explicitly.

@param $element
```

## Code

```php
  public function element($element) {
    $this->element = $element;
    if ($element >= self::$maxElement) {
      self::$maxElement = $element + 1;
    }
    return $this;
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
