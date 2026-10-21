# NodeController::buildQuery()

- **Type:** Method
- **File:** [`modules/node/node.module`](../_file.md), lines 4181–4191 · [local source](../../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4181-L4191)
- **Class:** [NodeController](../NodeController.md)
- **Module/theme:** node

## Signature

```php
protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE) {
    // Ensure that uid is taken from the {node} table,
    // alias timestamp to revision_timestamp and add revision_uid.
    $query = parent::buildQuery($ids, $conditions, $revision_id);
    $fields =& $query->getFields();
    unset($fields['timestamp']);
    $query->addField('revision', 'timestamp', 'revision_timestamp');
    $fields['uid']['table'] = 'base';
    $query->addField('revision', 'uid', 'revision_uid');
    return $query;
  }
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
