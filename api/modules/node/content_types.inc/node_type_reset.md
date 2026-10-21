# node_type_reset()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 398–408 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L398-L408)
- **Module/theme:** node

## Signature

```php
function node_type_reset($type)
```

## Documentation

```text
Resets relevant fields of a module-defined node type to their default values.

@param $type
  The node type to reset. The node type is passed back by reference with its
  resetted values. If there is no module-defined info for this node type,
  then nothing happens.
```

## Code

```php
function node_type_reset($type) {
  $info_array = module_invoke_all('node_info');
  if (isset($info_array[$type->orig_type])) {
    $info_array[$type->orig_type]['type'] = $type->orig_type;
    $info = node_type_set_defaults($info_array[$type->orig_type]);

    foreach ($info as $field => $value) {
      $type->$field = $value;
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
