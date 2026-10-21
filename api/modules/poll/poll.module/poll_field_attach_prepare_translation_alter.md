# poll_field_attach_prepare_translation_alter()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 476–483 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L476-L483)
- **Module/theme:** poll
- **Implements:** [hook_field_attach_prepare_translation_alter()](../../field/field.api.php/hook_field_attach_prepare_translation_alter.md)

## Signature

```php
function poll_field_attach_prepare_translation_alter(&$entity, $context)
```

## Documentation

```text
Implements hook_field_attach_prepare_translation_alter().
```

## Code

```php
function poll_field_attach_prepare_translation_alter(&$entity, $context) {
  if ($context['entity_type'] == 'node' && $entity->type == 'poll') {
    $entity->choice = $context['source_entity']->choice;
    foreach ($entity->choice as $i => $options) {
      $entity->choice[$i]['chvotes'] = 0;
    }
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
