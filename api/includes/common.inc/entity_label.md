# entity_label()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8412–8423 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8412-L8423)

## Signature

```php
function entity_label($entity_type, $entity)
```

## Documentation

```text
Returns the label of an entity.

See the 'label callback' component of the hook_entity_info() return value
for more information.

@param $entity_type
  The entity type; e.g., 'node' or 'user'.
@param $entity
  The entity for which to generate the label.

@return
  The entity label, or FALSE if not found.
```

## Code

```php
function entity_label($entity_type, $entity) {
  $label = FALSE;
  $info = entity_get_info($entity_type);
  if (isset($info['label callback']) && function_exists($info['label callback'])) {
    $label = $info['label callback']($entity, $entity_type);
  }
  elseif (!empty($info['entity keys']['label']) && isset($entity->{$info['entity keys']['label']})) {
    $label = $entity->{$info['entity keys']['label']};
  }

  return $label;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
