# entity_get_controller()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8248–8259 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8248-L8259)

## Signature

```php
function entity_get_controller($entity_type)
```

## Documentation

```text
Gets the entity controller for an entity type.

@return DrupalEntityControllerInterface
  The entity controller object for the specified entity type.
```

## Code

```php
function entity_get_controller($entity_type) {
  $controllers = &drupal_static(__FUNCTION__, array());
  if (!isset($controllers[$entity_type])) {
    $type_info = entity_get_info($entity_type);
    // Explicitly fail for malformed entities missing a valid controller class.
    if (!isset($type_info['controller class']) || !class_exists($class = $type_info['controller class'])) {
      throw new EntityMalformedException(t('Missing or non-existent controller class on entity of type @entity_type.', array('@entity_type' => $entity_type)));
    }
    $controllers[$entity_type] = new $class($entity_type);
  }
  return $controllers[$entity_type];
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
