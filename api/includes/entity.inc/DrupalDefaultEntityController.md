# DrupalDefaultEntityController

- **Type:** Class
- **File:** [`includes/entity.inc`](_file.md), lines 48–436 · [local source](../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L48-L436)

## Signature

```php
class DrupalDefaultEntityController implements DrupalEntityControllerInterface
```

## Documentation

```text
Default implementation of DrupalEntityControllerInterface.

This class can be used as-is by most simple entity types. Entity types
requiring special handling can extend the class.
```

## Properties

### $entityCache

```php
protected $entityCache;
```

```text
Static cache of entities, keyed by entity ID.

@var array
```

### $entityType

```php
protected $entityType;
```

```text
Entity type for this controller instance.

@var string
```

### $entityInfo

```php
protected $entityInfo;
```

```text
Array of information about the entity.

@var array

@see entity_get_info()
```

### $hookLoadArguments

```php
protected $hookLoadArguments;
```

```text
Additional arguments to pass to hook_TYPE_load().

Set before calling DrupalDefaultEntityController::attachLoad().

@var array
```

### $idKey

```php
protected $idKey;
```

```text
Name of the entity's ID field in the entity database table.

@var string
```

### $revisionKey

```php
protected $revisionKey;
```

```text
Name of entity's revision database table field, if it supports revisions.

Has the value FALSE if this entity does not use revisions.

@var string
```

### $revisionTable

```php
protected $revisionTable;
```

```text
The table that stores revisions, if the entity supports revisions.

@var string
```

### $cache

```php
protected $cache;
```

```text
Whether this entity type should use the static cache.

Set by entity info.

@var boolean
```

## Methods (derived index)

- [__construct()](DrupalDefaultEntityController/__construct.md) — Constructor: sets basic variables.
- [resetCache()](DrupalDefaultEntityController/resetCache.md) — Implements DrupalEntityControllerInterface::resetCache().
- [load()](DrupalDefaultEntityController/load.md) — Implements DrupalEntityControllerInterface::load().
- [cleanIds()](DrupalDefaultEntityController/cleanIds.md) — Ensures integer entity IDs are valid.
- [filterId()](DrupalDefaultEntityController/filterId.md) — Callback for array_filter that removes non-integer IDs.
- [buildQuery()](DrupalDefaultEntityController/buildQuery.md) — Builds the query to load the entity.
- [attachLoad()](DrupalDefaultEntityController/attachLoad.md) — Attaches data to entities upon loading.
- [cacheGet()](DrupalDefaultEntityController/cacheGet.md) — Gets entities from the static cache.
- [cacheSet()](DrupalDefaultEntityController/cacheSet.md) — Stores entities in the static entity cache.

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
