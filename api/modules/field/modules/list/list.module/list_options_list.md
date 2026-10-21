# list_options_list()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 438–440 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L438-L440)
- **Module/theme:** list
- **Implements:** [hook_options_list()](../../options/options.api.php/hook_options_list.md)

## Signature

```php
function list_options_list($field, $instance, $entity_type, $entity)
```

## Documentation

```text
Implements hook_options_list().
```

## Code

```php
function list_options_list($field, $instance, $entity_type, $entity) {
  return list_allowed_values($field, $instance, $entity_type, $entity);
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
