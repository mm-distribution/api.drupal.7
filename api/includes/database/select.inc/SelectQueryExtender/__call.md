# SelectQueryExtender::__call()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 840–854 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L840-L854)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __call($method, $args)
```

## Documentation

```text
Magic override for undefined methods.

If one extender extends another extender, then methods in the inner extender
will not be exposed on the outer extender.  That's because we cannot know
in advance what those methods will be, so we cannot provide wrapping
implementations as we do above.  Instead, we use this slower catch-all method
to handle any additional methods.
```

## Code

```php
  public function __call($method, $args) {
    $return = call_user_func_array(array($this->query, $method), $args);

    // Some methods will return the called object as part of a fluent interface.
    // Others will return some useful value.  If it's a value, then the caller
    // probably wants that value.  If it's the called object, then we instead
    // return this object.  That way we don't "lose" an extender layer when
    // chaining methods together.
    if ($return instanceof SelectQueryInterface) {
      return $this;
    }
    else {
      return $return;
    }
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
