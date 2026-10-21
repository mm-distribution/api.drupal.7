# hook_entity_view()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 428–434 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L428-L434)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_view($entity, $type, $view_mode, $langcode)
```

## Documentation

```text
Act on entities being assembled before rendering.

@param $entity
  The entity object.
@param $type
  The type of entity being rendered (i.e. node, user, comment).
@param $view_mode
  The view mode the entity is rendered in.
@param $langcode
  The language code used for rendering.

The module may add elements to $entity->content prior to rendering. The
structure of $entity->content is a renderable array as expected by
drupal_render().

@see hook_entity_view_alter()
@see hook_comment_view()
@see hook_node_view()
@see hook_user_view()
```

## Code

```php
function hook_entity_view($entity, $type, $view_mode, $langcode) {
  $entity->content['my_additional_field'] = array(
    '#markup' => $additional_field,
    '#weight' => 10,
    '#theme' => 'mymodule_my_additional_field',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_view()".

- [taxonomy_test_entity_view()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_entity_view.md) — `modules/simpletest/tests/taxonomy_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
