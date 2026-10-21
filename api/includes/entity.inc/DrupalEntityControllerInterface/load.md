# DrupalEntityControllerInterface::load()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 39–39 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L39)
- **Class:** [DrupalEntityControllerInterface](../DrupalEntityControllerInterface.md)

## Signature

```php
public function load($ids = array(), $conditions = array());
```

## Documentation

```text
Loads one or more entities.

@param $ids
  An array of entity IDs, or FALSE to load all entities.
@param $conditions
  An array of conditions. Keys are field names on the entity's base table.
  Values will be compared for equality. All the comparisons will be ANDed
  together. This parameter is deprecated; use an EntityFieldQuery instead.

@return
  An array of entity objects indexed by their ids. When no results are
  found, an empty array is returned.
```

## Code

```php
  public function load($ids = array(), $conditions = array());
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
