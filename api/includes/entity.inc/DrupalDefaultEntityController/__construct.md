# DrupalDefaultEntityController::__construct()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 120–138 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L120-L138)
- **Class:** [DrupalDefaultEntityController](../DrupalDefaultEntityController.md)

## Signature

```php
public function __construct($entityType)
```

## Documentation

```text
Constructor: sets basic variables.

@param $entityType
  The entity type for which the instance is created.
```

## Code

```php
  public function __construct($entityType) {
    $this->entityType = $entityType;
    $this->entityInfo = entity_get_info($entityType);
    $this->entityCache = array();
    $this->hookLoadArguments = array();
    $this->idKey = $this->entityInfo['entity keys']['id'];

    // Check if the entity type supports revisions.
    if (!empty($this->entityInfo['entity keys']['revision'])) {
      $this->revisionKey = $this->entityInfo['entity keys']['revision'];
      $this->revisionTable = $this->entityInfo['revision table'];
    }
    else {
      $this->revisionKey = FALSE;
    }

    // Check if the entity type supports static caching of loaded entities.
    $this->cache = !empty($this->entityInfo['static cache']);
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
