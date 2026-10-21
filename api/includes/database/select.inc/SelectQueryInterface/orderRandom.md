# SelectQueryInterface::orderRandom()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 407–407 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L407)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function orderRandom();
```

## Documentation

```text
Orders the result set by a random value.

This may be stacked with other orderBy() calls. If so, the query will order
by each specified field, including this one, in the order called. Although
this method may be called multiple times on the same query, doing so
is not particularly useful.

Note: The method used by most drivers may not scale to very large result
sets. If you need to work with extremely large data sets, you may create
your own database driver by subclassing off of an existing driver and
implementing your own randomization mechanism. See

http://jan.kneschke.de/projects/mysql/order-by-rand/

for an example of such an alternate sorting mechanism.

@return SelectQueryInterface
  The called object
```

## Code

```php
  public function orderRandom();
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
