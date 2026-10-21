# TableSort

- **Type:** Class
- **File:** [`includes/tablesort.inc`](_file.md), lines 15–104 · [local source](../../../source/includes/tablesort.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc#L15-L104)

## Signature

```php
class TableSort extends SelectQueryExtender
```

## Documentation

```text
Query extender class for tablesort queries.
```

## Properties

### $header

```php
protected $header = array();
```

```text
The array of fields that can be sorted by.

@var array
```

## Methods (derived index)

- [__construct()](TableSort/__construct.md)
- [orderByHeader()](TableSort/orderByHeader.md) — Order the query based on a header array.
- [init()](TableSort/init.md) — Initializes the table sort context.
- [getSort()](TableSort/getSort.md) — Determine the current sort direction.
- [getQueryParameters()](TableSort/getQueryParameters.md) — Compose a URL query parameter array to append to table sorting requests.
- [order()](TableSort/order.md) — Determine the current sort criterion.

---
_Drupal 7.103 · [includes/tablesort.inc](https://github.com/drupal/drupal/blob/7.103/includes/tablesort.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
