# EntityFieldQuery::execute()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1210–1222 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1210-L1222)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function execute()
```

## Documentation

```text
Executes the query.

After executing the query, $this->ordered_results will contain a list of
the same stub entities in the order returned by the query. This is only
relevant if there are multiple entity types in the returned value and
a field ordering was requested. In every other case, the returned value
contains everything necessary for processing.

@return
  Either a number if count() was called or an array of associative arrays
  of stub entities. The outer array keys are entity types, and the inner
  array keys are the relevant ID. (In most cases this will be the entity
  ID. The only exception is when age=FIELD_LOAD_REVISION is used and field
  conditions or sorts are present -- in this case, the key will be the
  revision ID.) The entity type will only exist in the outer array if
  results were found. The inner array values are always stub entities, as
  returned by entity_create_stub_entity(). To traverse the returned array:
  @code
    foreach ($query->execute() as $entity_type => $entities) {
      foreach ($entities as $entity_id => $entity) {
  @endcode
  Note if the entity type is known, then the following snippet will load
  the entities found:
  @code
    $result = $query->execute();
    if (!empty($result[$my_type])) {
      $entities = entity_load($my_type, array_keys($result[$my_type]));
    }
  @endcode
```

## Code

```php
  public function execute() {
    // Give a chance to other modules to alter the query.
    drupal_alter('entity_query', $this);
    $this->altered = TRUE;

    // Initialize the pager.
    $this->initializePager();

    // Execute the query using the correct callback.
    $result = call_user_func($this->queryCallback(), $this);

    return $result;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
