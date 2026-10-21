# DrupalDefaultEntityController::attachLoad()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 350–373 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L350-L373)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function attachLoad(&$queried_entities, $revision_id = FALSE)
```

## Documentation

```text
Attaches data to entities upon loading.

This will attach fields, if the entity is fieldable. It calls
hook_entity_load() for modules which need to add data to all entities.
It also calls hook_TYPE_load() on the loaded entities. For example
hook_node_load() or hook_user_load(). If your hook_TYPE_load()
expects special parameters apart from the queried entities, you can set
$this->hookLoadArguments prior to calling the method.
See NodeController::attachLoad() for an example.

@param $queried_entities
  Associative array of query results, keyed on the entity ID.
@param $revision_id
  ID of the revision that was loaded, or FALSE if the most current revision
  was loaded.
```

## Code

```php
  protected function attachLoad(&$queried_entities, $revision_id = FALSE) {
    // Attach fields.
    if ($this->entityInfo['fieldable']) {
      if ($revision_id) {
        field_attach_load_revision($this->entityType, $queried_entities);
      }
      else {
        field_attach_load($this->entityType, $queried_entities);
      }
    }

    // Call hook_entity_load().
    foreach (module_implements('entity_load') as $module) {
      $function = $module . '_entity_load';
      $function($queried_entities, $this->entityType);
    }
    // Call hook_TYPE_load(). The first argument for hook_TYPE_load() are
    // always the queried entities, followed by additional arguments set in
    // $this->hookLoadArguments.
    $args = array_merge(array($queried_entities), $this->hookLoadArguments);
    foreach (module_implements($this->entityInfo['load hook']) as $module) {
      call_user_func_array($module . '_' . $this->entityInfo['load hook'], $args);
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
