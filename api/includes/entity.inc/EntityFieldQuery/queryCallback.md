# EntityFieldQuery::queryCallback()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1230–1257 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1230-L1257)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function queryCallback()
```

## Documentation

```text
Determines the query callback to use for this entity query.

@return
  A callback that can be used with call_user_func().
```

## Code

```php
  public function queryCallback() {
    // Use the override from $this->executeCallback. It can be set either
    // while building the query, or using hook_entity_query_alter().
    if (function_exists($this->executeCallback)) {
      return $this->executeCallback;
    }
    // If there are no field conditions and sorts, and no execute callback
    // then we default to querying entity tables in SQL.
    if (empty($this->fields)) {
      return array($this, 'propertyQuery');
    }
    // If no override, find the storage engine to be used.
    foreach ($this->fields as $field) {
      if (!isset($storage)) {
        $storage = $field['storage']['module'];
      }
      elseif ($storage != $field['storage']['module']) {
        throw new EntityFieldQueryException(t("Can't handle more than one field storage engine"));
      }
    }
    if ($storage) {
      // Use hook_field_storage_query() from the field storage.
      return $storage . '_field_storage_query';
    }
    else {
      throw new EntityFieldQueryException(t("Field storage engine not found."));
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
