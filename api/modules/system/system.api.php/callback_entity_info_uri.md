# callback_entity_info_uri()

- **Type:** Function
- **File:** [`modules/system/system.api.php`](_file.md), lines 4893–4897 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4893-L4897)
- **Module/theme:** system
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_entity_info_uri($entity)
```

## Documentation

```text
Return the URI for an entity.

Callback for hook_entity_info().

@param $entity
  The entity to return the URI for.

@return
  An associative array with the following elements:
  - 'path': The URL path for the entity.
  - 'options': (optional) An array of options for the url() function.
  The actual entity URI can be constructed by passing these elements to
  url().
```

## Code

```php
function callback_entity_info_uri($entity) {
  return array(
    'path' => 'node/' . $entity->nid,
  );
}
```

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
