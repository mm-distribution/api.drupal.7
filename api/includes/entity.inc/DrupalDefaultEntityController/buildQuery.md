# DrupalDefaultEntityController::buildQuery()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 288–331 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L288-L331)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE)
```

## Documentation

```text
Builds the query to load the entity.

This has full revision support. For entities requiring special queries,
the class can be extended, and the default query can be constructed by
calling parent::buildQuery(). This is usually necessary when the object
being loaded needs to be augmented with additional data from another
table, such as loading node type into comments or vocabulary machine name
into terms, however it can also support $conditions on different tables.
See CommentController::buildQuery() or TaxonomyTermController::buildQuery()
for examples.

@param $ids
  An array of entity IDs, or FALSE to load all entities.
@param $conditions
  An array of conditions. Keys are field names on the entity's base table.
  Values will be compared for equality. All the comparisons will be ANDed
  together. This parameter is deprecated; use an EntityFieldQuery instead.
@param $revision_id
  The ID of the revision to load, or FALSE if this query is asking for the
  most current revision(s).

@return SelectQuery
  A SelectQuery object for loading the entity.
```

## Code

```php
  protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE) {
    $query = db_select($this->entityInfo['base table'], 'base');

    $query->addTag($this->entityType . '_load_multiple');

    if ($revision_id) {
      $query->join($this->revisionTable, 'revision', "revision.{$this->idKey} = base.{$this->idKey} AND revision.{$this->revisionKey} = :revisionId", array(':revisionId' => $revision_id));
    }
    elseif ($this->revisionKey) {
      $query->join($this->revisionTable, 'revision', "revision.{$this->revisionKey} = base.{$this->revisionKey}");
    }

    // Add fields from the {entity} table.
    $entity_fields = $this->entityInfo['schema_fields_sql']['base table'];

    if ($this->revisionKey) {
      // Add all fields from the {entity_revision} table.
      $entity_revision_fields = drupal_map_assoc($this->entityInfo['schema_fields_sql']['revision table']);
      // The id field is provided by entity, so remove it.
      unset($entity_revision_fields[$this->idKey]);

      // Remove all fields from the base table that are also fields by the same
      // name in the revision table.
      $entity_field_keys = array_flip($entity_fields);
      foreach ($entity_revision_fields as $key => $name) {
        if (isset($entity_field_keys[$name])) {
          unset($entity_fields[$entity_field_keys[$name]]);
        }
      }
      $query->fields('revision', $entity_revision_fields);
    }

    $query->fields('base', $entity_fields);

    if ($ids) {
      $query->condition("base.{$this->idKey}", $ids, 'IN');
    }
    if ($conditions) {
      foreach ($conditions as $field => $value) {
        $query->condition('base.' . $field, $value);
      }
    }
    return $query;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
